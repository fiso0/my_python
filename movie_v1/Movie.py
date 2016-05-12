#1.SaveMoviePage
#2.ParseMoviePage
#3.ParseMovieResource

from SaveMoviePage import SaveMoviePage
from ParseMoviePage1 import ParseMoviePage
from ParseMovieResource import ParseMovieResource

print('将要从BT天堂读取电影资源，请选择筛选评分和资源大小')
print('评分>?')
score_th=float(input())
print('资源大小>?GB')
size_th=float(input())

SaveMoviePage('2')
movie=ParseMoviePage('2')
result=[]
for i in movie:
	title=i[0]
	score=float(i[1])
	href=i[2]
	try:
		print('==='+title+'==='+str(score)+'===')
	except:
		print('===电影名无法显示在Console===')
	if score > score_th:
		try:
			resource=ParseMovieResource(href,size_th)
			result.append([title,score,href,resource])
		except:
			pass

from datetime import datetime
time_now=datetime.now()
resFile=time_now.strftime('%y-%m-%d_')+'tt_movie_download.txt'#beta edition
try:
	f=open(resFile,'x',encoding='utf-8')
	for i in result:
		resource=i[3]
		if len(resource)>0:
			f.write('==='+i[0]+'==='+str(i[1])+'===\n')
			f.write('\t'+str(resource[0][0])+'GB\n\t'+resource[0][1]+'\n')
		# else:
		# 	f.write('无高清资源\n')
	f.close()
except FileExistsError as e:
	print('同名结果文件已存在')


print('\n请按回车键退出')
input()
