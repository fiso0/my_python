#!/usr/bin/env python3
# Parse Movie web page.

# Web page's URL:
print('请选择要解析的页面：1.豆瓣电影 2.BT天堂')
select_page=input()
if select_page=='1':
	tag='db'
elif select_page=='2':
	tag='tt'

from datetime import datetime
time_now=datetime.now()
filename=time_now.strftime('%y-%m-%d_%H-%M-%S_')+tag+'.htm'#alpha edition
filename=time_now.strftime('%y-%m-%d_')+tag+'.htm'#beta edition

try:
	f=open(filename,encoding='utf-8')#parameter 'encoding' is important!
	html=f.read().encode('utf-8','ignore')

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html,"html.parser")

	if select_page=='1':#豆瓣电影
		print('豆瓣正在热映：')
		div_hot = soup.find('div',{"id":"screening"})
		for i in div_hot.find_all('li',class_='title'):
			movie_title = i.a.get_text()
			print('  '+movie_title)

	elif select_page=='2':#BT天堂
		print('最新电影')
		div_hot = soup.find_all('div',class_='title')
		for i in div_hot:
			movie_title = i.a.get_text()
			print('  '+movie_title)
			
except FileNotFoundError as e:
	print('文件不存在，请先下载网页（执行SaveWebPage.py）')

print('\n请按回车键退出')
input()