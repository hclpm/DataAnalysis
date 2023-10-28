from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import GridSearchCV


wineD = load_wine()
x = wineD.data
y = wineD.target
accuracy_arr = []


for i in range(5):

    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Random Forest 모델 학습
    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)

    # 테스트 데이터 예측
    pred = rf_classifier.predict(X_test)

    # 정확도 계산
    accuracy = accuracy_score(y_test, pred)
    print(f"Act{i:2}| Accuracy:", accuracy)

    accuracy_arr.append(accuracy)

print(f"\n[Average Accuracy: {round((sum(accuracy_arr)/len(accuracy_arr)), 4) * 100} %]\n")



#########
# 하이퍼 파라미터 적용
#########

# 하이퍼 파라미터 후보 값 지정
param = {
    'max_depth' : [4],
    'min_samples_leaf' : [1, 2, 3, 4],
    'min_samples_split' : [4, 5, 6, 7, 8]
}

grid_rf_classifier = GridSearchCV(rf_classifier, param_grid=param, scoring='accuracy', cv=5)
grid_rf_classifier.fit(X_train, y_train)

print(f"Best Parameters: {grid_rf_classifier.best_params_}")

pred_withBP = grid_rf_classifier.best_estimator_.predict(X_test)
print(f"Accuracy of HyperParameter Applied Model: {accuracy_score(y_test, pred_withBP)}")