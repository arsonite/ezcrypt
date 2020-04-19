#!/usr/bin/env python

from re import search

from util.os import cp, mkdir, paths, recursiveSearch, rm, write

# Doesn't bundle entire source code if production == False
production = False
print(f'Production flag set to {production}.\n')

buildDirectory = paths['root'] + '\\build'
osBuildDirectory = buildDirectory + '\\nt'
entrypointDirectory = osBuildDirectory + '\\entrypoint.bat'

# Windows .bat assembly
print('... Assembling entrypoint.bat\n')
entrypoint = '@ECHO OFF\n'
entrypoint += 'py ' + paths['main'] + ' %*'
print('Assembling complete.\n')

mkdir(buildDirectory)
print('Created build directory.\n')
mkdir(osBuildDirectory)
print('Created os-specific build sub-directory.\n')
write(entrypointDirectory, entrypoint)
print('Written entrypoint script to entrypoint.bat.\n')

print('Recursively searching for all python script directories.\n')
scripts = recursiveSearch(paths['home'], r'.*\\Python\\.*\\Scripts')

for script in scripts:
    cp(osBuildDirectory + '\\entrypoint.bat', script + '\\vs.bat')
    print(f'\nCopied vs.bat to script directory {script}.\n')

if(search('[Yy]', input('\nDo you want to delete the build-folder? (Y/N)'))):
    rm(buildDirectory)
    print('\nRemoved build directory and contents.\n')

# TODO: Look if python scripts directory is in PATH

# TODO: On UNIX look for bin directories in PATH

# subprocess.check_call(["pip", "install", '.'])
