print("\t\t\t\t\twelcome to Food court")
opt=input("do you want to order y/n")
bal=0


while (opt == "y"):
    menu_1=int(input("Please select below option\n1.Veg\n2.Non Veg\n"))
    if (menu_1==1):
        print("Menu Name\t\t\t\tPrice\n1.Sandwich\t\t\t\t20rs\n2.Franky\t\t\t\t25rs\n3.Veg Momos\t\t\t\t30rs")
        opt_1=int(input("Please Select option"))
        qty = int(input("please select quantity"))
        if (opt_1==1):
                print("you have selected Sandwtch")
                bal=bal+20*qty
        elif (opt_1==2):
                print("you have selected Franky")
                bal=bal+25*qty
        elif (opt_1==3):
                print("you have selected Veg Momos")
                bal=bal+30*qty
        else:
            print("invalid option")

    elif (menu_1==2):
        print("Menu Name\t\t\t\tPrice\n1.Shawarma\t\t\t\t50rs\n2.Chicken65\t\t\t\t60rs\n3.Lolipop\t\t\t\t80rs")
        opt_2 = int(input("Please Select option"))
        qty_1= int(input("please select quantity"))
        if (opt_2==1):
            print("you have selected Shawarma")
            bal=bal+50*qty_1
        elif (opt_2==2):
            print("you have selected Chicken65")
            bal = bal+60*qty_1
        elif (opt_2==3):
            print("you have selected Lolipop")
            bal=bal+80*qty_1
        else:
            print("invalid option")
    else:
        print("invalid option")

    opt=input("do you want to oreder again y/n")
    print("your total bill is",bal,"rs")
print("thank you for visiting us have a great day")
