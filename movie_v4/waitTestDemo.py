import mymovie_v4
filename='waitTest.txt'
url='http://www.bttiantang.com/?PageNo=0'
wait=[]
wait.append(url)
wait

mymovie_v4.SaveWaitInFile('waitTest.txt',wait)

new_wait=mymovie_v4.ReadWaitInFile('waitTest.txt')
new_wait