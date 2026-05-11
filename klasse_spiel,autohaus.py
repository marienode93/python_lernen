class Car:

    dealership_name = "Python Autohaus"
    next_id = 1000

    def __init__(
        self,
        brand,
        model,
        year,
        price
    ):

        self.validate_text(
            brand,
            "Marke"
        )

        self.validate_text(
            model,
            "Modell"
        )


        if not isinstance(year, int):

            raise ValueError(
                "Baujahr muss eine ganze Zahl sein!"
            )

        current_year = 2026

        if year < 1886 or year > current_year:

            raise ValueError(
                "Ungültiges Baujahr!"
            )


        self.validate_number(
            price,
            "Preis"
        )

        if price <= 0:

            raise ValueError(
                "Preis muss größer als 0 sein!"
            )


        self.id = Car.next_id
        Car.next_id += 1


        self.brand = (
            brand
            .strip()
            .title()
        )

        self.model = (
            model
            .strip()
            .title()
        )

        self.year = year
        self.price = float(price)

        self.sold = False
        self.owner = None

        self.kilometers = 0.0


        self.service_history = {
            "inspection": False,
            "oil_change": False
        }

    @property
    def specs(self):

        return (
            self.brand,
            self.model,
            self.year
        )

    def __str__(self):

        status = (
            "Verkauft"
            if self.sold
            else "Verfügbar"
        )

        return (
            f"[ID: {self.id}] "
            f"{self.brand} "
            f"{self.model} "
            f"({self.year}) | "
            f"{self.price:.2f} Euro | "
            f"{status}"
        )

    @staticmethod
    def validate_text(
        text,
        field_name
    ):

        if not isinstance(text, str):

            raise ValueError(
                f"{field_name} muss Text sein!"
            )

        if not text.strip():

            raise ValueError(
                f"{field_name} darf nicht leer sein!"
            )

    @staticmethod
    def validate_number(
        value,
        field_name
    ):

        if isinstance(value, bool):

            raise ValueError(
                f"{field_name} darf "
                f"nicht True/False sein!"
            )

        if not isinstance(
            value,
            (int, float)
        ):

            raise ValueError(
                f"{field_name} muss "
                f"eine Zahl sein!"
            )

    def extra_info(self):

        return ""

    def show_info(self):

        print("\n========== AUTO-INFOS ==========")

        print(f"ID: {self.id}")

        print(
            f"Marke: {self.brand}"
        )

        print(
            f"Modell: {self.model}"
        )

        print(
            f"Baujahr: {self.year}"
        )

        print(
            f"Preis: "
            f"{self.price:.2f} Euro"
        )

        print(
            f"Kilometer: "
            f"{self.kilometers:.1f} km"
        )

        print(
            f"Status: "
            f"{'Verkauft' if self.sold else 'Verfügbar'}"
        )

        print(
            f"Besitzer: "
            f"{self.owner if self.owner else 'Kein Besitzer'}"
        )

        print(
            f"Spezifikationen: "
            f"{self.specs}"
        )

        extra = self.extra_info()

        if extra:

            print(extra)

        print("\nServicehistorie:")

        for service, done in (
            self.service_history.items()
        ):

            status = (
                "Ja"
                if done
                else "Nein"
            )

            print(
                f"- {service}: {status}"
            )

        print("================================")

    def sell_car(
        self,
        buyer
    ):

        if self.sold:

            raise ValueError(
                "Auto wurde bereits verkauft!"
            )

        self.validate_text(
            buyer,
            "Käufer"
        )

        self.sold = True

        self.owner = (
            buyer
            .strip()
            .title()
        )

        print(
            f"{self.brand} "
            f"{self.model} "
            f"wurde an "
            f"{self.owner} verkauft!"
        )

    def drive(
        self,
        km,
        driver
    ):

        self.validate_number(
            km,
            "Kilometer"
        )

        if km <= 0:

            raise ValueError(
                "Kilometer müssen "
                "größer als 0 sein!"
            )

        if km > 2000:

            raise ValueError(
                "Unrealistische Strecke!"
            )

        self.validate_text(
            driver,
            "Fahrer"
        )

        driver = (
            driver
            .strip()
            .title()
        )

        if self.sold:

            if driver != self.owner:

                raise ValueError(
                    "Nur der Besitzer "
                    "darf fahren!"
                )

            print(
                f"{driver} fährt "
                f"{km:.1f} km "
                f"mit dem "
                f"{self.brand} "
                f"{self.model}."
            )

        else:

            print(
                f"{driver} macht eine "
                f"Probefahrt mit dem "
                f"{self.brand} "
                f"{self.model} "
                f"({km:.1f} km)."
            )

        self.kilometers += float(km)

        print(
            f"Neuer Kilometerstand: "
            f"{self.kilometers:.1f} km"
        )

    def discount(
        self,
        percent
    ):

        self.validate_number(
            percent,
            "Rabatt"
        )

        if percent <= 0 or percent >= 100:

            raise ValueError(
                "Rabatt muss zwischen "
                "1 und 99 liegen!"
            )

        old_price = self.price

        self.price *= (
            1 - percent / 100
        )

        print(
            f"Alter Preis: "
            f"{old_price:.2f} Euro"
        )

        print(
            f"Neuer Preis: "
            f"{self.price:.2f} Euro"
        )

    def add_service(
        self,
        service_name
    ):

        self.validate_text(
            service_name,
            "Service"
        )

        service_name = (
            service_name
            .strip()
            .lower()
        )

        self.service_history[
            service_name
        ] = True

        print(
            f"Service "
            f"'{service_name}' "
            f"hinzugefügt."
        )

