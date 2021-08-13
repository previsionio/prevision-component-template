import yaml
import argparse
from install.docstrings import parse_docstring
from src.main import main

PYTHON_KFLOW_TYPE_MAPPING = {
    int: 'Integer',
    str: 'String',
    float: 'Float'
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sample')

    parser.add_argument('--name',
                        type=str,
                        required=True,
                        help='name of the component, only characters & "_" authorized')

    parser.add_argument('--label',
                        type=str,
                        required=True,
                        help='label to display in the UI')

    args = parser.parse_args()

    with open('install/component.yaml', 'r') as stream:
        yaml_template = yaml.safe_load(stream)

    yaml_template['name'] = args.name
    yaml_template['label'] = args.label

    docstring = parse_docstring(main.__doc__)

    yaml_template['description'] = docstring['long_description'].strip()

    for param in docstring['params']:
        if param['name'] == 'dataframe':
            continue

        param_name = param['name']
        try:
            param_type = PYTHON_KFLOW_TYPE_MAPPING[main.__annotations__[param_name]]
        except KeyError:
            print('invalid type:', param_name, main.__annotations__[param_name])
            continue

        input_desc = {
            'name': param_name,
            'label': param_name,
            'type': param_type,
            'is_property': True,
            'description': param['doc'].strip()
        }

        yaml_template['inputs'].append(input_desc)

        command_args = [
            '--{}'.format(param_name),
            {'inputValue': param_name}
        ]

        yaml_template['implementation']['container']['args'].append(command_args)

    # custom way to dump the yaml, because the default parser doesn't format nested lists well
    desc_keys = {key: val for key, val in yaml_template.items() if key in {'name', 'label', 'description'}}

    yaml_str = yaml.safe_dump(desc_keys, sort_keys=False)
    yaml_str += 'inputs:\n' + yaml.dump(yaml_template['inputs'], sort_keys=False)
    yaml_str += 'outputs:\n' + yaml.dump(yaml_template['outputs'], sort_keys=False)

    yaml_str += 'implementation:\n  container:\n    command: [python, components/src/component.py]\n    '
    yaml_str += 'args: ' + yaml.dump(yaml_template['implementation']['container']['args'],
                                            sort_keys=False,
                                            default_flow_style=True)
    with open('component.yaml', 'w') as stream:
        stream.write(yaml_str)

    # testing it can be loaded
    with open('component.yaml', 'r') as stream:
        try:
            yaml_template = yaml.safe_load(stream)
        except Exception as e:
            print('failed to load created .yaml:', e)

    print('Success, component.yaml written to ./component.yaml')
