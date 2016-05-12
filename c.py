number=23
guess=int(input('Enter an integer:'))
if guess==number:
    print('Congratulations')
    print('But here is no prize')
elif guess<number:
    print('too small')
else:
    print('too big')
print('done')
