#!/usr/bin/python

import sys, os;
import glob;
import argparse;
from os.path import expanduser;
from subprocess import run;

__author__ = "Jeetesh Mangwani";

def main():
    parser = argparse.ArgumentParser(description="This script changes filename extensions in bulk.");
    parser.add_argument("-id", "--inputdirectory", type=str, help="The input directory that will be traversed for photos and videos", required=True);
    args = parser.parse_args();

    print("Input directory: ", args.inputdirectory);
    
    for filename in glob.iglob(os.path.join(args.inputdirectory, '*.' + "aac")):
        command = ["ffmpeg.exe", "-i", filename, "-acodec", "libmp3lame", "-ab", "128k", filename + ".mp3"];
        print("Command: ", " ".join(command));
        run(command);

main();
