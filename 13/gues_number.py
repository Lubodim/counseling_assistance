from random import choice
secret_number = choice(range(1, 1_000_000))

while True:
    num = input("Enter a gues number: ")
    if num.lower() == "stop":
        break
    num = int(num)
    if num < secret_number:
        print("To small number! Try with bigger!")
    elif num > secret_number:
        print("To big number! Try with smaller!")
    else:
        print("U Win the game")
        break