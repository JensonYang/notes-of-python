# Author: Li tianyang
product_list = [
    ("Iphone", 5000),
    ("Mac", 8000),
    ("Bike", 1000),
    ("Camera", 800),
    ("Coffee", 800),
    ("Machine Learning", 800),
]
shopping_list = []
salary = input("Please input your salary :")
if salary.isdigit():
    salary = int(salary)
    while True:
        for item in product_list:
            print(product_list.index(item), item)

        user_choose = input("Please choose your goods:")

        if user_choose.isdigit():
            user_choose = int(user_choose)
            if user_choose <= len(product_list) and user_choose >= 0:
                p_item = product_list[user_choose]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added  %s in your shopping cart, your current balance is %s" %(p_item,salary))
                else:
                    print("You don't have enough money to pay for it.")
            else:
                print("product code %s is not exist!" %(user_choose))
        elif user_choose =='q':
            print("-----shopping_list-------")
            for i in shopping_list:
                print(shopping_list.index(i), i)
            exit()
        else:
            print("Invaild option!")