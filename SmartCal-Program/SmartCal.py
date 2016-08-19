#!usr/bin/python
#Filename:SmartCal.py
import time
import string

print('''.''')
time.sleep(0.3)
print('''.''')
time.sleep(0.3)
print('''.''')
time.sleep(0.5)
print('''Hello friends, welcome to the SmartCal Program.
		\r\nThere are four arithmetics in your chosen list.
		\r\nYou can chose one of them to continue our program.''')
time.sleep(1)
shou
while True:
	chosen = (input('''\r\nPlease type in the arithmetic you like(Addition;Subtraction;Multiplication;Division or End):'''))
	if chosen == 'Addition':
		import Addition
	elif chosen == 'Subtraction':
		import Subtraction
	elif chosen == 'Multiplication':
		import Multiplication
	elif chosen == 'Division':
		import Division
	elif chosen == 'End':
		break
	else:
		print('''Please check your input. And please begin with a capital.''')
