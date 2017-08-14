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
        outputWidth=640 #will be used if aspect ratio > 1
        outputHeight=480 #will be used if aspect ratio <= 1
        outputSize="50"
    elif args.imagesize == "medium":
        outputWidth=800 #will be used if aspect ratio > 1
        outputHeight=600 #will be used if aspect ratio <= 1
        outputSize="200"
    else:
        outputWidth=1000 #will be used if aspect ratio > 1
        outputHeight=750 #will be used if aspect ratio <= 1
        outputSize="1000"

    #using exact path because there is another program called "convert" in Windows
    command = ["C:\Program Files\ImageMagick-7.0.6-Q16\convert.exe", filePath, "-define", "jpeg:extent=" + outputSize + "kb", "-resize", str(outputWidth) + "x" + str(outputHeight), destinationFilePath];

    print("Command: ", " ".join(command));

    if not os.path.exists(destinationDirectoryPath):
        print("Creating directory: " + destinationDirectoryPath);
        os.makedirs(destinationDirectoryPath);
        
    run(command);

def resizeVideoFile(path, subdirs, file, args):
    size = args.videosize;
    verbose = args.verbose;
    filePath = os.path.join(path, file);
    relativeFilePath = os.path.relpath(filePath, args.inputdirectory);
    relativeDirectoryPath = os.path.relpath(path, args.inputdirectory);
    destinationFilePath = os.path.join(args.outputdirectory, relativeFilePath);
    destinationDirectoryPath = os.path.join(args.outputdirectory, relativeDirectoryPath);
    fps="24";
    
    print("Resizing to Size: {1} Input: {0} Output: {2}".format(filePath, size, destinationFilePath));

    if args.imagesize == "small":
        outputWidth=640
    elif args.imagesize == "medium":
        outputWidth=800
    else:
        outputWidth=1000

    command = ["ffmpeg", "-i", filePath, "-vf", "scale=" + str(outputWidth) + ":trunc(ow/a/2)*2, fps=" + fps, "-c:a", "copy", "-y", destinationFilePath];

    print("Command: ", " ".join(command));

    if not os.path.exists(destinationDirectoryPath):
        print("Creating directory: " + destinationDirectoryPath);
        os.makedirs(destinationDirectoryPath);
        
    run(command);
