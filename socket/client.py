# 导入socket库
import socket

# 创建一个socket 使用IPv4 TCP
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接 端口号80表示Web服务
s.connect(('www.sina.com.cn',80))

# 发送数据 获取页面内容
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer=[]
while True:
	# 每次最多接收1024字节
	try:
		d=s.recv(1024)
		if d:
			buffer.append(d)
		# 反复接收直到返回空 表示接收完毕
		else:
			# 关闭连接
			s.close()
	except:
		pass

data=b''.join(buffer)

# 分离HTTP头和网页内容
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
# 把网页内容写入文件
with open('baidu.htm','wb') as f:
	f.write(html)
