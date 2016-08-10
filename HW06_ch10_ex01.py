# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def nested_sum(list_input):
	total = 0
	for item in list_input:
		if type(item) != int:
			total += sum(item)
		else:	
			total += item
	return total


def main():
	pass

if __name__ == '__main__':
    main()