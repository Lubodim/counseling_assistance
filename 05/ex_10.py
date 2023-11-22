number = int(input())

even_sum = 0
odd_sum = 0
for i in range(1, number +1):
    new_number = int(input())
    if i % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

difference = abs(even_sum - odd_sum)
if odd_sum == even_sum: # if not difference:, if difference == 0
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {difference}")
