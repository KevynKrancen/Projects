import joblib
import numpy as np
from numpy import log2 as log
from pyitlib import discrete_random_variable as drv
from Functions import Discretize

#Machine limits for floating point types
eps = np.finfo(float).eps
number_Of_Bins=3

def find_entropy(df):
    Class = df.keys()[-1]  # To make the code generic, changing target variable class name
    entropy = 0
    values = df[Class].unique()
    for value in values:
        fraction = df[Class].value_counts()[value] / len(df[Class])
        entropy += -fraction * np.log2(fraction)
    return entropy


def find_entropy_attribute(df, attribute):
    Class = df.keys()[-1]
    # This gives all 'Yes' and 'No'
    target_variables = df[Class].unique()
    variables = df[
        attribute].unique()
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute] == variable][df[Class] == target_variable])
            den = len(df[attribute][df[attribute] == variable])
            fraction = num / (den + eps)
            entropy += -fraction * log(fraction + eps)
            fraction2 = den / len(df)
            entropy2 += -fraction2 * entropy
    return abs(entropy2)


def find_winner(df):
    Entropy_att = []
    IG = []
    for key in df.keys()[:-1]:
        IG.append(find_entropy(df) - find_entropy_attribute(df, key))
    return df.keys()[:-1][np.argmax(IG)]


def bestInfoGainAttr(data, attributes, toSplit=False):
    classEntropy = drv.entropy(data['class']).item(0)
    attrsIG = {}
    for attr in attributes:
        attrsIG[attr] = find_entropy(data) - find_entropy_attribute(data, attr)
    maxGain = max(attrsIG.values())
    for attr in attrsIG:
        if attrsIG[attr] == maxGain:
            return attr

def Build_Dictionary(data):
    attributes = {}
    for i in data:
        attr = i.split()[1]
        x = i.split()[2]
        if i.split()[2] == 'NUMERIC':
            field = list(range(number_Of_Bins))
        else:
            field = x.replace('{','').replace('}','').split(',')
        attributes[attr]=field
    return attributes

def buildingTree(classDict, data, attributes, attrList, toSplit = False,numNodes = 100):
    if len(data['class'])<=numNodes and len(data['class'])>0:
        return data['class'].mode().iloc[0]
    else:
        if len(attrList) > 0:
            bestOption = bestInfoGainAttr(data,attrList,toSplit)
            classDict[bestOption]={}
            for val in attributes[bestOption]:
                if len(data.loc[data[bestOption] == val]) > 0 and len(attrList) > 0:
                    newAttrsList = attrList.copy()
                    newAttrsList.remove(bestOption)
                    classDict[bestOption][val] = buildingTree({},data.loc[data[bestOption] == val],attributes,newAttrsList)
            return classDict
        else:
            return data['class'].mode().iloc[0]

def testing(tree, test):
    """
    tree -> decision tree dictionary
    test -> testing examples in form of pandas dataframe
    """
    res = []
    for _, e in test.iterrows():
        x = prediction(tree, e)
        res.append(x)
    return res


def prediction(tree, subFrame):
    """
    tree -- decision tree dictionary
    subFrame -- a testing example in form of pandas series
    """
    t = tree
    while isinstance(t, dict):
        root = list(t.keys())[0]
        try:
            v = subFrame[root]
        except:
            for i in t[root]:
                print('r:', root)
                print('sb|:', subFrame[root])
                if subFrame[root] in i:
                    v = i
                    break
            print('i', i)
            v = i
        try:
            t = t[root][v]
        except:
            t = t[root][list(t[root].keys())[0]]
    return t


def result(arrayExpected, arrayTest):
    match = 0
    fail = 0
    for _ in range(len(arrayExpected)):
        if arrayExpected[_] != None and arrayTest[_] != None:
            if arrayExpected[_] == arrayTest[_]:
                match += 1
            else:
                fail += 1
    print('ID3 Accuracy:', (match / (match + fail)), '%')

def ID3_algorithm(train,test,structFile):
    train = Discretize(number_Of_Bins, train, structFile)
    test = Discretize(number_Of_Bins, test, structFile)
    attributes = Build_Dictionary(open(structFile))
    attrList= list(attributes.keys())
    attrList.remove('class')
    Decision_tree = buildingTree({},train,attributes,attrList)

    #save model to file
    filename='ID3_model.sav'
    joblib.dump(Decision_tree,filename)

    result(testing(Decision_tree, test), list(test['class']))

