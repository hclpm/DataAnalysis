from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_wine
import math

wineD = load_wine()
x = wineD.data
y = wineD.target    
accuracy_arr = []

print("\n")
for i in range(5):

    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Random Forest 모델 학습
    lr_classifier = LogisticRegression(max_iter=10000)
    lr_classifier.fit(X_train, y_train)

    # 테스트 데이터 예측
    pred = lr_classifier.predict(X_test)

    # 정확도 계산
    accuracy = accuracy_score(y_test, pred)
    print(f"Act{i:2}| Accuracy:", accuracy)
    accuracy_arr.append(accuracy)

print(f"\n[Average Accuracy: {round((sum(accuracy_arr)/len(accuracy_arr)), 4) * 100} %]\n")