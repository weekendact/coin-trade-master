import csv
import os

def save_to_csv(data, filename="data/raw/candles.csv"):
    """
    데이터를 CSV 파일로 저장
    Args:
        data (list): 저장할 데이터 리스트 (JSON 형태)
        filename (str): 저장할 파일 경로
    """
    # 디렉토리 생성 (필요 시)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # 데이터 저장
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # 테스트: 샘플 데이터 저장
    sample_data = [
        {"time": "2024-12-03T10:00:00", "price": 50000},
        {"time": "2024-12-03T10:05:00", "price": 51000},
    ]
    save_to_csv(sample_data)
