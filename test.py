# import csv
# def getData(file):
# 	csv_file=open(file)
# 	reader=csv.DictReader(csv_file)
# 	dict_lst=[]
# 	for item in reader:
# 		dict_lst.append(item)
# 	return dict_lst
# 	pass

# dict_lst=getData('P1DataA.csv')
# frsh=0
# soph=0
# jr=0
# sr=0
# for person in dict_lst:
# 	if person['Class']=='Freshman':
# 		frsh+=1
# 	elif person['Class']=='Sophomore':
# 		soph+=1
# 	elif person['Class']=='Junior':
# 		jr+=1
# 	else:
# 		sr+=1
# frsh=('Freshmen', frsh)
# soph=('Sophomore', soph)
# jr=('Junior', jr)
# sr=('Senior', sr)
# class_lst=[frsh, soph, jr, sr]
# sorted_class_lst=sorted(class_lst, key=lambda x:-x[1])
# print (sorted_class_lst)
print ("[('Senior', 26), ('Junior', 25), ('Freshmen', 21), ('Sophomore', 18)]"=="[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]")





