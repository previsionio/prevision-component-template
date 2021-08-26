# prevision component template

### why am I here ?
You want to create a custom component to be use in a Prevision.io 
pipeline.  

### How to use this repo

- Fork this repo with the name you want to give your component.
- Write the component. 2 ways : 
    - easy: writing code in src/main.py and properly documenting the function and its inputs
    - advanced: writing yourself the src/component.py file and component.yaml
 

#### Easy
Edit the main function in src/main.py, taking care to document it
properly in the docstring format, as well as typing all the 
parameters you might add in the function 
(and keeping the `dataframe` as first argument and return value).

Then you may run 

```shell script
python install.render_yaml <component_name> <component_label>
```
`component_name` must start with a character, and have no spaces or special characters besides underscore "`_`"
`component_label` can be a quoted string.

add & commit everything you've created, including the `component.yaml`
