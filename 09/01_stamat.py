name = input()
grade_sum = 0
count = 0
while True:
    grade = input()
    if grade == "END TERM":
        break
    grade = float(grade)
    if not 2 <= grade <= 6:
        print(f"Invalid grade {grade},  system was hacked")
        break

    grade_sum += grade
    count += 1

avg = grade_sum / count

print(f"{avg:.2f}")
