# Save Movie web page to a .htm file, name with today's date.
# You can open the _home.htm file with Notepad,
# chinese character displayed wrong in other editor software.

def SaveMoviePage(select_page):
	# Web page's URL:
	if select_page=='1':
		url='http://movie.douban.com'
		tag='db'
	elif select_page=='2':
		url='http://www.bttiantang.com/'
		tag='tt'

	from urllib import request
	html=request.urlopen(url).read()
	print('HTML内容已准备')

	from datetime import datetime
	time_now=datetime.now()
	# filename=time_now.strftime('%y-%m-%d_%H-%M-%S_')+tag+'.htm'#alpha edition
	filename=time_now.strftime('%y-%m-%d_')+tag+'_home.htm'#beta edition

	# Write in file (for test)
	try:
		f=open(filename,'x',encoding='utf-8')#parameter 'encoding' is important!
		print('文件已准备')

		f.write(str(html.decode('utf-8')))
		print('HTML内容写入')

		f.close()
		print('文件已完成')
	except FileExistsError as e:
		print('同名文件已存在')

# # TEST
# print('请选择要获取的页面：1.豆瓣电影 2.BT天堂')
# select_page=input()
# SaveMoviePage(select_page)

# print('\n请按回车键退出')
# input()