import pandas as pd
import time
import requests

def fetch_real_time_data(market="KRW-BTC"):
    url = f"https://api.upbit.com/v1/candles/minutes/1"
    params = {"market": market, "count": 10}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            # DataFrame으로 바로 반환
            return pd.DataFrame([{
                "trade_price": data[0]["trade_price"],
                "timestamp": data[0]["timestamp"],
                "feature_1": 0.0,  # 추가 feature 계산 가능
                "feature_2": 0.0,
                "feature_3": 0.0,
                "feature_4": 0.0,
                "feature_5": 0.0
            }])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching real-time data: {e}")
        return None
