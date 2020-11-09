# ask a user for name
# example - Alok Rathore
# print count for each words

#output 
name = input("please enter your name")
# Alok Rathore

name.count("A")
name.count("l")
name.count("o")
name.count("k")
name.count(" ")
name.count("R")
name.count("a")
name.count("t")
name.count("h")
name.count("o")
name.count("r")
name.count("e")

temp_var = ""
i= 0
while i< len(name):
    if name[i] not in temp_var:
        temp_var= temp_var + name[i]
    print(f"{name[i]}: {name.count(name[i])}")
    i = i+1
