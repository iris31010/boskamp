def uitkijktoren():
    import state
    from locaties.pad import pad

    print("UITKIJKTOREN")
    print("Boven in de toren ligt een KAART.")
    print("Je kunt KAART pakken of TERUG gaan.")
    antwoord = input("> ")

    if antwoord == "KAART":
        if not state.kaartGevonden:
            state.kaartGevonden = True
            print("Je pakt de kaart. Hier staat een geheime poort op!")
        else:
            print("Je hebt de kaart al.")
        uitkijktoren()

    elif antwoord == "TERUG":
        pad()
    else:
        uitkijktoren()
