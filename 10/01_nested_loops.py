counter = 0
for x1 in range(26):
    for x2 in range(26):
        for x3 in range(26):
            for x4 in range(26):
                if x1 + x2 + x3 + x4 == 25:
                    counter += 1
print(counter)