import pickle as p

shoplistFile = 'shoplist.pickle'
shoplist = ['apple','mango','carrot']

with open(shoplistFile,'wb') as fw:
    p.dump(shoplist, fw, p.HIGHEST_PROTOCOL)

with open(shoplistFile,'rb') as fr:
    data = p.load(fr)

print(data)
