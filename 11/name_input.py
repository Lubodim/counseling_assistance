count_name = 0
while True:
    name = input()
    if name == "END":
        break
    count_name += 1
    if count_name == 5:
        break

print(count_name)