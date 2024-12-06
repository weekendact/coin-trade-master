import pandas as pd

def label_data(data, threshold_up=0.02, threshold_down=-0.02):
    """
    라벨링 함수: 가격 변동성을 기준으로 라벨 생성
    - 1: 가격이 threshold_up 이상 상승
    - -1: 가격이 threshold_down 이하 하락
    - 0: 그 외의 경우
    
    Args:
        data (pd.DataFrame): 데이터프레임, 'price_change_ratio' 컬럼 포함 필요.
        threshold_up (float): 상승 임계값.
        threshold_down (float): 하락 임계값.
        
    Returns:
        pd.DataFrame: 라벨링된 데이터.
    """
    data['label'] = 0
    data.loc[data['price_change_ratio'] >= threshold_up, 'label'] = 1
    data.loc[data['price_change_ratio'] <= threshold_down, 'label'] = -1
    return data
