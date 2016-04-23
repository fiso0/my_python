def ReadPage(url):  # 获取.htm内容
	from urllib import request
	html = request.urlopen(url).read()
	return html


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


def ParseIndex(href):  # 从网址获取网址内的数字部分（索引号）
	import re
	pattern = re.compile("\d+")
	index = int(pattern.search(href).group(0))
	return index


def ParseMainPage(html):  # 从htm获取所有电影标题、评分、电影子页网址和豆瓣链接
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


def ParseMoviePage(url, file_size):  # 获取某电影下载资源并按大小排序
	html = ReadPage(url)

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html, "html.parser")

	resource = []  # 存放所有满足大小要求的资源
	for i in soup.find_all('div', class_='tinfo'):
		try:
			size = i.p.em.get_text()
		except AttributeError as e:
			print('找不到下载资源')
			break

		import re
		pattern = re.compile('(\d*.?\d*)(?=[Gg][Bb])')
		try:
			size_num = float(pattern.search(size).group(0))
		except AttributeError as e:
			size_num = 0

		if size_num > file_size:
			down_addr = 'http://www.bttiantang.com' + i.a.get('href')
			resource.append((size_num, down_addr))
			print('\t' + str(size) + '\t下载地址：' + down_addr)
		else:
			print('\t' + str(size) + '\t该资源太小')
	if len(resource) > 1:
		resource.sort(key=lambda x: x[0])
	return resource


def ReadIndexInFile(filename):  # 从索引文件读取索引号
	index = []
	try:
		f = open(filename, encoding='utf-8')
		for line in f.readlines():
			index.append(int(line))
		f.close()
	except FileNotFoundError:  # 索引文件不存在
		print('暂无索引文件')
	return index


def SaveIndexInFile(filename, index):  # 添加索引号到索引文件，输入index为list
	try:  # 索引文件已存在
		f = open(filename, 'a', encoding='utf-8')
	except FileNotFoundError as e:  # 索引文件不存在
		f = open(filename, 'x', encoding='utf-8')
	finally:
		for i in index:
			f.write(str(i) + '\n')
		f.close()
		print('索引号已更新到：' + filename)


def SavePage(html):  # 保存页面内容到.htm文件
	from datetime import datetime
	time_now = datetime.now()
	filename = time_now.strftime('%y-%m-%d %H-%M-%S') + '.htm'
	with open(filename, 'x', encoding='utf-8') as f:
		f.write(str(html.decode('utf-8')))


def SaveResultInFile(filename, result):  # 保存到文件
	if len(result) > 0:
		if len(result) > 1:
			result.sort(key=lambda x: x[1], reverse=True)  # 所有结果按评分由高到低排序
		try:
			f = open(filename, 'x', encoding='utf-8')
		except FileExistsError as e:
			f = open(filename, 'a', encoding='utf-8')
		finally:
			for i in result:
				resource = i[3]
				if len(resource) > 0:
					title = i[0]
					score = i[1]
					href = i[2]
					link = i[4]
					size = resource[0][0]
					download = resource[0][1]
					f.write('=== ' + title + ' ===\n')
					f.write('\t豆瓣评分：' + str(score) + '\n')
					f.write('\t豆瓣链接：' + link + '\n')
					f.write('\t电影链接：' + href + '\n')
					f.write('\t下载地址：[' + str(size) + 'GB]' + download + '\n\n')
			f.close()
			print('结果已保存到：' + filename)
	else:
		print('没有结果需要保存')


def SaveWaitInFile(filename, wait):  # 添加需等待电影
	try:
		f = open(filename, 'x', encoding='utf-8')
	except FileExistsError:
		f = open(filename, 'a', encoding='utf-8')
	finally:
		for movie in wait:
			title = movie[0]
			score = movie[1]
			href = movie[2]
			link = movie[3]
			f.write(title + ' , ' + score + ' , ' + href + ' , ' + link + '\n')
		f.close()


def ReadWaitInFile(filename):  # 读取需等待电影
	wait = []
	try:
		f = open(filename, encoding='utf-8')
		for line in f.readlines():
			movie = line[:-1].split(' , ')  # 去掉每行最后的\n
			wait.append(movie)
		f.close()
	except FileNotFoundError:
		print('暂无等待文件')
	return wait


def UpdateWaitInFile(filename, wait):
	try:
		f = open(filename, 'w', encoding='utf-8')
		for movie in wait:
			title = movie[0]
			score = movie[1]
			href = movie[2]
			link = movie[3]
			f.write(title + ' , ' + score + ' , ' + href + ' , ' + link + '\n')
		f.close()
	except FileNotFoundError:
		print('无等待文件')
