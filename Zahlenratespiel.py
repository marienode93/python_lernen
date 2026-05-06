def play_game():
    print("Willkommen zum Zahlenratespiel!")

    level = input("Wähle Schwierigkeit (leicht/mittel/schwer): ")

    if level == "leicht":
        max_number = 20
        max_attempts = 10
    elif level == "mittel":
        max_number = 50
        max_attempts = 10
    else:
        max_number = 100
        max_attempts = 10

    import random
    secret_number = random.randint(1, max_number)

    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Rate eine Zahl zwischen 1 und {max_number}: "))
            attempts += 1

            if guess < secret_number:
                print(f"Dein Tipp ({guess}) ist zu niedrig.")
            elif guess > secret_number:
                print(f"Dein Tipp ({guess}) ist zu hoch.")
            else:
                print(f"Richtig! Du hast {attempts} Versuche gebraucht.")
                return

        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
            continue

    print(f"Leider verloren. Die richtige Zahl war {secret_number}.")

play_game()
