#!usr/bin/python
#Filename:Addition.py
import time

print('''Ah thank you for chosing me. I can not wait any longer!
''')
time.sleep(1)
a = int(input('''Now plese type in a number named a:'''))
b = int(input('''Thank you, and type in another number named b:'''))
c = a+b
print('''
Ok, let`s add a to b.''')
time.sleep(1)

while True:
	x = int(input('''
Type in your answer:'''))
	if c == x:
		print('''Canguadulations! You made it! Thank you for your practice.''')
		break
	else:
		print('''Incorrect...Come on! Try again!''')