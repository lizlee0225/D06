#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
import os

def has_no_e(word):
	if 'e' in word:
		return False
	else:
		return True

def print_no_e():
	fin = open('words.txt', 'r')
	count = 0
	total = 0
	for line in fin:
		txt_word = line.strip()
		total += 1
		if 'e' not in txt_word:
			print(txt_word)
			count += 1
	no_e = int(count/total*100)
	print("{}%".format(no_e))

##############################################################################
def main():
	print(has_no_e('Liz'))
	print_no_e()

if __name__ == '__main__':
	main()
