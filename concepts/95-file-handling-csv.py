# to read CSV file we need a module "pandas"
# by default "pandas" is not available with python
# pip install pandas
import pandas as pd

filepath = './concepts/95c-test.csv'

dataframe = pd.read_csv(filepath)

print(dataframe)
## OUTPUT:
#        name  age        city
#0   abhishek   50      London
#1        rob   55       Paris
#2        bob   44      Munich
#3        tom   69      Oxford
#4       maya   48   Bangalore
#5        ali   55       Dubai
#6   mohammad   20   Abu Dhabi
#7        ben   30    bradford
#8       alex   34        kent
#9     simone   44    florence
#10       dom   37      London
#11    claire   47     Halifax

print(dataframe.head())
## OUTPUT:
#        name  age        city
#0   abhishek   50      London
#1        rob   55       Paris
#2        bob   44      Munich
#3        tom   69      Oxford
#4       maya   48   Bangalore

print(dataframe.head(2))
## OUTPUT:
#        name  age        city
#0   abhishek   50      London

print(dataframe.tail())
## OUTPUT:
#        name  age        city
#7        ben   30    bradford
#8       alex   34        kent
#9     simone   44    florence
#10       dom   37      London
#11    claire   47     Halifax

print(dataframe.tail(2))
## OUTPUT:
#        name  age        city
#11    claire   47     Halifax

print(dataframe.info())
## OUTPUT:
#<class 'pandas.core.frame.DataFrame'>
#RangeIndex: 12 entries, 0 to 11
#Data columns (total 3 columns):
# #   Column  Non-Null Count  Dtype 
#---  ------  --------------  ----- 
# 0   name    12 non-null     object
# 1   age     12 non-null     int64 
# 2   city    12 non-null     object
#dtypes: int64(1), object(2)
#memory usage: 416.0+ bytes
#None







# CLEANING DATA
## BAD data can be
## - Empty cells
## - Data in wrong format
## - Wrong data
## - Duplicates
dirtyfilepath = './concepts/95d-dirty.csv'

dirtydata = pd.read_csv(dirtyfilepath)

print("--------Original data--------")
print(dirtydata)

# remove empty cell
## by default it will return a new dataframe post deleting the rows containing empty rows
## use "inplace = True"
postDeleteNa = dirtydata.dropna()
print(postDeleteNa)

# fill empty values with something
## read about mean, median and mode in "statistics basics" in README.md
## new_df = df.fillna(130) # return  a new data frame
## df.fillna(130, inplace = True) # original dataframe will be updated
## df["Calories"].fillna(130, inplace = True)# replace only in specified column
## df["Calories"].fillna(df["Calories"].mean(), inplace = True) # fill with mean data (this is common way to fill empty cell)
## df["Calories"].fillna(df["Calories"].median(), inplace = True) # fill with mean data
## df["Calories"].fillna(df["Calories"].mode()[0], inplace = True) # fill with mean data


# WRONG format
#postDeleteNa['Date'] = pd.to_datetime(postDeleteNa['Date'])
#print(postDeleteNa.to_string())

# REMOVE Duplicates
## below line only identifies duplicate rows. True for duplicate row else False
postDeleteNa.duplicated()
postRemoveDuplicate = postDeleteNa.drop_duplicates() # can use inplace=True
print(postRemoveDuplicate)

### There are many more like find corelation. Corelation between other rows, plot data in graph.
