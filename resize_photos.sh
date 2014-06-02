#!/bin/bash

# Author: Jeetesh Mangwani

# Objective: Scale down photos so that they occupy less space
# Prerequisites: ffmpeg package

ROOT_DIRECTORY=~/my-albums
OUTPUT_WIDTH=1000 #will be used if aspect ratio > 1.33
OUTPUT_HEIGHT=750 #will be used if aspect ratio <= 1.33

cd $ROOT_DIRECTORY
dirs=`ls | grep "20*"`

for dir in  $dirs #list of directories
do
	echo 'Inside directory' $dir
	cd $dir
	files=`ls -1 | grep -e "jpg\|JPG"`
	for file in $files
	do
		echo 'Dealing with' $dir '/' $file
		
		#for photos
		ffmpeg -i $file -vf scale="'if(gt(a,4/3),1000,-1)':'if(gt(a,4/3),-1,750)'" -y $file
		
		#for videos
		#sleep 30s #if we don't sleep, system overheats and shuts down
		#ffmpeg -i $file -vf "scale=640:trunc(ow/a/2)*2, fps=24" -c:a copy -y r$file
	done
	cd ..
done
exit
