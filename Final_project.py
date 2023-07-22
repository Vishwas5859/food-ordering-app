# Design a Food Ordering app for a restaurant:              

welcome = input("Welcome to ABC restaurant, if you are new user type yes or no: " )

import re
if welcome == "yes":
    name = input("Enter your name: ")
    Contact_No = input("Enter the Contact_No: ")
    Email_ID = input("Enter the Email.ID: ")
    Address = input("Enter the Address: ")
    
    while True:
        Set_Password = input("Set Password: ")
        pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$" 
    
        if re.match(pattern, Set_Password):
            print("Password is set")
            print("Welcome to the ABC restaurent, Please select your food from the menu ")
            break
        else:
            print("Set correct Password!, Click on Password Criteria")  
            print("Password must consist: One capital letter, one special char like $,@,&, and numerical char")
    
elif welcome == "no":
    while True:
        Password = input("Enter the Password: ")
        pattern = "Rock@119"

        if re.match(pattern,Password):
            print("Welcome to the ABC restaurant, Please select your food form the menu")
            break
        else:
            print("Enter correct Password!")  

Address2 = "House No. 123, Flower street, Block 2"

#-------------------------------------------------------------------------------------------------------

from datetime import date
from datetime import datetime
order_history1 = "['Tandoori Chicken (4 pieces)','Truffle Cake', 'Orange Juice'] on 2023-03-12"
order_history2 = "['Tandoori Chicken (4 pieces)','Hot Chocolate Fudge'] on 2023-05-22"

Discount_alloted = 0.05 # 5% Discount based on previous orders.
to_see_order_history = input("Do you want to see your Order History, Click yes or no: ")

food = ['Vegan Burger','Tandoori Chicken (4 pieces)', 'Truffle Cake']
price = [240,320,900]


if to_see_order_history == "yes":
    print("Your Previous order's are: ",order_history1,order_history2)
else: 
    print("Continue ordering... ")

print("              ")
myordered_food = []
myodered_cost =[]
Qty = []

counter = 0
total = 0

order = input("Can i take your order? yes/no: ")

if order == "no":
    exit()
else:
    print("Thank you,Today's menu is: ",food)    


Next_order = True

while Next_order == True:
    food_order = input("Please enter the item: ")

    if food_order == 'Vegan Burger':
        myordered_food.append(food[0])
        myodered_cost.append(price[0])
        Quantity1 = input("Enter the quantity of Vegan Burger: ")
        Qty.append(Quantity1)
        counter = counter +1
        total = total+(price[0]) * int(Quantity1)
        
    elif food_order == 'Tandoori Chicken (4 pieces)':
        myordered_food.append(food[1])
        myodered_cost.append(price[1])
        Quantity2 = input("Enter the quantity of Tandoori Chicken: ")
        Qty.append(Quantity2)
        counter = counter +1
        total = total+(price[1]) * int(Quantity2)
        

    elif food_order == 'Truffle Cake':
        myordered_food.append(food[2])
        myodered_cost.append(price[2])
        Quantity3 = input("Enter the quantity of Truffle Cake: ")
        Qty.append(Quantity3)
        counter = counter +1
        total = total+(price[2]) * int(Quantity3)
        
    else:
        print("Not in menu")  

    finished = input("Have you finished ordering yes/no ")
    if finished == "no":
        Next_order = True
    else:
        Next_order = False


y = 0
print("Here is your order")
print("    ")
print("---------------------")
while y < counter:
    print('Item:'+(myordered_food[y]))
    print("Price: "+str(myodered_cost[y]), "  ","Quantity: ",Qty[y]) 
    y =y+1

print("---------------------")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("The Total cost is: Rs",str(total),"Date & Time: " ,date.today(),"|", now.strftime("%H:%M"))

print("Price after discount is:Rs",str(total - total*Discount_alloted)," Date & Time: ",date.today(),"|",now.strftime("%H:%M"))
print("           ")
print("--THANK YOU--")
print("The order will be delivered to the addres ",Address2)

#---------------------------------------------------------------------------------------------------------------

# ADMIN (Code) --
name1 = input("Enter admin name: ")
while True:
        Password = input("Enter the Admin Password: ")
        pattern = "ABC@123"

        if re.match(pattern,Password):
            print("Welcome to the ABC restaurant")
            print("Admin name: ",name1)
            break
        else:
            print("Enter correct Password!")  

#-------------------------------------------------------------------------------------------------------------

