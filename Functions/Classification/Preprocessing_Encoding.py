# [Format]
#
# HC_LableEncoder(dataset)
# HC_OneHotEncoder(dataset)
# HC_DummyEncoder(dataset or dataframe)


# LableEncoder: 문자열 형태의 데이터를 정수형 데이터로 치환
def HC_LableEncoder(dataset):
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()

    # 인코더에 dataset 학습
    encoder.fit(dataset)
    print(f"Classes: {encoder.classes_}")

    # 인코딩된 값으로 dataset 변환
    dataset_modified = encoder.transform(dataset)
    print(f"dataset1_original: {dataset}")
    print(f"dataset1_modified: {dataset_modified}")
    return dataset_modified

# OneHotEncoder: 문자열 형태의 데이터를 길이가 총 데이터 종류인 배열 값으로 치환
# 배열은 0과 1로 구성되며, 1은 한 개의 인덱스에만 존재
# 예시: [0, 0, 0, 0, 0, 1, 0, 0] --> 데이터 8종류, 6번째 분류
def HC_OneHotEncoder(dataset):
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    # 정수형으로 변환 + 2차원 세로 배열로 변환
    encoder = LabelEncoder()

    # 인코더에 dataset 학습
    encoder.fit(dataset)
    print(f"Classes: {(encoder.classes_)}")
    # 인코딩된 값으로 dataset 변환
    dataset_modified1 = encoder.transform(dataset)
    dataset_modified2 = dataset_modified1.reshape(-1, 1)

    
    encoder = OneHotEncoder(sparse_output=True) # sparse_output(True = 희소행렬, False = 밀집행렬)
    # 변환된 dataset을 OneHotEncoder에 학습
    encoder.fit(dataset_modified2)
    # 다시 변환
    dataset_modified3 = encoder.transform(dataset_modified2)
    print(dataset_modified3)
    return dataset_modified3


# DummyEncoder: pandas의 함수
# 단 한줄로 원하는 데이터셋/프레임을 원하는 자료형의 값으로 인코딩
def HC_DummyEncoder(dataset):
    import pandas as pd
    # dataset을 dtype의 형태로 원핫인코딩
    dataset_modified = pd.get_dummies(dataset, dtype=int)
    print(dataset_modified)
    return dataset_modified
