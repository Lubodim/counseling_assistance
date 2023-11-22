text = input()

# print(text.swapcase())
total_sum = 0

for t in text:
    if t.lower() == 'a':
        total_sum += 1 # total_sum = total_sum + 1
    elif t.lower() == 'e':
        total_sum += 2
    elif t.lower() == 'i':
        total_sum += 3
    elif t.lower() == 'o':
        total_sum += 4
    elif t.lower() == 'u':
        total_sum += 5
print(total_sum)
