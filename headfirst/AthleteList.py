class AthleteList(list):
	def __init__(self,a_name,a_dob=None,a_times=[]):
		list.__init__([]) # 为啥不能直接传入a_times初始化？
		self.name=a_name
		self.dob=a_dob
		self.extend(a_times)

	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])

def sanitize(time_string):
        if '-' in time_string:
                splitter = '-'
        elif ':' in time_string:
                splitter = ':'
        else:
                return(time_string)
        (mins,secs) = time_string.split(splitter)
        return(mins+'.'+secs)

def get_coach_data(file_name):
	try:
		with open(file_name) as f:
			data = f.readline().strip().split(',')
		athlete = AthleteList(data.pop(0),data.pop(0),data)
		# mydict = {'name' : data.pop(0), \
		# 'dob' : data.pop(0), \
		# 'tops' : str(sorted(set([sanitize(t) for t in data]))[0:3])}
		return(athlete)
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

# vera=AthleteList('Vera Vi',a_times=['1.12','2.34'])
# vera.append('1.31')
# print(vera.top3())
# vera.extend(['2.22','1-21','2:22'])
# print(vera.top3())

# james=get_coach_data('james2.txt')
# print(james.name + "'s fastest times are: " + str(james.top3()))
