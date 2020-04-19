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

loop = True
prefix = out('Please enter your desired prefix:')
length = list(map(int, re.findall(r'\d+', out('\nPlease enter your desired output length:'))))[0]
copyToClipboard = True if out('\nCopy result to clipboard instead of displaying it? (Y/N)') == 'Y' else False
availableHashAlgorithms = list()
selectedHashAlgorithm = ''

while loop:
    md5 = hashlib.md5()

    inputHash = out('\nEnter your input hash:')
    
    if inputHash == 'exit':
        loop = False
        continue
    elif inputHash == 'reset':
        var = out('\nEnter the variable you want to reset:')
        if var == 'prefix':
            prefix = out('\nPlease enter your desired prefix:')
        elif var == 'length':
            length = re.findall(r'\d+', out('\nPlease enter your desired output length:'))[0]
        elif var == 'copyToClipboard':
            copyToClipboard = True if out('\nCopy result to clipboard instead of displaying it? (Y/N)') == 'Y' else False  
        continue

    output = md5.update(bytes(inputHash, encoding='utf-8'))
    output = prefix + str(md5.hexdigest()).upper()[:length]

    if copyToClipboard:
        clipboard.copy(output)
    else:
        print(f'\nOutput: {output}')
