import pandas as pd

def build_data(prices_dfs: list) -> pd.DataFrame:
    """
     creates a stock dataframe from list of dfs
    """

    print('building data...')

    prices_dfs = pd.concat(prices_dfs, sort=True).reset_index()
    prices_dfs_clean = prices_dfs.pivot_table(values='Adj. Close',
                                              index='Date',
                                              columns='Ticker')

    return prices_dfs_clean
