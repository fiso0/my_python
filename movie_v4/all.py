import mymovie
from datetime import datetime

print('开始检查等待列表中的电影......')

SIZE_MIN = 3  # 至少3GB

WAIT_FILE = 'WaitingRoom.txt'

time_now = datetime.now()
RESULT_FILE = 'Wait_' + time_now.strftime('%Y%m%d') + '.txt'

waits_old = mymovie.ReadWaitInFile(WAIT_FILE)
waits_new = []  # 暂缓的结果
results = []  # 成功的结果

# 从第一部等待电影开始解析
for movie in waits_old:
	title = movie[0]
	score = float(movie[1])
	href = movie[2]
	link = movie[3]

	# 打印电影信息
	try:
		print('===' + title + '===' + str(score) + '===')
	except UnicodeEncodeError:
		print('===电影名无法显示在Console===')

	resource = mymovie.ParseMoviePage(href, SIZE_MIN)  # 解析电影子页，查找高清资源
	if len(resource) > 0:  # 有高清资源
		print('\t>>解析完毕')
		results.append([title, score, href, resource, link])  # 保存成功结果
	else:  # 没有满足大小要求的资源
		print('\t>>无高清资源，保留在等待列表')
		waits_new.append(movie)  # 保存暂缓结果

if len(results) > 0:
	# 更新等待文件
	mymovie.UpdateWaitInFile(WAIT_FILE, waits_new)
	print('等待文件已更新')

	# 保存结果
	mymovie.SaveResultInFile(RESULT_FILE, results)
	print('结果已保存到' + RESULT_FILE)
else:
	print('没有发现更新')

print('\n开始新的检查......')

SCORE_MIN = 7  # 至少7分
SIZE_MIN = 3  # 至少3GB
PAGE_MAX = 10  # 最多解析10页

INDEX_FILE = 'Index.txt'
WAIT_FILE = 'WaitingRoom.txt'

time_now = datetime.now()
RESULT_FILE = 'Result_' + time_now.strftime('%Y%m%d') + '.txt'

indexes = mymovie.ReadIndexInFile(INDEX_FILE)  # 读取索引文件
indexes_new = []  # 新的索引号
waits = []  # 暂缓的结果
results = []  # 成功的结果

finish = False
page = 0
while page < PAGE_MAX and not finish:
	page += 1  # 从第一页开始解析
	print('开始解析第' + str(page) + '页')
	url = 'http://www.bttiantang.com/?PageNo=' + str(page)
	html = mymovie.ReadPage(url)

	# 从第一页的htm获取所有电影标题、评分、电影子页网址和豆瓣链接
	movies = mymovie.ParseMainPage(html)

	# 从第一部电影开始比对索引号是否已解析过
	for movie in movies:
		title = movie[0]
		score = float(movie[1])
		href = movie[2]
		link = movie[3]

		index = mymovie.ParseIndex(href)
		if index in indexes:
			finish = True
			# print('\t此电影曾经解析过')
			break
		else:
			# 打印电影信息
			try:
				print('===' + title + '===' + str(score) + '===')
			except UnicodeEncodeError:
				print('===电影名无法显示在Console===')

			indexes_new.append(index)  # 增加新解析过的索引号

			# 检查评分
			if score < SCORE_MIN:
				print('\t评分太低')
			else:
				resource = mymovie.ParseMoviePage(href, SIZE_MIN)  # 评分满足要求，进一步解析电影子页，查找高清资源
				if len(resource) > 0:  # 有高清资源
					print('\t解析完毕')
					results.append([title, score, href, resource, link])  # 保存成功结果
				else:  # 没有满足大小要求的资源
					print('\t无高清资源，加入等待列表')
					waits.append(movie)  # 保存暂缓结果
print('新电影解析完毕')

mymovie.SaveResultInFile(RESULT_FILE, results)
mymovie.SaveIndexInFile(INDEX_FILE, indexes_new)
mymovie.SaveWaitInFile(WAIT_FILE, waits)

print('\n请按回车键退出')
input()