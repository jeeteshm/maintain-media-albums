#!/bin/bash

# Author: Jeetesh Mangwani

display_help() {
    cat <<EOF
Usage: ${0##*/} -s OUTPUT_SIZE -d DIRECTORY [-fvh] 
Objective: Scale down photos so that they occupy less space
Prerequisites: ffmpeg package
-s desired output size: small, medium or large
-d directory where the images reside
-f image format: jpg, png, gif; if not specified then assumes all files are images
-v display details as we progress
EOF
}

OPTIND=1
DIRECTORY=""
OUTPUT_SIZE="large"
IMAGE_FORMAT=""

while getopts "hs:d:f:v" opt; do
    case $opt in
	h)
	    display_help
	    exit 0
	    ;;
	s)
	    OUTPUT_SIZE=$OPTARG
	    ;;
	d)
	    DIRECTORY=$OPTARG
	    ;;
	f)
	    IMAGE_FORMAT=$OPTARG
	    ;;
	v)
	    VERBOSE=1
	    ;;
	'?')
	    display_help
	    exit 1
	    ;;
    esac
done

shift "$((OPTIND-1))" #remove remaining options on the command line
	
if [ -z $DIRECTORY ]; then
 echo "Directory not specified"
 display_help
 exit 1
fi

if [ "$OUTPUT_SIZE" = "small" ]; then
    OUTPUT_WIDTH=640 #will be used if aspect ratio > 1.33
    OUTPUT_HEIGHT=480 #will be used if aspect ratio <= 1.33
elif [ "$OUTPUT_SIZE" = "medium" ]; then
    OUTPUT_WIDTH=800 #will be used if aspect ratio > 1.33
    OUTPUT_HEIGHT=600 #will be used if aspect ratio <= 1.33
else
    OUTPUT_WIDTH=1000 #will be used if aspect ratio > 1.33
    OUTPUT_HEIGHT=750 #will be used if aspect ratio <= 1.33
fi

cd $DIRECTORY
#dirs=`ls | grep "20*"`
dirs=.

for dir in  $dirs #list of directories
do
	echo 'Inside directory' $dir
	cd $dir
	files=""
	if [ -z "$IMAGE_FORMAT" ]
	then
	    files=`ls -1`
	else
	    files=`ls -1 | grep -ie "$IMAGE_FORMAT"`
	fi

 if [ -z "$files" ]; then
  echo "No $IMAGE_FORMAT images found"
 else
  for file in $files
  do
   echo 'Dealing with' $dir'/'$file
   
   scale="'if(gt(a,4/3),$OUTPUT_WIDTH,-1)':'if(gt(a,4/3),-1,$OUTPUT_HEIGHT)'"
   if [ -z "$VERBOSE" ]
   then
       ffmpeg -i $file -vf scale=$scale -y $file 1>&2 2>/dev/null
   else
       ffmpeg -i $file -vf scale=$scale -y $file
   fi

  done
 fi

	cd ..
done
exit
