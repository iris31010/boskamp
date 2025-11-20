
def start():
    print("BOSKAMP")
    print("Je staat op een verlaten BOSKAMPPLEIN met een PAD en een SCHUUR.")
    print("Wil je naar het PAD of naar de SCHUUR?")
    antwoord = input("> ")

    if antwoord == "PAD":
        pad()
    elif antwoord == "SCHUUR":
        schuur()
    else:
        print("Dat kan niet.")
        start()


def schuur():
    global mesGepakt
    print("SCHUUR")
    print("Je komt in een donkere schuur. Er ligt een MES op tafel.")
    print("Je kunt het MES pakken of TERUG naar het plein.")
    antwoord = input("> ")

    if antwoord == "MES":
        if not mesGepakt:
            mesGepakt = True
            print("Je pakt het mes. Handig!")
        else:
            print("Je hebt het mes al.")
        schuur()

    elif antwoord == "TERUG":
        start()
    else:
        schuur()


def pad():
    print("BOSPAD")
    print("Je loopt een bospaadje op. Je ziet een UITKIJKTOREN en een GROT.")
    print("Waar ga je heen? UITKIJKTOREN of GROT?")
    antwoord = input("> ")

    if antwoord == "UITKIJKTOREN":
        uitkijktoren()
    elif antwoord == "GROT":
        grot()
    else:
        pad()


def uitkijktoren():
    global kaartGevonden
    print("UITKIJKTOREN")
    print("Boven in de toren ligt een KAART.")
    print("Je kunt KAART pakken of TERUG gaan.")
    antwoord = input("> ")

    if antwoord == "KAART":
        if not kaartGevonden:
            kaartGevonden = True
            print("Je pakt de kaart. Hier staat een geheime poort op!")
        else:
            print("Je hebt de kaart al.")
        uitkijktoren()

    elif antwoord == "TERUG":
        pad()
    else:
        uitkijktoren()


def grot():
    global kompasGevonden, poortOpen
    print("GROT")
    print("In de grot hoor je water druppen. Je ziet een KOMPAS op de grond.")
    print("Verderop is een POORT met een slot.")
    print("Opties: KOMPAS, POORT, TERUG")
    antwoord = input("> ")

    if antwoord == "KOMPAS":
        if not kompasGevonden:
            kompasGevonden = True
            print("Je raapt het kompas op. Het wijst ergens naartoe…")
        else:
            print("Je hebt het kompas al.")
        grot()

    elif antwoord == "POORT":
        if kaartGevonden and mesGepakt:
            print("Je steekt met het mes tussen het slot en wrikt het open.")
            poortOpen = True
            eindgebied()
        else:
            print("De poort zit vast. Misschien mis je gereedschap…")
            grot()

    elif antwoord == "TERUG":
        pad()

    else:
        grot()


def eindgebied():
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
    print("EINDE VAN HET VERHAAL")
    if mesGepakt and kaartGevonden and kompasGevonden:
        print("Je gebruikt al je gevonden spullen en ontdekt een verborgen hut.")
        print("Je ontsnapt veilig uit het boskamp. Goed gedaan. Keer nu terug naar de START!")
    elif antwoord == "START":
        start()
    else:
        print("Je hebt het einde bereikt, maar mist belangrijke spullen…")
        print("Het kamp blijft een mysterie voor je. Keer nu terug naar START en probeer het opnieuw.")
        start()



start()
