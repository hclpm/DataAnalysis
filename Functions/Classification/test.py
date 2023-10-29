# function test file

################# model test ##################
from sklearn.datasets import load_wine
import models as my

wineD = load_wine()
x = wineD.data
y = wineD.target

my.HC_DecisionTree(x, y)
# my.HC_RandomForest(x, y)
# my.HC_LogisticRegression(x, y)


################# encoder test ##################
# import Preprocessing_Encoding as my
# import pandas as pd
# sample_dataset = ['a', 'a', 'b', 'a', 'c', 'c', 'b','i','u', 'y', 't', 'v', 'n']
# dataset_df = pd.DataFrame(data=sample_dataset)
# my.HC_LableEncoder(sample_dataset)
# my.HC_OneHotEncoder(sample_dataset)
# my.HC_DummyEncoder(sample_dataset)