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
import os
if __name__ == "__main__":
    print("ok")
    desc = "Resume Builder Run Script"
    parser = argparse.ArgumentParser(description = desc)
    default_dir = os.path.join(os.getcwd(), "data")
    parser.add_argument(
                        "-d",
                        "--data", 
                        type=str, #path is a string
                        default=default_dir,
                        help="Path to data folder."
                        )
    parser.add_argument(
                        "-v", "--verbose",
                        action="store_true",
                        help=("increase output "
                                "verbosity")
                    )
    args = parser.parse_args()
    path_to_data = args.data
    if args.verbose:
        print("Verbose mode on.")
    if not os.path.isdir(path_to_data):
        message = ("No data folder "
                    "available at"
                    " {}.").format(path_to_data)
        print(message)



