import tensorflow as tf


# 기본 tensor 만들기
# tensor에는 숫자, 리스트 등을 할당할 수 있음
# tensor 자료형은 행렬연산에 용이함
tensor = tf.constant([0, 10])
tensor2 = tf.constant([5,6])
tensor3 = tf.constant([[1, 2],
                      [3, 4]]
                      )
print(tensor * tensor2)
print(tensor * tensor3)
print(tf.add(tensor, tensor3))
# tf. // add, subtract, divide, multiply, matmul

# 0으로만 구성된 tensor 형성
tensor4 = tf.zeros([2,2])
print(tensor4)