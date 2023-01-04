#  Author: Leong Jia Jun
#  Admin No: 214181e

items = {'IM': {'description': 'Iced Milo', 'price': 1.50, 'quantity': 2},
         'IC': {'description': 'Iced Coffee', 'price': 1.50, 'quantity': 2},
         'CC': {'description': 'Coca cola', 'price': 1.30, 'quantity': 50},
         'HM': {'description': 'Hot Milo', 'price': 1.20, 'quantity': 20},
         'HC': {'description': 'Hot Coffee', 'price': 1.20, 'quantity': 0},
         '1P': {'description': '100 Plus', 'price': 1.10, 'quantity': 50}}

loop1 = int(1)
numberdrinks = int(0)
totalprice = float(0)

NO = """Welcome to ABC Vending Machine.
Select from the following choices to continue:
IM. Iced Milo (S$1.5)
HM. Hot Milo (S$1.2)
IC. Iced Coffee (S$1.5)
HC. Hot Coffee (S$1.2)
1P. 100 Plus (S$1.1)
CC. Coca Cola (S$1.3)
0. Exit / Payment"""
YES = """Welcome to ABC Vending Machine.
Select from the following choices to continue:
1. Add Drink Type
2. Replenish Drink
0. Exit"""
cancel2 = 0
while cancel2 == 0:  #loop to return to this question after purchase is cancelled
    vendor = input("Are you a vendor (Y/N)? ").upper()

    if vendor == "N":
        print(NO)  #drinks menu
        while loop1 != 0:  #loop until user enter 0 for payment/exit
            NOchoice = input("Enter Choice: ")
            if NOchoice.upper() == "IM":
                numberdrinks += 1
                print("No. of drinks selected =", numberdrinks)
                totalprice = totalprice + items["IM"]["price"]
            elif NOchoice.upper() == "HM":
                numberdrinks += 1
                print("No. of drinks selected =", numberdrinks)
                totalprice = totalprice + items["HM"]["price"]
            elif NOchoice.upper() == "IC":
                numberdrinks += 1
                print("No. of drinks selected =", numberdrinks)
                totalprice = totalprice + items["IC"]["price"]
            elif NOchoice.upper() == "HC":
                numberdrinks += 1
                print("No. of drinks selected =", numberdrinks)
                totalprice = totalprice + items["HC"]["price"]
            elif NOchoice.upper() == "1P":
                numberdrinks += 1
                print("No. of drinks selected =", numberdrinks)
                totalprice = totalprice + items["HP"]["price"]
            elif NOchoice.upper() == "CC":
                numberdrinks += 1
                print("No. of drinks selected =", numberdrinks)
                totalprice = totalprice + items["CC"]["price"]
            elif NOchoice == "0":
                loop1 = 0
                loop2 = 0
                while loop2 == 0:
                    if numberdrinks > 0:
                     print("Please Pay:", "$%.2f" % totalprice)
                     print("Indicate your payment")
                     tendollar = int(input("Enter no. of $10 notes: "))
                     totalpaid = float(0)
                     totalpaid = totalpaid + (tendollar*10)
                     if totalpaid >= totalprice:
                        change = totalpaid - totalprice
                        print("Please collect your change:", "$%.2f" % change)
                        print("Drinks paid. Thank You.")
                        loop2 = 1
                     else:
                        fivedollar = int(input("Enter no. of $5 notes: "))
                        totalpaid = totalpaid + (fivedollar*5)
                        if totalpaid >= totalprice:
                           change = totalpaid - totalprice
                           print("Please collect your change:", "$%.2f" % change)
                           print("Drinks paid. Thank You.")
                           loop2 = 1
                        else:
                            twodollar = int(input("Enter no. of $2 notes: "))
                            totalpaid = totalpaid + (twodollar*2)
                            if totalpaid >= totalprice:
                                change = totalpaid - totalprice
                                print("Please collect your change:", "$%.2f" % change)
                                print("Drinks paid. Thank You.")
                                loop2 = 1
                            elif totalpaid < totalprice:
                                print("Not enough to pay for the drinks")
                                print("Take back your cash!")
                                cancel = input("Do you want to cancel the purchase? Y/N: ")
                                if cancel == "Y" or cancel == "y":
                                    print("Purchase is cancelled. Thank you.")
                                    cancel2 = 0
                                    loop2 = 1
                                elif cancel == "N" or cancel == "n":
                                    loop2 = 0

            else:
                print("Invalid option")

    elif vendor == "Y":
        print(YES)
        YESchoice = int(input("Enter Choice: "))

    else:
        print("You did not type Y or N.")
