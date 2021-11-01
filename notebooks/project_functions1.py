import pandas as pd

def load_and_process('../data/raw/android-games.csv'):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv('../data/raw/android-games.csv')
          .dropna(how="any")
          .sort_values("installs")
          .reset_index(drop=True)
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
      )

    # Make sure to return the latest dataframe

    return df2 
