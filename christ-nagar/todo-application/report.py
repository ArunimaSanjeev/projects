'''
The report module.  Generates report of all the tasks as a CSV file.
'''

import csv
import database as database_module

def generate_report():
	tasks = database_module.fetch_all_tasks()
	generate_csv(tasks)
	print('task_report.csv has been generated!')

def generate_csv(tasks):
	with open('task_report.csv', 'w', newline='') as f:
		csv_writer = csv.writer(f, delimiter=',')
		fields = ['Id', 'Category', 'Deadline', 'Description', 'Status']
		csv_writer.writerow(fields)
		for i in tasks:
			csv_writer.writerow(i)
