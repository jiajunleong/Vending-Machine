#  Author: Leong Jia Jun
#  Admin No: 214181e

numberdrinks = int(0)

NO = """Welcome to ABC Vending Machine.
Select from the following choices to continue:
IM. Iced Milo (S$1.50)
HM. Hot Milo (S$1.20)
IC. Iced Coffee (S$1.50)
HC. Hot Coffee (S$1.20)
1P. 100 Plus (S$1.10)
CC. Coca Cola (S$1.30)
0. Exit / Payment"""
YES = """Welcome to ABC Vending Machine.
Select from the following choices to continue:
1. Add Drink Type
2. Replenish Drink
0. Exit"""
items = {'IM': {'description': 'Iced Milo', 'price': 1.50, 'quantity': 2},
         'IC': {'description': 'Iced Coffee', 'price': 1.50, 'quantity': 2},
         'CC': {'description': 'Coca cola', 'price': 1.30, 'quantity': 50},
         'HM': {'description': 'Hot Milo', 'price': 1.20, 'quantity': 20},
         'HC': {'description': 'Hot Coffee', 'price': 1.20, 'quantity': 0},
         '1P': {'description': '100 Plus', 'price': 1.10, 'quantity': 50}}

items2 = {'IM': {'description': 'Iced Milo', 'price': 1.50, 'quantity': 0},
          'IC': {'description': 'Iced Coffee', 'price': 1.50, 'quantity': 0},
          'CC': {'description': 'Coca cola', 'price': 1.30, 'quantity': 0},
          'HM': {'description': 'Hot Milo', 'price': 1.20, 'quantity': 0},
          'HC': {'description': 'Hot Coffee', 'price': 1.20, 'quantity': 0},
          '1P': {'description': '100 Plus', 'price': 1.10, 'quantity': 0}}


while True:
    loop1 = int(1)
    numberdrinks = 0
    totalprice = float(0)

    for id in items2:
        items2[id]["quantity"] = 0

    vendor = input("Are you a vendor (Y/N)? ").upper()

    if vendor == "N":
        #output drinks and quantity for selection
        for key in items:
            print(key, ' : ', items[key])
        while loop1 != 0:
            #loop to choose drinks until user enter 0 to stop
            NOchoice = input("Enter Choice: ").upper()
            if NOchoice in items:  #if drink id exist in dictionary:
                if (items[NOchoice]["quantity"]) != (items2[NOchoice]["quantity"]):  #if drink's quantity same in both dictionary, it is out of stock
                    numberdrinks += 1  #calculate total number of drinks
                    items2[NOchoice]["quantity"] += 1  #new dictionary update for stock
                    print("No. of drinks selected =", numberdrinks)
                    totalprice = totalprice + items[NOchoice]["price"]
                else:
                    print(items[NOchoice]["description"] + " is out of stock.")

            elif NOchoice == "0":
                loop2 = int(0)
                while loop2 == 0:
                    loop1 = 0
                    totalpaid = 0
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
                        for key in items:
                            items[key]["quantity"] = items[key]["quantity"] - items2[key]["quantity"]  #update on main dictionary on stocks
                        print("UPDATED STOCKS:")
                        for key in items:
                            print(key, ' : ', items[key])  #output drinks and quantity to show updated stocks
                    else:
                        fivedollar = int(input("Enter no. of $5 notes: "))
                        totalpaid = totalpaid + (fivedollar*5)
                        if totalpaid >= totalprice:
                            change = totalpaid - totalprice
                            print("Please collect your change:", "$%.2f" % change)
                            print("Drinks paid. Thank You.")
                            loop2 = 1
                            for key in items:
                                items[key]["quantity"] = items[key]["quantity"] - items2[key]["quantity"]  #update on main dictionary on stocks
                            print("UPDATED STOCKS:")
                            for key in items:
                                print(key, ' : ', items[key])  #output drinks and quantity to show updated stocks
                        else:
                            twodollar = int(input("Enter no. of $2 notes: "))
                            totalpaid = totalpaid + (twodollar*2)
                            if totalpaid >= totalprice:
                                change = totalpaid - totalprice
                                print("Please collect your change:", "$%.2f" % change)
                                print("Drinks paid. Thank You.")
                                loop2 = 1
                                for key in items:
                                    items[key]["quantity"] = items[key]["quantity"] - items2[key]["quantity"]  #update on main dictionary on stocks
                                print("UPDATED STOCKS:")
                                for key in items:
                                    print(key, ' : ', items[key])  #output drinks and quantity to show updated stocks
                            elif totalpaid < totalprice:
                                print("Not enough to pay for the drinks")
                                print("Take back your cash!")
                                cancel = input("Do you want to cancel the purchase? Y/N: ").upper()
                                if cancel.upper() == "Y":
                                    loop2 = 1
                                    print("Purchase is cancelled. Thank you.")

                                elif cancel.upper() == "N":
                                    loop2 = 0

    elif vendor == "Y":  #vendor's point of view
        print(YES)
        YESchoice = int(input("Enter Choice: "))
        if YESchoice == 1:
            loop3 = 0
            new = ()
            while loop3 == 0:  #loop until user input a new drink ID
                new = input("Enter Drink ID: ").upper()
                if (new in items) is True:
                   print("drink id EXIST!!")
                else:
                   loop3 = 1
            new2 = input("Enter Description of Drink: ")  #new drink description
            new3 = float(input("Enter Price of New Item: "))  #new drink price
            new4 = int(input("Enter Quantity of New Item: "))  #new drink quantity

            def add_drink_type(drink_id, description, price, quantity):
                items[new] = {description: new2, price: new3, quantity: new4}  #update new drink in main dictionary
                items2[new] = {description: new2, price: new3, quantity: 0}  #update new drink in 2nd dictionary(update main dict on stocks when user buy)

                for key4 in items:
                    print(key4, ' : ', items[key4])  #output drinks and quantity to show updated new drink
            add_drink_type('drink_id', 'description', 'price', 'quantity')

        elif YESchoice == 2:
            for key2 in items:
                print(key2, ' : ', items[key2])   #output drinks and quantity to show current stocks
                loop4 = 0

                replenishchoice = ()
                while loop4 == 0:  #loop until user enter drink id that exist in main dictionary
                    replenishchoice = input("Enter drink id: ").upper()
                    if (replenishchoice in items) is False:
                        print("no drink with this drink id. Try again.")
                    else:
                        loop4 = 1
                    while loop4 == 1:
                        if items[replenishchoice]["quantity"] > 5:
                            print("No need to replenish. Quantity is greater than 5.")
                            loop4 = 0
                        elif items[replenishchoice]["quantity"] <= 5:
                            loop4 = 5

                replenishquantity = input("Enter quantity: ")
                specialcheckdigit = 0
                while specialcheckdigit == 0:  #loop until user enter a positive number
                    if replenishquantity.isdigit():
                        if int(replenishquantity) > 0:
                            specialcheckdigit = 1
                    elif replenishquantity.isdigit() is False:
                        replenishquantity = input("Enter quantity: ")

            def replenish_drink(drink_id, quantity):
                drink_id = replenishchoice
                prevquantity = items[drink_id][quantity]  #current stocks
                topup = int(prevquantity) + int(replenishquantity)  #add current stocks with replenish quantity
                items[drink_id][quantity] = topup  #update the replenished amount of stocks
                print(drink_id, " has been top up!")
                for key3 in items:
                    print(key3, ' : ', items[key3])  #output drinks and quantity to show updated stocks
            replenish_drink('drink_id', 'quantity')