class ElectricCar(Car):

    def __init__(
        self,
        brand,
        model,
        year,
        price,
        battery_capacity
    ):

        super().__init__(
            brand,
            model,
            year,
            price
        )

        self.validate_number(
            battery_capacity,
            "Batteriekapazität"
        )

        if battery_capacity <= 0:

            raise ValueError(
                "Batterie muss "
                "größer als 0 sein!"
            )

        self.battery_capacity = (
            float(battery_capacity)
        )

        self.battery_level = 100.0

    def charge(self):

        self.battery_level = 100.0

        print(
            f"{self.brand} "
            f"{self.model} "
            f"wurde geladen."
        )

    def drive(
        self,
        km,
        driver
    ):

        battery_usage = (
            km * 0.15
        )

        if battery_usage > self.battery_level:

            raise ValueError(
                "Nicht genug Akku!"
            )

        super().drive(
            km,
            driver
        )

        self.battery_level -= (
            battery_usage
        )

        print(
            f"Akkustand: "
            f"{self.battery_level:.1f}%"
        )

    def extra_info(self):

        return (
            f"Batterie: "
            f"{self.battery_capacity:.1f} kWh\n"
            f"Akkustand: "
            f"{self.battery_level:.1f}%"
        )

class SportsCar(Car):

    def __init__(
        self,
        brand,
        model,
        year,
        price,
        horsepower
    ):

        super().__init__(
            brand,
            model,
            year,
            price
        )

        self.validate_number(
            horsepower,
            "PS"
        )

        if horsepower <= 0:

            raise ValueError(
                "PS müssen größer "
                "als 0 sein!"
            )

        self.horsepower = int(
            horsepower
        )

    def turbo_mode(self):

        print(
            f"{self.brand} "
            f"{self.model} "
            f"aktiviert Turbo-Modus!"
        )

    def extra_info(self):

        return (
            f"Leistung: "
            f"{self.horsepower} PS"
        )

def get_car_by_id(car_database):

    try:

        car_id = int(
            input("Auto-ID: ")
        )

    except ValueError:

        print(
            "Ungültige ID!"
        )

        return None

    return car_database.get(car_id)

car1 = ElectricCar(
    "Tesla",
    "Model S",
    2025,
    95000,
    100
)

