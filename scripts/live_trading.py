import time
import pandas as pd
from src.api.upbit_realtime_api import fetch_real_time_data
from src.models.lightgbm_model import load_model, predict
from src.strategies.trading_logic import trade_logic, trade_log

# 초기 설정
INITIAL_BALANCE = 10000  # 10,000 KRW
balance = INITIAL_BALANCE
assets = 0
model_path = "models/lightgbm_model.pkl"
TRADE_FEE_RATE = 0.001  # 수수료

def main():
    global balance, assets
    print("Loading model...")
    model = load_model(model_path)

    print("Starting live trading simulation...")
    start_time = time.time()
    duration = 30 * 60  # 30 minutes

    while time.time() - start_time < duration:
        # 실시간 데이터 수집
        data_df = fetch_real_time_data()
        if data_df is None:
            print("Failed to fetch data. Retrying...")
            time.sleep(30)  # 재시도 간 대기 시간 증가
            continue

        print(f"Real-time data fetched:\n{data_df}")

        # 모델 예측
        try:
            prediction = predict(model, data_df)
            print(f"Prediction: {prediction}")
        except Exception as e:
            print(f"Error during prediction: {e}")
            time.sleep(30)
            continue

        # 매매 로직 실행
        current_price = data_df["trade_price"].iloc[0]
        balance, assets = trade_logic(current_price, prediction[0], balance, assets, TRADE_FEE_RATE)

        # 60초 대기
        time.sleep(60)

    # 결과 출력
    print("\n=== Trade Log ===")
    for log in trade_log:
        print(log)

    final_value = balance + (assets * current_price if assets > 0 else 0)
    print(f"\nFinal Balance: {balance:.2f} KRW")
    print(f"Final Assets: {assets:.5f}")
    print(f"Total Value: {final_value:.2f} KRW")
    roi = ((final_value / INITIAL_BALANCE) - 1) * 100
    print(f"ROI: {roi:.2f}%")

if __name__ == "__main__":
    main()
