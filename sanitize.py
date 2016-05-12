def sanitize(time_string):
	if '-' in time_string:
		splitter='-'
	elif ':' in time_string:
		splitter=':'
	else:
		return(time_string)
	(mins, secs)=time_string.split(splitter)
	return(mins+'.'+secs)

time_string="2-21"
print(sanitize(time_string))
print(sanitize("2:10"))
print(sanitize("3.3"))
input()