# Filename:try_except.py

import sys

try:
    s = input('Enter something -->')
except EOFError:
    print('Why did you do an EOF on me?')
    sys.exit()
except:
    print('Some error/exception occured.')

print('Done')
