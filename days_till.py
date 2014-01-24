"""
How many days from yyyy mm dd until the next mm dd
CIS 210 assignment 3, Winter 2014
Usage example: python days_till.py	2012 09 24 06 14
	(first day of fall classes until end of spring finals)

Authors:	Austin Dayton
			Mark Poliquin
			
Consulted with: Anna the lab aid helped us realize the reason our functions were not 
				outputting correctly was that we were not calling them in the main function. 
"""


import sys		  # For exit with a message
import argparse # Fancier command line parsing

monthLen = [ 0, # No month zero
	31, # 1. January
	28, # 2. February (Will get changed if leap year)
	31, # 3. March
	30, # 4. April
	31, # 5. May
	30, # 6. June
	31, # 7. July
	31, # 8. August
	30, # 9. September
	31, #10. October
	30, #11. November
	31, #12. December
	]
	
year = 0

#Determines if dates are valid		  
def valid_date(year, start_month, start_day, end_month, end_day):
		if not leapyr(year) and start_month == 2:
			if  start_day == 29:
				return False
		if not (year >= 1800 and year <= 2500):
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
		elif n % 100 == 0 and n % 400 != 0:
				return False
		elif n % 4 == 0:
				return True
		else:
				return False

#Calculates the days left
def calc_days(start_month, start_day, end_month, end_day):
	inbetween_days = 0
	afterdays = (monthLen[start_month] - start_day) + end_day
	global year
	#Checks if the year it goes into the next year
	partOne = 0
	partTwo = 0
	if start_month > end_month:
		if leapyr(year):
			monthLen[2] = 29
		for i in range((start_month + 1), 13):
			partOne = monthLen[i] + partOne

		if leapyr(year + 1):
			monthLen[2] = 29
		else:
			monthLen[2] = 28
		for i in range(1, end_month):
			partTwo = monthLen[i] + partTwo

		inbetween_days = partOne + partTwo		

	#Checks if the year is the same 
	elif start_month < end_month:
		#Loops and checks within the same year
		for i in range((start_month + 1), end_month):
			inbetween_days = monthLen[i] + inbetween_days

	totalDays = afterdays + inbetween_days 

	#If the month is the same, this corrects the issue of including the months days
	if start_month == end_month:
		totalDays = totalDays - monthLen[start_month]

	print(totalDays)#Output the days left


#Main Function
def main():
		"""
		Main program gets year number from command line,
		invokes computation, reports result on output.
		args: none (reads from command line)
		returns: none (write to standard output)
		effects: message or result printed on standard output
		"""
		## The standard way to get arguments from the command line,
		##		   make sure they are the right type, and print help messages
		parser = argparse.ArgumentParser(description="Compute days from yyyy-mm-dd to next mm-dd.")
		parser.add_argument('year', type=int, help="Start year, between 1800 and 2500")
		parser.add_argument('start_month', type=int, help="Starting month, integer 1..12")
		parser.add_argument('start_day', type=int, help="Starting day, integer 1..31")
		parser.add_argument('end_month', type=int, help="Ending month, integer 1..12")
		parser.add_argument('end_day', type=int, help="Ending day, integer 1..31")
		args = parser.parse_args()		  # will get arguments from command line and validate them
		global year
		year = args.year
		start_month = args.start_month
		start_day = args.start_day
		end_month = args.end_month
		end_day = args.end_day

		#If dates are invalid the program will exit and indicate the correct dates
		if valid_date(year, start_month, start_day, end_month, end_day):
				leapyr(year)
		else:
				print ("Must start on valid date between 1800 and 2500")
				exit(1)
		 
		##Changes February to 29 days if it is a leap year.
		if leapyr(year):
			monthLen[2] = 29
			calc_days(start_month, start_day, end_month, end_day)
		else:
			calc_days(start_month, start_day, end_month, end_day)
		

if __name__ == "__main__":
		main()