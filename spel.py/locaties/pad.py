def pad():
    from locaties.uitkijktoren import uitkijktoren
    from locaties.grot import grot
    from locaties.start import start

    print("BOSPAD")
    print("Je loopt een bospaadje op. Je ziet een UITKIJKTOREN .")
    print("Waar ga je heen? UITKIJKTOREN, GROT of TERUG naar het plein?")
    antwoord = input("> ")

    if antwoord == "UITKIJKTOREN":
        uitkijktoren()
    elif antwoord == "GROT":
        grot()
    else:
        start()
 
