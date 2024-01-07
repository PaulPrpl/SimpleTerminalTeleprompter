#!/bin/env python3

from time import sleep
import sys, os, re

file = sys.argv[1]

clear = r'[H[2J[3J'

buffer = []
countdown = 3
interCharsDelay = 0.048
wait = interCharsDelay
interLinesDelay = wait * 4
terminalMaxSize = os. get_terminal_size().columns * 80 / 100
paragraph = re.compile('\n')
smallBreath = re.compile(r',')
medBreath = re.compile(r';')
bigBreath = re.compile(r'[.!?]')

print(clear, end='\r')

def delay(cpt):
	for i in range(cpt):
		print(str(countdown-i)+'.'*(i+1), end='\r')
		sleep(1)

	print('Go !')
	sleep(1)

delay(countdown)

with open('./script.txt', 'r') as script:
	text = script.readlines()
	for line in text:
		sleep(interLinesDelay)
		for char in line:

			wait = interCharsDelay

			if len(buffer) > terminalMaxSize:
				if char == ' ':
					buffer = []
					print('')

			elif paragraph.match(char):
				wait = wait * 4
				buffer = []

			elif smallBreath.match(char):
				wait = wait * 8

			elif medBreath.match(char):
				wait = wait * 5

			elif    bigBreath.match(char):
				wait = wait * 3

			buffer.append(char)
			print(''.join(buffer), end='\r')
			sleep(wait)

		buffer = []
