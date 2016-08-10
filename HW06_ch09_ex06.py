#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words:596
##############################################################################

def is_abecedarian(word):
	prev_letter = word[0]
	for letter in word:
		if letter < prev_letter:
			return False
		prev_letter = letter
	return True

def count_abecedarian(file_name):
	fin = open(file_name, 'r')
	count = 0
	for line in fin:
		if(is_abecedarian(line.strip())):
			count += 1
	print(count)

##############################################################################
def main():
   
    count_abecedarian('words.txt')

if __name__ == '__main__':
    main()
