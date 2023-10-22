chicken_menu_price = 10.35
fish_menu_price = 12.40
vegeterian_menu_price = 8.15
delivery = 2.50

num_chicken_menu = int(input())
num_fish_menu = int(input())
num_vegeterian_menu = int(input())

all_menus_prise = (vegeterian_menu_price * num_vegeterian_menu +
                   fish_menu_price * num_fish_menu +
                   chicken_menu_price * num_chicken_menu)
desert_price = all_menus_prise * 0.20

total_price = all_menus_prise + desert_price + delivery

print(f"{total_price:.2f}")
