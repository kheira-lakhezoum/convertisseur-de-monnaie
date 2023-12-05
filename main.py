from forex_python.converter import CurrencyRates
c = CurrencyRates()
c.get_rates('EUR')
print("Pour 1€ en change, vous obtiendrez : ","\n", c.get_rates('EUR')['USD'],"USD","\n", c.get_rates('EUR')['GBP'],"GBP","\n", c.get_rates('EUR')['JPY'],"JPY","\n", c.get_rates('EUR')['CAD'],"CAD","\n", c.get_rates('EUR')['AUD'],"AUD")

def convertisseur():

    try:
        somme = int(input("Entrez une somme : "))
    except ValueError:
        print("Conversion impossible, veuillez entrer un nombre entier.")
        convertisseur()

    devise = str(input("Entrez une devise: ")).upper()

    c.get_rates('EUR')
    resultat = (c.convert ('EUR', devise, somme))
    print (round(resultat, 2))
    
    with open("historique.txt", "a") as fichier:
        fichier.write(f"Pour {somme} euros, vous obtiendrez : {round(resultat, 2)} {devise}" + "\n")

    exit()
    
convertisseur()