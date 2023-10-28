from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_wine


wineD = load_wine()
x = wineD.data
y = wineD.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


for i in range(5):
   # 데이터 분할
    # Random Forest 모델 학습
    dt_classifier = DecisionTreeClassifier(random_state=None)
    dt_classifier.fit(X_train, y_train)

    # 테스트 데이터 예측
    pred = dt_classifier.predict(X_test)

    # 정확도 계산
    accuracy = accuracy_score(y_test, pred)
    print(f"Act{i:2} Accuracy:", accuracy)