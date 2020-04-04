#Developed by Samson Lamichhane
#Take a table from HTML, convert to CSV,XLSX and perform desired Calculation

import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from decimal import *

with open ('HW-S-1.htm') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
filename = 'test.csv'
csv_writer = csv.writer(open(filename, 'w'))
heading = soup.find('h1')
print(heading.text)
for tr in soup.find_all('tr'):
    data = []

    for th in tr.find_all('th'):
        data.append(th.text)

    if(data):
        print("Inserting header : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue
    for td in tr.find_all('td'):
        data.append(td.text.strip())
    if(data):
        print("Instering Table Data:{}".format(','.join(data)))
        csv_writer.writerow(data)

read_file = pd.read_csv('test.csv')
df = pd.read_csv('test.csv')

df["x-axis acceleration"] = pd.to_numeric(df["x-axis acceleration"], downcast="float")
df["x-axis acceleration"] = ((df["x-axis acceleration"] * 9.81)/8192)

df["y-axis acceleration"] = pd.to_numeric(df["y-axis acceleration"], downcast="float")
df["y-axis acceleration"] = ((df["x-axis acceleration"] * 9.81)/8192)

df["z-axis acceleration"] = pd.to_numeric(df["z-axis acceleration"], downcast="float")
df["z-axis acceleration"] = ((df["x-axis acceleration"] * 9.81)/8192)

df["x-axis gyroscope"] = pd.to_numeric(df["x-axis gyroscope"], downcast="float")
df["x-axis gyroscope"] = (df["x-axis gyroscope"] / 16.4)

df["y-axis gyroscope"] = pd.to_numeric(df["y-axis gyroscope"], downcast="float")
df["y-axis gyroscope"] = (df["y-axis gyroscope"] / 16.4)

df["z-axis gyroscope"] = pd.to_numeric(df["z-axis gyroscope"], downcast="float")
df["z-axis gyroscope"] = (df["z-axis gyroscope"] / 16.4)

df["x-axis magnetometer"] = pd.to_numeric(df["x-axis magnetometer"], downcast="float")
df["x-axis magnetometer"] = (df["x-axis magnetometer"] * 0.6)

df["y-axis magnetometer"] = pd.to_numeric(df["y-axis magnetometer"], downcast="float")
df["y-axis magnetometer"] = (df["y-axis magnetometer"] * 0.6)

df["z-axis magnetometer"] = pd.to_numeric(df["z-axis magnetometer"], downcast="float")
df["z-axis magnetometer"] = (df["z-axis magnetometer"] * 0.6)

#Desired Table
df.to_csv('ProcessedData.csv', index=False)
df.to_excel('ProcessedData.xlsx', index=False)
