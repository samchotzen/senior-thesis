#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:5]
for k,v in items:
    print(k,':',v)

# create sorted dictionary before plotting
lists = sorted(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:5], key=lambda kv: kv[1])
key, value = zip(*lists)

# create bar graph
plt.bar(key, value, color = 'maroon', width = 0.4)

# add chart elements based on input path and key
if args.input_path == 'reduced.country':
    plt.xlabel("Country")
    plt.ylabel("Usage level of " + args.key)
    plt.title("Tweets with " + args.key + " in each country from 2017-2023")
else:
    plt.xlabel("Country")
    plt.ylabel("Usage level of " + args.key)
    plt.title("Tweets with " + args.key + " from each country from 2017-2023")

# save bar graph file to plots folder
plt.savefig(args.input_path + args.key + '.png')
