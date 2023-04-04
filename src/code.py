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
import sys

geoTwitterDataByDate = {}
for date in args.input_paths:
    with open(date) as dictionary:
        value = json.load(dictionary)
        geoTwitterDataByDate[date] = value

# Store tag argument in local parameter for clarity
tag = sys.argv

# Initialize dictionary to store tag count for each country by date
model = {}
dateKeys = geoTwitterDataByDate.keys()

for geoTwitterData in geoTwitterDataByDate:
    # Get date
    date = geoTwitterData.split('geoTwitter')[1].split('.zip.country')[0]
    print("date is: ", date)

    # TODO: Check date is valid datetime with regex (optional)
    
    # Filter data by tag
    dataForTag = geoTwitterData[tag]
    print("data for tag is: ", dataForTag)

    # Parse data for tag count by country and add to model
    for countryCode in dataForTag:
        countryTagCount = [countryCode, dataForTag[countryCode]]
        model[date] = countryTagCount
    
    return

print("model is: ", model)

# Plot with matplotlib