"""
从豆瓣电影获取所有“想看”的电影，然后自动到BT电影天堂去搜索，查看是否有高清资源，最后给出结果
"""

from bs4 import BeautifulSoup
import requests
import re
import pickle
import csv
import logging

BT_URL = 'http://www.bttiantang.com'
INDEX_PICKLE_FILE = 'Movie_wish.pickle'
RESULT_CSV_FILE = 'Movie_wish.csv'

def get_soup_of(url):
	"""获取某个url的soup
	:param url: 待获取的网页地址
	"""
	try:
		html = requests.get(url).text
		soup = BeautifulSoup(html, 'lxml')
	except:
		soup = None
	return soup


def get_bt_search_url(movie_title):
	"""拼接得到在BT天堂搜索某部电影时用到的url
	:param movie_title: 电影名
	"""
	search_head = 'http://www.bttiantang.com/s.php?q='
	search_tail = '&sitesearch=www.bttiantang.com&domains=bttiantang.com&hl=zh-CN&ie=UTF-8&oe=UTF-8'
	return search_head + movie_title + search_tail


def get_douban_url(url):
	"""根据BT给出的跳转链接获得豆瓣页url
	:param url: BT天堂给出的豆瓣页中间跳转页面地址
	"""
	soup = get_soup_of(url)

	if soup == None:
		return None

	text = soup.get_text()

	link = url
	try:
		link = re.search("\"([^\"]*)\"", text).group(1)
	except AttributeError:  # 有可能显示"error!
		pass
	return link


def get_movie_index(url):
	index = re.split(r'/', url)[-2]
	return index


def search_bt_movie(movie_title):
	"""在BT天堂上搜索电影
	:param movie_title: 需要搜索的电影标题
	:return: 所有搜索结果的BT页面地址和对应的豆瓣页面地址（元祖列表）
	"""
	print('开始搜索BT电影天堂')
	bt_search_url = get_bt_search_url(movie_title)
	soup = get_soup_of(bt_search_url)

	if soup == None:
		return []

	# BT天堂搜索结果的详细电影页面地址
	movies_bt_url = [BT_URL + a.get('href') for a in soup.select('.title .tt a')]

	# BT天堂搜索结果对应的豆瓣页地址
	bt_douban_link = soup.find_all('a', title='去豆瓣查看影片介绍')
	bt_douban_jump = [BT_URL + link.get('href') for link in bt_douban_link]
	bt_douban_url = [get_douban_url(jump) for jump in bt_douban_jump]

	results = [(bt, douban) for bt in movies_bt_url for douban in bt_douban_url]
	return results


def get_downloads(url, file_size=3):
	"""获取某电影下载资源并按大小排序
	:param file_size: 高清电影资源的大小下限，默认3GB
	:param url: BT天堂网址中某部电影的页面地址
	:return: 所有下载资源的大小和地址（字典列表）
	"""
	resource = []  # 存放所有满足大小要求的资源

	soup = get_soup_of(url)

	if soup == None:
		return resource

	downloads = soup.find_all('div', class_='tinfo')

	if len(downloads) == 0:
		print('找不到下载资源')
		return []

	for i in downloads:
		try:
			size = i.p.em.get_text()
			(size_num, size_unit) = re.search(r'(\d*.?\d*)([GgMm][Bb])', size).groups()
			size_num = float(size_num)

			if (size_unit == 'GB' or size_unit == 'gb') and size_num > file_size:
				down_addr = BT_URL + i.a.get('href')
				down_info = {'size': size_num, 'download_addr': down_addr}
				resource.append(down_info)
				print('\t' + str(size) + '\t下载地址：' + down_addr)
			else:
				print('\t' + str(size) + '\t该资源太小')
		except AttributeError:
			print('\t没搜索到下载资源')

	# if len(resource) > 1:
	# 	resource.sort(key=lambda x: x[0])
	return resource


def save_in_txt(filename, results):
	if len(results) > 0:
		try:
			f = open(filename, 'x', encoding='utf-8')
		except FileExistsError:
			f = open(filename, 'a', encoding='utf-8')
		finally:
			for i in results:
				resource = i['download']
				if len(resource):
					title = i['title']
					link = i['douban_url']
					href = i['bt_url']
					f.write('=== ' + '/'.join(title) + ' ===\n')
					f.write('\t豆瓣链接：' + link + '\n')
					f.write('\t电影链接：' + href + '\n')
					f.write('\t下载地址：\n')
					for res in resource:
						size = res['size']
						download = res['download_addr']
						f.write('\t[' + str(size) + 'GB]\t' + download + '\n')
					f.write('\n')
			f.close()
			print('结果已保存到：' + filename)
	else:
		print('没有结果需要保存')


