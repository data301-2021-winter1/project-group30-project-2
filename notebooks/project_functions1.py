import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    dfg1 = (
          pd.read_csv('../data/raw/android-games.csv')
          .dropna(axis=0)
          .reset_index(drop=True)
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    dfg2 = (
          dfg1
          .drop(['growth (30 days)','growth (60 days)','paid'], axis=1)
          .sort_values('5 star ratings', ascending=False)
      )

    return dfg2 

load_and_process('../data/raw/android-games.csv')

