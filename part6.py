import pickle
import os
import datetime as dt
import pandas_datareader.data as web


def get_data_from_yahoo(reload=False):
    if reload:
        import part5
        part5.save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    start = dt.datetime(2016,1,1)
    end = dt.datetime(2018,10,1)
    for ticker in tickers:
        ticker = ticker.replace('.', '-')
        print ticker
        if not os.path.exists('stock_dfs_full/{}.csv'.format(ticker)):
            try:
                df = web.DataReader(ticker, 'yahoo', start, end)
            except KeyError:
                continue
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print "ticker exists: {}".format(ticker)

