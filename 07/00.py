# num = -10
# while True:
#     print(num)
#     num += 1
#     if num == 1:
#         break
#
# num = -10
# while num <= 0:
#     print(num)
#     num += 1


name = input()
counter = 0

while name != "END":
    if counter > 5:
        break
    counter += 1
    name = input()

print(counter)





counter = 0
while True:
    name = input()
    if counter > 5:
        break
    if name == "END":
        break
    counter += 1
print(counter)