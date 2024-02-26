from random import choice
cards = [2, 3, 4, 5, 6, 7, 8, 9, "reverse", "Color change", "+4", "+2", "Block"]
colors = ["Blue", "Green", "Yellow", "Red"]
total_cards = []
for el in cards:
    for el2 in colors:
        total_cards.append(f"{el}-{el2}")

given_cards = []

player_1 = input()
player_2 = input()

player_1_cards = []
player_2_cards = []

for _ in range(2):
    for _ in range(7):
        card = ""
        while True:
            card = choice(total_cards)
            if card in given_cards:
                continue
            given_cards.append(card)
            break
        player_1_cards.append(card)
    player_1, player_2, player_1_cards, player_2_cards = player_2, player_1, player_2_cards, player_1_cards

print(f"{player_1} have {player_1_cards}")
print(f"{player_2} have {player_2_cards}")

