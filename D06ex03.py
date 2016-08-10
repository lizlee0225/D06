fin = open('roster.txt', 'r')
count = 0
lst_names = []
for line in fin:
	names = line.split()
	for name in names:
		if 'e' in name:
			count += 1
			lst_names.append(name)
print(count)
print(lst_names)