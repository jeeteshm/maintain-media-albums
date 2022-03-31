#!/usr/bin/python

import sys, os;
import glob;
import argparse;
from os.path import expanduser;
from subprocess import run;

__author__ = "Jeetesh Mangwani";

def main():
    parser = argparse.ArgumentParser(description="This script unarchives files in bulk.");
    parser.add_argument("-id", "--inputdirectory", type=str, help="The input directory that will be traversed for to-be-unarchived files", required=True);
    parser.add_argument("-p", "--password", type=str, help="The password that will be used for unarchiving", required=True);
    args = parser.parse_args();

    print("Input directory: ", args.inputdirectory);
    print("Input password: <redacted>");

    for filename in glob.iglob(os.path.join(args.inputdirectory, '*.zip')):
        command = ["7z.exe", "-p" + args.password, "-o" + args.inputdirectory, "x", filename];
        print("Command: ", " ".join(command));
        run(command);

main();
