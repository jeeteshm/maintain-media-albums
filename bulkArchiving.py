#!/usr/bin/python

import sys, os;
import glob;
import argparse;
from os.path import expanduser;
from subprocess import run;

__author__ = "Jeetesh Mangwani";

def main():
    parser = argparse.ArgumentParser(description="This script archives files in bulk.");
    parser.add_argument("-id", "--inputdirectory", type=str, help="The input directory that will be traversed for to-be-archived files", required=True);
    parser.add_argument("-e", "--extension", type=str, help="Only files with this extension will be archived", required=True);
    parser.add_argument("-p", "--password", type=str, help="The password that will be used for archiving", required=True);
    args = parser.parse_args();

    # Keeping it simple for now. Later, add support for extensions of any length
    if len(args.extension) != 3:
        raise "Only three-letter extensions allowed"

    print("Input directory: ", args.inputdirectory);
    print("Input extension: ", args.extension);
    print("Input password: <redacted>");

    for filename in glob.iglob(os.path.join(args.inputdirectory, '*.' + args.extension)):
        outputFilename = filename[:-4] + ".zip"
        command = ["7z.exe", '-mx9', '-p' + args.password, "-tzip", "a", outputFilename, filename];
        print("Command: ", " ".join(command));
        run(command);

main();
