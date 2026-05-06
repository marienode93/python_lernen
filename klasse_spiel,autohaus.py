class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.sold = False
        self.kilometers = 0
        self.owner = None

    def show_info(self):

        print("\n----- AUTO-INFOS -----")
        print("Marke:", self.brand)
        print("Modell:", self.model)
        print("Baujahr:", self.year)
        print("Preis:", self.price, "Euro")
        print("Kilometer:", self.kilometers)

        if self.owner:
            print("Besitzer:", self.owner)
        else:
            print("Besitzer: Kein Besitzer")

        if self.sold:
            print("Status: Verkauft")
        else:
            print("Status: Verfügbar")

        print("----------------------")

    def drive(self, km):

        if self.sold:

            self.kilometers += km

            print(self.brand, self.model, "fährt", km, "Kilometer.")

        else:
            print("Das Auto wurde noch nicht verkauft!")

    def sell_car(self, buyer):

        if self.sold:

            print(self.brand, self.model, "ist bereits verkauft!")

        else:

            self.sold = True
            self.owner = buyer

            print(self.brand, self.model, "wurde an", buyer, "verkauft!")

    def discount(self, percent):

        discount_amount = self.price * (percent / 100)

        self.price -= discount_amount

        print(percent, "% Rabatt wurden angewendet!")

    def repair(self):

        print(self.brand, self.model, "wird repariert.")

        repair_cost = 500

        self.price += repair_cost

        print("Der Wert steigt um", repair_cost, "Euro.")



cars = [
    Car("Audi", "A4", 2020, 25000),
    Car("BMW", "M3", 2022, 55000),
    Car("Tesla", "Model 3", 2023, 45000)
]


while True:

    print("\n===== AUTOHAUS =====")
    print("1 = Autos anzeigen")
    print("2 = Auto verkaufen")
    print("3 = Auto fahren")
    print("4 = Rabatt geben")
    print("5 = Auto reparieren")
    print("6 = Spiel beenden")

    choice = input("Deine Auswahl: ")


    if choice == "1":

        for car in cars:
            car.show_info()


    elif choice == "2":

        car_index = int(input("Welches Auto verkaufen? (0-2): "))
        buyer = input("Name des Käufers: ")

        cars[car_index].sell_car(buyer)


    elif choice == "3":

        car_index = int(input("Welches Auto fahren? (0-2): "))
        km = int(input("Wie viele Kilometer?: "))

        cars[car_index].drive(km)


    elif choice == "4":

        car_index = int(input("Welches Auto Rabatt geben? (0-2): "))
        percent = int(input("Wie viel Prozent Rabatt?: "))

        cars[car_index].discount(percent)


    elif choice == "5":

        car_index = int(input("Welches Auto reparieren? (0-2): "))

        cars[car_index].repair()


    elif choice == "6":

        print("Programm beendet.")
        break


    else:
        print("Ungültige Eingabe!")