def save_result_in_csv(result, filename = RESULT_CSV_FILE):
	result_list = [result['index'], result['title'][0], result['douban_url'], result['bt_url']]
	for down_info in result['download']:
		result_list.append(str(down_info['size']))
		result_list.append(down_info['download_addr'])

	try:
		f = open(filename, 'x', newline='')
	except FileExistsError:
		f = open(filename, 'a', newline='')
	finally:
		spam_writer = csv.writer(f)
		spam_writer.writerow(result_list)
		f.close()
		print('结果已保存到：' + filename)

def save_in_pickle(filename, results):
	if len(results) > 0:
		try:
			f = open(filename, 'bx')
		except FileExistsError:
			f = open(filename, 'bw')
		finally:
			pickle.dump(results, f)
			f.close()
			print('索引已保存到：' + filename)
	else:
		print('没有索引需要保存')


def finish_parse(result, index=None):
	# 保存结果
	result_txt_file = 'Movie_wish.txt'
	save_in_txt(result_txt_file, result)

	if index:
		# 保存索引号
		save_in_pickle(INDEX_PICKLE_FILE, index)


def get_from_pickle(filename):
	print('读取已解析电影索引号')
	try:
		with open(filename, 'br') as f:
			index = pickle.load(f)
			print('读取成功：')
			print(index)
	except FileNotFoundError:
		index = set([])
		print('读取失败,新建索引集合')
	return index


def get_index_from_csv(filename = RESULT_CSV_FILE):
	print('读取已解析电影索引号')
	index = set([])
	try:
		with open(filename, newline='') as f:
			spam_reader = csv.reader(f)
			for row in spam_reader:
				index.add(row[0])
	except FileNotFoundError:
		print('读取失败,新建索引集合')
	return index


# 主程序

# 所有解析成功的电影索引号集合（无重复）
# index_set = get_from_pickle(INDEX_PICKLE_FILE)
index_set = get_index_from_csv()
print('结果中已有' + str(len(index_set)) + '部电影')

# 用于保存所有新解析结果的列表
movie_list = []

# 豆瓣电影 我的想看 页面
douban_url = 'https://movie.douban.com/people/35209764/wish'
soup = get_soup_of(douban_url)

# 总的想看电影数量
douban_wish_cnt = int(re.findall(r'\d+', soup.select_one('#db-usr-profile .info h1').text)[0])

# 获取想新解析多少部电影
user_input = input('请输入想新解析多少部电影(0表示全部)：')
try:
	wish_count = int(user_input)
except ValueError:
	wish_count = 0

if wish_count == 0 or wish_count > douban_wish_cnt:
	wish_count = douban_wish_cnt

# 从第一页开始 对每一页解析
for start in range(0, wish_count, 15):
	douban_page_url = douban_url + '?start=' + str(start)
	soup = get_soup_of(douban_page_url)

	# 该页内所有的电影条目（默认最大15条）
	items_in_one_page = soup.select('.item')

	parse_continue = True
	# 对一部电影解析
	for item in items_in_one_page:
		if parse_continue:
			# 保存一部电影的全部信息：包括豆瓣链接，豆瓣电影索引号，电影标题，下载资源（字典）
			movie = {}

			# 电影标题
			movie_titles = item.select_one('.title').text.replace(' ', '').replace('\n', '').split('/')
			movie['title'] = movie_titles
			print('电影：' + movie_titles[0])

			# 豆瓣电影页网址
			movie_douban_url = item.select_one('.title a').get('href')
			movie['douban_url'] = movie_douban_url
			print('豆瓣链接：' + movie_douban_url)

			# 豆瓣电影索引号
			movie_douban_index = get_movie_index(movie_douban_url)
			movie['index'] = movie_douban_index
			if movie_douban_index in index_set:
				print('已解析过此电影，下一部')
				continue

			# 尝试到BT天堂上搜索该电影，获取搜索结果的BT页面地址和对应的豆瓣页面地址
			search_results = search_bt_movie(movie_titles[0])

			# 根据豆瓣页面是否相同确认为正确的搜索结果
			for (bt, douban) in search_results:
				if douban.split(':')[1] == movie_douban_url.split(':')[1]:
					print('搜索到该电影，开始搜索下载资源')

					# 电影的bt页面地址
					movie['bt_url'] = bt

					# 获取高清资源大小和下载地址（字典列表）
					movie_downloads = get_downloads(bt)
					break
				# else:
				# 	print(douban)
				# 	print(movie_douban_url)
			else:
				print('没有搜索到该电影')
				movie_downloads = []

			# 电影下载资源
			movie['download'] = movie_downloads
			# 搜索到了可下载资源
			if len(movie_downloads):
				index_set.add(movie_douban_index)

				# 将此部电影所有相关信息添加到电影结果列表中
				movie_list.append(movie)

				# 保存该电影结果到输出文件
				save_result_in_csv(movie)

			if len(movie_list) >= wish_count:
				parse_continue = False

		else:
			break

print('已解析完毕')
