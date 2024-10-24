#----step1
import pandas as pd

from scipy import stats
import numpy as np

#----step2   Read csv file
dfsubscriber = pd.read_csv(r"E:\Python projects 2024\Datapreprocessing\SubscribersData.csv")

#----step3   print some rows from csv file
print(dfsubscriber.head)

# ---step 4  it will print number of rows and columns
print(dfsubscriber.shape)

"""
output:
(505, 11)

"""
#---step 5
print(dfsubscriber.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 505 entries, 0 to 504
Data columns (total 11 columns):
 #   Column                    Non-Null Count  Dtype 
---  ------                    --------------  ----- 
 0   SubscriberIdentityNumber  505 non-null    int64 
 1   Phone Number              505 non-null    int64 
 2   Subscriber Name           505 non-null    object
 3   SSN                       505 non-null    int64 
 4   Subscriber Age            505 non-null    int64 
 5   State                     505 non-null    object
 6   Zip Code                  505 non-null    int64 
 7   SubscribedFromDate        505 non-null    object
 8   Internet Service          505 non-null    object
 9   SMS Service               501 non-null    object
 10  Churn Status              499 non-null    object
dtypes: int64(5), object(6)
memory usage: 43.5+ KB
None

Process finished with exit code 0


"""

#---- step 6 to describe the  mean max of all columns
print(dfsubscriber.describe())

"""
output:

       SubscriberIdentityNumber  Phone Number  ...  Subscriber Age      Zip Code
count              5.050000e+02  5.050000e+02  ...      505.000000    505.000000
mean               3.452812e+14  1.513510e+09  ...       38.572277  33571.891089
std                1.458411e+09  1.396134e+08  ...       14.192946  17933.348377
min                3.452787e+14  1.000000e+01  ...       15.000000   7039.000000
25%                3.452799e+14  1.526695e+09  ...       30.000000  10017.000000
50%                3.452812e+14  1.526695e+09  ...       36.000000  44115.000000
75%                3.452824e+14  1.526695e+09  ...       44.000000  44140.000000
max                3.452836e+14  1.888777e+09  ...       78.000000  85005.000000

[8 rows x 5 columns]


"""
# ----------------------------------------Data Cleaning ---------------------------------
#----step 7  to describe the all the column count of all NA values
print(dfsubscriber.isna().sum())

"""
SubscriberIdentityNumber    0
Phone Number                0
Subscriber Name             0
SSN                         0
Subscriber Age              0
State                       0
Zip Code                    0
SubscribedFromDate          0
Internet Service            0
SMS Service                 4
Churn Status                6
dtype: int64

"""



#---step 8   it will place somthing value on that empty place

dfsubscriber["SMS Service"].fillna("Active",inplace=True)
dfsubscriber["Churn Status"].fillna("Active",inplace=True)

print(dfsubscriber.isna().sum())


#step 9   --------changing droping valuers----------------------

#In some cases, it is not possible to fill the missing values and the records might be incorrect and
# does not serve the purpose for analytics.
# The best solution is to delete those rows.

print(dfsubscriber.dropna(axis=0,how='any'))
print(dfsubscriber)

"""
output:

     SubscriberIdentityNumber  Phone Number  ... SMS Service  Churn Status
0             345278656547333    1654788999  ...      Active        Active
1             345278666547334    1888777222  ...      Active        Active
2             345278676547335    1122765445  ...      Active        Active
3             345278686547336            10  ...         NaN        Active
4             345278696547337    1590741891  ...      Active           NaN
..                        ...           ...  ...         ...           ...
500           345283606547828    1526695270  ...      Active        Active
501           345283616547829    1526695271  ...      Active        Active
502           345283626547830    1526695272  ...      Active        Active
503           345283636547831    1526695273  ...      Active        Active
504           345283646547832    1526695274  ...      Active        Active

[505 rows x 11 columns]

"""

# ------step 10  --------checking the outliers and following methods to print them-------
#for this outlier we have to use numpy and scipy libraries
# in phonenumber column we found 10 as a outlier
print(dfsubscriber["Phone Number"])
"""
output:
0      1654788999
1      1888777222
2      1122765445
3              10
4      1590741891
          ...    
500    1526695270
501    1526695271
502    1526695272
503    1526695273
504    1526695274
Name: Phone Number, Length: 505, dtype: int64

"""



# applying zscore
# it will print the array where the zscore get applied and place one values

zscores_PN = np.abs(stats.zscore((dfsubscriber['Phone Number'])))
print(np.where(zscores_PN > 3))

"""
output : 
(array([ 3,  5,  6, 13, 16], dtype=int64),)
"""
# to check the array numbers displaying correct output use iloc it print every column of that index
print(dfsubscriber.iloc[13])

"""
output:
SubscriberIdentityNumber    345278786547346
Phone Number                             10
Subscriber Name                      Timoty
SSN                               214448894
Subscriber Age                           54
State                               Newyork
Zip Code                              10016
SubscribedFromDate                 2/9/2019
Internet Service                   InActive
SMS Service                          Active
Churn Status                         Active
Name: 13, dtype: object
"""

#so the above array is needs to drop
dfsubscriber = dfsubscriber.drop([3,5,6,13,16], axis=0)

#After dropping the index
print(dfsubscriber.shape)

# -------------------------Data Reduction -----------------------------------------------------------

#Removing duplicate records
print(dfsubscriber.duplicated(subset = None, keep ='first').sum())
# output : 5
print(dfsubscriber.shape)
#(505, 11)
dfsubscriber.drop_duplicates(subset=None, keep='first', inplace=True)
print(dfsubscriber.shape)
# After dropping output : (500, 11)
