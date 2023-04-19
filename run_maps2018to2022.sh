#!/bin/sh

# loops over each file in the dataset and runs map.py on that file
for file in /data/Twitter\ dataset/geoTwitter18*; do
    nohup ./src/map.py --input_path="$file" &
    echo $file
done
for file in /data/Twitter\ dataset/geoTwitter19*; do
    nohup ./src/map.py --input_path="$file" &
    echo $file
done
for file in /data/Twitter\ dataset/geoTwitter20*; do
    nohup ./src/map.py --input_path="$file" &
    echo $file
done
for file in /data/Twitter\ dataset/geoTwitter21*; do
    nohup ./src/map.py --input_path="$file" &
    echo $file
done
for file in /data/Twitter\ dataset/geoTwitter22*; do
    nohup ./src/map.py --input_path="$file" &
    echo $file
done
for file in /data/Twitter\ dataset/tweets-2022*; do
    nohup ./src/map.py --input_path="$file" &
    echo $file
done
