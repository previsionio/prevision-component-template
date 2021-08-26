# Check that all modules needed are put in your requirements.txt file
 
import pandas as pd
import argparse
import pandas as pd

from pathlib import Path



def main(dataframe: pd.DataFrame, arg_1: str='nothing') -> pd.DataFrame:
    """Add a new column named placeholder fill with the arg_1 value


    :param dataframe: The input dataframe. This should not be changed.
    :param arg_1 : 

    :returns: The updated dataframe
    """
    dataframe["placeholder"] = arg_1
    return dataframe


if __name__ == '__main__':
    # Test your component
    # By executing your script with a python main [ARGS]

    # Put meaningful description and args for your user
    parser = argparse.ArgumentParser(description='Extracting Storage Requirements from text')
    
    # do not use positionnal argument, always use the --arg syntax
    # note all the args name are they must be reported in the yaml component file
    parser.add_argument('--src', required=True, type=str, help='Path of the local file containing the Input data.')
    parser.add_argument('--dst', required=True, type=str, help='Path of the local file for output data.')
    parser.add_argument('--arg-1', required=True, type=str, help='Some parameter')

        

    args = parser.parse_args()
    src = args.src
    dst=args.dst
    
    # Warning : remember that argparse will convert any - to _ ( https://docs.python.org/dev/library/argparse.html#dest 
    arg1 = args.arg_1

    df = pd.read_csv(src)

    # entry point of your transformation
    ef = main(df,arg1)

    # if you save some data , your component must create the output path
    # Even if a file as pipeline may required to create a temp path
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    ef.to_csv(dst, index=False)

