import os

current_directory = os.getcwd()
html_directory = current_directory+"\\html"
html_list = os.listdir(html_directory)
file_name_list = []
search_name = name = input("Enter Name for search: ")

for file_name_obj in html_list:
	file_name = html_directory+"\\"+file_name_obj
	with open(file_name) as html_file:
		if search_name in html_file.read():
			file_name_list.append(file_name_obj)
	if len(file_name_list) == 3:
		break

if len(file_name_list) !=0:
	print("Search Result:")
	for file_name_data in file_name_list:
		print(file_name_data)
else:
	print("No such name found.")
