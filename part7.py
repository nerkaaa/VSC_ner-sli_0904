
import pickle
import pandas as pd




def compile_data():
    """
    Takes all 500 companies and takes Adj Close data,
    renames it to companies ticker
    puts everything in to one file: sp500_joined_closes.csv
    :return: file  sp500_joined_closes.csv
    """
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df = pd.DataFrame()
    for count, ticker in enumerate(tickers):
        ticker = ticker.replace(".", "-")
        try:
            df = pd.read_csv('stock_dfs/{}.csv'. format(ticker))
        except IOError:
            continue

        df.set_index('Date', inplace=True)
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['High','Low','Open','Close','Volume'], 1, inplace=True)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')

        if count % 10 == 0:
            print count

    main_df.to_csv('sp500_joined_closes.csv')

