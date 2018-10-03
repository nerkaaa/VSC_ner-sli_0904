from zipline.api import sid, schedule_function, record, get_open_orders, order_target_percent

def initialize(context):
    context.aapl = sid(24)
    schedule_function(ma_crossover_handling,
                      date_rules.every_day(),
                      time_rules.market_open(hours=1))

def ma_crossover_handling(context, data):
    hist = data.history(context.aapl, 'price', 50, '1d')
    print(hist.head())
    sma_50 = hist.mean()
    sma_20 = hist[-20:].mean

    open_orders = get_open_orders()  # patikrina ar nera jau esanciu rinkoje pavedimu

    if sma_20 > sma_50:
        if context.aapl not in open_orders:
            order_target_percent(context.aapl, 1.0)
    elif sma_50 > sma_20:
        if context.aapl not in open_orders:
            order_target_percent(context.aapl, -1.0)

    record(leverage=context.account.leverage)


