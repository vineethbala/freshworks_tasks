import os
import json
import glob

#Path for the file 
file_path = input("Enter the folder path: ")
#Base name for the file
file_basename = input("Enter the base name: ")
#File Size Threshold
file_size_threshold = input("Enter the Max File Size of the Resultant Merged File(bytes): ")


#Check if the file size crosses the threshold
def check_if_the_size_greater_than_threshold(filename):
    st = os.stat(filename)
    return st.st_size

dir = os.path.abspath(file_path)
files = glob.glob(file_basename+'[1-9]*.json')

key_val = {}

#To read a content from file
for file in files:
	file_n = open(file,encoding = 'utf-8', mode='r')
	file_contents = file_n.read()
	json_content = json.loads(file_contents)
	for key,value in json_content.items():
		if key not in key_val:
			key_val[key] = value
		else:
			for values in value:
				#append the other files values in single key
				key_val.setdefault(key, [])
				key_val[key].append(values)
file_n.close()

#create and write the merged details in file
write_file = open("merged.json",encoding = 'utf-8', mode= 'w')
write_file.write(str(json.dumps(key_val)))
write_file.close()
current_size = check_if_the_size_greater_than_threshold('merged.json')
if (int(current_size) > int(file_size_threshold)):
	print ("Merged successfully, but the file Size Exceeds the Threshold")
else:
	print ("Merge was Successfull")