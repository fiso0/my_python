#!/usr/bin/env python3
# Parse Movie web page.
# Save result in _list.txt file if possible.

def ParseMoviePage(select_page):
	# return value
	movie=[]
	
	# # Web page's URL:
	# print('请选择要解析的页面：1.豆瓣电影 2.BT天堂')
	# select_page=input()
	if select_page=='1':
		tag='db'
	elif select_page=='2':
		tag='tt'

	from datetime import datetime
	time_now=datetime.now()

	# 待解析源文件（.htm）
	# filename=time_now.strftime('%y-%m-%d_%H-%M-%S_')+tag+'.htm'#alpha edition
	filename=time_now.strftime('%y-%m-%d_')+tag+'_home.htm'#beta edition
	try:
		sourceFile=open(filename,encoding='utf-8')#parameter 'encoding' is important!
	except FileNotFoundError as e:
		print('文件不存在，请先下载网页（执行SaveMoviePage.py）:'+filename)
		return# 必须有源文件，否则直接退出

	# 用于保存解析结果的问题
	resultFile=time_now.strftime('%y-%m-%d_')+tag+'_list.txt'#beta edition
	try:
		resFile=open(resultFile,'x',encoding='utf-8')
	except FileExistsError as e:
		print('同名结果文件已存在:'+resultFile)
		# 可以不写结果文件

	html=sourceFile.read().encode('utf-8')

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html,"html.parser")

	if select_page=='1':# 豆瓣电影
		print('豆瓣电影 正在热映：')
		div_hot = soup.find_all('li',class_='poster')
		for i in div_hot:
			movie_title = i.img.get('alt')
			try:
				print(movie_title)
				resFile.write(movie_title+'\n')
			except:
				print('some error')
	elif select_page=='2':# BT天堂
		print('BT天堂 最新电影')

		movie_title=[]
		title_hot = soup.find_all('div',class_='title')
		size_t = len(title_hot)

		movie_score=[]
		score_hot = soup.find_all('p',class_='rt')
		size_s = len(score_hot)

		movie_href=[]

		if size_s==size_t:
			import re
			p = re.compile("\d.?\d")
			for i in range(0,size_t):
				title=title_hot[i].a.get_text()
				score=p.search(score_hot[i].get_text()).group(0)
				href='http://www.bttiantang.com'+title_hot[i].a.get('href')
				movie_title.append(title)
				movie_score.append(score)
				movie_href.append(href)
				movie.append((title,score,href))
				try:
					print('评分'+score+'\t片名：'+title+'\t'+href)
				except:
					print('some error 1')
				# try:
				# 	resFile.write('评分'+movie_score[i]+'\t片名：'+movie_title[i]+'\n')
				# except:
				# 	print('some error 2')
			# 按评分由高到低排序
			movie.sort(key=lambda x:x[1],reverse=True)
			for i in range(0,size_t):
				try:
					resFile.write('评分'+movie[i][1]+'\t片名：'+movie[i][0]+'\t'+movie[i][2]+'\n')
				except:
					# print('some error 2')
					pass
	try:
		resFile.close()
	except:
		# print('some error 3')
		pass
	return movie

# print('\n请按回车键退出')
# input()