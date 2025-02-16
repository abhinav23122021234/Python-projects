#with open("weather_data.csv") as data_file:
 #   data=data_file.readlines()
  #  print(data) # gives a list having each row as tuple inside
#import csv
#with open("weather_data.csv") as data_file:
#    data=csv.reader(data_file)
#    #print(data) returns csv.reader object at some location
#    temp=[]
#    for row in data:
#        if row[1]!="temp":
#            temp.append(row[1])
#    print(temp)

import pandas as pd
data=pd.read_csv("weather_data.csv")
#print(data)
#print(data["temp"])
#tempe=data["temp"]
#avg=tempe.sum()/len(tempe)
#print(avg)
#print(data["temp"].mean())

#printing monday row
#print(data[data["day"]=="Monday"])

#printing row with max temp
print(data[data["temp"]==data["temp"].max()])