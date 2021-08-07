import pandas as pd
from KNNClassifier import KNNClassifier
from NaiveBayes import naiveBayes
from Id3 import ID3_algorithm
from Id3SKlearn import ID3_SKlearn
from sklearnNaiveBayes import sklearnNaiveBayes

#importing the DataSets
struct_File= 'C:/Users/shira/Documents/כריית נתונים/Structure.txt'
train_File="C:/Users/shira/Documents/כריית נתונים/train.csv"
test_File="C:/Users/shira/Documents/כריית נתונים/test.csv"

#define the datasets
train = pd.read_csv(train_File)
test = pd.read_csv(test_File)

#implementation
naiveBayes(test,train,struct_File)
sklearnNaiveBayes(test,train,struct_File)
ID3_algorithm(train,test,struct_File)
ID3_SKlearn(train,test,struct_File)
KNNClassifier(train,struct_File)
