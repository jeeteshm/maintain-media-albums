#!/usr/bin/python

import sys, os;
import argparse;
from os.path import expanduser;

__author__ = "Jeetesh Mangwani"

def resizeFile(filePath, args):
    print("Dealing with the file: ", filePath);