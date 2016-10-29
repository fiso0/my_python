import time
import sys

# server
SERVER_DOMAIN = '111.4.117.68'
SERVER_PORT = 6263

SEND_DATA = [\
	b'test123',\
	b'test456'\
	]

BUF_LEN = 1024



# 输出“[时间]发送**字节：***”
def print_send(bytes):
	if len(bytes) > 0:
		print("%s 发送%d字节:\n%s\n"%(time.strftime('%H:%M:%S', time.localtime()),len(bytes),bytes.decode('utf-8')))


# 输出“[时间]接收**字节：***”
def print_recv(bytes):
	if len(bytes) > 0:
		print("%s 接收%d字节:\n%s\n"%(time.strftime('%H:%M:%S', time.localtime()),len(bytes),bytes.decode('utf-8')))


def delay(sec):
	print("等待%ds..."%(sec))
	time.sleep(sec)

# 从给定的地址和端口接收（广播）内容
def recv_from(s):
	buffer = []
	while True:
		try:
			d = s.recv(BUF_LEN) # 每次最多接收BUF_LEN字节
			if d:
				buffer.append(d)
				# print_recv(d)
			else:
				break
		except Exception as e:
			print("发生错误：%s"%(e))
			break
	# 关闭连接
	s.close()
	print("关闭连接")
	data = b''.join(buffer)
	return data


# 向给定的地址和端口发送请求，并接收（响应）内容，从响应中解析长度，若接收正确则主动断开连接
def send_to(s, send):
	# 发送数据 获取内容
	s.send(send)
	print_send(send)


def create_socket(addr, port):
	import socket

	# 创建一个socket 使用IPv4 UDP
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# s.settimeout(5)

	# 建立连接
	s.connect((addr, port))

	return s


def close_socket(s):
	s.close()
	print("关闭连接")

for line in SEND_DATA:
	try:
		s = create_socket(SERVER_DOMAIN, SERVER_PORT)
		send_to(s, line)
		# data = recv_from(s)
		data = s.recv(BUF_LEN)
		print_recv(data)
		delay(5) # 延迟5s再发下一条
	except Exception as e:
		print(e)