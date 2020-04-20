import clipboard
import hashlib
import re

print('\nWelcome to the convenient hasher "ezcrypt"\n')
print('Type in "exit" at any time to close the CLI\n')
print('Type in "reset" at any time to choose a variable to reset\n')

def out(statement=None):
    inputIndicator = '> '
    if statement != None:
        print(f'{statement}\n')
    return input(inputIndicator)

options = dict()
options['prefix'] = out('Please enter your desired prefix:')
options['length'] = list(map(int, re.findall(r'\d+', out('\nPlease enter your desired output length:'))))[0]
options['clipboard'] = True if out('\nCopy result to clipboard instead of displaying it? (Y/N)') == 'Y' else False

loop = True
while loop:
    md5 = hashlib.md5()

    inputHash = out('\nEnter your input hash:')
    
    if inputHash == 'exit':
        loop = False
        continue
    elif inputHash == 'reset':
        var = out('\nEnter the variable you want to reset:')
        if var == 'prefix':
             options['prefix'] = out('\nPlease enter your desired prefix:')
        elif var == 'length':
            options['length'] = re.findall(r'\d+', out('\nPlease enter your desired output length:'))[0]
        elif var == 'clipboard':
            options['clipboard'] = True if out('\nCopy result to clipboard instead of displaying it? (Y/N)') == 'Y' else False  
        continue

    output = md5.update(bytes(inputHash, encoding='utf-8'))
    output = options.get('prefix') + str(md5.hexdigest()).upper()[:options.get('length')]

    if options.get('clipboard'):
        clipboard.copy(output)
    else:
        print(f'\nOutput: {output}')
