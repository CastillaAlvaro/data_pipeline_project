import quandl
import pandas as pd
from tqdm import tqdm

def setup_quandl(api_key: str) -> None:
    """
    set quandl api key
    """
    quandl.ApiConfig.api_key = api_key

def get_tickers(path: str):

    companies = pd.read_csv(path)
    ticker_list = companies['Ticker'].to_list()
    print('retrieved', str(len(ticker_list)), 'ticker symbols')
    return ticker_list

def get_prices(ticker):

    print(f'getting prices data for company: {ticker}...')

    prices_full = quandl.get(f'WIKI/{ticker}')
    prices_full.to_csv(f'./data/raw/{ticker}.csv', index=True)

    prices = prices_full['Adj. Close'].reset_index()
    prices['Ticker'] = ticker

    return prices

def acquire(path, api_key):

    # quandl api key setup
    print(f'setting quandl api key: {api_key}...')
    setup_quandl(api_key)

    #reading companies from file
    print(f'getting tickers form path: {path}...')
    tickers = get_tickers(path)


    # getting stocks from quandl
    print('getting data from quandl...')
    prices_dfs = []
    for ticker in tqdm(tickers):
        prices = get_prices(ticker)
        prices_dfs.append(prices)

    return prices_dfs
