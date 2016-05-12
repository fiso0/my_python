# TEST
from ParseMoviePage1 import ParseMoviePage

print('请选择要解析的页面：1.豆瓣电影 2.BT天堂')
select_page=input()
movie=ParseMoviePage(select_page)

print('\n请按回车键退出')
input()