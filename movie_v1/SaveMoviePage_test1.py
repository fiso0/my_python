from urllib import request
url='http://www.bttiantang.com/'
html=request.urlopen(url).read()
data=html.decode('utf-8')

from datetime import datetime
time_now=datetime.now()
filename=time_now.strftime('%Y-%m-%d')+'.htm'

try:
	f=open(filename,'x',encoding='utf-8')#parameter 'encoding' is important!
	f.write(data)
	f.close()
except FileExistsError as e:
	print('同名文件已存在')