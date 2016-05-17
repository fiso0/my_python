def open_file(file):
	log = []
	with open(file, 'r') as f:
		for line in f.readlines():
			log.append(line)
	return log  # string list

# 从line_from到line_to找出内容包含string的行，返回行号
def search_in(string, line_from=0, line_to=0, pt=False):
	global file
	log = open_file(file)
	search_res = []
	if line_from == 0:
		start = 0
	else:
		start = line_from

	if line_to == 0:
		stop = len(log)
	else:
		stop = line_to

	for line_index in range(start, stop):
		if string in log[line_index]:
			# search_res.append((line_index,log[line_index]))
			search_res.append(line_index)
			if pt:
				print(line_index, log[line_index])

	print(string, ': ', str(len(search_res)))
	return search_res  # list


# 找出line_list中最接近（小于）line_goal的一个
def find_nearest(line_list, line_goal):
	for line_no in line_list:
		if line_no < line_goal:
			res = line_no
	return res

# 基础解析
def basic_parse():
	global file,svn,stop,stop_1,stop_all,stop_hold,drv_start,period,start,stop_2,stop_pos,stop_ack,GGA
	file = input('待解析文件地址：')

	print('__svn__')
	svn = search_in('FW', pt=True)

	print('__stop__',end='')
	stop = search_in('[GPSstop]')

	print('__stop_1__',end='')
	stop_1 = search_in('[GPSstop]phase 1 timeout')
	print('__stop_all__',end='')
	stop_all = search_in('[GPSstop]phase all timeout')
	print('__stop_hold__',end='')
	stop_hold = search_in('[GPSstop]hold timer timeout')

	print('__drv_start__',end='')
	drv_start = search_in('mx_gps_ctrl_drv_start')
	print('__period__',end='')
	period = search_in('mx_location_period_timer__cb')

	start = drv_start+period
	start.sort()
	print('__start__ = drv_start + period')

	print('__stop_2__',end='')
	stop_2 = search_in('[GPSstop]phase 2 end')
	print('__stop_pos__',end='')
	stop_pos = search_in('[GPSstop]postion complete')
	print('__stop_ack__',end='')
	stop_ack = search_in('[GPSstop]ACKOK all done')

	print('__GGA__',end='')
	GGA = search_in('GGA')

	input('基础分析到此完毕')

'''
	示例：
	parse_srv_log.basic_parse()
	查看个数不为0的stop的行序号，查询在start和stop之间的GGA的个数
	parse_srv_log.start
	parse_srv_log.period
	parse_srv_log.stop_2
	parse_srv_log.stop_pos
	parse_srv_log.stop_ack
	parse_srv_log.find_nearest(parse_srv_log.period,1362)
	GGA_seg_1 = parse_srv_log.search_in('GGA',1301,1362)
'''

basic_parse()