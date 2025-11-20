

def schuur():
    import state
    from locaties.start import start
    print("SCHUUR")
    print("Je komt in een donkere schuur. Er ligt een MES op tafel.")
    print("Je kunt het MES pakken of TERUG naar het plein.")
    antwoord = input("> ")

    if antwoord == "MES":
        if not state.mesGepakt:
            state.mesGepakt = True
            print("Je pakt het mes. Handig!")
        else:
            print("Je hebt het mes al.")
        schuur()

    elif antwoord == "TERUG":
        start()
    else:
        schuur()
