#take two comma separated input from user
#1. user's name
#2. a single character


#output -2 print lines
#1. user name length
#2. count the character that user inputed (bonus : case insensitive count)

user_name, char = input("enter user name  and character").split(",")
print(f"length your name is {len(user_name)}")
print(f"count your character{user_name.strip().lower().count(char.strip().lower())}")