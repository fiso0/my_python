import mymovie
from datetime import datetime

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
		print('\t解析完毕')
		results.append([title, score, href, resource, link])  # 保存成功结果
	else:  # 没有满足大小要求的资源
		print('\t无高清资源，保留在等待列表')
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

print('\n请按回车键退出')
input()
