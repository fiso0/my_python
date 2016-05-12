row_data={}
with open('PaceData.csv') as paces:
	column_headings = paces.readline().strip().split(',')
	column_headings.pop(0)
	for each_line in paces:
		row = each_line.strip().split(',')
		row_label = row.pop(0)
		inner_dict = {}
		for i in range(len(row)):
			inner_dict[row[i]] = column_headings[i]
		row_data[row_label] = inner_dict

num_cols = len(column_headings)
print(num_cols, end=' -> ')
print(column_headings)

num_2mi = len(row_data['2mi'])
print(num_2mi, end=' -> ')
print(row_data['2mi'])

num_Marathon = len(row_data['Marathon'])
print(num_Marathon, end=' -> ')
print(row_data['Marathon'])

input()

times = [t for t in row_data['Marathon'].keys]
times = []
for t in row_data['Marathon'].keys():
	times.append(t)

headings = [h for h in sorted(row_data['10mi'].values(), reverse=True)]
headings = []
for h in sorted(row_data['10mi'].values(), reverse=True):
	headings.append(h)

time = [t for t in row_data['20k'].keys() if row_data['20k'][t] == '79.3']
time = []
for t in row_data['20k'].keys():
	if row_data['20k'][t] == '79.3':
		time.append(t)

def find_nearest_time(look_for, target_data):
	look_for_secs = time2secs(look_for)
	result = secs2time(find_closet(look_for_secs, [time2secs(t) for t in target_data]))
	return(result)