"""
How many days from yyyy mm dd until the next mm dd
CIS 210 assignment 3, Winter 2014
Usage example: python days_till.py	2012 09 24 06 14
	(first day of fall classes until end of spring finals)

Authors: #FIXME: List both authors here
Consulted with:	 #FIXME: If you discussed design with others who are not authors of this 
		 code, credit them here.  You don't have to credit the course instructor, 
		 GTFs, or tutors / helpers in office hours. 
"""

import sys	# For exit with a message
import argparse # Fancier command line parsing

#Determines if dates are valid	
def valid_date(year, start_month, start_day, end_month, end_day):
	if  not (year >= 1800 and year <= 2500):
		return False
	if not (start_month >= 1 and start_month <= 12):
		return False
	if not (end_month >= 1 and end_month <= 12):
		return False
	if not (start_day >= 1 and start_day <= 31):
		return False
	if not (end_day >= 1 and end_day <= 31):
		return False
	else: 
		return True

#Determines if year is a leap year
def leapyr(n):
	if n % 4 == 0 and n % 400 == 0:
		return True
	if n % 100 == 0 and n % 400 != 0:
		return False
	if n % 4 == 0:
		return True
	else:
		return False

#

# Note to CIS 210 students: 
#	 To save some time and demonstrate the standard way that the command line is 
#	 read in typical Python programs, I've written the main program, as well as 
#	 code that invokes it.	The argparse module from the standard Python library 
#	 greatly simplifies the command line processing, but it's still rather tedious,
#	 as you can see.  As you develop your program, you may uncomment some lines below
#	 and comment out (or delete) others. 
def main():
	"""
	Main program gets year number from command line, 
	invokes computation, reports result on output. 
	args: none (reads from command line)
	returns: none (write to standard output)
	effects: message or result printed on standard output
	"""
	## The standard way to get arguments from the command line, 
	##	  make sure they are the right type, and print help messages
	parser = argparse.ArgumentParser(description="Compute days from yyyy-mm-dd to next mm-dd.")
	parser.add_argument('year', type=int, help="Start year, between 1800 and 2500")
	parser.add_argument('start_month', type=int, help="Starting month, integer 1..12")
	parser.add_argument('start_day', type=int, help="Starting day, integer 1..31")
	parser.add_argument('end_month', type=int, help="Ending month, integer 1..12")
	parser.add_argument('end_day', type=int, help="Ending day, integer 1..31")
	args = parser.parse_args()	# will get arguments from command line and validate them
	year = args.year
	start_month = args.start_month
	start_day = args.start_day
	end_month = args.end_month
	end_day = args.end_day
	
	print("Checking date ", str(year) + "/" + str(start_month) + "/" + str(start_day))
	
	# if the dates entered are valid, run leapyr 
	if valid_date(year, start_month, start_day, end_month, end_day):
		leapyr(year)
	else:
		print ("Must start on valid date between 1800 and 2500")
	
	# if leap year, run leap year calculator, else run regular calculator
	if leapyr(year):
		#run lycalc_diff
	#else:
		#run calc_diff 
		
		print ("leap year")
	else:
		print ("not a leap year")
	
	
	# if not is_valid(year, start_month, start_day) : 
	#	  sys.exit("Must start on a valid date between 1800 and 2500")
	# if not is_valid(2000, end_month, end_day):
	#	 sys.exit("Ending month and day must be part of a valid date")
	# print("Days in starting month:", days_in_month(start_month, year))
	# print(days_between(year, start_month, start_day, end_month, end_day))	  


#  Note to CIS 210 students: 
#	   You'll see code like the following a lot in Python programs. This is so 
#	   that I could re-use the functions in days_till without reusing the main 
#	   program.	 We'll talk more about it later, when we write separate "module" 
#	   files (like the Python library modules) and use them together in a program. 
#	   For now, what you need to know is that if you run this program from the 
#	   command line, there will be a global variable called __name__ and its 
#	   value will be "__main__"	 (i.e., Python is telling us "You are the main program, 
#	   go do your stuff!"), so the code below will call the function main() just above. 
#
if __name__ == "__main__":
	main()

"""
#stackoverflow.com/questions/11621740/python-leap-year-calculator
def leapyr(n):
	if n % 4 == 0:
		return True
	if n % 100 == 0:
		return False
	if n % 4 == 0:
		return True
	else:
		return False
print leapyr(1990)
"""