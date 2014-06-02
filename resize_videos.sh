#!/bin/bash

# Author: Jeetesh Mangwani

# Objective: Scale down videos so that they occupy less space
# Prerequisites: ffmpeg package

# Trivia: I wasn't able to process long videos: the system would shut
# down due to overheating. Hence, I used process synchronization
# techniques to keep processor usage under control as follows: run the
# video processing for UP_TIME many seconds then sleep for DOWN_TIME
# many seconds; do this until we are over with all the videos

ROOT_DIRECTORY=~/my-albums
UP_TIME=10s
DOWN_TIME=5s
FPS=24
OUTPUT_WIDTH=640
OUTPUT_FILE_PREFIX=r


resizeVideos() {
	cd $ROOT_DIRECTORY
	for dir in `ls | grep "20*"`
	#list of directories e.g. 2013-05-05, 2013-07-26 etc
	do
		echo 'INSIDE directory' $dir
		cd $dir
		files=`ls -1 *.mp4` #for mp4 videos
		#files=`ls -1 | grep -e "avi\|AVI"` #for avi videos
		for file in $files
		do
			echo 'DEALING with' $dir '/' $file
			
			ffmpeg -i $file -vf "scale=$OUTPUT_WIDTH:trunc(ow/a/2)*2, fps=$FPS" -c:a copy -y $OUTPUT_FILE_PREFIX$file &
			
			pid="$!"
			kill -s STOP $pid #freeze the newly created video processing thread
			echo $pid
			trap "echo \'TERMINATING\'; kill -s USR1 $pid; exit" INT

			ps cax | grep $pid > /dev/null
			while [ $? -eq 0 ] #while the processing is still incomplete
			do
				#do processing
				kill -s CONT $pid
				echo "resizing RESUMED"
				sleep $UP_TIME
				
				#sleep
				kill -s STOP $pid
				echo "resizing PAUSED"
				sleep $DOWN_TIME
				
				echo "PID: $pid"
				ps cax | grep $pid > /dev/null
			done
		done
		cd ..
	done
}

resizeVideos
exit
