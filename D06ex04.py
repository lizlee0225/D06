fin = open('roster.txt', 'r')
new_file = open('roster results.txt', 'w')
count = 0
for line in fin:
	names = line.split()
	for name in names:
		if 'e' in name:
			count += 1
			new_file.write(name + "\n")
new_file.write(str(count))
new_file.close()
