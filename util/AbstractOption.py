#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class AbstractOption:
    __metaclass__ = ABCMeta

    def __init__(self, xml):
        self.name = xml['name']
        self.description = xml['description']
        self.flags = xml['flags']
        pass

    def exists(self, key, value):
        try:
            return key[value]
        except:
            return None

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Abstract method for the main execution function
        """
        pass
