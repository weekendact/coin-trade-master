import pandas as pd
import os

def calculate_technical_indicators(data):
    """
    데이터프레임에 기술적 지표 추가
    Args:
        data (pd.DataFrame): 원본 데이터
    Returns:
        pd.DataFrame: 기술적 지표가 추가된 데이터
    """
    # EMA
    data["ema_7"] = data["trade_price"].ewm(span=7, adjust=False).mean()
    data["ema_21"] = data["trade_price"].ewm(span=21, adjust=False).mean()
    data["ema_50"] = data["trade_price"].ewm(span=50, adjust=False).mean()

    # SMA
    data["sma_7"] = data["trade_price"].rolling(window=7).mean()
    data["sma_21"] = data["trade_price"].rolling(window=21).mean()

    # Bollinger Bands
    data["sma_20"] = data["trade_price"].rolling(window=20).mean()
    data["bollinger_upper"] = data["sma_20"] + 2 * data["trade_price"].rolling(window=20).std()
    data["bollinger_lower"] = data["sma_20"] - 2 * data["trade_price"].rolling(window=20).std()

    # RSI
    delta = data["trade_price"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data["rsi"] = 100 - (100 / (1 + rs))

    # MACD
    ema_12 = data["trade_price"].ewm(span=12, adjust=False).mean()
    ema_26 = data["trade_price"].ewm(span=26, adjust=False).mean()
    data["macd"] = ema_12 - ema_26
    data["macd_signal"] = data["macd"].ewm(span=9, adjust=False).mean()

    # Volatility
    data["volatility"] = data["trade_price"].rolling(window=14).std()

    return data

def preprocess_data(input_file="data/raw/candles.csv", output_file="data/processed/candles_processed.csv"):
    """
    수집된 데이터를 전처리하여 저장
    Args:
        input_file (str): 원본 데이터 파일 경로
        output_file (str): 전처리된 데이터 저장 경로
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    data = pd.read_csv(input_file)
    print(f"Original data size: {data.shape[0]} rows, {data.shape[1]} columns")

    # 데이터 형식 변환
    data["candle_date_time_utc"] = pd.to_datetime(data["candle_date_time_utc"])
    data["candle_date_time_kst"] = pd.to_datetime(data["candle_date_time_kst"])

    # 추가 특성 생성 및 기술적 지표 계산
    data["price_change"] = data["trade_price"] - data["opening_price"]
    data["price_change_ratio"] = data["price_change"] / data["opening_price"] * 100
    data = calculate_technical_indicators(data)

    # 결측값 제거
    original_size = data.shape[0]
    data.dropna(inplace=True)
    processed_size = data.shape[0]
    print(f"Processed data size: {processed_size} rows, {data.shape[1]} columns")
    print(f"Rows removed during preprocessing: {original_size - processed_size}")

    # 정렬 및 저장
    data.sort_values("candle_date_time_utc", inplace=True)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    data.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")



if __name__ == "__main__":
    preprocess_data()
