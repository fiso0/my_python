def ReadPage(url):  # 获取.htm内容
	from urllib import request
	html = request.urlopen(url).read()
	return html


def SavePage(html):  # 保存页面内容到.htm文件
	from datetime import datetime
	time_now = datetime.now()
	filename = time_now.strftime('%y-%m-%d %H-%M-%S') + '.htm'
	with open(filename, 'x', encoding='utf-8') as f:
		f.write(str(html.decode('utf-8')))


def GetDoubanLink(url):
	html = ReadPage(url)

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html, "html.parser")
	text = soup.get_text()

	import re
	p = re.compile("\"([^\"]*)\"")

	try:
		link = p.search(text).group(1)
	except:  # 有可能显示"error!
		link = url
	return link


def ParseMainPage(html):  # 获取所有电影标题、评分和链接
	movie = []

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html, "html.parser")

	movie_title = []
	title_hot = soup.find_all('div', class_='title')
	size_t = len(title_hot)

	movie_score = []
	score_hot = soup.find_all('p', class_='rt')
	size_s = len(score_hot)

	movie_href = []

	movie_link = []
	link_hot = soup.find_all('a', title='去豆瓣查看影片介绍')

	if size_s == size_t:
		import re
		p = re.compile("\d.?\d")
		for i in range(0, size_t):
			title = title_hot[i].a.get_text()
			score = p.search(score_hot[i].get_text()).group(0)
			href = 'http://www.bttiantang.com' + title_hot[i].a.get('href')
			link_jump = 'http://www.bttiantang.com' + link_hot[i].get('href')
			link = GetDoubanLink(link_jump)
			movie_title.append(title)
			movie_score.append(score)
			movie_href.append(href)
			movie_link.append(link)
			movie.append((title, score, href, link))
		# movie.sort(key=lambda x:x[1],reverse=True)
	return movie


def ParseIndex(href):
	import re
	pattern = re.compile("\d+")
	index = int(pattern.search(href).group(0))
	return index


def ParseMoviePage(url, file_size):  # 获取某电影下载资源并按大小排序
	html = ReadPage(url)

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html, "html.parser")

	resource = []
	for i in soup.find_all('div', class_='tinfo'):
		size = i.p.em.get_text()
		import re
		pattern = re.compile('(\d*.?\d*)(?=[Gg][Bb])')
		try:
			size_num = float(pattern.search(size).group(0))
		except AttributeError as e:
			size_num = 0
		if size_num > file_size:
			href = 'http://www.bttiantang.com' + i.a.get('href')
			resource.append((size_num, href))
			print(str(size) + '\t下载地址：' + href)
		else:
			print(str(size) + '\t该资源太小')
	if len(resource) > 1:
		resource.sort(key=lambda x: x[0])
	else:#该电影暂无高清资源
		pass#todo:高质量电影，待日后重查资源
	return resource


def SaveResultInFile(result,score_th,size_th,pages):  # 保存到文件
	from datetime import datetime
	time_now = datetime.now()
	resFile = time_now.strftime('%y-%m-%d') + \
				'_' + str(score_th) + '_' + str(size_th) + \
				'_' + str(pages) + '.txt'
	try:
		f = open(resFile, 'x', encoding='utf-8')
	except FileExistsError as e:
		f = open(resFile, 'w', encoding='utf-8')
	finally:
		for i in result:
			resource = i[3]
			if len(resource) > 0:
				title = i[0]
				score = i[1]
				link = i[4]
				size = resource[0][0]
				download = resource[0][1]
				f.write('=== ' + title + ' ===\n')
				f.write('\t豆瓣评分：' + str(score) + '\n')
				f.write('\t豆瓣链接：' + link + '\n')
				f.write('\t下载地址：[' + str(size) + 'GB]' + download + '\n\n')
		f.close()
		print('\n结果已保存到：' + resFile)


def SaveIndexInFile(index):
	filename = 'MovieIndex.txt'
	index = set(index)
	try:  # 索引文件已存在
		f = open(filename, 'a', encoding='utf-8')
	except FileNotFoundError as e:  # 索引文件不存在
		f = open(filename, 'x', encoding='utf-8')
	finally:
		for i in index:
			f.write(str(i) + '\n')
		f.close()
		print('\n结果已保存到：' + filename)


def ReadIndexInFile():
	filename = 'MovieIndex.txt'
	index = set([])
	try:
		f = open(filename, encoding='utf-8')
		for line in f.readlines():
			index.add(int(line))
		f.close()
	except FileNotFoundError as e:  # 索引文件不存在
		print('暂无索引文件')
	return index


# 主程序
# 与索引文件内的记录对比，只解析没有记录的电影
# 所有解析过的电影索引都保存在MovieIndex.txt文件中
# 新解析的电影结果存到当日日期文件中
print('将要从BT天堂读取电影资源，请输入最低评分和资源大小')
print('请输入能接受的最低评分：')
score_th = float(input())
print('请输入能接受的最小资源（GB）：')
size_th = float(input())

print('请输入想要读取多少页：')
pages = int(input())

result = []
index_old = ReadIndexInFile()
index_new = set([])
for pageNo in range(1, pages + 1):
	url = 'http://www.bttiantang.com/?PageNo=' + str(pageNo)
	html = ReadPage(url)
	movie = ParseMainPage(html)
	for i in movie:
		title = i[0]
		score = float(i[1])
		href = i[2]
		index = ParseIndex(href)
		link = i[3]
		try:
			print('\n===' + title + '===' + str(score) + '===')
		except:
			print('\n===电影名无法显示在Console===')
		if score <= score_th:
			print('评分太低')
		elif index in index_old:
			print('此电影已解析过')
		else:
			index_new.add(index)
			print('豆瓣链接：' + link)
			resource = ParseMoviePage(href, size_th)
			result.append([title, score, href, resource, link])

SaveResultInFile(result,score_th,size_th,pages)
SaveIndexInFile(index_new)

print('请按回车键退出')
input()
