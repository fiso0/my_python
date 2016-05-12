number=23
running=True

while running:
    guess=int(input('Enter an integer:'))
    if guess==number:
        print('Congratulations')
        print('But here is no prize')
        running=False
    elif guess<number:
        print('too small')
    else:
        print('too big')
print('done')
