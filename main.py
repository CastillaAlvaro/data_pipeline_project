import argparse
from p_acquisition.m_acquisition import acquire
from p_wrangling.m_wrangling import build_data
from p_analysis.m_analysis import compute_returns, compute_risk_ratio, compute_corr
from p_reporting.m_reporting import report

def argument_parser():
    """
    parse arguments to script
    ArgumentParser -> Class
    parser -> Instance
    parser.add_argument -> method
    parse_args() -> method que parsea los argumentos
    """

    parser = argparse .ArgumentParser(description='pass companies and set chart type...')

    #arguments here!
    parser.add_argument("-p", "--path", help="specify companies list file", type=str, required=True)
    parser.add_argument("-k", "--key", help="quandl API key", type=str, required=True)
    # arguments here!

    args = parser.parse_args()

    return args

def main(arguments):

    print('starting process...')

    path = arguments.path
    api_key = arguments.key

    prices_dfs = acquire(path=path, api_key=api_key)
    stocks = build_data(prices_dfs)
    returns = compute_returns(stocks)
    risk_ratios = compute_risk_ratio(returns)
    top_return_risk_companies = risk_ratios.nlargest(10, 'Ratio')
    returns_corr = compute_corr(returns[top_return_risk_companies['Company'].to_list()])
    report(top_return_risk_companies, returns_corr)

    print('finished process...')



if __name__ == '__main__':

    arguments = argument_parser()
    main(arguments)

