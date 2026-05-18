def battle_logger(func):

    def wrapper(*args, **kwargs):

        print("\n======================")
        print("KAMPF STARTET")
        print("======================")

        result = func(*args, **kwargs)

        print("======================")
        print("KAMPF BEENDET")
        print("======================\n")

        return result

    return wrapper


class Character:

    def __init__(self, name, health, damage, **kwargs):

        self.name = name
        self.health = health
        self.damage = damage

        self.level = kwargs.get("level", 1)
        self.weapon = kwargs.get("weapon", "Fäuste")

    def show_stats(self):

        print("Name:", self.name)
        print("Leben:", self.health)
        print("Schaden:", self.damage)
        print("Level:", self.level)
        print("Waffe:", self.weapon)
        print("-------------------")

    @battle_logger
    def attack(self, *targets):

        for target in targets:

            if target.health <= 0:
                print(target.name, "ist bereits besiegt.")
                continue

            target.health -= self.damage

            print(self.name, "greift", target.name, "an!")
            print(target.name, "verliert", self.damage, "Leben!")

            if target.health <= 0:
                target.health = 0
                print(target.name, "wurde besiegt!")
            else:
                print(target.name, "hat noch", target.health, "Leben")

            print()


def main():

    player = Character(
        "Held",
        100,
        20,
        level=5,
        weapon="Flammenschwert"
    )

    enemies = [
        Character("Goblin", 50, 10),
        Character("Ork", 80, 15, weapon="Axt"),
        Character("Drache", 150, 30, level=10)
    ]

    print("\nSPIELER")
    player.show_stats()

    print("\nGEGNER")

    for enemy in enemies:
        enemy.show_stats()

    print("\nKAMPF BEGINNT")

    player.attack(*enemies)


main()
