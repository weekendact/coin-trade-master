from src.api.upbit_api import get_candles
from src.utils.data_saver import save_to_csv

def collect_and_save_data(market="KRW-BTC", unit=5, count=200, filename="data/raw/candles.csv"):
    """
    Upbit 데이터를 수집하고 CSV 파일로 저장
    Args:
        market (str): 마켓 이름 (예: KRW-BTC)
        unit (int): 분봉 단위 (1, 3, 5, 10, ...)
        count (int): 가져올 데이터 수
        filename (str): 저장할 파일 경로
    """
    print(f"Collecting data for {market}...")
    data = get_candles(market=market, unit=unit, count=count)
    print(f"Saving data to {filename}...")
    save_to_csv(data, filename)
    print("Data collection and saving complete.")

if __name__ == "__main__":
    # 실제 데이터 수집 및 저장 실행
    collect_and_save_data()
