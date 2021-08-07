import joblib
from sklearn.tree import DecisionTreeClassifier
from dataProj.Functions import Discretize,fit_transforms

number_of_Bins = 3

def ID3_SKlearn(train,test,structure):
    train = Discretize(number_of_Bins, train, structure)
    test = Discretize(number_of_Bins, test, structure)

    train=fit_transforms(train)
    train_target= train['class']
    train_feature=train.drop('class', axis='columns')

    test=fit_transforms(test)
    test_target= test['class']
    test_feature=test.drop('class', axis='columns')

    tree=DecisionTreeClassifier(criterion='entropy',max_depth=100).fit(train_feature,train_target)

    prediction = tree.predict(test_feature)

    #save model to file
    filename='ID3_SKlearn_model.sav'
    joblib.dump(tree,filename)

    return("ID3_SKlearn_algorithm accuracy is: ",tree.score(test_feature,test_target)*100,"%")
