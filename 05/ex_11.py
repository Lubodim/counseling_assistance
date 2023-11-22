number = int(input())
max_number = 0
min_number = 0


for i in range(number):
    new_number = int(input())
    if new_number > max_number:
        max_number = new_number
    if new_number < min_number:
        min_number = new_number
print(f"Min number: {min_number}")
print(f"Max number: {max_number}")