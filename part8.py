import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import part5, part6, part7
style.use('ggplot')  #matplotlib style




part5.save_sp500_tickers()
part6.get_data_from_yahoo()
part7.compile_data()

def visualize_data():
    """

    :return: visualisation of correlated sp500 tickers
    """
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr()

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)

    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_lables = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_lables)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()


visualize_data()
