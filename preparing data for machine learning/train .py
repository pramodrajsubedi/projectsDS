import pandas as pd
import numpy as np
df_transformed = pd.read_csv("customer_train.csv")
#  to make duplicate dataframe for the comparision of maemory usafe between these two dataframe
df_transformed = df_transformed.copy()
print(df_transformed.head(10))
print(df_transformed.info())
print(df_transformed.value_counts(dropna= False))
df_transformed["relevant_experience"] = df_transformed["relevant_experience"].convert_dtypes(str)
print(df_transformed['relevant_experience'].dtype)

#  for identifying the datatypes of each columns of the df_transformed
for col in df_transformed.select_dtypes("object").columns:
    print(df_transformed[col].value_counts(), '\n')


# for converting two factor categories into boolean
df_transformed["relevant_experience"]= np.where(df_transformed["relevant_experience"].str.contains("Has", regex= False), True, False)
df_transformed['relevant_experience'] = df_transformed["relevant_experience"].convert_dtypes(bool)
print(df_transformed["relevant_experience"].value_counts())
print(df_transformed["relevant_experience"].dtype)

#  for the column job_change
print(df_transformed['job_change'].dtypes) # check the datatype of the job_type column
df_transformed["job_change"] = np.where(df_transformed["job_change"].astype(str).str.contains("1", regex= False), True, False)
print(df_transformed['job_change'].value_counts())
print(df_transformed["job_change"].dtype)

ordered_cats = {
    'enrolled_university': ['no_enrollment', 'Part time course', 'Full time course'],
    'education_level': ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'],
    'experience': ['<1'] + list(map(str, range(1, 21))) + ['>20'],
    'company_size': ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'],
    'last_new_job': ['never', '1', '2', '3', '4', '>4']
}


# for converting the integer column to int32
for col in df_transformed:

    # Convert integer columns to int32
    if col in ['student_id', 'training_hours']:
        df_transformed[col] = df_transformed[col].astype('int32')
    
    # Convert float columns to float16
    elif col == 'city_development_index':
        df_transformed[col] = df_transformed[col].astype('float16')
    
    # Convert columns containing ordered categorical data to ordered categories using dict
    elif col in ordered_cats.keys():
        category = pd.CategoricalDtype(ordered_cats[col], ordered=True)
        df_transformed[col] = df_transformed[col].astype(category)
    
    # Convert remaining columns to standard categories
    else:
        df_transformed[col] = df_transformed[col].astype('category')

print(df_transformed.info())
# After the converdion memory usage dropped grom 2.0 Mb+  to 400.4 KB