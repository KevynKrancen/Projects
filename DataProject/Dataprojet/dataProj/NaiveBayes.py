import joblib
import pandas as pd
from dataProj.Functions import getColumnTitles, Discretize, valuesType, probability_ArrayByFeature

#column=['campaign','previous','age','balance','day','duration']
number_Of_Bins = 3

def allArraysOfFetures(table, classCol):
    thisDict = {}
    for i in getColumnTitles(table):
        if i not in classCol:
            for j in valuesType(table, classCol):
                thisDict[i, j] = probability_ArrayByFeature(table, i, j, classCol)
                # print(pArrayByFeature(train,i,j,classCol))
    return thisDict

def naiveBayes(test, train,structure):
    train = Discretize(number_Of_Bins, train, structure)
    test = Discretize(number_Of_Bins, test, structure)
    thisDict=allArraysOfFetures(train, 'class')

    #save model to file
    filename='NaiveBayes_model.sav'
    joblib.dump(thisDict,filename)

    rows = test.shape[0]
    classMatch = 0
    classDismatch = 0

    column = getColumnTitles(test)[:-1]  # clean 'class' column
    for _ in range(rows):
        NO = 1
        YES = 1
        for col in column:
            try:
                index = valuesType(train, col).index(test.iloc[_][col])
                YES *= thisDict[(col,'yes')][index]
                NO *= thisDict[(col,'no')][index]
            except:
                continue
        if YES > NO:
            if test.iloc[_]['class'] == 'yes':
                classMatch += 1
            else:
                classDismatch += 1
        else:
            if test.iloc[_]['class'] == 'no':
                classMatch += 1
            else:
                classDismatch += 1
    print(classMatch / rows)
    return (classMatch / rows)