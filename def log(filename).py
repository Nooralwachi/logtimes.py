from collections import defaultdict
from datetime import datetime, timedelta
def log(filename):
	process = defaultdict(list)
	with open(filename, 'r') as file:
		file.readline()
		for line in file:
			time, date, pid, status = line.strip().split()
			d=datetime.strptime(f'{time} {date}', "%H:%M:%S %m/%d/%Y")
			if status ==  'start':
				process[pid]= d
			else:
				diff = d-process[pid]
				print(pid+ ' '+ str(diff))


log('pid.txt')