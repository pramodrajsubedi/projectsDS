import pandas as pd
import numpy as np 
from statsmodels.formula.api import logit
#read the csv file
df = pd.read_csv("car_insurance.csv")
# to print the head of dataframe
print(df.head())
# to print out the sum of null values contained in any column of dataframe
print(df.isnull().sum()) # this showed two coulmns have null values to be filled with mean
# to print the datatyes
print(df.dtypes)
print(df.info())
print(df.describe())

# to fill the missing values with mean of respective column
df["credit_score"].fillna(df["credit_score"].mean(), inplace= True)
df["annual_mileage"].fillna(df["annual_mileage"].mean(), inplace=True)

# create a empty list
model = []
# create a cariable called features which contains columns except outcome and id
features = df.drop(columns = ["outcome", "id"]).columns

for col in features:
    mode = logit(f"outcome ~ {col}", data= df).fit()
    model.append(mode)

accuracies = []
for feature in range(0, len(model)):
    conf_matrix = model[feature].pred_table()
    tn =conf_matrix[0,0]
    tp = conf_matrix[1,1]
    fn = conf_matrix[1,0]
    fp = conf_matrix[0,1]
    acc = (tn + tp)/(tn + tp + fn + fp)
    accuracies.append(acc)

best_feature = features[accuracies.index(max(accuracies))]
best_feature_df = pd.DataFrame({"best_feature":best_feature,
                                "best_accuracies":max(accuracies)}, index=[0])
print(best_feature_df)