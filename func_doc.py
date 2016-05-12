def func(a,b=5,c=10):
    '''This doc must start with a Capital letter
Prints a,b,c
default is b=5,c=10
and this doc must end with a dot.'''
    print('a is',a,'and b is',b,'and c is',c)

func(3,7)
func(25,c=24)
func(c=2,a=4)
