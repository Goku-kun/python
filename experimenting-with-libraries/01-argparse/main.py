import argparse
import os
import sys

dir_parser = argparse.ArgumentParser(prog="customls",
                                     description="List the content of a folder")

dir_parser.version = "1.0.0"

dir_parser.add_argument("Path", metavar="path", type=str,
                        help="path to list a directory", action="store", )

dir_parser.add_argument(
    "--verbose", "-v", help="To print verbose output", action="store_true")


args = dir_parser.parse_args()
# print(args) # namespace object
input_path = args.Path


if not os.path.isdir(input_path):
    print(input_path, "does not exist")
    sys.exit(1)

for line in os.listdir(input_path):
    if args.verbose:  # Simplified long listing
        size = os.stat(os.path.join(input_path, line)).st_size
        line = f'{line}  {size}'
    print(line)
