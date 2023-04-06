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

geoTwitterDataByDate = {}
for date in args.input_paths:
    with open(date) as dictionary:
        value = json.load(dictionary)
        geoTwitterDataByDate[date] = value

# Store tag argument in local parameter for clarity
tag = args.key

# Initialize dictionary to store tag count for each country by date
model = {}
dateKeys = geoTwitterDataByDate.keys()
print("dateKeys is: ", dateKeys)

i = 0

for geoTwitterDataKey in geoTwitterDataByDate:
    # Get date
    date = geoTwitterDataKey.split('geoTwitter')[1].split('.zip.country')[0]
    model[date] = {}

    # TODO: Check date is valid datetime with regex (optional)
    
    # Filter data by tag
    geoTwitterData = geoTwitterDataByDate.get(geoTwitterDataKey)
    if tag in geoTwitterData:
        dataForTag = geoTwitterData[tag]
    else:
        continue

    # Parse data for tag count by country and add to model
    for countryCode in dataForTag:
        countryAndTagCount = {countryCode : dataForTag[countryCode]}
        model[date].update(countryAndTagCount)

    i += 1
    if i > 10:
        break

print("model is: ", model)

# Plot with matplotlib
dateList = list(model.keys())
x = np.array(dateList)

print("x is: ", x)

countryCodeList = []
for date in model:
    dateData = model[date]
    for countryCode in dateData:
        if countryCode not in countryCodeList:
            countryCodeList.append(countryCode)
        else:
            continue

print("countryCodeList is: ", countryCodeList)

for date in model:
    dateData = model[date]
    for countryCode in dateData:
        if countryCode in dateData:
            countryCodeValue = dateData[countryCode]
            countryCodeList.append(countryCodeValue)
        else:
            countryCodeValue = 0
            countryCodeList.append(countryCodeValue)

#        y = np.array(model[date2][country])
#        plt.plot(x, y)
# plt.show()
# countryCodeTagVector = {}