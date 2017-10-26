# -*- coding: utf-8 -*-

from sklearn.linear_model import (
    Ridge, LinearRegression, TheilSenRegressor, RANSACRegressor, HuberRegressor, LassoCV, ElasticNetCV)
from sklearn.model_selection import cross_val_score
from scipy.stats import norm
#from sklearn.cross_validation import cross_val_score
from scipy import stats
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn import ensemble

import pandas as pd
from pandas import Series, DataFrame

#numpy, matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

DataTrain = pd.read_csv("DataTrain.csv")
#print DataTrain.head()
#print DataTrain.info()
#print DataTrain.describe(include = 'all')

house_prices = pd.read_csv("house_prices.csv")
#print house_prices.info()

missing = pd.read_csv("missing.csv")

#print missing.info()

TrainData1 = DataTrain.loc[DataTrain['House ID'].isin(house_prices['House ID'])]
TestData = DataTrain.loc[DataTrain['House ID'].isin(missing['House ID'])]
#print TrainData1.head()
#print house_prices.head()


TrainData = TrainData1.merge(house_prices, on="House ID", how="outer")

#print TrainData.head()
#print TrainData.info()

id1 = TestData["House ID"]
TrainData = TrainData.drop("House ID",axis = 1)
TestData = TestData.drop("House ID",axis = 1)

fullData = [TrainData, TestData]

Location_mapping = {"No Location":0,
                    "Servant's Premises" : -2,
                  "The Mountains" : -1
                  , "King's Landing":6, 
                  "Cursed Land":-3
                  }


for data in fullData:
    data['Location'] = data['Location'].map(Location_mapping)

'''
TrainData["Date Built"] = pd.to_datetime(TrainData["Date Built"])
TestData["Date Built"] = pd.to_datetime(TestData["Date Built"])

TrainData["Date Priced"] = pd.to_datetime(TrainData["Date Priced"])
TestData["Date Priced"] = pd.to_datetime(TestData["Date Priced"])
'''

'''for col in fareTrain:
    print (type(fareTrain[col][1]))
'''
'''

column_1 = TrainData["Date Built"]
data1 = pd.DataFrame({
            "year1": column_1.dt.year,
             "month1" :column_1.dt.month,
             "day1":column_1.dt.day,
             "hour1":column_1.dt.hour,
             "minute1" :column_1.dt.minute,
             "second1":column_1.dt.second,
             })
#fareTrain = fareTrain.append(data1)
TrainData = pd.concat([TrainData, data1], axis=1)
    
    
column_1 = TestData["Date Built"]
data1 = pd.DataFrame({
             "year1": column_1.dt.year,
             "month1" :column_1.dt.month,
             "day1":column_1.dt.day,
             "hour1":column_1.dt.hour,
             "minute1" :column_1.dt.minute,
             "second1":column_1.dt.second,
             })
#fareTrain = fareTrain.append(data1)
TestData = pd.concat([TestData, data1], axis=1)

column_1 = TrainData["Date Priced"]
data1 = pd.DataFrame({
            "year2": column_1.dt.year,
             "month2" :column_1.dt.month,
             "day2":column_1.dt.day,
             "hour2":column_1.dt.hour,
             "minute2" :column_1.dt.minute,
             "second2":column_1.dt.second,
             })
#fareTrain = fareTrain.append(data1)
TrainData = pd.concat([TrainData, data1], axis=1)
    
    
column_1 = TestData["Date Priced"]
data1 = pd.DataFrame({
             "year2": column_1.dt.year,
             "month2" :column_1.dt.month,
             "day2":column_1.dt.day,
             "hour2":column_1.dt.hour,
             "minute2" :column_1.dt.minute,
             "second2":column_1.dt.second,
             })
#fareTrain = fareTrain.append(data1)
TestData = pd.concat([TestData, data1], axis=1)
   
 

TrainData["Date Built"] = TrainData["Date Built"].astype(str)
TrainData["Date Priced"] = TrainData["Date Priced"].astype(str)

print TrainData.head()
print TrainData.info()
'''

#TrainData = TrainData.drop("Date Built",axis=1)
#TestData = TestData.drop("Date Built",axis=1)
#TrainData = TrainData.drop("Date Priced",axis=1)
#TestData = TestData.drop("Date Priced",axis=1)


#print TrainData.head()
#print TestData.head()

TrainData = TrainData.dropna(axis=0, how='all')
TestData = TestData.dropna(axis=0, how='all')


#TrainData = TrainData.drop(TrainData.index[16500:20000])
#TestData = TestData.drop(TestData.index[0:1073])
#print TrainData.info()
#print TestData.info()



LST = ["GARDEN SPACE","Renovation","bathrooms","bedrooms","blessings","dining rooms","pay","sorcerer","tree", "Location","Date Built Y","Date Priced Y", "Date Built M","Date Priced M","Meridian1","Meridian2"]
TrainData[LST] = TrainData[LST].astype(int)


#TrainData["Date"] = TrainData["Date Priced"] - TrainData["Date Built"]
#TestData["Date"] = TestData["Date Priced"] - TestData["Date Built"]
#TrainData = TrainData.drop("Date Built",axis=1)
#TestData = TestData.drop("Date Built",axis=1)
#TrainData = TrainData.drop("Date Priced",axis=1)
#TestData = TestData.drop("Date Priced",axis=1)
#print TrainData.info()


#print TestData

'''
sns.set(style="ticks", color_codes=True)
grid = sns.PairGrid(TrainData)
grid.map( plt.scatter )
'''


'''
colormap = plt.cm.viridis
plt.figure(figsize = (15,15))
plt.title('Correlation of Features', y = 1.05, size = 15)
sns.heatmap(TrainData.corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
'''




'''
var = 'Location'
data = pd.concat([TrainData['Golden Grains'], TrainData[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y="Golden Grains", data=data)
fig.axis(ymin=500000, ymax=1000000);

'''
     


DropElements = ["Knights house","Renovation","Meridian1","Meridian2","Time1","Time2"]
TrainData = TrainData.drop(DropElements,axis = 1)
TestData = TestData.drop(DropElements,axis = 1)

Train1 = TrainData[:11550]
Train2 = TrainData[11550:]

Y_train = Train1["Golden Grains"]
Y_test = Train2["Golden Grains"]
X_train = Train1.drop("Golden Grains",axis = 1)
X_test = Train2.drop("Golden Grains",axis = 1)

#ax = sns.distplot(Y_train)

model = ensemble.GradientBoostingRegressor(n_estimators=3000, learning_rate=0.035, max_depth=2, max_features='sqrt',
                                               min_samples_leaf=15, min_samples_split=10, loss='huber')

model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print r2_score(Y_test,Y_pred)*200



'''
degree = 3
model = make_pipeline(PolynomialFeatures(degree),LinearRegression())
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print r2_score(Y_test,Y_pred)*200
   
'''
'''

StackingSubmission = pd.DataFrame({"House ID":id1,"Golden Grains": Y_pred })
StackingSubmission["House ID"] = StackingSubmission["House ID"]
StackingSubmission["Golden Grains"] = StackingSubmission["Golden Grains"]
StackingSubmission = StackingSubmission[["House ID","Golden Grains"]]
StackingSubmission = missing.merge(StackingSubmission, on="House ID", how="outer")

StackingSubmission.to_csv("predicted.csv", index=False)
'''