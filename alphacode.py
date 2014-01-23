"""
alphacode.py:  CIS 210 assignment 1, Fall 2013
author: Austin Bitterman Dayton, Sean Grady
Credits: Consulted with Sean Grady on style, development, language, code
Convert 4-digit PIN to alphabetic code
"""

## Constants used by this program
CONSONANTS = "bcdfghjklmnpqrstvwyz" 
VOWELS = "aeiou"  

## Get pin code from command line
import sys
if (len(sys.argv) > 1) :
    pincode = int(sys.argv[1])
else :
    print("Usage: python3 alphacode 9999")
    exit(1)  ## Quit the program right here, indicating a problem


##split integer into two digit chunks

mod = pincode % 100
divi = pincode // 100
	
##convert last two decimal digits into letters

lastconvNoun = VOWELS[(mod % 5)]
lastconvCons = CONSONANTS[(mod // 5)]
	
##convert first two decimal digits into letters

firstconvNoun = VOWELS[(divi % 5)]
firstconvCons = CONSONANTS[(divi // 5)]

##add converted numbers together to form phrase

pincode = (firstconvCons + firstconvNoun + lastconvCons + lastconvNoun)
	

print("Pin code from command line", pincode)