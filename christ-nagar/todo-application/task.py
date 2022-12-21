'''
The task module.  Responsible for creating, updating, listing tasks.
'''

import database as database_module

def create_task():
	category = input('Enter the category (press enter to skip): ')
	deadline = input('Enter the deadline in yyyy-mm-dd format (press enter to skip): ')
	description = input('Enter the description (max 25 chars): ')
	database_module.create_task(category, deadline, description)
	print('Done!')

def list_open_tasks():
	tasks = database_module.fetch_open_tasks()
	print_tasks(tasks)

def list_open_tasks_of_category():
	category = input('Enter the category: ')
	print()
	tasks = database_module.fetch_open_tasks_of_category(category)
	print_tasks(tasks)

def list_open_tasks_before_deadline():
	deadline = input('Enter the deadline in yyyy-mm-dd format: ')
	tasks = database_module.fetch_open_tasks_before_deadline(deadline)
	print_tasks(tasks)

def list_completed_tasks():
	tasks = database_module.fetch_completed_tasks()
	print_tasks(tasks)

def list_all_tasks():
	tasks = database_module.fetch_all_tasks()
	print_tasks(tasks)

def print_tasks(tasks):
	if len(tasks) == 0:
		print('No tasks found!')
		return
	print('-' * 76)
	print('|', '%4s' % 'Id', '|', '%10s' % 'Category', '|', '%11s' % 'Deadline', '|', '%25s' % 'Description', '|', '%10s' % 'Status', '|')
	print('-' * 76)
	for task in tasks:
		print('|', '%4s' % task[0], '|', '%10s' % task[1], '|', '%11s' % task[2], '|', '%25s' % task[3], '|', '%10s' % task[4], '|')
	print('-' * 76)

def update_task():
	id = int(input('Enter the task id: '))
	print()
	print('1. Category')
	print('2. Deadline')
	print('3. Description')
	attribute = ['category', 'deadline', 'description'][int(input('Enter the attribute to update (1-3): ')) - 1]
	if attribute == 'deadline':
		value = input('Enter the deadline in yyyy-mm-dd format: ')
	else:
		value = input('Enter the new value: ')
	database_module.update_task(id, attribute, value)
	print('Done!')
	print()

def mark_task_pending():
	id = int(input('Enter the task id: '))
	print()
	database_module.update_task(id, 'status', 'Pending')
	print('Done!')
	print()	

def mark_task_completed():
	id = int(input('Enter the task id: '))
	print()
	database_module.update_task(id, 'status', 'Completed')
	print('Done!')
	print()
