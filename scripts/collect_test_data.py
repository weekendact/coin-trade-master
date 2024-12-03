from src.api.upbit_api import get_candles
from src.utils.data_saver import save_to_csv

def collect_test_data(market="KRW-BTC", unit=5, count=10, filename="data/test/candles_test.csv"):
    """
    테스트 데이터를 수집하고 CSV 파일로 저장
    Args:
        market (str): 마켓 이름 (예: KRW-BTC)
        unit (int): 분봉 단위 (1, 3, 5, 10, ...)
        count (int): 가져올 데이터 개수 (최대 200)
        filename (str): 저장할 파일 경로
    """
    print(f"Collecting test data for {market} (unit={unit}, count={count})...")
    data = get_candles(market=market, unit=unit, count=count)
    save_to_csv(data, filename)
    print(f"Test data collection complete. Saved to {filename}")


if __name__ == "__main__":
    collect_test_data()
