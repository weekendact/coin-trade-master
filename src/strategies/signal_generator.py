def generate_signals(data):
    data["buy_signal"] = (data["rsi"] < 30) & (data["macd"] > data["macd_signal"])
    data["sell_signal"] = (data["rsi"] > 70) & (data["macd"] < data["macd_signal"])
    return data
