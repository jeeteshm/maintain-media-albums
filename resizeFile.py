#!/usr/bin/python

import sys, os;
import argparse;
from os.path import expanduser;
from subprocess import run;

__author__ = "Jeetesh Mangwani"

def resizeFile(path, subdirs, file, args):
    name, extension = os.path.splitext(file);
    image_file_extensions = [".png", ".jpg", ".jpeg"];
    video_file_extensions = [".avi", ".mp4"];

    if(extension in image_file_extensions):
        resizeImageFile(path, subdirs, file, args);
    elif(extension in video_file_extensions):
        resizeVideoFile(path, subdirs, file, args);
    else:
        print("Ignoring the file: ", os.path.join(path, file));
    

def resizeImageFile(path, subdirs, file, args):
    size = args.imagesize;
    verbose = args.verbose;
    filePath = os.path.join(path, file);
    relativeFilePath = os.path.relpath(filePath, args.inputdirectory);
    relativeDirectoryPath = os.path.relpath(path, args.inputdirectory);
    destinationFilePath = os.path.join(args.outputdirectory, relativeFilePath);
    destinationDirectoryPath = os.path.join(args.outputdirectory, relativeDirectoryPath);
    
    #print("Resizing to Size: {1} Input: {0} Output: {2}".format(filePath, size, destinationFilePath));

    if args.imagesize == "small":
        outputWidth=640 #will be used if aspect ratio > 1.33
        outputHeight=480 #will be used if aspect ratio <= 1.33
    elif args.imagesize == "medium":
        outputWidth=800 #will be used if aspect ratio > 1.33
        outputHeight=600 #will be used if aspect ratio <= 1.33
    else:
        outputWidth=1000 #will be used if aspect ratio > 1.33
        outputHeight=750 #will be used if aspect ratio <= 1.33

    #using exact path because there is another program called "convert" in Windows
    command = ["C:\Program Files\ImageMagick-7.0.6-Q16\convert.exe", filePath, "-define", "jpeg:extent=50kb", "-resize", str(outputWidth) + "x" + str(outputHeight), destinationFilePath];
    print("Command: ", " ".join(command));

    if not os.path.exists(destinationDirectoryPath):
        print("Creating directory: " + destinationDirectoryPath);
        os.makedirs(destinationDirectoryPath);
        
    run(command);

def resizeVideoFile(path, subdirs, file, args):
    print("Dealing with the video file: ", path);
