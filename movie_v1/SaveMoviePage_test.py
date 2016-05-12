# TEST SaveMoviePage.py
from SaveMoviePage import SaveMoviePage

print('请选择要获取的页面：1.豆瓣电影 2.BT天堂')
select_page=input()
SaveMoviePage(select_page)

print('\n请按回车键退出')
input()