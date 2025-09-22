#import pandas library as pd

import pandas as pd

#load the dataset
df = pd.read_csv(r"C:\Users\Abhilash\Downloads\students data\students_data.csv")

#check if there any duplicates present in the dataset
print(df.duplicated())

#remove the duplicates from the dataset
df=df.drop_duplicates()

#check for missing values
print(df.isnull().sum())

#Capitalize the name column
df.loc[:, "name"]=df["name"].str.lower().str.title()

print(df["age"].unique())

#fill missing age with mean
age_mean=df["age"].mean().round(0)
df.loc[:,"age"]=df["age"].fillna(age_mean)

#Capitalize gender
df.loc[:,"gender"]=df["gender"].str.lower().str.title()

#Standardize grade
df.loc[:, "grade"]=df["grade"].replace({'10th':'10','11th':11})

#filling math_score with mean
math_mean=df["math_score"].mean()
df.loc[:, "math_score"]=df["math_score"].fillna(math_mean)

# Convert english_score to numeric and handle invalid values
df["english_score"] = pd.to_numeric(df["english_score"], errors='coerce')

# Calculate mean after conversion
english_mean = df["english_score"].mean()

# Fill missing english_score with mean
df["english_score"] = df["english_score"].fillna(english_mean).astype(float)


#Standardize enrolled_date to yyyy-mm-dd
dic_date={
    '10-06-2022':'2022-06-10',
    '06/12/2022':'2022-06-12',
    '2022/06/11':'2022-06-11'
    }
df.loc[:,"enrolled_date"]=df["enrolled_date"].replace(dic_date)
pd.to_datetime(df["enrolled_date"])

#standardize remarks
dict_remark={
    'excellent': 'Excellent',
    'GOOD': 'Good',
    'needs improvement': 'Needs Improvement',
    'average':'Average',
    'poor':'Poor',
    'good_student': 'Good'
    }
df.loc[:,"remarks"]=df["remarks"].replace(dict_remark)

#show cleaned data
print(df.info())
print(df.head())
print(df)