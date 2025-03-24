# import necessary libraries
import pandas as  pd
import numpy as np

# load/read the data 
df1 = pd.read_csv("airbnb_price.csv")
data = pd.ExcelFile("airbnb_room_type.xlsx")
df2 = pd.read_excel(data)
df3 = pd.read_csv("airbnb_last_review.tsv", sep= "\t")

# print the head of the dataframes
print(df1.head())
print(df2.head())
print(df3.head())


#  merge the two dataframes
data_1 = pd.merge(df1, df2, on="listing_id")
print(data_1.head()) # to check the merged dataframe

# again merge the remaining to create a final dataframe
df = pd.merge(data_1, df3, on ="listing_id")
print(df.head()) #to check the merged dataframe

# convert the date into the desired date fromet
df['last_review_date'] = pd.to_datetime(df['last_review'], format='%B %d %Y')
print(df.head()) # to check whether it is converted or not

first_reviewed = df['last_review_date'].min()
print(first_reviewed) #prints the first reviewed date

last_reviewed = df['last_review_date'].max()
print(last_reviewed) # #prints the first reviewed date


# Convert the strings into lowercase
df["room_type"] = df['room_type'].str.lower()
print(df["room_type"].head())


# to find out the no of private rooms in airbnb 
nb_private_rooms = df[df["room_type"] == "private room"].shape[0]
print(nb_private_rooms)
print(df['price'].head())

# replace or remove the string: dollars for the calculation and 
#  convert the column onto float dtype
df['price'] =df['price'].str.replace("dollars", "").astype("float")
print(df["price"].head())

# Calculate the average price of rooms in aribnb
avg_price = df["price"].mean().round(2)
print(avg_price)


# create the new dataframe consisting the values calculated above i.e firstreviewed, 
# lastreviewed, average price and number of private rooms

review_dates  = pd.DataFrame({
    'first_reviewed' : [first_reviewed],
    'last_reviewed' : [last_reviewed],
    'nb_private_rooms' : [nb_private_rooms],
    'avg_price' : [avg_price]
})

print(review_dates.head())