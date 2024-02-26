# row_col = int(input())
# counter = 1
# matrix = []
# for row in range(row_col):
#     matrix.append([])
#     for col in range(row_col):
#         matrix[row].append(counter)
#         counter += 1
# print(*matrix, sep="\n")

#
# number = int(input())
# matrix = []
# for row in range(number):
#     matrix.append([])
#     for col in range(number):
#         matrix[row].append(row +1)
#
# for row in matrix:
#     print(*row, sep=", ")

#
# numb = int(input())
#
# matrix = []
#
# for row in range(numb):
#     current_row = input().split(", ")
#     matrix.append(current_row)
#
# for row in matrix:
#     print(*row, sep=", ")


numb = int(input())
total_sum = 0

for _ in range(numb):
    current_row = [int(x) for x in input().split(", ")]
    total_sum += sum(current_row)
print(total_sum)