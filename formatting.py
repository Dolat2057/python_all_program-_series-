#string formatting
name = "alok"
age = 23
print("hello " + name+ " your age is " +str(age) )

#python 3 gives the clean method for string formatting
print("hello {}  your age is {}".format(name,age))

#python 3.6 gives more accurate and clean method
print(f"hello {name} your age is {age+2}")