# Filename:record.py

import pickle as p

class Record:
    '''Record the experience of looking for a job.'''
    company = ''
    state = ''
    date = ''

    def __init__(self, company, state, date):
        self.company = company
        self.state = state
        self.date = date

'''load'''
with open('records.txt','rb') as file:
    record_dict = p.load(file)
print('after load:',record_dict)

'''add some records'''
r1 = Record('Tecent', 'fail', '2014-04-02')
r2 = Record('Baidu', 'fail', '2014-04-07')
record_dict['Tecent_fail'] = r1
record_dict['Baidu_fail'] = r2
'''print'''
print('after add:',record_dict)

'''del some records'''
if record_dict.__contains__('Baidu'):
    del record_dict['Baidu']
'''print'''
print('after del:',record_dict)

'''save'''
with open('records.txt','wb') as file:
    p.dump(record_dict, file)
