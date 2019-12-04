#!/usr/bin/python

import os
import sys

CURRENT_DIR = os.getcwd()

def main(source):
    if not os.path.isdir(source):
        print("Not a directory!")

    else:
        result = open("input/input_sequence", "w")
        
        input_files = [os.path.join(source, x) for x in os.listdir(source) if os.path.isfile(os.path.join(source, x))]

        for x in input_files:
            result.write(x + "\n")

        result.close()

if __name__ == "__main__":
    if sys.argv[1] is None:
        print("Must provide the source's directory!")
    else:
        path = sys.argv[1]
        main(path)