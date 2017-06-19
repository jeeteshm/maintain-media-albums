#!/usr/bin/python

import sys, os;
import argparse;
from os.path import expanduser;

__author__ = "Jeetesh Mangwani"

def resizeFile(filePath, args):
    name, extension = os.path.splitext(filePath);
    image_file_extensions = [".png", ".jpg", ".jpeg"];
    video_file_extensions = [".avi", ".mp4"];

    if(extension in image_file_extensions):
        resizeImageFile(filePath, args);
    elif(extension in video_file_extensions):
        resizeVideoFile(filePath, args);
    else:
        print("Ignoring the file: ", filePath);
    

def resizeImageFile(filePath, args):
    print("Dealing with the image file: ", filePath);

def resizeVideoFile(filePath, args):
    print("Dealing with the video file: ", filePath);
