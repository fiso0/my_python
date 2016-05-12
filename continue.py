while True:
    s=input('enter something long:')
    if s=='quit':
        print('Done')
        break
    if len(s)<3:
        continue;
    print('input ok')
