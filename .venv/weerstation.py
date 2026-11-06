
def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    totaal = 0

    for dag in range(1, 8):

        while True:
            invoer = input(f"Wat is op dag {dag} de temperatuur[C]: ")
            if invoer == "":
                print("bye")
                return
            try:
                temp_celcius = float(invoer)
                break
            except ValueError:
                print("Voer een geldig getal in.")

        while True:
            invoer = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ")
            if invoer == "":
                print("bye")
                return
            try:
                windsnelheid = float(invoer)
                if windsnelheid >= 0:
                    break
                print("Voer een geldige windsnelheid in.")
            except ValueError:
                print("Voer een geldig getal in.")

        while True:
            invoer = input(f"Wat is op dag {dag} de vochtigheid[%]: ")
            if invoer == "":
                print("bye")
                return
            try:
                luchtvochtigheid = int(invoer)
                if 0 <= luchtvochtigheid <= 100:
                    break
                print("Voer een getal tussen 0 en 100 in.")
            except ValueError:
                print("Voer een geheel getal in.")

        fahrenheit = Fahrenheit(temp_celcius)
        rapport = weerrapport(temp_celcius, windsnelheid, luchtvochtigheid)

        totaal = totaal + temp_celcius
        gemiddelde = totaal / dag

        print(f"Het is {temp_celcius:.1f}C ({fahrenheit:.1f}F)")
        print(rapport)
        print(f"Gem. temp tot nu toe is {gemiddelde:.1f}")
        print("======================================")


if __name__ == "__main__":
    weerstation()
