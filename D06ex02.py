import os
import random

new_file = open('ex02file.txt', 'w')
count = 0
while count < 10:
	new_file.write(str(random.randint(0,100000)))
	new_file.write(str('\n'))
	count += 1
new_file.close()