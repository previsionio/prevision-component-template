import pandas as pd


def main(dataframe: pd.DataFrame, arg1: int) -> pd.DataFrame:
    """Short description.

    Long description.

    :param dataframe: The input dataframe. This should not be changed.
    :param arg1: One of the possible parameter of the function.

    :returns: The function should always return a dataframe.
    """

    return dataframe.sample(frac=0.1)


if __name__ == '__main__':
    # test your component here
    # e.g.
    dataset = pd.read_csv('data/some_data.csv')
    print(main(dataset).describe())
