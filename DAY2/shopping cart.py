# Author:Li tianyang

product_list = [
    ("Iphone", 5800),
    ("Mac Pro", 8000),
    ("Bike", 800),
    ("Watch", 10800),
    ("Coffee", 30),
    ("Machine Learning", 65),
]
shopping_list = []
salary = input("Please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for item in product_list:
            print(product_list.index(item), item) #索引获取下标，充当序号

        user_choice = input("请选购你的商品：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice <= len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if  p_item[1] <= salary:   #买的起 p_item[1] 1代表的是价格
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into your shopping cart, your current balance is %s"%(p_item, salary))
                else:
                    print("You don't have enough money to pay for it!")
            else:
                print("product code %s is not exist"%(user_choice) )
        elif user_choice == 'q':
            print("------shopping list--------")
            for p in shopping_list:
                print(shopping_list.index(p), p)

            exit()    ######## 此处要离开！！！！！！
        else:
            print("invaild option!")