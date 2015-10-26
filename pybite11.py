# coding: utf-8

name_line = ""
names_stream = ""
empty_line = 0

while empty_line != 2:
    name_line = input("Podaj kolejne imię > ")
    if name_line == "":
        empty_line += 1
    else:
        empty_line = 0
        #if names_stream != "":
            #names_stream += "\n"
        # zależy czy chcemy też koniec linii po ostatnim imieniu
        # tutaj chcemy
        names_stream += name_line
        names_stream += "\n"

print(names_stream)

file_names = open("names", "w")
file_names.write(names_stream)
file_names.close()
