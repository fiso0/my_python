print('请输入要解析的电影列表网址')
url=input()

import mymovie
from datetime import datetime

SCORE_MIN = 0  # 对分数没要求
SIZE_MIN = 3  # 至少3GB

time_now = datetime.now()
RESULT_FILE = 'ListCheckResult_' + time_now.strftime('%Y%m%d') + '.txt'

results = []  # 成功的结果

html = mymovie.ReadPage(url)

# 从htm获取所有电影标题、评分、电影子页网址和豆瓣链接
movies = mymovie.ParseMainPage(html)

# 从第一部电影开始比对索引号是否已解析过
for movie in movies:
	title = movie[0]
	score = float(movie[1])
	href = movie[2]
	link = movie[3]

	# 打印电影信息
	try:
		print('===' + title + '===' + str(score) + '===')
	except UnicodeEncodeError:
		print('===电影名无法显示在Console===')

	# 检查评分
	if score < SCORE_MIN:
		print('\t评分太低')
	else:
		resource = mymovie.ParseMoviePage(href, SIZE_MIN)  # 评分满足要求，进一步解析电影子页，查找高清资源
		if len(resource) > 0:  # 有高清资源
			print('\t解析完毕')
			results.append([title, score, href, resource, link])  # 保存成功结果
		else:  # 没有满足大小要求的资源
			print('\t无高清资源')

mymovie.SaveResultInFile(RESULT_FILE, results)

print('\n请按回车键退出')
input()
