import time
time.sleep(2)
print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
print("                                 o                                         ")
print("                                // \ " )
print("                                \ //  ")
print("                                 o  ")
print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
time.sleep(2)
print("----------------------------------------------------------------------------")
print("||************************JOSHI'S CAKE SHOP*******************************||")
print("||****************************WELCOME*************************************||")
print("----------------------------------------------------------------------------")
print("Hello, Welcome to our cake shop.")
time.sleep(2)
name = input("What is your name sir?\n")
time.sleep(1)
print("hiii " + name +" Here you can get your desired cake")
time.sleep(1)
print("""\n\n@@@@Today's menu@@@@
1.Mango cake - 400
2.Butterscotch cake - 400
3.Oreo cake - 400
4.Kitkat cake - 400
5.Black Forest cake - 400""")
      
cake_price = 400
time.sleep(1)
cake_flavor = input("Which cake flavor you want?\n")
time.sleep(1)
cake_quantity = input("How many " + cake_flavor + " do you want?\n")
total = cake_price * int(cake_quantity)
time.sleep(1)
print("your sub-total is $",total)
time.sleep(1)
if total > 2000:
    print("congratulations, you get a 10% discount coupon for your next order.")
else:
    print("congratulations, you get a 5% discount coupon for your next order.")
time.sleep(1)
print("Thank you for visiting us. Please come again!")










