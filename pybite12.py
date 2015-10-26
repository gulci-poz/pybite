# coding: utf-8

names_read = open("names")
names_list = names_read.readlines()
names_read.close()

print(names_list)
names_dir = {}
names_dir = {i : d for i, d in enumerate(names_list)}
print(names_dir)
