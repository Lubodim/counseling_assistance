number = int(input())
sum_1 = 0
sum_2 = 0

for i in range(number):
    new_number = int(input())
    sum_1 += new_number

for _ in range(number):
    new_numbers = int(input())
    sum_2 += new_numbers

difference = abs(sum_1 - sum_2)
if sum_1 == sum_2:
    print(f"Yes, sum = {sum_1}")
else:
    print(f"No, diff = {difference}")
