import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
data_path = "data/processed/candles_processed.csv"
data = pd.read_csv(data_path)

# 시각화 스타일 설정
plt.style.use('ggplot')

# 1. 기술적 지표 분포 시각화
def plot_distributions(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['rsi'], bins=30, kde=True, color='blue', label='RSI')
    plt.title('RSI Distribution')
    plt.xlabel('RSI')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(data['price_change_ratio'], bins=30, kde=True, color='green', label='Price Change Ratio')
    plt.title('Price Change Ratio Distribution')
    plt.xlabel('Change Ratio (%)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

# 2. 상관관계 분석
def plot_correlation(data):
    corr = data[['price_change_ratio', 'rsi', 'macd', 'volatility']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

# 3. 지표와 가격 흐름 시각화
def plot_time_series(data):
    plt.figure(figsize=(14, 8))
    plt.plot(data['candle_date_time_kst'], data['trade_price'], label='Trade Price', color='black')
    plt.plot(data['candle_date_time_kst'], data['ema_7'], label='EMA 7', color='blue')
    plt.plot(data['candle_date_time_kst'], data['ema_21'], label='EMA 21', color='orange')
    plt.title('Price and Moving Averages Over Time')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# EDA 실행
plot_distributions(data)
plot_correlation(data)
plot_time_series(data)
