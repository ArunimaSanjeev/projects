'''
The database module.  Responsible for all interactions with the database.
'''

import mysql.connector

taskdb = mysql.connector.connect(host='localhost', user='root', database='taskdb')
cursor = taskdb.cursor()

def create_task(category, deadline, description):
	if category == '':
		category = None
	if deadline == '':
		deadline = None
	query = 'insert into task(category, deadline, description) values(%s, %s, %s)'
	cursor.execute(query, [category, deadline, description])
	taskdb.commit()

def update_task(id, attribute, value):
	query = 'update task set {}=%s where id=%s'.format(attribute)
	cursor.execute(query, [value, id])
	taskdb.commit()

def fetch_open_tasks():
	query = 'select * from task where status=\'Pending\''
	cursor.execute(query)
	return cursor.fetchall()

def fetch_all_tasks():
	query = 'select * from task'
	cursor.execute(query)
	return cursor.fetchall()

def fetch_open_tasks_of_category(category):
	query = 'select * from task where status=\'Pending\' and category=%s'
	cursor.execute(query, [category])
	return cursor.fetchall()

def fetch_completed_tasks():
	query = 'select * from task where status=\'Completed\''
	cursor.execute(query)
	return cursor.fetchall()

def fetch_open_tasks_before_deadline(deadline):
	query = 'select * from task where deadline <= date %s and status=0'
	cursor.execute(query, [deadline])
	return cursor.fetchall()
