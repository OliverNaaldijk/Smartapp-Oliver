
import json
import urllib.request
import urllib.parse
import ssl
import certifi

from weerstation import weerstation
from smart_app_controller import smart_app_controller


def temperatuur_stad():
    stad = input("Voer een stad in: ")

    if stad == "":
        print("Geen stad ingevoerd.")
        return

    try:
        context = ssl.create_default_context(cafile=certifi.where())

        # Stad zoeken
        url = "https://geocoding-api.open-meteo.com/v1/search?name="
        url += urllib.parse.quote(stad)
        url += "&count=1&language=en&format=json"

        with urllib.request.urlopen(url, context=context) as bestand:
            gegevens = json.load(bestand)

        if "results" not in gegevens:
            print("Stad niet gevonden.")
            return

        latitude = gegevens["results"][0]["latitude"]
        longitude = gegevens["results"][0]["longitude"]
        naam = gegevens["results"][0]["name"]
        land = gegevens["results"][0]["country"]

        # Temperatuur ophalen
        url = "https://api.open-meteo.com/v1/forecast?"
        url += "latitude=" + str(latitude)
        url += "&longitude=" + str(longitude)
        url += "&current=temperature_2m"

        with urllib.request.urlopen(url, context=context) as bestand:
            weer = json.load(bestand)

        temperatuur = weer["current"]["temperature_2m"]

        print("Stad:", naam)
        print("Land:", land)
        print("Temperatuur:", temperatuur, "°C")

    except Exception as fout:
        print("Kan de temperatuur niet ophalen.")
        print("Fout:", fout)


def smart_app_platform():
    while True:
        print("\nSMART APP PLATFORM")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Temperatuur van een stad")
        print("4. Stoppen")

        try:
            keuze = int(input("Maak een keuze: "))

            if keuze == 1:
                weerstation()

            elif keuze == 2:
                smart_app_controller()

            elif keuze == 3:
                temperatuur_stad()

            elif keuze == 4:
                print("Programma gestopt.")
                break

            else:
                print("Ongeldige keuze.")

        except ValueError:
            print("Voer een geldig getal in.")


smart_app_platform()
