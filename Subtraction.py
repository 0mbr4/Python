#!usr/bin/python
#Filename:Subtraction.py
import time

print('''Ah thank you for chosing me. I can not wait any longer!''')
time.sleep(1)
a = int(input('''\r\nNow plese type in a number named a:'''))
b = int(input('''Thank you, and type in another number named b:'''))
c = a-b
print('''\r\nOk, let`s subtract b from a.''')
time.sleep(1)

while True:
	x = int(input('''\r\nType in your answer:'''))
	if c == x:
		print('''Canguadulations! You made it! Thank you for your practice.''')
		break
	else:
		print('''Incorrect...Come on! Try again!''')