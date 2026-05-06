class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def show_stats(self):
        print("Name:", self.name)
        print("Leben:", self.health)
        print("Schaden:", self.damage)
        print("-------------------")

    def attack(self, target):
        target.health -= self.damage

        print(self.name, "greift an!")
        print(target.name, "verliert", self.damage, "Leben!")

        if target.health <= 0:
            print(target.name, "wurde besiegt!")
        else:
            print(target.name, "hat noch", target.health, "Leben")


player = Character("Held", 100, 20)

enemies = [
    Character("Goblin", 50, 10),
    Character("Ork", 80, 15),
    Character("Drache", 150, 30)
]


player.show_stats()

for enemy in enemies:
    enemy.show_stats()


for enemy in enemies:
    player.attack(enemy)
    print()
