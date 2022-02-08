import pandas as pd
import numpy as np

#For data visualization 
import matplotlib.pyplot as plt


df_cleaned = pd.read_csv('data_cleaned.csv',sep = ";") 
print(df_cleaned.shape)

print(df_cleaned.dtypes)

cols = df_cleaned.columns
num_cols = df_cleaned._get_numeric_data().columns
print(num_cols)
print(list(set(cols) - set(num_cols)))

# converting string to numeric

df_cleaned['Surface kitchen'] = pd.to_numeric(df_cleaned['Surface kitchen'],errors='coerce')
df_cleaned['Surface bedroom 1'] = pd.to_numeric(df_cleaned['Surface bedroom 1'],errors='coerce')
df_cleaned['Surface of living-room'] = pd.to_numeric(df_cleaned['Surface of living-room'],errors='coerce')
df_cleaned['Surface bedroom 2'] = pd.to_numeric(df_cleaned['Surface bedroom 2'],errors='coerce')
df_cleaned['Surface bedroom 3'] = pd.to_numeric(df_cleaned['Surface bedroom 3'],errors='coerce')

cols = df_cleaned.columns
num_cols = df_cleaned._get_numeric_data().columns
print(num_cols)
non_num_cols = list(set(cols) - set(num_cols))
print(non_num_cols)
quantitative_variables = len(num_cols)
qualitative_variables = len(non_num_cols)

print(f"How many qualitative variables : {qualitative_variables}")
print(f"How many quantitative variables : {quantitative_variables}")

# To replace different conditions of property by number for better analysis in futur 
print(df_cleaned['State of the property'].value_counts())
df_cleaned.replace({'State of the property':{'To be renovated' : 1, 'Normal' : 2, "Fully renovated" : 3, "Excellent":4, "New" : 5 }}, inplace = True)
print(df_cleaned["State of the property"]) 

# To replace different kitchen equipment by number for better analysis in futur 
print(df_cleaned['Kitchen equipment'].value_counts())
df_cleaned.replace({'Kitchen equipment':{'Not equipped' : 1, 'Partially equipped' : 2, "Fully equipped" : 3, "Super equipped" : 4}}, inplace = True)
print(df_cleaned["Kitchen equipment"]) 


# correlation between variables and targets

price_cor = df_cleaned[df_cleaned.columns[1:]].corr()['Price'][:]
print(price_cor.sort_values(ascending=False))


# plotting some graphs to analyse Data

plt.bar(df_cleaned['Type of property'], height= 15000, color ='g') 

plt.show()