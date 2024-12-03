import pandas as pd

def validate_processed_data(file_path="data/processed/candles_processed.csv"):
    """
    전처리된 데이터의 유효성을 검증
    Args:
        file_path (str): 전처리된 데이터 파일 경로
    """
    try:
        # 데이터 로드
        data = pd.read_csv(file_path)
        print(f"Loaded data from {file_path} with shape: {data.shape}")

        # 결측값 확인
        missing_values = data.isnull().sum()
        print("\nMissing Values:")
        print(missing_values[missing_values > 0])

        # 데이터 형식 확인
        print("\nData Types:")
        print(data.dtypes)

        # 기술적 지표 확인 (샘플 데이터)
        print("\nSample Data:")
        print(data[["trade_price", "ema_7", "ema_21", "rsi", "macd", "bollinger_upper", "bollinger_lower"]].head())

        # 주요 지표 검증
        if "rsi" in data.columns:
            print("\nRSI Range Check:")
            print(f"RSI Min: {data['rsi'].min()}, RSI Max: {data['rsi'].max()}")

        if "price_change_ratio" in data.columns:
            print("\nPrice Change Ratio Sample:")
            print(data[["price_change_ratio"]].head())

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"Error during validation: {e}")

if __name__ == "__main__":
    validate_processed_data()
