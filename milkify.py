#!/usr/bin/env python3

import sys
import os
from functools import reduce

def process_line(line):
    return " milk ".join(line.split())

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Not enough arguments")
        exit()

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("File path invalid")
        exit()

    # if not os.access(os.path.dirname(file_path), os.W_OK):
    #     print("Cannot write to given file path")
    #     exit()

    f = open(file_path, "r")
    lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = process_line(lines[i])

    f = open(file_path, "w")
    f.writelines(lines)
