from src.api.upbit_api import get_candles
from src.utils.data_saver import save_to_csv
import datetime
import time

def collect_long_term_data(market="KRW-BTC", unit=5, count=200, days=1095, filename="data/raw/candles.csv"):
    """
    장기 데이터를 수집하여 CSV에 저장
    Args:
        market (str): 마켓 이름 (예: KRW-BTC)
        unit (int): 분봉 단위 (1, 3, 5, 10, ...)
        count (int): 한 번에 가져올 데이터 개수 (최대 200)
        days (int): 가져올 데이터의 총 기간 (일 단위)
        filename (str): 저장할 파일 경로
    """
    end_time = datetime.datetime.utcnow()  # 현재 시간 기준
    collected_data = []

    for _ in range(int(days * (24 * 60) / (unit * count))):
        # ISO 8601 형식으로 종료 시간 지정
        to = end_time.strftime("%Y-%m-%dT%H:%M:%S")
        print(f"Fetching data up to {to}...")

        # API 요청
        candles = get_candles(market=market, unit=unit, count=count, to=to)
        if not candles:
            break

        # 데이터 추가 및 종료 시간 갱신
        collected_data.extend(candles)
        end_time = datetime.datetime.strptime(candles[-1]["candle_date_time_utc"], "%Y-%m-%dT%H:%M:%S")

        # 속도 제한 (API 요청 사이에 대기 시간 설정)
        time.sleep(1)

    # CSV 파일에 저장
    save_to_csv(collected_data, filename)
    print(f"Data collection complete. Saved to {filename}")


if __name__ == "__main__":
    collect_long_term_data(market="KRW-BTC", unit=5, days=1095)
