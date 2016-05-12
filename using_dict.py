ab={'Li Hengchao':15271815937,
    'Wang Gongyong':13237171008,
    'Wang Lili':18971238049
    }
print("Wang Gongyong's number is %s"%ab['Wang Gongyong'])

# add a key/value pair
ab['Wang Chuan'] = 13808628863

# delete a key/value pair
del ab['Li Hengchao']

print("There are %d contacts in the address-book"%len(ab))
for name,number in ab.items():
    print('%s:%d'%(name,number))

if 'Wang Chuan' in ab:
    print('%s:%d'%('Wang Chuan',ab['Wang Chuan']))

input()
