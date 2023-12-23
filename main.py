import csv
import pandas

# with open("") as data:
#     contents = csv.reader(data)
#     temperatures = []
#     for row in contents:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#
contents = pandas.read_csv("weather_data.csv")
print(contents)
