import state

def grot():
    from locaties.pad import pad
    from locaties.eindgebied import eindgebied

    print("GROT")
    print("In de grot hoor je water druppen. Je ziet een KOMPAS op de grond.")

    
    if state.kaartGevonden:
        print("Verderop is een POORT met een slot.")
        print("Opties: KOMPAS, POORT, TERUG")
    else:
        print("Je ziet iets donkers achterin, maar je weet niet wat…")
        print("Opties: KOMPAS, TERUG")

    antwoord = input("> ")

    if antwoord == "KOMPAS":
        if not state.kompasGevonden:
            state.kompasGevonden = True
            print("Je raapt het kompas op. Het wijst ergens naartoe…")
        else:
            print("Je hebt het kompas al.")
        grot()

    elif antwoord == "POORT":
    
        if not state.kaartGevonden:
            print("Je ziet hier geen poort… Misschien mis je iets.")
            grot()
        else:
            
            if state.mesGepakt:
                print("Je steekt met het mes tussen het slot en wrikt het open.")
                state.poortOpen = True
                eindgebied()
            else:
                print("De poort zit vast. Misschien mis je gereedschap…")
                grot()

    elif antwoord == "TERUG":
        pad()

    else:
        grot()
