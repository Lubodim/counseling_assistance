rotations = int(input())
max_num = float("-inf")
min_num = float("inf")

for _ in range(rotations):
    new_number = int(input())
    if new_number > max_num:
        max_num = new_number
    if new_number < min_num:
        min_num = new_number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")