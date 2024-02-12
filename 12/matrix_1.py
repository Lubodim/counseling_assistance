row_cow = int(input())

matrix = []
sub_matrix = []
for _ in range(row_cow):
    matrix.append([int(x) for x in input().split()])
for r in range(row_cow - 1):
    for c in range(len(matrix[0]) - 1):
        cu_el = matrix[r][c]
        ri_el = matrix[r][c + 1]
        do_el = matrix[r + 1][c]
        di_el = matrix[r + 1][c + 1]
        if cu_el == ri_el and cu_el == di_el and cu_el == do_el:
            for f in matrix:
                print(f)
