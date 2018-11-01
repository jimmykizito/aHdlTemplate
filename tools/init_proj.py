#!/usr/bin/env python
"""
Initialise HDL project.
"""

import argparse
import os
import shutil
import sys

# TODO: Refactor to use ProjMgmt class.

def init_proj_fmt_name(proj_arg):
    """
    Format project name argument such that:
    - It is all lower case.
    - Words are separated by underscores.
    """
    proj_name = '_'.join(proj_arg.lower().split())
    return proj_name

def init_proj_fmt_dir(proj_name):
    """
    Format project name argument such that:
    - It is CamelCase.
    - It is prepended by the letter 'a'.
    """
    proj_dir = 'a' + ''.join([word.title() for word in proj_name.split('_')])
    return proj_dir

if __name__ == '__main__':

    # Parse arguments.
    PROJ_DIR_DEFAULT = 'aHdlTemplate.git'
    parser = argparse.ArgumentParser(description='Initialise HDL project.')
    parser.add_argument('proj_name', help='Project name.')
    parser.add_argument('--dir_orig', '-d', default=PROJ_DIR_DEFAULT,
                        help='Original project directory name. [default:%s]' %
                        (PROJ_DIR_DEFAULT))
    args = parser.parse_args()

    # Delete .git directory after determining project path.
    path_script = os.path.dirname(os.path.realpath(__file__))
    path_proj = path_script
    while args.dir_orig != os.path.basename(path_proj):
        path_proj = os.path.split(path_proj)[0]
        if os.path.split(path_proj)[1] == '':
            print 'Unable to find dir(%s)' % (args.dir_orig)
            sys.exit(-1)
    path_git = os.path.join(path_proj, '.git')
    if os.path.isdir(path_git):
        print 'Removing git directory: %s' % (path_git)
        shutil.rmtree(path_git)

    # Format project name and project directory name.
    proj_name = init_proj_fmt_name(args.proj_name)
    print 'Project name (%s) derived from script arg (%s).' \
        % (proj_name, args.proj_name)
    proj_dir = init_proj_fmt_dir(proj_name)
    print 'Project directory (%s) derived from project name (%s).' \
        % (proj_dir, proj_name)

# rename 's/hdl_bits/__proj__/g' *.py

    # TODO: Rather search project directory (to max depth ~3) for files with
    #       template marker "__proj__".
    # Initialise project files.
    # Constant list of prject files to modify.
    # Each row it the path of the file relative to the project root directory.
    PROJ_FILES = [
        ['hdl', 'verilog', 'top___proj__.v'],
        ['hdl', 'vhdl', 'top___proj__.vhd'],
        ['tests', 'cocotb', 'test___proj__.py'],
        ['tests', 'cocotb', 'verilog', 'Makefile'],
        ['tests', 'cocotb', 'vhdl', 'Makefile']
    ]
    PROJ_NAME_DEFAULT = '__proj__'

    for proj_file in PROJ_FILES:
        in_file = os.path.join(path_proj, *proj_file)
        print 'Initialising (%s)' % (in_file)
        # Create a temporary file for project files that will not be renamed.
        if PROJ_NAME_DEFAULT in in_file:
            out_file = in_file.replace(PROJ_NAME_DEFAULT, proj_name)
        else:
            out_file = in_file + '.tmp'
        with open(in_file, 'r') as file_in, open(out_file, 'w') as file_out:
            for line_in in file_in:
                line_out = line_in.replace(PROJ_NAME_DEFAULT, proj_name)
                file_out.write(line_out)
        if PROJ_NAME_DEFAULT in in_file:
            os.remove(in_file)
        else:
            os.rename(out_file, in_file)

    # Rename project directory.
    proj_dir_old = path_proj
    proj_dir_new = path_proj.replace(args.dir_orig, proj_dir)
    print 'Project directory (%s) renamed as (%s).' \
        % (proj_dir_old, proj_dir_new)
    #Python 3 ? os.renames(proj_dir_old, proj_dir_new)
    shutil.move(proj_dir_old, proj_dir_new)
