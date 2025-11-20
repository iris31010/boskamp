def eindgebied():
    from locaties.grot import grot
    import state

    print("GEHEIME POORT")
    print("Je hebt de poort geopend. Achter de poort ligt een verlaten kampvuur.")
    print("Je voelt dat je bijna bij de waarheid bent.")
    print("Wil je DOORLOPEN of TERUG?")
    antwoord = input("> ")

    if antwoord == "DOORLOPEN":
        einde()
    elif antwoord == "TERUG":
        grot()
    else:
        eindgebied()


def einde():
    import state
    from locaties.start import start

    print("EINDE VAN HET VERHAAL")

    if state.mesGepakt and state.kaartGevonden and state.kompasGevonden:
        print("Je gebruikt al je gevonden spullen en ontdekt een verborgen hut.")
        print("Je ontsnapt veilig uit het boskamp. Goed gedaan! Keer nu terug naar de START!")
    elif antwoord == "START":
        start()
    else:
        print("Je hebt het einde bereikt, maar mist belangrijke spullen…")
        print("Het kamp blijft een mysterie voor je.")

    print("\nKeer nu terug naar START!")
    start()
