def sayHelloTo(name):
    print('Hello,',name)

while True:
    name=input("what's your name?")
    if name=='quit':
        break
    sayHelloTo(name)
print('Done')

input()