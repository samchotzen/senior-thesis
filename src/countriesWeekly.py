#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--key',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
from matplotlib.dates import YearLocator, DateFormatter

# get data from all geoTwitter files into one dictionary
geoTwitterDataByDate = {}
for date in args.input_paths:
    with open(date) as dictionary:
        value = json.load(dictionary)
        geoTwitterDataByDate[date] = value

# store tag argument in local parameter for clarity
tag = args.key

# initialize dictionary to store tag count for each country by date
model = {}
dateKeys = geoTwitterDataByDate.keys()

for geoTwitterDataKey in geoTwitterDataByDate:
    # get date
    if 'geoTwitter' in geoTwitterDataKey:
        date = geoTwitterDataKey.split('geoTwitter')[1].split('.zip.country')[0]
    elif 'tweets-' in geoTwitterDataKey:
        date = geoTwitterDataKey.split('tweets-')[1].split('.zip.country')[0]
        date = datetime.datetime.strptime(date,'%Y%m%d').date().isoformat()[2:]
    else:
        continue
    model[date] = {}

    # TODO: check date is valid datetime with regex (optional)
    
    # filter data by tag
    geoTwitterData = geoTwitterDataByDate.get(geoTwitterDataKey)
    if tag in geoTwitterData:
        dataForTag = geoTwitterData[tag]
    else:
        continue

    # parse data for tag count by country and add to model
    for countryCode in dataForTag:
        countryAndTagCount = {countryCode : dataForTag[countryCode]}
        model[date].update(countryAndTagCount)

# create array of x coordinates
dateList = list(model.keys())
dateListCopy = list(dateList)
weeklyDateList = []
dateDayCount = 1
for date in dateListCopy:
    if dateDayCount % 7 == 0:
        weeklyDateList.append(date)
    dateDayCount += 1

x = np.array(weeklyDateList)
print("x is: ", x)
#print("x is: ", x)
# simplify x-axis from days to years
#fig, ax = plt.subplots()
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)

# create list of all country codes that use the tag
countryCodeList = ['US', 'CA', 'GB', 'DE', 'IN'] #'ES', 'AU', 'NL', 'FR', 'JP',]
#for date in model:
    #dateData = model[date]
    #for countryCode in dateData:
        #if countryCode not in countryCodeList:
            #countryCodeList.append(countryCode)
        #else:
            #continue

# create array of y coordinates and plot with matplotlib
for countryCode in countryCodeList:
    weekDay = 1
    countryTagCountList = []
    countryTagCountWeek = 0
    for date in model:
        dateData = model[date]
        if countryCode in dateData:
            countryTagCountWeek += dateData[countryCode]
        else:
            countryTagCountWeek += 0
        if weekDay == 7:
            print("date is: ", date)
            weekDay = 1
            countryTagCountList.append(countryTagCountWeek)
            countryTagCountWeek = 0
        else:
            weekDay += 1
    y = np.array(countryTagCountList)
    ax.plot(x, y, label=countryCode)

# add chart elements based on input key
ax.legend()
ax.set_xticks(['18-01-01', '19-01-01', '20-01-01', '21-01-01', '22-01-01'])
ax.set_xticklabels(['2018', '2019', '2020', '2021', '2022',])
ax.set_xlabel("Date")
ax.set_ylabel("Usage level of " + args.key + " per day")
ax.set_title("Tweets with " + args.key + " in each country from 2018-2022")

# save bar graph file to plots folder
plt.savefig(args.key + 'Weekly.png')
