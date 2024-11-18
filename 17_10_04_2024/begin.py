# # print(*[int(x) for x in input().split("-")], sep=":")
# my_list = input().split(" ")
# my_list.pop(0)
# print(my_list)
#
my_list = [1, 2, 3, 4, 5]
# my_list_2 = [6, 7, 8, 9, 10, 11, 12, 13, 14]
# my_list.extend(my_list_2)
# print(my_list)
 a = my_list.copy(my_list)
 my_list.extend(a)
 print(a)