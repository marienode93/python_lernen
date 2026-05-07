players = ["mario", "luigi", "peach", "toad"]

print("Startliste:")
print(players)

print("----------------")

players.append("yoshi")

print("Nach append:")
print(players)

print("----------------")

players.insert(1, "bowser")

print("Nach insert:")
print(players)

print("----------------")

players.remove("toad")

print("Nach remove:")
print(players)

print("----------------")

last_player = players.pop()

print("Pop entfernt:")
print(last_player)

print("Liste nach pop:")
print(players)

print("----------------")

print("Erstes Element:")
print(players[0])

print("----------------")

print("Letztes Element:")
print(players[-1])

print("----------------")

print("Slicing 1 bis 3:")
print(players[1:3])

print("----------------")

print("Alles außer erstes Element:")
print(players[1:])

print("----------------")

print("Rückwärtsliste:")
print(players[::-1])

print("----------------")

print("Großbuchstaben:")
print(players[0].upper())

print("----------------")

print("Erster Buchstabe groß:")
print(players[2].capitalize())

print("----------------")

players[1] = "wario"

print("Element ersetzt:")
print(players)

print("----------------")

players.sort()

print("Sortiert:")
print(players)

print("----------------")

players.reverse()

print("Umgedreht:")
print(players)

print("----------------")

print("Anzahl Elemente:")
print(len(players))
