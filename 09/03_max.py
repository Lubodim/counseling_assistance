max_number = float("-inf")
while True:
    number = input()
    if number == "END":
        break
    number = int(number)
    if number > max_number:
        max_number = number
print(max_number)