#!/usr/bin/python

import sys, os, glob;
import argparse;
from os.path import expanduser;
from subprocess import run;

__author__ = "Jeetesh Mangwani"

def main():
    parser = argparse.ArgumentParser(description="This script converts every page of a PDF into a JPG image. Needs pdftk, imagemagick and ghostscript to be available in the system path.");
    parser.add_argument("-f", "--inputfile", type=str, help="The input PDF pages of which are needed in JPG format", required=True, default=None);
    args = parser.parse_args();
    print("Input file: ", args.inputfile);

    pdf = args.inputfile;
    dirname = os.path.splitext(pdf)[0];
    prefix=dirname;
    cwd = os.getcwd();
    dirpath = os.path.join(cwd, dirname);

    if not os.path.exists(dirpath):
        os.mkdir(dirpath);

    command = ["pdftk", pdf, "burst", "output", os.path.join(dirpath, prefix + "%04d.pdf")];
    print("Command: ", " ".join(command));
    run(command);

    metadatafile = os.path.join(dirpath, "metadata.txt");
    command = ["pdftk", pdf, "dump_data", "output", metadatafile];
    print("Command: ", " ".join(command));
    run(command);

    for file in glob.glob(os.path.join(dirpath, "*.pdf")):
        completepath = os.path.join(dirpath, file);
        basename = os.path.splitext(completepath)[0];
        imagename = basename + ".jpg";
        # explicitly setting this path because there is a system utility with the same name on Windows systems
        command = ["C:\Program Files\ImageMagick-7.0.9-2-portable-Q16-x64\convert.exe", "-colorspace", "RGB", "-interlace", "none", "-density", "300x300", "-quality", "100", file, imagename];
        print("Command: ", " ".join(command));
        run(command);
        os.remove(file);

    # sometimes, the metadata file is not found
    # os.remove(metadatafile)

main();