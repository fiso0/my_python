# Filename:using_file.py

poem='''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt', 'w') # open for 'w'riting
f.write(poem)
f.close()

f = open('poem.txt')
# if no mode is specified, 'r'ead mode is assumed
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line,)
f.close() # close the file

wait=input()