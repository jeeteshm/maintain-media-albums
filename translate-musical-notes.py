#!/usr/bin/python

import sys, os, glob;
import argparse;
from os.path import expanduser;
from subprocess import run;
import re;

__author__ = "Jeetesh Mangwani"

def main():
    parser = argparse.ArgumentParser(description="This script translates musical notes to numeric format");
    parser.add_argument("-i", "--inputfile", type=str, help="The input file containing musical notes", required=True, default=None);
    parser.add_argument("-o", "--outputfile", type=str, help="The output file containing translated musical notes", required=True, default=None);
    args = parser.parse_args();
    print("Input file: ", args.inputfile);
    print("Output file: ", args.outputfile);

    with open(args.inputfile, "r") as rawLines:
        with open(args.outputfile, "w") as translatedLines:
            for rawLine in rawLines:
                musicRegex = re.compile(r"^([A-G][\-\+#b_]* +)*[A-G][\-\+#b_]*$")
                translatedLines.write(rawLine);
                m = musicRegex.search(rawLine);

                if(m):
                    translatedLines.write(
                        rawLine
                            .replace("C", "1")
                            .replace("D", "2")
                            .replace("E", "3")
                            .replace("F", "4")
                            .replace("G", "5")
                            .replace("A", "6")
                            .replace("B", "7")
                            .replace("+", "#")
                            .replace("^", "#")
                            .replace("_", "b")
                            .replace("-", "b")
                    )

main();