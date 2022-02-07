import pandas as pd
import numpy as np

df = pd.read_csv("./../data_set.csv")
df = df.replace("None", pd.NA)
to_drop = df.columns[41:-1]
df = df.drop(to_drop, axis=1)
df = df.drop(["Currently leased", "Availability", "Frontage width", "Office surface", "Total land surface", "Kitchen type", "Gas"], axis=1)
df.drop_duplicates(inplace = True)

# Cleans the price col
df = df.drop(df[df["Price"].isnull()].index)
def int_of_price(x):
    for d in x.split():
        if d.isdigit():
            return int(d)
df["Price"] = df["Price"].apply(int_of_price)

# Cleans subtypes
def clean_subtype(subtype):
    if "flat---" in subtype:
        return subtype.replace("flat---", "")
    else:
        return subtype

df["Subtype of property"] = df["Subtype of property"].apply(clean_subtype)

def int_of_string(x):
    if pd.isna(x):
        return x
    else:
        return int(x)
df["Number of bedrooms"]=df["Number of bedrooms"].apply(int_of_string)

def none_to_default(value, default):
    if pd.isna(value):
        return default
    else:
        return value
for label in ["Furnished", "Balcony", "Elevator", "Terrace", "Security door", "Access for disabled", "Garden", "Garage", "Cellar"]:
    df[label] = df[label].apply(lambda val : none_to_default(val, 0))
df["Balcony"] = df["Balcony"].apply(lambda val: none_to_default(val,0))
for label in ["Sewer Connection", "Number of showers", "Number of bathrooms", "Number of toilets"]:
    df[label] = df[label].apply(lambda val: none_to_default(val,1))
df["Kitchen equipment"] = df["Kitchen equipment"].apply(lambda val: none_to_default(val, "Partially equipped"))
df["State of the property"] = df["State of the property"].apply(lambda val: none_to_default(val, "Normal"))


def remove_unit(value):
    for s in str(value).split():
        if s.isdigit:
            return float(s)

# Cleans surfaces
for label in ["Livable surface", "Surface of living-room", "Surface bedroom 1", "Surface bedroom 2", "Surface kitchen", "Surface terrace", "Surface garden", "Surface bedroom 3"]:
    df[label]=df[label].map(remove_unit, na_action="ignore")

df = df.drop(df[df["Livable surface"]==0.].index)

def mean_val(ref_col, target_col):
    ratios = target_col.divide(ref_col)
    mean = ratios.mean()
    default_values = ref_col.map(lambda x: x * mean, na_action="ignore")
    return target_col.fillna(default_values)
for label in ["Surface of living-room", "Surface bedroom 1", "Surface bedroom 2", "Surface bedroom 3", "Surface kitchen"]:
    df[label] = mean_val(df["Livable surface"], df[label])

def facade_of_type(type_):
    if type_ in ["villa", "master-house", "cottage", "bungalow", "chalet", "mansion"]:
        return 4
    else:
        return 2

def facade_of_na(types, target):
    default = types.map(facade_of_type)
    return target.fillna(default)

df["Number of facades"] = facade_of_na(df["Subtype of property"],df["Number of facades"])

df["Terrace"] = df["Terrace"].map(lambda val: none_to_default(val,'0'))
df["Surface terrace"] = df["Surface terrace"].map(remove_unit, na_action="ignore")


def mean(ref_col, target_col):
    ratios = target_col.divide(ref_col)
    return ratios.mean()
def replace_ter_surf(row, mean):
    if row["Terrace"] == 1 and pd.isna(row["Surface terrace"]):
        row["Surface terrace"] = mean * row["Livable surface"]
    elif row["Terrace"] == 0:
        row["Surface terrace"] = 0
    return row

mean = mean(df["Livable surface"], df["Surface terrace"])

df = df.apply(lambda row: replace_ter_surf(row, mean) ,axis = 1)

def entry_phone(row):
    if row["Type of property"] == "flat" and pd.isna(row["Entry phone"]):
        row["Entry phone"] = 1
    if row["Type of property"] == "house" and pd.isna(row["Entry phone"]):
        row["Entry phone"] = 0
    return row

df = df.apply(entry_phone, axis=1)

df.to_csv("data_cleaned.csv")
