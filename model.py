#Importing required libraries
import pandas as pd
import numpy as np
import json
#Reading data file
data=pd.read_csv('C:/Users/Mari/Heroku/datasets_Person_Gender_Height_Weight_Index.csv')

#Checking if we have any missing values
data.isnull().sum()

#Checking info about data
data.info()

#Most of the Machine learning algorithms can not handle categorical variables unless we convert them to numerical values. Hence we are replacing categorical into numbers.
gender = {'Male' : 1, 'Female' : 0}
data['Gender']=data['Gender'].map(gender)

json_file= {"Gender":{'Male' : 1, 'Female' : 0}}
with open('json_file.json', 'w') as file:
    json.dump(json_file, file)

#We can see Index columns having numbers and having no information. So we can assume obesity level for those numbers as an additional column.
status = ['Extremely Weak','Weak','Normal','Overweight','Obesity','Extreme Obesity']
mapping = {i : status[i] for i in range(0,6)}
data['status']= data.Index.map(mapping)
data


x = data.drop(['Index','status'],axis=1)
y= data['Index'] 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


RFC = RandomForestClassifier(n_estimators=200, criterion='entropy', random_state=0)
model_RFC = RFC.fit(x_train, y_train)
y_pred_RFC = model_RFC.predict(x_test)
y_pred_RFC
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred_RFC)

cross_val_score(model_RFC,x,y, cv=10, scoring='accuracy')

import pickle

file = open('BMI_calc.pkl', 'wb')
pickle.dump(model_RFC, file)

#model_RFC.predict([[1,171,70]])

