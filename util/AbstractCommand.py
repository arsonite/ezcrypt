#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class AbstractCommand:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.subcommands = list()

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

    def addSubcommand(self, subcommand):
        """Function to add subcommand to internal list

        Arguments:
            subcommand {Object} -- Subcommand
        """
        self.subcommands.append(subcommand)
