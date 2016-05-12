import pickle
from AthleteList import AthleteList

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline().strip().split(',')
		athlete = AthleteList(data.pop(0),data.pop(0),data)
		return(athlete)
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

def put_to_store(files_list):
	all_athletes={}
	for file in files_list:
		athlete=get_coach_data(file)
		all_athletes[athlete.name]=athlete
	try:
		with open('athletes.pickle','wb') as f:
			pickle.dump(all_athletes,f)
	except IOError as err:
		print('File error (put_to_store): '+str(err))
	return(all_athletes)

def get_from_store():
	all_athletes={}
	try:
		with open('athletes.pickle','rb') as f:
			all_athletes=pickle.load(f)
	except IOError as err:
		print('File error (get_from_store): '+str(err))
	return all_athletes

the_files=['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data=put_to_store(the_files)
for each_a in data:
        print(data[each_a].name+' '+data[each_a].dob)

data2=get_from_store()
for each_a in data2:
        print(data2[each_a].name+' '+data2[each_a].dob)
