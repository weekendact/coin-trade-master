import pandas as pd
from src.strategies.signal_generator import generate_signals
from src.utils.metrics import calculate_roi, calculate_win_rate
from src.utils.visualization import plot_profit_distribution

# 초기 설정
INITIAL_BALANCE = 10000000
entry_price = None  # entry_price를 초기화합니다.

# 데이터 로드
data = pd.read_csv("data/processed/candles_processed.csv")

# 매수/매도 신호 생성
data = generate_signals(data)

# 백테스트 로직
balance = INITIAL_BALANCE
trade_count = 0
win_count = 0
profits = []

for _, row in data.iterrows():
    if row["buy_signal"] and entry_price is None:  # 매수 신호가 활성화되고, 현재 포지션이 없을 때
        entry_price = row["trade_price"]
    elif row["sell_signal"] and entry_price is not None:  # 매도 신호가 활성화되고, 매수 포지션이 있을 때
        profit = (row["trade_price"] - entry_price) / entry_price * 100
        profits.append(profit)
        trade_count += 1
        if profit > 0:
            win_count += 1
        entry_price = None  # 매도 후 포지션 해제

# ROI 계산
final_balance = balance * (1 + sum(profits) / 100)
roi = calculate_roi(INITIAL_BALANCE, final_balance)
win_rate = calculate_win_rate(win_count, trade_count)

# 결과 출력
print(f"Initial Balance: {INITIAL_BALANCE} KRW")
print(f"Final Balance: {final_balance:.2f} KRW")
print(f"ROI: {roi:.2f}%")
print(f"Number of Trades: {trade_count}")
print(f"Win Rate: {win_rate:.2f}%")

# 결과 시각화
plot_profit_distribution(profits)
