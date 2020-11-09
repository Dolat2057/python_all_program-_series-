name = "   alok rathore   "
dots= "...........    ...."
#strip method used to remove the spaces.
# to remove left space in a string lstrip() method
#to remove right space in a string rstrip()

print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip()) # this method removes all the spaces from right and left side
print(name.replace(" ","") + dots.replace(" ","")) # replace all the spaces with the without spaces