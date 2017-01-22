#!/usr/bin/python

import sys;
import argparse;
from os.path import expanduser;

__author__ = "Jeetesh Mangwani"
o
def main():
    parser = argparse.ArgumentParser(description="This script compresses photos and videos in a given directory");
    parser.add_argument("-d", "--directory", type=str, help="The directory that will be traversed for photos and videos", required=False, default=expanduser("~"));
    parser.add_argument("-is", "--imagesize", type=str, help="Output image size; one of 'small', 'medium' or 'large'", required=False, default="small");
    parser.add_argument("-vs", "--videosize", type=str, help="Output video size; one of 'small', 'medium', or 'large'", required=False, default="small");
    parser.add_argument("-v", "--verbose", help="Whether to output verbose output messages", required=False, default=False);
    args = parser.parse_args();

    print(args.directory);
    print(args.imagesize);
    print(args.videosize);
    print(args.verbose);

main();