car2 = SportsCar(
    "Ferrari",
    "488 GTB",
    2022,
    280000,
    670
)

car3 = ElectricCar(
    "Bmw",
    "I4",
    2024,
    72000,
    85
)

car_database = {
    car1.id: car1,
    car2.id: car2,
    car3.id: car3
}

while True:

    print("\n========== AUTOHAUS ==========")

    print("1 - Auto erstellen")
    print("2 - Alle Autos anzeigen")
    print("3 - Auto-Infos")
    print("4 - Auto verkaufen")
    print("5 - Auto fahren")
    print("6 - Rabatt geben")
    print("7 - Service hinzufügen")
    print("8 - Elektroauto laden")
    print("9 - Turbo-Modus")
    print("0 - Programm beenden")

    choice = input(
        "\nAuswahl: "
    ).strip()

    try:

        if choice == "1":

            print("\n1 - Elektroauto")
            print("2 - Sportwagen")

            car_type = input(
                "Typ wählen: "
            ).strip()

            brand = input(
                "Marke: "
            )

            model = input(
                "Modell: "
            )

            year = int(
                input("Baujahr: ")
            )

            price = float(
                input("Preis: ")
            )

            if car_type == "1":

                battery = float(
                    input(
                        "Batteriekapazität: "
                    )
                )

                car = ElectricCar(
                    brand,
                    model,
                    year,
                    price,
                    battery
                )

            elif car_type == "2":

                horsepower = int(
                    input("PS: ")
                )

                car = SportsCar(
                    brand,
                    model,
                    year,
                    price,
                    horsepower
                )

            else:

                print(
                    "Ungültiger Typ!"
                )

                continue

            car_database[
                car.id
            ] = car

            print(
                f"Auto erstellt! "
                f"ID: {car.id}"
            )

        elif choice == "2":

            print(
                "\n===== AUTOS ====="
            )

            for car in (
                car_database.values()
            ):

                print(car)

        elif choice == "3":

            car = get_car_by_id(
                car_database
            )

            if car:

                car.show_info()

            else:

                print(
                    "Auto nicht gefunden!"
                )

        elif choice == "4":

            car = get_car_by_id(
                car_database
            )

            if car:

                buyer = input(
                    "Käufername: "
                )

                car.sell_car(
                    buyer
                )

            else:

                print(
                    "Auto nicht gefunden!"
                )

        elif choice == "5":

            car = get_car_by_id(
                car_database
            )

            if car:

                driver = input(
                    "Fahrername: "
                )

                km = float(
                    input(
                        "Kilometer: "
                    )
                )

                car.drive(
                    km,
                    driver
                )

            else:

                print(
                    "Auto nicht gefunden!"
                )

        elif choice == "6":

            car = get_car_by_id(
                car_database
            )

            if car:

                percent = float(
                    input(
                        "Rabatt in %: "
                    )
                )

                car.discount(
                    percent
                )

            else:

                print(
                    "Auto nicht gefunden!"
                )

        elif choice == "7":

            car = get_car_by_id(
                car_database
            )

            if car:

                service = input(
                    "Service-Name: "
                )

                car.add_service(
                    service
                )

            else:

                print(
                    "Auto nicht gefunden!"
                )

        elif choice == "8":

            car = get_car_by_id(
                car_database
            )

            if isinstance(
                car,
                ElectricCar
            ):

                car.charge()

            else:

                print(
                    "Das ist kein Elektroauto!"
                )

        elif choice == "9":

            car = get_car_by_id(
                car_database
            )

            if isinstance(
                car,
                SportsCar
            ):

                car.turbo_mode()

            else:

                print(
                    "Das ist kein Sportwagen!"
                )

        elif choice == "0":

            print(
                "Programm beendet."
            )

            break

        else:

            print(
                "Ungültige Auswahl!"
            )

    except ValueError as error:

        print(
            f"\nFehler: {error}"
        )

    except Exception as error:

        print(
            f"\nUnerwarteter Fehler: {error}"
        )
