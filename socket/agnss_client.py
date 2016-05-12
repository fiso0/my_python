# 导入socket库
import socket

'''
域名	agnss-server-1.wh-mx.com
IP	27.17.32.34
端口	32101

GET /v1/device/agnss?client_id=cmcc-mxt535&device_id=356674060511518&protocol=whmx&data_type=eph&gnss=gps%2Cbds&pos=30.50%2C114.39 HTTP/1.1
'''

SERVER_DOMAIN = 'agnss-server-1.wh-mx.com'
SERVER_PORT = 32101
GET_DATA = b'GET /v1/device/agnss?client_id=cmcc-mxt535&device_id=356674060511518&protocol=whmx&data_type=eph&gnss=gps%2Cbds&pos=30.50%2C114.39 HTTP/1.1\r\n\r\n'

# 创建一个socket 使用IPv4 TCP
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect((SERVER_DOMAIN,SERVER_PORT))

# 发送数据 获取页面内容
s.send(GET_DATA)

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
		break

data=b''.join(buffer)

# 分离HTTP头和网页内容
header, content=data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把网页内容写入文件
with open('AGNSS_test.txt','wb') as f:
	f.write(content)
