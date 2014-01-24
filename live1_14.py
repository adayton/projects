#factorial
"""
def fact(n):
	if n < 2:
		return 1
	else:
		return n * fact(n-1)
		

print(fact(5)) 
"""

def pal(s):
	if len(s) <= 1
		return True
	else:
		return s[0] == s[-1] and pal( s[1:-1] )
			
print( pal( "racecar" ) )
