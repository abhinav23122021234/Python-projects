import pandas as pd
df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df.head())
grey_squirrel_count=len(df[df["Primary Fur Color"]=="Gray"])
red_squirrel_count=len(df[df["Primary Fur Color"]=="Cinnamon"])
Black_squirrel_count=len(df[df["Primary Fur Color"]=="Black"])
data_dict={
    "Fur Color": ["Gray","Red","Black"] ,
    "Squirrel Count": [grey_squirrel_count,red_squirrel_count,Black_squirrel_count]
}
new_data=pd.DataFrame(data_dict)
print(new_data)
new_data.to_csv("squirrel_count.csv")