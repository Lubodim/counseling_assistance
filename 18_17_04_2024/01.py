max_num = float("-inf")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for i, el in enumerate(my_list):
    if i + 1 == len(my_list):
        break
    current = el + my_list[i+1]
    if current > max_num:
        max_num = current
print(max_num)




