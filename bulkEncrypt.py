#!/usr/bin/python

import sys, os, glob;
import argparse;
from os.path import expanduser;
from subprocess import run;

__author__ = "Jeetesh Mangwani"

def main():
    parser = argparse.ArgumentParser(description="This script compresses and encrypts input files.");
    parser.add_argument("-d", "--inputdirectory", type=str, help="The input directory that will be traversed for input files", required=True);
    parser.add_argument("-p", "--password", type=str, help="The password for the output archives", required=True);
    parser.add_argument("-ie", "--inputextension", type=str, help="The file extension of the input files", required=False, default="pdf");
    parser.add_argument("-oe", "--outputextension", type=str, help="The file extension of the output archives", required=False, default="zip");
    args = parser.parse_args();

    print("Input directory: ", args.inputdirectory);
    print("Password: ", args.password);
    print("Input extensions: ", args.inputextension);
    print("Output extension: ", args.outputextension);

    for filename in glob.iglob(os.path.join(args.inputdirectory, '*.' + args.inputextension)):
        outputArchiveName = filename[:-4] + '.' + args.outputextension
        print("Processing " + filename + " into " + outputArchiveName);
        command = ["7z.exe", "a", "-tzip", "-p" + args.password, outputArchiveName, filename];
        print("Command: ", " ".join(command));
        run(command);

main();