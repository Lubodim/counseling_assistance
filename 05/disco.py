money = float(input())
age = int(input())

entre = 20
wiskey = 10
cola = 5
nuts = 10


if age >= 18 and money >= entre:
    print("Welcome to the disco")
    money -= entre
    if money >= wiskey:
        money -= wiskey
        print("now U can drink wiskey!")
    elif money >= cola:
        money -= cola
        print("now U can drink cola!")
    elif money >= nuts:
        print("now U can eat nuts!")
    else:
        print("U dont have enough money for anything")
else:
    print("u dont have enough money or age")


