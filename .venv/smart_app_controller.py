
def aantal_dagen(inputFile):
    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()

    return len(regels) - 1


def auto_bereken(inputFile, outputFile):
    with open(inputFile, "r") as bestand:
        regels = bestand.readlines()

    with open(outputFile, "w") as bestand:
        for regel in regels[1:]:
            gegevens = regel.split()

            datum = gegevens[0]
            personen = int(gegevens[1])
            setpoint = float(gegevens[2])
            buiten = float(gegevens[3])
            neerslag = float(gegevens[4])

            verschil = setpoint - buiten

            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            ventilatie = personen + 1
            if ventilatie > 4:
                ventilatie = 4

            if neerslag < 3:
                bewatering = True
            else:
                bewatering = False

            bestand.write(f"{datum};{cv};{ventilatie};{bewatering}\n")


def overwrite_settings(outputFile):
    with open(outputFile, "r") as bestand:
        regels = bestand.readlines()

    datum = input("Welke datum wil je aanpassen? ")

    gevonden = False

    for regel in regels:
        gegevens = regel.strip().split(";")
        if gegevens[0] == datum:
            gevonden = True

    if not gevonden:
        return -1

    print("1. CV ketel")
    print("2. Ventilatie")
    print("3. Bewatering")

    systeem = input("Welk systeem wil je aanpassen? ")

    if systeem not in ["1", "2", "3"]:
        return -3

    invoer = input("Wat is de nieuwe waarde? ")

    try:
        waarde = int(invoer)
    except ValueError:
        return -3

    if systeem == "1":
        if waarde < 0 or waarde > 100:
            return -3

    elif systeem == "2":
        if waarde < 0 or waarde > 4:
            return -3

    elif systeem == "3":
        if waarde != 0 and waarde != 1:
            return -3

    with open(outputFile, "w") as bestand:
        for regel in regels:
            gegevens = regel.strip().split(";")

            if gegevens[0] == datum:
                if systeem == "1":
                    gegevens[1] = str(waarde)

                elif systeem == "2":
                    gegevens[2] = str(waarde)

                elif systeem == "3":
                    if waarde == 1:
                        gegevens[3] = "True"
                    else:
                        gegevens[3] = "False"

            bestand.write(";".join(gegevens) + "\n")

    return 0


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print("\nSMART APP CONTROLLER")
        print("1. Hoeveel dagen zijn er aanwezig?")
        print("2. Autobereken alle actuatoren")
        print("3. Overschrijf een berekende waarde")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            try:
                dagen = aantal_dagen(inputFile)
                print("Aantal dagen:", dagen)
            except FileNotFoundError:
                print("Invoerbestand niet gevonden.")

        elif keuze == "2":
            try:
                auto_bereken(inputFile, outputFile)
                print("Actuatoren berekend en opgeslagen.")
            except FileNotFoundError:
                print("Invoerbestand niet gevonden.")
            except (ValueError, IndexError):
                print("Ongeldige gegevens in het invoerbestand.")

        elif keuze == "3":
            try:
                resultaat = overwrite_settings(outputFile)

                if resultaat == 0:
                    print("Waarde succesvol aangepast.")
                elif resultaat == -1:
                    print("Datum niet gevonden.")
                elif resultaat == -3:
                    print("Ongeldig systeem of ongeldige waarde.")

            except FileNotFoundError:
                print("Uitvoerbestand niet gevonden. Kies eerst optie 2.")

        elif keuze == "4":
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    smart_app_controller()
