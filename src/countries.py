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

i = 0

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

    i += 1
    if i > 10:
        break

#print("model is: ", model)

# plot with matplotlib
dateList = list(model.keys())
x = np.array(dateList)

print("dateList is: ", dateList)
print("x is: ", x)

# create list of all country codes that use the tag
countryCodeList = []
for date in model:
    dateData = model[date]
    for countryCode in dateData:
        if countryCode not in countryCodeList:
            countryCodeList.append(countryCode)
        else:
            continue

for countryCode in countryCodeList:
    countryTagCountList = []
    for date in model:
        dateData = model[date]
        if countryCode in dateData:
            countryTagCountList.append(dateData[countryCode])
        else:
            countryTagCountList.append(0)
    y = np.array(countryTagCountList)
    plt.plot(x, y)

# add chart elements based on input key
plt.xlabel("Date")
plt.ylabel("Usage level of " + args.key + " per day")
plt.title("Tweets with " + args.key + " in each country from 2018-2022")

# save bar graph file to plots folder
plt.savefig(args.key + '.png')