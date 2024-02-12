n, m = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(', '))))

max_sum = float("-inf")
sub_matrix = []
for r in range(n -1):
    for c in range(m - 1):
        current_element = matrix[r][c]
        right_element = matrix[r][c + 1]
        down_element = matrix[r + 1][c]
        diagonal_element = matrix[r + 1][c + 1]
        current_sum = current_element + right_element + down_element + diagonal_element
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [current_element, right_element, down_element, diagonal_element]

for index, element in enumerate(sub_matrix):
    if index % 2 == 0:
        print(element, end=" ")
    else:
        print(element)


print(max_sum)
