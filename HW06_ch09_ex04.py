#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
import random

def uses_only(word, letters):
	for letter in word:
		if letter not in letters:
			return False
	return True		#returns True if the word contains only letters in letters

def make_sentence():
	

##############################################################################
def main():
    pass  # Call your function(s) here.

if __name__ == '__main__':
    main()
