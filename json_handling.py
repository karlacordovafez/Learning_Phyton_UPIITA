
import json

data = [
	{'id':1,'studen_name':'Karla Cordova','birth_month':'Octubre','career':'Telematica'},
	{'id':2,'studen_name':'Harry Potter','birth_month':'Julio','career':'Mago'},
	{'id':3,'studen_name':'Draco Malfoy','birth_month':'Junio','career':'Mago'},
	{'id':4,'studen_name':'Dimash Kudaibergen','birth_month':'Mayo','career':'Cantante'},
	{'id':5,'studen_name':'Andrew Biersack','birth_month':'Diciembre','career':'Artista'},
	{'id':6,'studen_name':'Taylor Momsen','birth_month':'Julio','career':'Artista'}
]

new_data = {
	'students':[]
}

ID_record = [

] 

for i in data:
	if (('id' in i) and ('student_name' in i)):
		if((type(i['id']) == int) or (type(i['id']) == float)):
			#print(f"{elem['id']} --> {type(elem['id'])}")
			if (i['id'] not in ID_record):
				ID_record.append(i['id'])
				new_data['students'].append(i)
			


with open("students.json",mode = "w") as json_file:
	print("Opened file")
	json.dump(new_data,json_file,indent=4)
	print("Wrote file")

with open("students.json",mode = "r") as json_file:
	print("Opened file")
	data = json.load(json_file)
	for elem in data.values():
		for e in elem:
			for k in e.keys():
				print(f"{k}: {e[k]}",end = " / ")
			print("\n")

	print("Read file")