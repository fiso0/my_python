an_2 = 0
an_1 = 1
print(str(an_1)+'\n')
for i in range(1,10):
	an = an_2+an_1
	print(str(an)+'\n')
	an_2=an_1
	an_1=an

input()