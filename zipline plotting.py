from zipline.api import order, record, symbol
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), 'price'))


def analyse(context, perf):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    perf.portfolio_value.plot(ax=ax1)
    ax1.set_ylabel('portfolio % value')
    plt.legend(loc=0)
    plt.show()

