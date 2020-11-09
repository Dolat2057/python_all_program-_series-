#if elif else statement

#show ticket pricing
#0 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = input("your age is:")
age = int(age)
if  0<=age<=3:
    print("your tickets are free")
elif  4<age<=10:
        print("150 charges")
elif 11<age<=60:
        print("250charges")
else:
            print("200 charges")