import argparse
import pandas as pd
from pathlib import Path
from src.main import main


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sample')

    parser.add_argument('--input-dataset-path', type=str, required=True, help='input dataset')
    parser.add_argument('--output-dataset-path', type=str, required=True, help='output dataset')

    for param_name, param_type in [(k, v) for k, v in main.__annotations__.items() if k not in {'dataframe', 'return'}]:
        parser.add_argument('--{}'.format(param_name), type=param_type)

    args = parser.parse_args()
    df = pd.read_csv(args.input_dataset_path)

    main_kwargs = {k: v for k, v in args.__dict__.items() if k not in {'input_dataset_path', 'output_dataset_path'}}

    result = main(df, **main_kwargs)

    Path(args.output_dataset_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output_dataset_path, index=False)
