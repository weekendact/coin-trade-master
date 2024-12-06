import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 파일 경로
TRAIN_PATH = 'data/labeled/X_train_labeled.csv'
VAL_PATH = 'data/labeled/X_val_labeled.csv'
TEST_PATH = 'data/labeled/X_test_labeled.csv'

# 데이터 로드
print("Loading labeled data...")
X_train = pd.read_csv(TRAIN_PATH)
X_val = pd.read_csv(VAL_PATH)
X_test = pd.read_csv(TEST_PATH)

# 라벨 분리
y_train = X_train.pop('label')
y_val = X_val.pop('label')
y_test = X_test.pop('label')

# 정규화 (스케일링)
print("Scaling data...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# 결과 저장 (분리된 데이터와 스케일링된 데이터를 저장)
print("Saving processed data...")
pd.DataFrame(X_train_scaled, columns=X_train.columns).to_csv('data/labeled/X_train_scaled.csv', index=False)
pd.DataFrame(X_val_scaled, columns=X_val.columns).to_csv('data/labeled/X_val_scaled.csv', index=False)
pd.DataFrame(X_test_scaled, columns=X_test.columns).to_csv('data/labeled/X_test_scaled.csv', index=False)

y_train.to_csv('data/labeled/y_train.csv', index=False)
y_val.to_csv('data/labeled/y_val.csv', index=False)
y_test.to_csv('data/labeled/y_test.csv', index=False)

print("Data preparation completed.")
