
from urllib import request
from bs4 import BeautifulSoup

url = 'http://movie.douban.com'
f = request.urlopen(url)
html = f.read()
soup = BeautifulSoup(html)

print('豆瓣正在热映：')
div_hot = soup.find('div',{"id":"screening"})
for i in div_hot.find_all('li',class_='title'):
	movie_title = i.a.get_text()
	print(movie_title)

# print('豆瓣近期热门：')
# div_new = soup.find('div',class_='list')
# for i in div_new.find_all('li',class_='title'):
# 	movie_new = i.a.get_text()
# 	print(movie_new)

print('\n按回车结束\n')
input()
