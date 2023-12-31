# 딥러닝 모델 만들기(자동) + 학습

# 데이터 전처리
import pandas as pd

data = pd.read_csv('DataAnalysis/DeepLearning/gpascore.csv')
data = data.dropna()
# data.fillna()도 가능

y = data['admit']
x = data.drop(columns='admit')
x = x.values.tolist()

# x, y 값이 list면 fit에 넣을 수 없기 때문에 numpy array로 변환
import numpy as np

x = np.array(x)
y = np.array(y)

# 모델 만들기
import tensorflow as tf

# 모델 생성
model = tf.keras.models.Sequential([
    # 레이어 1 생성(노드 개수 -> 실험적, 주로 2의 배수 + 활성함수 종류)
    tf.keras.layers.Dense(16, activation='sigmoid'),
    # 레이어 2 생성...
    tf.keras.layers.Dense(32, activation='tanh'),
    tf.keras.layers.Dense(4, activation='relu'),
    # 출력 레이어 생성(노드 1개)
    # 출력 레이어의 결과값은 0~1 사이의 값으로 출력하고 싶기 때문에 sigmoid를 사용했음
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# 모델 완성
# compile(최적화 함수(adam, sgd, adagrad...))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 모델 학습
# fit(x, y, epochs)
model.fit(x, y, epochs=500)


# 모델 사용해서 예측
predict1, predict2 = model.predict(np.array([[930, 3.51, 1], [200, 1.41, 1]]))

print(predict1, predict2)