import pandas as pd
import numpy as np

# visualization
# import matplotlib.pyplot as plt

df = pd.read_csv('data_set.csv',sep = ",")  # this will read the file in tabular form
# print(df)

print(df.shape)                             # [no. of rows, no. of columns]
# print(df.columns.tolist())                  # this will give list of columns 


#To check empty cells
null_num = df.isnull().sum()        # This will give count of missing values in each columns
print(null_num)
print(max(null_num))

#But in my dataframe there is None, replace 'None' into NaN
df.replace(to_replace=['None'], value=np.nan, inplace=True)     # Becareful the elem you want to change is string or value
print(df)


#To check missing values in complete dataframe 
     
null_num = df.isnull().sum()        # This will give count of missing values in each columns
print(null_num)

percent_missing = df.isnull().sum() * 100 / len(df)
missing_value_df = pd.DataFrame({'column_name': df.columns,'percent_missing': percent_missing})
print(missing_value_df)

#Check duplicacy in our data frame 
df.duplicated()                 # this will give me table boolean 
print(df.duplicated().sum())        #To check number of dupicacy of or rows in the dataframe 
# print(df.loc[df.duplicated(), :])       # To check location of duplicacy in the dataframe 
df.drop_duplicates(inplace=True)            # To remove duplicate rows from dataframe 
print(df.shape)


# After discussion we selected columns 
# for Balcony we are taking NaN as 0 
print(df['Balcony'].value_counts())
df['Balcony'] = df['Balcony'].fillna(0)
# print(df['Balcony'])




# To replace different conditions of property by number for better analysis in futur 
print(df['State of the property'].value_counts())
df.replace({'State of the property':{'To be renovated' : 1, 'Normal' : 2, "Fully renovated" : 3, "Excellent":4, "New" : 5 }}, inplace = True)
# print(df["State of the property"]) 


# for Elevator we are taking NaN as 0 
print(df['Elevator'].value_counts())
df['Elevator'] = df['Elevator'].fillna(0)
# print(df['Elevator'])







