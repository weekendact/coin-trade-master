import pandas as pd

trade_log = []

def trade_logic(current_price, prediction, balance, assets, fee_rate=0.001):
    global trade_log

    if isinstance(current_price, pd.Series):
        current_price = current_price.iloc[0]

    if prediction == 2:  # 매수 신호
        if balance > 0:
            assets_bought = (balance * (1 - fee_rate)) / current_price
            assets += assets_bought
            trade_log.append(f"Buy at {current_price:.2f}, Assets: {assets:.5f}")
            balance = 0

    elif prediction == 0:  # 매도 신호
        if assets > 0:
            balance_sold = assets * current_price * (1 - fee_rate)
            balance += balance_sold
            trade_log.append(f"Sell at {current_price:.2f}, Balance: {balance:.2f}")
            assets = 0

    return balance, assets
