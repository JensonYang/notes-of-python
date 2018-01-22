# Author:Li tianyang                  ## 重点程序，要自己独立写几次。
i = 0                                 # while else语法？ python强大之处
age_of_oldboy = 56

while  i<3 :
    guess_age = int(input("guess_age:"))

    if guess_age == age_of_oldboy:
        print("Yes,you got it!")
        break
    elif guess_age > age_of_oldboy:
        print("think samell....")
    else:
        print("think bigger!")
        i+=1
    if i == 3:
        continue_confirm = input("Do you want to continue this game?")
        if continue_confirm != 'n':
             i = 0
else:
    print("You have tried too many time..fuck off")

# if i==3:    此种写法是可以的，但是太low
# print("You have tried too many time..fuck off")

# print("You have tried too many time..fuck off")   如果这样，即使输入正确也会fuck off