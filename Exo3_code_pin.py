while True:
    codePin= input("Veuillez saisir le code PIN: ")
 
    valide = False
    if codePin.isdigit() and 4 <=len(codePin)<=6:
        for cara in codePin:
            if int(cara)%2== 0:
                valide = True 
                break    
    if valide:
        print("Pin Valide")
        break
    else:
        print("Pin invalide")
