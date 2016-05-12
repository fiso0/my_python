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
		mydict = {'name' : data.pop(0), \
		'dob' : data.pop(0), \
		'tops' : str(sorted(set([sanitize(t) for t in data]))[0:3])}
		return(mydict)
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

sarah = get_coach_data('sarah2.txt')
print(sarah['name'] + "'s fastest times are: " + sarah['tops'])
