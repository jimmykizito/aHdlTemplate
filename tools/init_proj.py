#!/usr/bin/env python
"""
Initialise HDL project.
"""

import argparse
import os
import shutil

if __name__ == "__main__":

    # Parse arguments.
    DIR_DEFAULT = 'aHdlTemplate.git'
    parser = argparse.ArgumentParser(description='Initialise HDL project.')
    parser.add_argument('proj', nargs=1, help='Project name.')
    parser.add_argument('--dir_orig', '-d', default=DIR_DEFAULT, nargs=1,
                        help='Original project directory name. [default:%s]' %
                        (DIR_DEFAULT))
    args = parser.parse_args()
    print(args)

    # Delete .git directory after determining project path.
    path_script = os.path.dirname(os.path.realpath(__file__))
    path_proj = path_script
    while args.dir_orig != os.path.basename(path_proj):
        path_proj = os.path.split(path_proj)[0]
    path_git = os.path.join(path_proj, '.git')
    if os.path.isdir(path_git):
        print("shutil.rmtree(path_git) %s" % (path_git))
        shutil.rmtree(path_git)

    # Initialise project files

    # Initialise project file names

