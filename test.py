import csv
def getData(file):
	csv_file=open(file)
	reader=csv.DictReader(csv_file)
	dict_lst=[]
	for item in reader:
		dict_lst.append(item)
	return dict_lst
	pass

dict_lst=getData('P1DataA.csv')
common_bday={}
for person in dict_lst:
	dob_lst=person['DOB'].split('/')
	if dob_lst[1] not in common_bday:
		common_bday[dob_lst[1]]=1
	else:
		common_bday[dob_lst[1]]+=1
bday_lst=common_bday.items()
sorted_bday=sorted(bday_lst, key=lambda x:-x[1])
print (type(sorted_bday[0][0]))











