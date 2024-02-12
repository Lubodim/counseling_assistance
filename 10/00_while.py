counter = 0
name = input()
while name != "END":
    counter += 1
    if counter >= 5:
        break
    name = input()
print(counter)