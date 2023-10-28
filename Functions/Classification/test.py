from sklearn.datasets import load_wine
import models as my

wineD = load_wine()
x = wineD.data
y = wineD.target

my.HC_DecisionTree(x, y)
my.HC_RandomForest(x, y)
my.HC_LogisticRegression(x, y)