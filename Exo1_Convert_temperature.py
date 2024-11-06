while True:
    choix = input("""
Que voulez vous faire?
1: Celsius en Fahrenheit
2: Fahrenheit en Celsius
3: Quitter  
>                                                              
""")
    
    if choix =="3":
        print("Vous avez choisi de quitter\nAurevoir.")
        break

    elif choix =="1":
        temperature_en_C = float(input("Veuillez saisir la valeur de la température en °C: "))
        fraenheit = temperature_en_C * 9/5 +32
        print("La température en °F:",fraenheit)

    elif choix =="2":
        temperature_en_F = float(input("Veuillez saisir la valeur de la température en °F: "))
        celsius = (temperature_en_F - 32) * 5/9
        print("La température en °F:",celsius)
    else:
        print("Je n'ai pas compris votre choix")
