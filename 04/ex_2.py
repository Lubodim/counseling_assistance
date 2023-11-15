number_of_dancers = int(input())
points = float(input())
season = input()
place = input()

sum_of_price = 0

if place == "Bulgaria":
    sum_of_price = points * number_of_dancers
elif place == "Abroad":
    # sum_of_price = (points * number_of_dancers +
    #                 (points * number_of_dancers / 2))
    sum_of_price = (points * number_of_dancers) * 1.5

if place == "Bulgaria":
    if season == "summer":
        sum_of_price *= 0.95
    elif season == "winter":
        sum_of_price *= 0.92
elif place == "Abroad":
    if season == "summer":
        sum_of_price *= 0.90
    elif season == "winter":
        sum_of_price *= 0.85

sum_after_donation = sum_of_price * 0.25
sum_per_dancer = sum_after_donation / number_of_dancers

print(f"Charity - {(sum_of_price - sum_after_donation):.2f}")
print(f"Money per dancer - {sum_per_dancer:.2f}")
