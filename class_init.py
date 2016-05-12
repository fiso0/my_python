class Person:
    def __init__(self,name):
        self.name=name;
    def sayHi(self):
        print("Hello, I'm %s"%self.name)

p = Person('Jackie')
p.sayHi()
input()
