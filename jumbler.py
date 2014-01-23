"""
jumbler.py:  CIS 210 assignment 2a, Fall 2013
author: Austin Bitterman Dayton, Sean Grady
Credits: Consulted with Sean Grady on style, development, language, code
Consulted Mark Poliquin on function and design
Compare jumbled words to a list
"""
#import command line arguments
import sys 

USAGE = "Usage: python jumbler.py dict.txt"

#opening path to dictionary
def open_dict(path):
	f = open(path)
	return f

# Get the dictionary to search
def main(): 
	index = 0 
	match = 0 
	if len(sys.argv) != 3:
		print(USAGE)
		exit(1)
	dict_path = sys.argv[2] 
	words = open_dict(dict_path)


#check scrambled word against all words in list
	for line in words:
		index += 1
		wordlist = []
		word = line.rstrip()
	
		#check dictionary for words with same length
		if len(word) == len(sys.argv[1]):
			wordlist.append(word)
		#sort word in alphabetic order, check if matches words with same length
		for x in wordlist:
		
			if sorted(x) == sorted(sys.argv[1]):
				match += 1
				print(x)
	print (match, "matches from", index, "words")
#print dictionary word

print()

main()