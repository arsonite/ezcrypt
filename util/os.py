#!/usr/bin/env python3

from collections import OrderedDict
from os import environ, getcwd, name, scandir
from os import mkdir as osdir
from pathlib import Path
from platform import architecture, machine, processor, platform, release, system, version
from re import search
from shutil import copy, move, rmtree
from sys import executable, version_info

def append(path, content):
    """Appends string content to an existing file

    Arguments:
        path {String} -- Path
        content {String} -- Content
    """
    f = open(path, "a")
    f.write(content)
    f.close()

def cp(copyFrom, copyTo):
    copy(copyFrom, copyTo)

def ls(path):
    pass

def mkdir(path):
    try:
        osdir(path)
    except FileExistsError:
        return

def mv(moveFrom, moveTo):
    move(moveFrom, moveTo)

def read(path):
    f = open(path, "r")
    return f.read()

def rm(path):
    rmtree(path)

def recursiveSearch(path, regex):
    paths = list()

    def recursive(path, regex):
        for entry in scandir(path):
            if entry.is_dir():
                if search(regex, str(entry.path)):
                    paths.append(entry.path)
                else:
                    try:
                        yield from recursive(entry.path, regex)
                    except:
                        continue

    for entry in recursive(path, regex):
        continue
    return paths

def write(path, content):
    f = open(path, "w")
    f.write(content)
    f.close()

paths = OrderedDict({
    'current': getcwd(),
    'executable': executable,
    'home': str(Path.home()),
    'PATH': environ.get('PATH'),
    'root': environ.get('PATH'),
})
paths['root'] = paths['home'] + '\\.ezcrypt\\cli'
paths['main'] = paths['root'] + '\\main.py'
paths = OrderedDict(sorted(paths.items()))

python = OrderedDict({
    'minimumVersion': '3.0',
    'maximumVersion': '3.6.8',
    'optimalVersion': '3.6.8',
    'systemVersion': f'{version_info[0]}.{version_info[1]}.{version_info[2]}',
})

system = OrderedDict({
    'isUnixBased': name != 'nt',

    'architecture': architecture()[0],
    'core': name,
    'machine': machine(),
    'processor': processor(),
    'platform': platform(),
    'release': release(),
    'system': system(),
    'version': version(),
})
