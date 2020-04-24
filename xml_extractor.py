import gzip
import xml.etree.ElementTree
import os
import csv
import glob
import time
import pandas as pd


start = time.time()
current_path = os.getcwd()
list_of_current_path = glob.glob(os.path.join(current_path,'*.gz'))
csv_path = os.path.join(current_path,'csv_template.csv')

# #Attributes to be extracted.
target_attributes = ['reg_num','subj','crse','title']

with open(csv_path,'a',newline='') as csv_file:
	writer = csv.DictWriter(csv_file,fieldnames=target_attributes)

	# Add title header on CSV file
	writer.writeheader()
	for t_path in list_of_current_path:
		#unzip .gzip extension
		with gzip.open(t_path,'rb') as uz_file:
			parse_xml = xml.etree.ElementTree.parse(uz_file)
			courses = parse_xml.findall('course')
			for i in courses:
				var_0 = i.find(target_attributes[0]).text
				var_1 = i.find(target_attributes[1]).text
				var_2 = i.find(target_attributes[1]).text
				var_3 = i.find(target_attributes[1]).text						
				writer.writerow({target_attributes[0]:var_0,target_attributes[1]:var_1,target_attributes[2]:var_2,target_attributes[3]:var_3})
			print('Extracted from:',t_path)
end = time.time()

print(f'finished in {end-start} second(s)')
print('Done!')				