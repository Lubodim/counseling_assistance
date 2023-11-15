def calculator(n, m, operator):
    if operator == '+':
        print(n + m)
    elif operator == '-':
        print(n - m)
    elif operator == '*':
        print(n * m)
    elif operator == '/':
        print(n / m)

num_1 = int(input())
num_2 = int(input())
operators = input()

calculator(num_1, num_2, operators)