
# [Format]
#
# HC_DecisionTree(X_train, y_train):
# DecisionTree 생성 -> 하이퍼파라미터 튜닝(Grid 5분할 교차검증) -> 10번 시행 평균
#
# HC_RandomForest(X_train, y_train):
# RandomForest 생성 -> 하이퍼파라미터 튜닝(Grid 5분할 교차검증) -> 3번 시행 평균
#
# HC_LogisticRegression(X_train, y_train):
# LogisticRegression 생성 -> 10번 시행 평균


def HC_DecisionTree(x, y):
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import GridSearchCV

    # 정확도 평균 계산용 배열
    accuracy_arr = []

    # 하이퍼 파라미터 후보 값 지정
    param = {
        'max_depth' : [1, 2, 3, 4],
        'min_samples_leaf' : [1, 2, 3, 4],
        'min_samples_split' : [4, 5, 6, 7, 8]
    }

    for i in range(10):
        # 데이터 분할(0.8 : 0.2)
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # DecisionTree모델 생성&학습
        dt_classifier = DecisionTreeClassifier(random_state=None)
        grid_dt_classifier = GridSearchCV(dt_classifier, param_grid=param, scoring='accuracy', cv=5, n_jobs=1)
        grid_dt_classifier.fit(X_train, y_train)

        pred_withBP = grid_dt_classifier.best_estimator_.predict(X_test)
        accuracy = accuracy_score(y_test, pred_withBP)
        accuracy_arr.append(accuracy)
    print(f"\n[DecisionTree Average Accuracy: {round((sum(accuracy_arr)/len(accuracy_arr)), 4) * 100} %]")


def HC_RandomForest(x, y):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import GridSearchCV
    
    # 정확도 평균 계산용 배열
    accuracy_arr = []

    # 하이퍼 파라미터 후보 값 지정
    param = {
        'max_depth' : [1, 2, 3, 4],
        'min_samples_leaf' : [1, 2, 3, 4],
        'min_samples_split' : [4, 5, 6, 7, 8]
    }

    for i in range(5):
        # 데이터 분할(0.8 : 0.2)
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # DecisionTree모델 생성&학습
        rf_classifier = RandomForestClassifier(random_state=None)
        grid_rf_classifier = GridSearchCV(rf_classifier, param_grid=param, scoring='accuracy', cv=5, n_jobs=1)
        grid_rf_classifier.fit(X_train, y_train)

        pred_withBP = grid_rf_classifier.best_estimator_.predict(X_test)
        accuracy = accuracy_score(y_test, pred_withBP)
        accuracy_arr.append(accuracy)

        #/print(f"HyperParameters: {grid_dt_classifier.best_params_}")

    print(f"\n[RandomForest Average Accuracy: {round((sum(accuracy_arr)/len(accuracy_arr)), 4) * 100} %]")


def HC_LogisticRegression(x, y):
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    accuracy_arr = []
    
    # 하이퍼 파라미터 후보 값 지정
    param = {
        'max_depth' : [1, 2, 3, 4],
        'min_samples_leaf' : [1, 2, 3, 4],
        'min_samples_split' : [4, 5, 6, 7, 8]
    }

    for i in range(10):
        # 데이터 분할(0.8 : 0.2)
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # LogisticRegression모델 생성&학습
        lr_classifier = LogisticRegression(max_iter=10000)
        lr_classifier.fit(X_train, y_train)

        # 테스트 데이터 예측
        pred = lr_classifier.predict(X_test)

        # 정확도 계산
        accuracy = accuracy_score(y_test, pred)
        accuracy_arr.append(accuracy)
        
    print(f"\n[LogisticRegression Average Accuracy: {round(accuracy_score(y_test, pred), 4) * 100} %]\n")

