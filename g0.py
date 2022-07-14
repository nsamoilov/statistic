import csv
import numpy as np 
import matplotlib.pyplot as plt
from itertools import groupby
import pandas as pd
%matplotlib inline

class Data():
    def __init__(self, country, data, case):
        self.country = country
        self.data = data
        self.case = case

allDataList = list()
with open('/Users/nsamoilove/Desktop/coronavirus_dataset3.csv', newline='') as File:  
    reader = csv.reader(File)
    firstInfoRow = True
    for row in reader: 
        if firstInfoRow == True:
            firstInfoRow = False
            continue
        data = Data(row[1],row[4],row[5])
        allDataList.append(data)

plt.figure(figsize=(25,50))
plt.title('График SARS-COV19')
plt.grid(True)
#country = list()
for countryName, countryGroup in groupby(allDataList, lambda x: x.country):
    cases = dict()
    values = list()
    date = ['2020-02']
    #country.append(countryName)
    for timeInfo in countryGroup:
        #print(countryName,'/', timeInfo.data, '/', timeInfo.case)
        if timeInfo.data[0:7] == '2020-01':
            continue #Пропускаем первый месяц - в нём слишком мало данных
        else:
            if timeInfo.data[0:7] in date:
                try:
                    cdata = int(timeInfo.case)
                    values.append(cdata)
                except:
                    continue
            else:
                if len(values) == 0:
                    del values
                else:
                    cases[date[-1]] = sum(values)
                    values = list()
                    date.append(timeInfo.data[0:7])
    plt.plot(cases.keys(), cases.values(), label=countryName, linewidth=1.0)
    #print("Next country")
country = country[1:]
plt.xlabel("Дата", fontsize=44, fontweight="bold")
plt.ylabel("Значения", fontsize=44, fontweight="bold")
plt.legend()
plt.show()
