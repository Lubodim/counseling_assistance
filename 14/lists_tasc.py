data = input().split()
numbers_list = []
command_list = []

for element in data:
    if element.isdigit():
        numbers_list.append(int(element))
    else:
        command_list.append(element)
print(numbers_list)

for word in command_list:
    if word == "add":
        numbers_list.append(101)
    elif word == "remove":
        numbers_list.remove(3)
    elif word == "clear":
        numbers_list.clear()
    elif word == "sort":
        numbers_list.sort()
        numbers_list.reverse()
    else:
        continue
print(command_list)
print("-".join(str(x) for x in numbers_list))
