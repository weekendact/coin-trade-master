import pandas as pd
from src.utils.labeling import label_data

# 입력 파일 경로
TRAIN_PATH = 'data/train/X_train.csv'
VAL_PATH = 'data/val/X_val.csv'
TEST_PATH = 'data/test/X_test.csv'

# 출력 파일 경로
TRAIN_OUTPUT = 'data/labeled/X_train_labeled.csv'
VAL_OUTPUT = 'data/labeled/X_val_labeled.csv'
TEST_OUTPUT = 'data/labeled/X_test_labeled.csv'

def main():
    # 데이터 로드
    print("Loading data...")
    train_data = pd.read_csv(TRAIN_PATH)
    val_data = pd.read_csv(VAL_PATH)
    test_data = pd.read_csv(TEST_PATH)

    # 라벨링 수행
    print("Labeling data...")
    train_data = label_data(train_data)
    val_data = label_data(val_data)
    test_data = label_data(test_data)

    # 라벨링된 데이터 저장
    print("Saving labeled data...")
    train_data.to_csv(TRAIN_OUTPUT, index=False)
    val_data.to_csv(VAL_OUTPUT, index=False)
    test_data.to_csv(TEST_OUTPUT, index=False)

    print("Data labeling completed!")

if __name__ == '__main__':
    main()
