"""
passwdcheck.py:  CIS 210 assignment 1b, Fall 2013
author: Austin Bitterman Dayton, Mark Poliquin
Credits: Consulted Mark Poliquin on entirety of code, consulted assignment page
including linked examples
Check password requirements
"""

##import password from command line
import sys
passwd = sys.argv[1]
##password must contain at least 6 characters
lengthChar = False
if (len(passwd) >= 6) :
	lengthChar = True

##password must contain lower case letter
caseLower = False
for character in passwd:
	if(character.islower()):
		caseLower = True
	
##password must contain upper case letter
caseUpper = False
for character in passwd:
	if(character.isupper()):
		caseUpper = True
##password must contain one digit 0-9
numDigit = False
for character in passwd:
	if(character.isdigit()):
		numDigit = True

##if the password meets all conditions, print "Good password"
if lengthChar + caseLower + caseUpper + numDigit:
	print("Good password")
##if password does not have correct character length, print notification	
if lengthChar:
	pass
else:
	print("Password must be at least 6 characters long")
##if password does not have a lower case character, print notification
if caseLower:
	pass
else:
	print("Password must include lower case letters")
##if password does not have an upper case character, print notification
if caseUpper:
	pass
else:
	print("Password must include upper case letters")
##if password does not have number digit, print notification
if numDigit:
	pass
else:
	print("Password must include digits")	