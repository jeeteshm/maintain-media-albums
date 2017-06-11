#!/usr/bin/python

import sys, os;
import argparse;
from os.path import expanduser;
from resizeFile import resizeFile;

__author__ = "Jeetesh Mangwani"

def main():
    parser = argparse.ArgumentParser(description="This script compresses photos and videos in a given directory");
    parser.add_argument("-d", "--directory", type=str, help="The directory that will be traversed for photos and videos", required=False, default=expanduser("~\my-photos"));
    parser.add_argument("-is", "--imagesize", type=str, help="Output image size; one of 'small', 'medium' or 'large'", required=False, default="small");
    parser.add_argument("-vs", "--videosize", type=str, help="Output video size; one of 'small', 'medium', or 'large'", required=False, default="small");
    parser.add_argument("-v", "--verbose", help="Whether to output verbose output messages", required=False, default=False);
    args = parser.parse_args();

    print("Root directory: ", args.directory);
    print("Output image size: ", args.imagesize);
    print("Output video size: ", args.videosize);
    print("Verbosity of log messages: ", args.verbose);

    for path, subdirs, files in os.walk(args.directory):
        for file in files:
            filePath = os.path.join(path, file)
            resizeFile(filePath, args)

main();