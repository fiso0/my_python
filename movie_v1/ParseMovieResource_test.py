# TEST ParseMovieResource.py
from ParseMovieResource import ParseMovieResource

url='http://www.bttiantang.com/subject/27747.html'
resource=ParseMovieResource(url)
if len(resource)==0:
	print('无高清结果')
else:
	print(resource[0][0]+'\t'+resource[0][1])
print('\n请按回车键退出')
input()