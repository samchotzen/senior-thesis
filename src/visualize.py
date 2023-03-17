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
from matplotlib.font_manager import FontProperties

# add Korean font path
font_paths = ['NotoSansKR-Regular.otf']

properties = []
for path in font_paths:
    properties.append(FontProperties(fname=path))

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# create sorted dictionary before plotting
lists = sorted(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10], key=lambda kv: kv[1])
key, value = zip(*lists)

# create bar graph
plt.bar(key, value, color = 'maroon', width = 0.4)

# check language of key
if args.key == '#coronavirus':
    language = 'English'
else:
    language = 'Korean'

# add chart elements based on input path and key
if args.input_path == 'reduced.lang' and args.key == '#coronavirus':
    plt.xlabel("Language")
    plt.ylabel("Usage level of " + args.key)
    plt.title("Tweets with " + args.key + " in each language in 2020")
elif args.input_path == 'reduced.lang' and args.key == '#코로나바이러스':
    plt.xlabel("Language")
    plt.ylabel("Usage level of " + args.key, fontproperties=properties[0])
    plt.title("Tweets with " + args.key + " in each language in 2020", fontproperties=properties[0])
elif args.input_path == 'reduced.country' and args.key == '#coronavirus':
    plt.xlabel("Country")
    plt.ylabel("Usage level of " + args.key)
    plt.title("Tweets with " + args.key + " in each country in 2020")
else:
    plt.xlabel("Country")
    plt.ylabel("Usage level of " + args.key, fontproperties=properties[0])
    plt.title("Tweets with " + args.key + " from each country in 2020", fontproperties=properties[0])

# save bar graph file to plots folder
plt.savefig(args.input_path + args.key + '.png')
