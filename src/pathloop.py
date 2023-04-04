#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--output_path',required=True)
#parser.add_argument('--key',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
import matplotlib.pyplot as plt 

# commented code adds all tweets per hashtag per day but combines countries
#allpaths = {}
#for path in args.input_paths:
#    value = {}
#    for hashtag in path:
#        alltweets = path[hashtag]
#        total = 0
#        for country in alltweets:
#            total += alltweets[country]
#        value[hashtag] = total
#    allpaths[path] = value

allpaths = {}
for path in args.input_paths:
    with open(path) as dictionary:
        value = json.load(dictionary)
        allpaths[path] = value
#print(allpaths)

# write the output path for allpaths
with open(args.output_path,'w') as f:
    f.write(json.dumps(allpaths))

# transform allpaths dictionary into a pandas dataframe
#df = pd.DataFrame.from_dict(allpaths)
#print(df)

# create xaxis list
#xlist = list(allpaths.keys())
#print(xlist)

# create yaxis list
#f = json.load(allpaths)
#counts = f

# create line plot
#plt.plot(xlist, ylist)

# save line plot to plots folder
#plt.savefig(args.key + 'lineplot.png')
