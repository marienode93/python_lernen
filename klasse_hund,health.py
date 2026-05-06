class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.energy = 100
        self.hunger = 0

    def show_info(self):
        print("Name:", self.name)
        print("Alter:", self.age)
        print("Rasse:", self.breed)
        print("Energie:", self.energy)
        print("Hunger:", self.hunger)
        print("-------------------")

    def bark(self):
        print(self.name, "sagt: Wuff!")

    def play(self):
        print(self.name, "spielt!")

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
        print(self.name, "frisst.")

        self.hunger -= 20

        if self.hunger < 0:
            self.hunger = 0

    def birthday(self):
        self.age += 1
        print(self.name, "hat Geburtstag und ist jetzt", self.age)


dog1 = Dog("Bella", 3, "Labrador")


dog1.show_info()

dog1.play()
dog1.show_info()

dog1.sleep()
dog1.show_info()

dog1.eat()
dog1.show_info()

dog1.birthday()
dog1.show_info()

dog1.bark()
