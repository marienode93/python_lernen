class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.energy = 100
        self.hunger = 0
        self.health = 100

    def show_info(self):
        print("\n----- HUNDE-INFOS -----")
        print("Name:", self.name)
        print("Alter:", self.age)
        print("Rasse:", self.breed)
        print("Energie:", self.energy)
        print("Hunger:", self.hunger)
        print("Gesundheit:", self.health)
        print("-----------------------")

    def bark(self):
        print(self.name, "sagt: Wuff!")

    def play(self):
        print(self.name, "spielt fröhlich!")

        self.energy -= 20
        self.hunger += 15

        if self.energy < 0:
            self.energy = 0

        if self.hunger > 100:
            self.hunger = 100

    def sleep(self):
        print(self.name, "schläft...")

        self.energy += 30

        if self.energy > 100:
            self.energy = 100

    def eat(self):
        print(self.name, "frisst etwas.")

        self.hunger -= 20

        if self.hunger < 0:
            self.hunger = 0

    def birthday(self):
        self.age += 1
        print(self.name, "hat Geburtstag!")
        print(self.name, "ist jetzt", self.age, "Jahre alt.")

    def check_status(self):

        if self.hunger >= 100:
            print(self.name, "hat zu großen Hunger!")
            self.health -= 30

        if self.energy <= 0:
            print(self.name, "ist komplett erschöpft!")
            self.health -= 20

        if self.health <= 0:
            print(self.name, "ist leider gestorben...")
        else:
            print(self.name, "geht es aktuell noch gut.")



dog1 = Dog("Bella", 3, "Labrador")


while dog1.health > 0:

    print("\nWÄHLE EINE AKTION")
    print("1 = Infos anzeigen")
    print("2 = Spielen")
    print("3 = Schlafen")
    print("4 = Essen")
    print("5 = Bellen")
    print("6 = Geburtstag")
    print("7 = Spiel beenden")

    choice = input("Deine Auswahl: ")


    if choice == "1":
        dog1.show_info()

    elif choice == "2":
        dog1.play()
        dog1.check_status()

    elif choice == "3":
        dog1.sleep()
        dog1.check_status()

    elif choice == "4":
        dog1.eat()
        dog1.check_status()

    elif choice == "5":
        dog1.bark()

    elif choice == "6":
        dog1.birthday()

    elif choice == "7":
        print("Spiel beendet.")
        break

    else:
        print("Ungültige Eingabe!")
