#!/usr/bin/env python3

from collections import OrderedDict
from sys import exit

from util.keys import NL, SPACE, TAB

class Parser():
    def __init__(self, argv):
        self.argv = argv

        # All arguments in parser
        self.commands = OrderedDict()

        # All options and flags in parser
        self.options = OrderedDict()

    def add_arg(self, *args, **kwargs):
        self.commands[kwargs.get('name')] = dict({
            'name': kwargs.get('name'),
            'description': kwargs.get('description'),
            'execute': kwargs.get('execute'),
        })
        self.commands = OrderedDict(sorted(self.commands.items()))

    def add_option(self, *args, **kwargs):
        self.options[kwargs.get('name')] = dict({
            'name': kwargs.get('name'),
            'description': kwargs.get('description'),
            'flags': kwargs.get('flags'),
            'execute': kwargs.get('execute', None),
            'enabled': False,
        })
        self.options = OrderedDict(sorted(self.options.items()))

    def enable_flag(self, flag):
        self.options[flag]['enabled'] = True

    def flag_enabled(self, flag):
        return self.options[flag]['enabled']

    def execute_command(self, *args, **kwargs):
        self.commands[kwargs.get('key')]['execute'](args=args, kwargs=kwargs)
        exit(0)

    def execute_option(self, *args, **kwargs):
        self.options[kwargs.get('key')]['execute'](args=args, kwargs=kwargs)
        exit(0)

    def info(self):
        message = f'{NL}usage: $ ezcrypt [OPTIONS] [COMMAND] [...SUB-COMMANDS]{NL}{NL}'
        message += f'A CLI for easy encryption.{NL}{NL}'

        # Options
        spaces = 20
        message += f'{SPACE}options:{NL}'
        for option in self.options.values():
            name = option['name']
            description = option['description']
            flags = option['flags']['flag']
            flag = f'{TAB}['
            for i in range(0, len(flags)):
                flag += f'{flags[i]}'
                if i < len(flags) - 1:
                    flag += ', '
            message += flag + ']'

            for i in range(0, (spaces - len(flag))):
                message += SPACE
            message += f'{description}{NL}'

        # Commands
        spaces = 12
        message += f'{NL}{SPACE}commands:{NL}'
        for command in self.commands.values():
            name = command['name']
            description = command['description']
            message += f'{TAB}{name}'

            for i in range(0, (spaces - len(name))):
                message += SPACE

            message += f'{description}{NL}'

        print(message)
        exit(1)

    def parse(self):
        params = self.argv

        if len(params) > 1:
            for param in params:
                if param in self.commands:
                    self.execute_command(key=param)
                else:
                    for option in self.options:
                        opt = self.options[option]
                        if param in opt['flags']:
                            if opt['execute'] != None:
                                self.execute_option(key=option)
                            self.enable_flag(option)
        else:
            self.info()

# print("ezcrypt: '' is not a valid command.")
# print('ezcrypt: flag '' needs an argument.')
