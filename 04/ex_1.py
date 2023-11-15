tax_per_year = int(input())
sneakers = tax_per_year * 0.60 # 60/100
equipment = sneakers * 0.80
ball = equipment * 0.25 # 25/100 # equipment/4
acsesoares = ball * 0.20 # 20/100 # ball/5
total_expeces = (tax_per_year +
                 sneakers +
                 ball +
                 acsesoares +
                 equipment)
print(f"{total_expeces:.2f}")
