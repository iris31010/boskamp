def start():
    from locaties.pad import pad
    from locaties.schuur import schuur
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
