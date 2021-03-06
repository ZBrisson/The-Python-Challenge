# The python challenge
# Challenge #1
# By: Zach Brisson
# Description: This program solves what is called a "Caesar ciper" aka a = c, b = d, etc.
# Reference Material that was consulted for this project can be found below:
# 1. https://inventwithpython.com/chapter14.html
# 2. https://wiki.python.org/moin/WhileLoop
# 3. http://stackoverflow.com/questions/1397827/how-to-read-formatted-input-in-python
from random import randint
from time import sleep
#Need this library for the psuedo random number generator.

while 1:
# 1. and 2. Using 1 instead of True because python has to look up the value of True vs. 1 being defined. Only occurs with Python 2.X	
	key = int(raw_input("Hello there. I am dubbed the Caesar Whisperer version .02. \nIf you know the key please enter it below, it should be a number 1-26: \n> "))
	if (key >= 1 and key <= 26):
		break

encrypted_text = raw_input("Please print the text you want deciphered on the line below: \n> ")
# 3. Use raw_input instead of input because python in input mode tries to return an expression. Only occurs with Python 2.X


def TranslatedMessage(encrypted_text):
	translated = ''
	for symbol in encrypted_text:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
		
			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
					if num > ord('z'):
						num  -= 26
					elif num < ord('a'):
						num += 26
			translated += chr(num)
		else:
			translated += symbol
	return translated
# I didn't want to copy and paste verbatim from the inventwithpython page. Will attempt a more clean approach as a follow up.
			
print "Ooo. That's a little tricky. Let me put the hamsters to work. Please hold"
sleep(3)
print "Almost there. We lost a hamster. Not to worry though. I've kept a stock pile of spare hamsters for just such an occasion."
sleep(5)
print "Tada! Only %s hamsters were lost in the making of this." % randint(0,9)
print (TranslatedMessage(encrypted_text))