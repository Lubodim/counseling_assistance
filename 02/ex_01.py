nylon_price_per_2_m = 1.50
paint_price_per_l = 14.50
thinner_price_per_l = 5.00
bags = 0.4

nylon_needed = int(input()) + 2
paint_needed = int(input()) * 1.1
thinner_needed = int(input())
hours_of_work = int(input())

end_nylon_price = nylon_needed * nylon_price_per_2_m
end_paint_price = paint_price_per_l * paint_needed
end_thinner_price = thinner_price_per_l * thinner_needed
total_price_materials = (end_nylon_price
               + end_paint_price
               + end_thinner_price
               + bags)
workers_per_hour = total_price_materials * 0.3
total_price_workers = workers_per_hour * hours_of_work

money_for_rework = total_price_workers + total_price_materials
print(money_for_rework)