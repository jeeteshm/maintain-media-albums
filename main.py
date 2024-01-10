#!/usr/bin/python

import sys, os;
import argparse;
from os.path import expanduser;
from resizeFile import resizeFile;

__author__ = "Jeetesh Mangwani"

def main():
    parser = argparse.ArgumentParser(description="This script compresses photos and videos in a given directory");
    parser.add_argument("-id", "--inputdirectory", type=str, help="The input directory that will be traversed for photos and videos", required=False, default=expanduser("~/my-photos/input"));
    parser.add_argument("-od", "--outputdirectory", type=str, help="The output directory where resized photos and videos will be put", required=False, default=expanduser("~/my-photos/output"));
    parser.add_argument("-is", "--imagesize", type=str, help="Output image size; one of 'small', 'medium' or 'large'", required=False, default="small");
    parser.add_argument("-vs", "--videosize", type=str, help="Output video size; one of 'small', 'medium', or 'large'", required=False, default="small");
    parser.add_argument("-v", "--verbose", help="Whether to output verbose output messages", required=False, default=False);
    args = parser.parse_args();
    print("Input directory: ", args.inputdirectory);
    print("Output directory: ", args.outputdirectory);
    print("Output image size: ", args.imagesize);
    print("Output video size: ", args.videosize);
    print("Verbosity of log messages: ", args.verbose);

    for path, subdirs, files in os.walk(args.inputdirectory):
        for file in files:
            resizeFile(path, subdirs, file, args)

main();