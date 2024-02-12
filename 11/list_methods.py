a = ["1", "2", "3", "4", "5", "6", "7"]
b = []
for digit in a:
    b.append(int(digit))
print(a)
print(b)
c = [int(digit) for digit in a]
print(c)
d = list(map(int, a))
print(d)


# a = [1, 2, 3.14, 4, True, 1, "7", 1, 1, 10]
# # for _ in range(4):
# #     a.append(22)
# print(a)
#
# b = [a.append(22) for _ in range(4)]
#
# print(a)







# count_number = a.count(1)
# a.insert(2, 22)
# print(count_number)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(a)
# b = [1, 2, 3, 4, 5, 6, 7]
# a.extend(b)
# print(a)