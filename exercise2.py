#1 Ask user to input 3 numbers and you have to print average of three numbers using string formatting
#1.1(part) try to take all three comma separted inputs in one line

number1,number2,number3 = input("enter the  three numbers that you want to average").split(",")
#python 3.6 formating method
print(f"the average is {(int(number1)+int(number2)+int(number3))/3}")
#python 3 string formatting method
print("the average is {}".format((int(number1)+int(number2)+int(number3))/3))