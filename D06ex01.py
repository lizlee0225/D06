import os

path = "C:/Users/Liz Hyemin/Documents/Summer 2016/pbc"
os.chdir(path)
for item in os.listdir():
	print(item)
