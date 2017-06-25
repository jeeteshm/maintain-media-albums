#!/usr/bin/python

import sys, os;
import argparse;
from os.path import expanduser;

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
    print("Resizing Image: {0} Size: {1}".format(filePath, size));
    relativePath = os.path.relpath(filePath, args.inputdirectory);
    destinationPath = os.path.join(args.outputdirectory, relativePath);
    print(destinationPath);
    

def resizeVideoFile(path, subdirs, file, args):
    print("Dealing with the video file: ", path);
