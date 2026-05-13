
player = {
    "name": "Mario",
    "health": 100,
    "coins": 250,
    "inventory": ["Schwert", "Trank", "Schild"]
}

player_position = (150, 300)

enemies = [
    {
        "name": "Goblin",
        "health": 50,
        "position": (400, 200)
    },

    {
        "name": "Ork",
        "health": 120,
        "position": (600, 100)
    },

    {
        "name": "Zombie",
        "health": 70,
        "position": (250, 500)
    }
]

print("SPIELER:")
print(player)

print("\nName:")
print(player["name"])

print("\nInventar:")
print(player["inventory"])

player["inventory"].append("Bogen")

print("\nNeues Inventar:")
print(player["inventory"])

x, y = player_position

print("\nSPIELER POSITION:")
print("X:", x)
print("Y:", y)

print("\nGEGNER:")

for enemy in enemies:

    print("\nName:")
    print(enemy["name"])

    print("Leben:")
    print(enemy["health"])

    enemy_x, enemy_y = enemy["position"]

    print("Position X:")
    print(enemy_x)

    print("Position Y:")
    print(enemy_y)

enemies[0]["health"] -= 20

print("\nGoblin nach Schaden:")
print(enemies[0])

print("\nErste zwei Inventaritems:")
print(player["inventory"][0:2])

print("\nUpper:")
print(player["name"].upper())

print("\nCapitalize:")
print(enemies[2]["name"].capitalize())

print("\nAnzahl Gegner:")
print(len(enemies))
