class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def show_info(self):
        print("Name:", self.name)
        print("Alter:", self.age)
        print("Rasse:", self.breed)
        print("-------------------")

    def bark(self):
        print(self.name, "sagt: Wuff!")


dogs = [
    Dog("Bella", 3, "Labrador"),
    Dog("Fiffy", 7, "Pudel"),
    Dog("Luna", 2, "Golden Retriever"),
    Dog("Max", 5, "Beagle"),
    Dog("Rocky", 4, "Bulldogge"),
    Dog("Milo", 1, "Dackel"),
    Dog("Nala", 6, "Schäferhund"),
    Dog("Charlie", 8, "Border Collie"),
    Dog("Balu", 9, "Bernhardiner"),
    Dog("Coco", 2, "Chihuahua")
]


for dog in dogs:
    dog.show_info()


for dog in dogs:
    dog.bark()
