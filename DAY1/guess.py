# Author:Li tianyang

age_of_oldboy = 56

guess_age = int(input("geuss age:"))   #需要强制类型转换

if guess_age == age_of_oldboy:
    print("Yes,you got it!")
elif guess_age > age_of_oldboy:         #    elif in python === else if in C
    print("think samell....")
else:
    print("think bigger!")