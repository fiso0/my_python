name='Jackie'

if name.startswith('J'):
    print('It starts with "J"')

if 'a' in name:
    print('It has "a"')

if name.find('ck') != -1:
    print('It contains "ck"')

delimiter='_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))
