import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os

def create_labels(data, threshold=0.005):
    """
    라벨 생성 함수
    :param data: 원본 데이터프레임
    :param threshold: 상승/하락 여부를 결정하는 기준값
    :return: 라벨이 포함된 데이터프레임
    """
    data['next_price'] = data['trade_price'].shift(-1)  # 다음 캔들의 가격
    data['price_diff'] = data['next_price'] - data['trade_price']
    data['price_change_ratio'] = data['price_diff'] / data['trade_price']
    data['label'] = (data['price_change_ratio'] > threshold).astype(int)
    return data

def prepare_data(file_path, features, output_dir):
    """
    데이터 준비 및 분할 함수
    :param file_path: 원본 데이터 경로
    :param features: 입력 데이터로 사용할 컬럼 리스트
    :param output_dir: 분할된 데이터를 저장할 디렉토리
    """
    # 데이터 로드
    data = pd.read_csv(file_path)

    # 라벨 생성
    data = create_labels(data)

    # 결측치 처리
    data = data.dropna()

    # 입력 데이터(X)와 라벨(y) 분리
    X = data[features]
    y = data['label']

    # 데이터 분할
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # 데이터 저장
    train_dir = f"{output_dir}/train"
    val_dir = f"{output_dir}/val"
    test_dir = f"{output_dir}/test"

    for dir_path in [train_dir, val_dir, test_dir]:
        os.makedirs(dir_path, exist_ok=True)

    X_train.to_csv(f"{train_dir}/X_train.csv", index=False)
    y_train.to_csv(f"{train_dir}/y_train.csv", index=False)
    X_val.to_csv(f"{val_dir}/X_val.csv", index=False)
    y_val.to_csv(f"{val_dir}/y_val.csv", index=False)
    X_test.to_csv(f"{test_dir}/X_test.csv", index=False)
    y_test.to_csv(f"{test_dir}/y_test.csv", index=False)

    print("데이터 준비 및 라벨링 완료.")
    print(f"데이터 저장 경로: {output_dir}")

if __name__ == "__main__":
    # 설정
    file_path = "data/processed/candles_processed.csv"
    features = ['rsi', 'macd', 'macd_signal', 'bollinger_upper', 'bollinger_lower', 
                'price_change_ratio', 'candle_acc_trade_volume']
    output_dir = "data"

    # 실행
    prepare_data(file_path, features, output_dir)
