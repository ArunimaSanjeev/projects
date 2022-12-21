'''
The main module.

Command to run:
>> python3 main.py
'''

import task as task_module
import report as report_module
import database as database_module

def get_user_choice():
	print('1. Create a task')
	print('2. List tasks')
	print('\ta. Open tasks')
	print('\tb. Open tasks of a category')
	print('\tc. Open tasks before deadline')
	print('\td. Completed tasks')
	print('\te. All tasks')
	print('3. Update a task')
	print('\ta. Modify attribute')
	print('\tb. Mark as completed')
	print('\tc. Mark as pending')
	print('4. Generate report')
	print('5. Exit the application')
	print()
	choice = input('Enter your choice (eg. 1, 2c, 3b, etc.): ')
	print()
	valid_choices = ['1', '2a', '2b', '2c', '2d', '2e', '3a', '3b', '3c', '4', '5']
	if choice not in valid_choices:
		print('Invalid choice entered!')
		return None
	return choice


print('=====================================')
print('+++++++ ToDo List Application +++++++')
print('=====================================')
print()

while(1):
	choice = get_user_choice()
	if choice == None:
		print('\n' * 5)
		continue
	elif choice[0] == '1':
		task_module.create_task()
	elif choice[0] == '2':
		if choice[1] == 'a':
			task_module.list_open_tasks()
		elif choice[1] == 'b':
			task_module.list_open_tasks_of_category()
		elif choice[1] == 'c':
			task_module.list_open_tasks_before_deadline()
		elif choice[1] == 'd':
			task_module.list_completed_tasks()
		else:
			task_module.list_all_tasks()
	elif choice[0] == '3':
		if choice[1] == 'a':
			task_module.update_task()
		elif choice[1] == 'b':
			task_module.mark_task_completed()
		else:
			task_module.mark_task_pending()
	elif choice[0] == '4':
		report_module.generate_report()
	else:
		break
	print('\n' * 5)

print('==================')
print('+++ Thank you! +++')
print('==================')
print()
