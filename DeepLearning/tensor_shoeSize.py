# 딥러닝 모델 만들기(수동)

import tensorflow as tf

# 키(h), 신발 사이즈(s) 사이의 관계 추론
# 신발사이즈가 주어졌을 때, 키를 예측하는 프로그램

h = [170]
s = [260]

# 식:
# tensor 변수 생성, 초기값 = 0.x
a = tf.Variable(0.00001)
b = tf.Variable(0.9)
h = a*s + b

# 손실함수 정의
# = (실제값 - 예측값)^2
def loss_function():
    return tf.square(170 - (a*s + b))


# 경사하강법에 사용할 optimizer 생성, learning rate optimizer = Adam, 초기값 = 0.1
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

# 경사하강 하기(100번)
# optimizer.minimize(손실함수, 경사하강법으로 조정할 가중치 변수 목록)
for i in range(500):
    optimizer.minimize(loss_function, var_list=[a,b])
    if i % 100 == 0:
        print(f"w : {a.numpy()}\tb: {b.numpy()}")