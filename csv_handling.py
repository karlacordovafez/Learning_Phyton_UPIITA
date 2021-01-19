import csv

with open('students_data.csv', mode='w') as csv_file:
	fieldnames = ['id','studen_name','birth_month','career']
	writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'id':1,'studen_name':'Karla Cordova','birth_month':'Octubre','career':'Telematica'})
	writer.writerow({'id':2,'studen_name':'Harry Potter','birth_month':'Julio','career':'Mago'})
	writer.writerow({'id':3,'studen_name':'Draco Malfoy','birth_month':'Junio','career':'Mago'})
	writer.writerow({'id':4,'studen_name':'Dimash Kudaibergen','birth_month':'Mayo','career':'Cantante'})
	writer.writerow({'id':5,'studen_name':'Andrew Biersack','birth_month':'Diciembre','career':'Artista'})
	writer.writerow({'id':6,'studen_name':'Taylor Momsen','birth_month':'Julio','career':'Artista'})

with open('students_data.csv', mode='r') as csv_file:
	reader = csv.DictReader(csv_file)
	line_count = 0
	for row in reader:
		if line_count == 0:
			print(f'Column names are {",".join(row)}')
			line_count += 1
		print(f'\t{row["studen_name"]} with id {row["id"]} is a {row["career"]}')
		line_count += 1
	print(f'Processed {line_count} lines.')

print(type(reader))
