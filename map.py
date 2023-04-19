#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--output_folder',default='outputs')
args = parser.parse_args()

# imports
import os
import zipfile
import datetime 
import json
from collections import Counter,defaultdict

# load EV keywords
hashtags = [
# General
    '#evs',
    '#electricvehicles',
    '#evcharging',
    '#evadoption',
    '#evrevolution',
    '#greentransportation',
    '#cleantransportation',
    '#electricvehiclecharging',
    '#electricvehicleadoption',
    '#sustainabletransport',
    '#sustainabletransportation',
    '#zeroemissions',
    '#electriccar',
    '#electriccars',
# Companies
    '#tesla',
    '#lucidmotors',
    '#zoox',
    '#aptiv',
    '#nio',
    '#volvoev',
    '#byd',
    '#canoo',
    '#electriccarstartup',
    '#rivian',
    '#nissanleaf',
    '#nissanev',
    '#chevybolt',
    '#chevyev',
    '#fordmustangmache',
    '#fordev',
    '#bmwi3',
    '#kianiroev',
    '#vwid4',
    '#audietron',
    '#hyundaikonaev',
    '#electricvehicleindustry',
# Technologies
    '#electricvehicletechnology',
    '#evtechnology',
    '#evtech',
    '#electricvehicletech',
    '#batterytechnology',
    '#chargingtechnology',
    '#selfdrivingcars',
    '#regenerativebraking',
    '#vehicletogrid',
    '#batterytech',
    '#chargingtech',
    '#autonomousvehicles',
# Policies
    '#evpolicy',
    '#evtaxcredits',
    '#evincentives',
    '#transportationpolicy',
    '#evtaxexemptions',
    '#evtaxdeductions',
    ]

# initialize counters
#counter_lang = defaultdict(lambda: Counter())
counter_country = defaultdict(lambda: Counter())

# open the zipfile
with zipfile.ZipFile(args.input_path) as archive:

    # loop over every file within the zip file
    for i,filename in enumerate(archive.namelist()):
        print(datetime.datetime.now(),args.input_path,filename)

        # open the inner file
        with archive.open(filename) as f:

            # loop over each line in the inner file
            for line in f:

                # load the tweet as a python dictionary
                tweet = json.loads(line)

                # convert text to lower case
                try:
                    text = tweet['text'].lower()
                except:
                    continue;

                # search hashtags
                for hashtag in hashtags:
                    try:
                        country = tweet['place']['country_code']
                    except:
                        country = None
                    if hashtag in text:
                        counter_country[hashtag][country] += 1
                    counter_country['_all'][country] += 1

# open the outputfile
try:
    os.makedirs(args.output_folder)
except FileExistsError:
    pass
output_path_base = os.path.join(args.output_folder,os.path.basename(args.input_path))

output_path_country = output_path_base+'.country'
print('saving',output_path_country)
with open(output_path_country,'w') as f:
    f.write(json.dumps(counter_country))
