import csv
import os
import datetime
import date
def getData(file):
	csv_file=open(file)
	reader=csv.DictReader(csv_file)
	dict_lst=[]
	for person in reader:
		dict_lst.append(person)
	return dict_lst
	
a=getData('P1DataA.csv')

total_age=0
for person in a:
	dob=datetime.datetime.strptime(person["DOB"], "%dd/%mm/%YYYY")
	print (dob)












