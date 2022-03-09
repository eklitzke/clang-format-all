#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path
import argparse
import logging

logging.basicConfig()
logger = logging.getLogger('check-all')
logger.setLevel(logging.INFO)


def parse_args():
    parser = argparse.ArgumentParser(description='check-all starts at this directory and drills down recursively')
    parser.add_argument('--root_dir', type=str, required=True,
                        help='Directory to start running clang-format at.')
    args = parser.parse_args()
    return args


def is_cpp_file(path: Path):
    return path.suffix == '.cpp'


def walk_recursive(root_dir: str):
    for root, dirs, files in os.walk(root_dir):
        if dirs:
            for d in dirs:
                walk_recursive((os.path.join(root, d)))
        for file in files:
            path = Path(os.path.join(root, file))
            if is_cpp_file(path):
                if subprocess.run(["clang-format", "--dry-run", "--Werror", "-style=file",
                                   path]).returncode != 0:
                    logger.info("\"%s\": does not comply to format according to clang-format", path)
                    exit(1)
                else:
                    logger.info("\"%s\": looks fine according to clang-format", path)


def main():
    args = parse_args()
    walk_recursive(args.root_dir)


main()
