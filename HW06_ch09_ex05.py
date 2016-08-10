#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################

def uses_all(word, req_letters):
	for letter in req_letters:
		if letter not in word:
			return False
	return True

def uses_vowels(letters):
	fin = open('words.txt', 'r')
	count = 0
	for line in fin:
		if uses_all(line.strip(), letters):
			count += 1
	print(count)


##############################################################################
def main():
    uses_vowels('aeiou')
    uses_vowels('aeiouy')

if __name__ == '__main__':
    main()
