#!/usr/bin/python3
"""Resume Builder run script.

This file can be used to build your resume. However
before you call it, ensure that you have the
required files in the structure below:
    data/
    data/personal_information/
    data/personal_information/images/
    data/education/
    data/education/images
    data/experience/
    data/experience/images
    data/projects/
    data/projects/images

Each of the sub folders within data will need at 
least one json file. Perhaps at a later date, I 
will make a GUI to better help with this 
information entry.
"""

#TODO: Need to figure out a structure for the JSONs.

import argparse

if __name__ == "__main__":
    print("ok")
    desc = "Resume Builder Run Script"
    parser = argparse.ArgumentParser(description = desc)
    parser.add_argument(
                        "path", 
                        metavar="P",
                        type=str,
                        default="data",
                        help="Path to data"
                        )
    args = parser.parse_args()
    print(args.path)
