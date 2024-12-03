import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
data = pd.read_csv('data/processed/candles_processed.csv')

# 그래프 저장 폴더 설정
output_folder = 'eda_outputs/'
import os
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 1. 기술적 지표의 분포 분석 (RSI, MACD, 볼린저 밴드 등)
def plot_technical_indicators_distribution(data):
    plt.figure(figsize=(10, 6))
    plt.hist(data['rsi'], bins=50, alpha=0.7, color='blue', label='RSI')
    plt.title('RSI Distribution')
    plt.xlabel('RSI')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f'{output_folder}rsi_distribution.png')
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.hist(data['macd'], bins=50, alpha=0.7, color='orange', label='MACD')
    plt.hist(data['macd_signal'], bins=50, alpha=0.7, color='green', label='Signal')
    plt.title('MACD and Signal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f'{output_folder}macd_distribution.png')
    plt.close()

# 2. 지표 간 상관관계 분석
def plot_correlation_matrix(data):
    indicators = ['rsi', 'macd', 'macd_signal', 'bollinger_upper', 'bollinger_lower', 'volatility']
    corr_matrix = data[indicators].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix of Technical Indicators')
    plt.savefig(f'{output_folder}correlation_matrix.png')
    plt.close()

# 3. 거래량과 가격 변화 간의 관계
def plot_volume_vs_price_change(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['candle_acc_trade_volume'], data['price_change_ratio'], alpha=0.5)
    plt.title('Volume vs Price Change Ratio')
    plt.xlabel('Volume')
    plt.ylabel('Price Change Ratio')
    plt.savefig(f'{output_folder}volume_vs_price_change.png')
    plt.close()

# 4. 시간대별 기술적 지표 분석
def plot_hourly_rsi(data):
    data['hour'] = pd.to_datetime(data['candle_date_time_kst']).dt.hour
    hourly_rsi = data.groupby('hour')['rsi'].mean()
    plt.figure(figsize=(10, 6))
    hourly_rsi.plot(kind='bar', color='blue')
    plt.title('Average RSI by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Average RSI')
    plt.savefig(f'{output_folder}hourly_rsi.png')
    plt.close()

# 5. 과매수/과매도 구간 분석
def plot_overbought_oversold_analysis(data):
    overbought = data[data['rsi'] > 70]
    oversold = data[data['rsi'] < 30]

    plt.figure(figsize=(10, 6))
    plt.hist(overbought['price_change_ratio'], bins=50, alpha=0.5, label='Overbought', color='red')
    plt.hist(oversold['price_change_ratio'], bins=50, alpha=0.5, label='Oversold', color='green')
    plt.title('Price Change Ratio in Overbought/Oversold Regions')
    plt.xlabel('Price Change Ratio')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(f'{output_folder}overbought_oversold_analysis.png')
    plt.close()

# 실행
if __name__ == '__main__':
    print("Performing EDA...")
    plot_technical_indicators_distribution(data)
    plot_correlation_matrix(data)
    plot_volume_vs_price_change(data)
    plot_hourly_rsi(data)
    plot_overbought_oversold_analysis(data)
    print(f"EDA Completed. Graphs are saved in the '{output_folder}' folder.")
