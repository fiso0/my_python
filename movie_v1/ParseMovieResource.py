#Parse the movie page, find if HD resourse available.

def ParseMovieResource(url,size_th):
	from urllib import request
	html=request.urlopen(url).read()

	from datetime import datetime
	time_now=datetime.now()

	# Write in file (for test)
	try:
		filename=time_now.strftime('%y-%m-%d_')+'tt_movie.htm'#beta edition
		f=open(filename,'x',encoding='utf-8')
		f.write(str(html.decode('utf-8')))
		f.close()
	except FileExistsError as e:
		print('同名结果文件已存在')

	# Parse html
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html,"html.parser")

	resource=[]
	for i in soup.find_all('div',class_='tinfo'):
		size=i.p.em.get_text()
		import re
		pattern=re.compile('(\d*.?\d*)(?=[Gg][Bb])')
		try:
			size_num=float(pattern.search(size).group(0))
		except AttributeError as e:
			size_num=0
		if size_num > size_th:
			href='http://www.bttiantang.com'+i.a.get('href')
			resource.append((size_num,href))
			print(str(size)+'该资源可能为高清\t下载地址：'+href)
		else:
			print(str(size)+'该资源不是高清')
	if len(resource)>1:
		# Sort
		resource.sort(key=lambda x:x[0])
	return resource

# # TEST
# url='http://www.bttiantang.com/subject/27724.html'
# resource=ParseMovieResource(url)
# print(resource[0][0]+'\t'+resource[0][1])
# print('\n请按回车键退出')
# input()