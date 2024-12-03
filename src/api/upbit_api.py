import os
import requests
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# API URL
BASE_URL = "https://api.upbit.com/v1"

def get_candles(market="KRW-BTC", unit=5, count=10, to=None):
    """
    Upbit 캔들 데이터 가져오기
    Args:
        market (str): 마켓 이름 (예: KRW-BTC)
        unit (int): 분봉 단위 (1, 3, 5, 10, 15, ...)
        count (int): 가져올 데이터 수 (최대 200)
        to (str): 데이터 종료 시점 (ISO 8601 또는 milliseconds)
    Returns:
        list: 캔들 데이터 리스트
    """
    url = f"{BASE_URL}/candles/minutes/{unit}"
    params = {"market": market, "count": count}
    if to:
        params["to"] = to  # 특정 종료 시간 지정
    response = requests.get(url, params=params)
    response.raise_for_status()  # 오류 발생 시 예외 처리
    return response.json()

if __name__ == "__main__":
    # 테스트: BTC/KRW 분봉 데이터 가져오기
    candles = get_candles(market="KRW-BTC", unit=5, count=5)
    for candle in candles:
        print(candle)
