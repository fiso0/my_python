shoplist=['apple','banana','mango','carrot']
print('I have',len(shoplist),'items to purchase.')
print('These items are:',)
for item in shoplist:
    print(item,)

print('\nI also have to buy rice')
shoplist.append('rice')
print('My shoplist is now',shoplist)

print('I will sort my list now')
shoplist.sort()
print('My shoplist is now',shoplist)

print('The first item to buy:',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought:',olditem)
print('My shoplist is now',shoplist)
