#!/usr/bin/python

import sys, os;
import glob;
import argparse;
from os.path import expanduser;
__author__ = "Jeetesh Mangwani";

def main():
    parser = argparse.ArgumentParser(description="This script changes filename extensions in bulk.");
    parser.add_argument("-id", "--inputdirectory", type=str, help="The input directory that will be traversed for photos and videos", required=True);
    parser.add_argument("-ie", "--inputextension", type=str, help="Output image size; one of 'small', 'medium' or 'large'", required=False, default="small");
    parser.add_argument("-oe", "--outputextension", type=str, help="Output video size; one of 'small', 'medium', or 'large'", required=False, default="small");
    args = parser.parse_args();

    print("Input directory: ", args.inputdirectory);
    print("Input extensions: ", args.inputextension);
    print("Output extension: ", args.outputextension);

    for filename in glob.iglob(os.path.join(args.inputdirectory, '*.' + args.inputextension)):
    	os.rename(filename, filename[:-4] + '.' + args.outputextension);

main();
