class Athlete:
	def __init__(self,a_name,a_dob=None,a_times=[]):
		self.name=a_name
		self.dob=a_dob
		self.times=a_times

	def top3(self):
		return(sorted(set([sanitize(t) for t in self.times]))[0:3])

	def add_time(self,time):
		self.times.append(time)

	def add_times(self,times):
			self.times.extend(times)

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
		athlete = Athlete(data.pop(0),data.pop(0),data)
		# mydict = {'name' : data.pop(0), \
		# 'dob' : data.pop(0), \
		# 'tops' : str(sorted(set([sanitize(t) for t in data]))[0:3])}
		return(athlete)
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))
