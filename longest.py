"""
Find the longest word(s) in a word list
 (CIS 210 sample by M Young, 9 Oct 2011, 
  Revised Fall 2012 for Python3)
  You may copy parts of this into projects, 
  if useful. 
"""

import sys  ## The 'sys' module lets us read command line arguments

USAGE = "Usage: python longest.py dict.txt"

def check_args():
    """longest.py should have exactly one command-line
    argument, in addition to the program name
    """

def open_dict(path):
    """Return a file object corresponding to the path"""
    f = open(path)
    ## FIXME:  Really ought to have some error handling here.
    ## We'll let that go for now.
    return f


def main():
    """
    Search dictionary for longest word.
    """
    # Get the dictionary to search 
    if len(sys.argv) != 2 :
        print(USAGE)
        exit(1)  ## the non-zero return code indicates an error
    dict_path = sys.argv[1]
    words = open_dict(dict_path)

    # Initially, the longest word we have seen is
    # nothing at all, which has length 0
    longest = ""
    maxlen = 0

    #  Search the word list for longer words
    for line in words:
        word = line.rstrip()  ## Chop off newline
        if len(word) > maxlen :
            ## New longest word
            maxlen = len(word)
            longest = word
            
    print("Longest word is '" + longest + "', which has length", maxlen)

# In-class exercise:  If there are more than one words of maximum
# length, let's print them all.  How will you approach it?

main()