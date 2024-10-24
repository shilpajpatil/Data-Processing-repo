
import pandas as pd
import numpy as np

#read csv file

dfactivity = pd.read_csv(r"E:\Python projects 2024\Datapreprocessing\ActivityData.csv", delimiter=',',header=None)

# print readed data
print(dfactivity.head())

# print shape of the data
print(dfactivity.shape)

#calculated na values
print(dfactivity.isna().sum())

# drop NA columns
dfactivity.drop([3],axis=1, inplace=True)

#after droping columns calculated data
print(dfactivity.isna().sum())

print(dfactivity.head(3))

# gives the column name of the csv data use df.columns[]using this method

dfactivity.columns=['Phone Number-SubscribersNumber', 'Duration', 'Activity-ErrorCode']
#print(dfactivity.head(3))

#----------- spliting the colms----------------------------

dfactivity[['Phone Number','SubscribersNumber']]=dfactivity['Phone Number-SubscribersNumber'].str.split('-',n=1,expand=True)
dfactivity= dfactivity.drop(columns=['Phone Number-SubscribersNumber'])
#print(dfactivity)


dfactivity[['Activity','ErrorCode']]= dfactivity['Activity-ErrorCode'].str.split('-',expand=True)
dfactivity = dfactivity.drop(columns=['Activity-ErrorCode'])
#print(dfactivity)

#rearrenge the columns in their original sequence

dfactivity= dfactivity[["SubscribersNumber","Phone Number","Duration","Activity","ErrorCode"]]
print(dfactivity)


# replace empty value with NAN
dfactivity = dfactivity.replace('',np.NaN)
#print(dfactivity)

#print(dfactivity.isna().sum())

dfactivity["ErrorCode"].fillna(0, inplace=True)
print(dfactivity.head(5))