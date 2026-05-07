# =========================================
# LISTE + TUPLE + DICTIONARY ZUSAMMEN
# MINI-SPIELBEISPIEL
# =========================================


# -----------------------------------------
# SPIELER (DICTIONARY)
# -----------------------------------------

player = {
    "name": "Mario",
    "health": 100,
    "coins": 250,
    "inventory": ["Schwert", "Trank", "Schild"]
}


# -----------------------------------------
# POSITION (TUPLE)
# -----------------------------------------

player_position = (150, 300)


# -----------------------------------------
# GEGNERLISTE
# LISTE MIT DICTIONARIES
# -----------------------------------------

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


# =========================================
# SPIELERDATEN
# =========================================

print("SPIELER:")
print(player)

print("\nName:")
print(player["name"])

print("\nInventar:")
print(player["inventory"])


# =========================================
# LISTE VERÄNDERN
# =========================================

player["inventory"].append("Bogen")

print("\nNeues Inventar:")
print(player["inventory"])


# =========================================
# TUPLE VERWENDEN
# =========================================

x, y = player_position

print("\nSPIELER POSITION:")
print("X:", x)
print("Y:", y)


# =========================================
# GEGNER DURCHGEHEN
# =========================================

print("\nGEGNER:")

for enemy in enemies:

    print("\nName:")
    print(enemy["name"])

    print("Leben:")
    print(enemy["health"])

    # Tuple auspacken
    enemy_x, enemy_y = enemy["position"]

    print("Position X:")
    print(enemy_x)

    print("Position Y:")
    print(enemy_y)


# =========================================
# SCHADEN MACHEN
# =========================================

enemies[0]["health"] -= 20

print("\nGoblin nach Schaden:")
print(enemies[0])


# =========================================
# SLICING
# =========================================

print("\nErste zwei Inventaritems:")
print(player["inventory"][0:2])


# =========================================
# UPPER + CAPITALIZE
# =========================================

print("\nUpper:")
print(player["name"].upper())

print("\nCapitalize:")
print(enemies[2]["name"].capitalize())


# =========================================
# LEN
# =========================================

print("\nAnzahl Gegner:")
print(len(enemies))
