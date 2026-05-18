print("=== Super Taschenrechner ===")

while True:

    print("\nVerfügbare Rechenarten:")
    print("+  Addition")
    print("-  Subtraktion")
    print("*  Multiplikation")
    print("/  Division")
    print("%  Modulo")
    print("** Potenz")
    print("q  Beenden")

    operator = input("\nWähle eine Rechenart: ")

    # Programm beenden
    if operator == "q":
        print("Programm beendet.")
        break

    # Prüfen ob Operator gültig ist
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        print("Ungültige Rechenart!")
        continue

    # Fehlerbehandlung für Eingaben
    try:
        zahl1 = float(input("Erste Zahl: "))
        zahl2 = float(input("Zweite Zahl: "))

    except ValueError:
        print("Fehler: Bitte nur Zahlen eingeben!")
        continue

    # Rechnungen
    if operator == "+":
        ergebnis = zahl1 + zahl2

    elif operator == "-":
        ergebnis = zahl1 - zahl2

    elif operator == "*":
        ergebnis = zahl1 * zahl2

    elif operator == "/":

        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            print("Division durch 0 ist nicht erlaubt!")
            continue

    elif operator == "%":

        if zahl2 != 0:
            ergebnis = zahl1 % zahl2
        else:
            print("Modulo mit 0 ist nicht erlaubt!")
            continue

    elif operator == "**":
        ergebnis = zahl1 ** zahl2

    # Ergebnis ausgeben
    print(f"\nErgebnis: {zahl1} {operator} {zahl2} = {ergebnis}")
