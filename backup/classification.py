from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neural_network import MLPClassifier
import pydot
import pandas as pd
import numpy as np


def classification(df,type):
    '''

    :param df: Diabetic dataset
    :return:
    '''
    if type == "PIMA":
        Y = df['Outcome']
        df.drop('Outcome' , inplace = True, axis =1)
    else:
        Y = df['diabetesMed']
        df.drop('diabetesMed', inplace = True, axis =1)
    X_train, X_test, Y_train, Y_test = train_test_split(df,Y, random_state=1)
    decisionTreeClassification(X_train, X_test, Y_train, Y_test)
    randomForestClassification(X_train, X_test, Y_train, Y_test)
    naiveBayesClassification(X_train, X_test, Y_train, Y_test)
    neuralNetwork(X_train, X_test, Y_train, Y_test)


def decisionTreeClassification(X_train, X_test, Y_train, Y_test):
    '''

    :param X_train:
    :param X_test:
    :param Y_train:
    :param Y_test:
    :return:
    '''

    model = DecisionTreeClassifier(max_depth= 5)
    model.fit(X_train, Y_train)
    Y_predict = model.predict(X_test)
    print("Accuracy using Decision Tree", accuracy_score(Y_test, Y_predict)*100,"%")
    data = export_graphviz(model, out_file= 'diabetes.dot', feature_names= X_train.columns)
    (graph,) = pydot.graph_from_dot_file('diabetes.dot')
    graph.write_png('diabetes_pima.png')
    print("Confusion Matrix of Decision Tree", confusion_matrix(Y_test, Y_predict))
    print("Classification report", classification_report(Y_test, Y_predict))

    model_entropy = DecisionTreeClassifier(criterion="entropy", max_depth=5)
    model_entropy.fit(X_train, Y_train)
    Y_predict = model_entropy.predict(X_test)
    print("Accuracy using Decision Tree-Entropy", accuracy_score(Y_test, Y_predict) * 100, "%")
    data = export_graphviz(model, out_file='diabetes.dot', feature_names=X_train.columns)
    (graph,) = pydot.graph_from_dot_file('diabetes.dot')
    graph.write_png('diabetes_pima_entropy.png')
    print("Confusion Matrix of Decision Tree", confusion_matrix(Y_test, Y_predict))
    print("Classification report", classification_report(Y_test, Y_predict))


def randomForestClassification(X_train, X_test, Y_train, Y_test):
    '''

    :param X_train:
    :param X_test:
    :param Y_train:
    :param Y_test:
    :return:
    '''
    model = RandomForestClassifier()
    model.fit(X_train, Y_train)
    Y_predict = model.predict(X_test)
    print("Accuracy for Random Forest Classifier", accuracy_score(Y_test, Y_predict)*100, "%")
    print("Confusion Matrix of Random Forest classifier", confusion_matrix(Y_test, Y_predict))
    print("Classification report", classification_report(Y_test, Y_predict))
    # model = RandomForestRegressor()
    # model.fit(X_train, Y_train)
    # Y_predict = model.predict(X_test)
    # print("Accuracy for Random Forest Regressor", accuracy_score(Y_test, Y_predict) * 100)
    # print("Confusion Matrix of Random Forest Regressor", confusion_matrix(Y_test, Y_predict))

def naiveBayesClassification(X_train, X_test, Y_train, Y_test):
    '''

    :param X_train:
    :param X_test:
    :param Y_train:
    :param Y_test:
    :return:
    '''
    model = GaussianNB()
    model.fit(X_train, Y_train)
    Y_predict = model.predict(X_test)
    print("Accuracy for Gaussian Naive Bayes Classifier", accuracy_score(Y_test, Y_predict) * 100, "%")
    print("Confusion Matrix of Naive Bayes classifier", confusion_matrix(Y_test, Y_predict))
    print("Classification report", classification_report(Y_test, Y_predict))

    model = MultinomialNB()
    model.fit(X_train, Y_train)
    Y_predict = model.predict(X_test)
    print("Accuracy for Multinomial Naive Bayes Classifier", accuracy_score(Y_test, Y_predict) * 100, "%")
    print("Confusion Matrix of Naive Bayes classifier", confusion_matrix(Y_test, Y_predict))
    print("Classification report", classification_report(Y_test, Y_predict))

def neuralNetwork(X_train, X_test, Y_train, Y_test):
    '''

    :param X_train:
    :param X_test:
    :param Y_train:
    :param Y_test:
    :return:
    '''
    model = MLPClassifier(hidden_layer_sizes = 9,  max_iter= 800)
    model.fit(X_train, Y_train)
    Y_predict = model.predict(X_test)
    print("Accuracy for Artificial Neural Network classifier", accuracy_score(Y_test, Y_predict) * 100, "%")
    print("Confusion Matrix of Artificial Neural Network classifier", confusion_matrix(Y_test, Y_predict))
    print("Classification report", classification_report(Y_test, Y_predict))


