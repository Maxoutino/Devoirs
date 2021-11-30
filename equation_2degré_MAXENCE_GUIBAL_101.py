from math import sqrt

a = float(input("Donnez la valeur a : "))
b = float(input("Donnez la valeur b : "))
c = float(input("Donnez la valeur c : "))

def polynome(a, b, c):
    discriminant = b**2 - 4*a*c
    if a == 0:
        texte = "Ce n'est pas une foncion polynome."
        return texte
    elif discriminant == 0:
        x0 = -b / 2*a
        texte = "La solution est : {" + str(x0) + "}"
        return texte
    elif discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2*a)
        x2 = (-b - sqrt(discriminant)) / (2*a)
        if x1 > x2:
            texte = "Les solutions sont : {" + str(x2) \
                + ";" + str(x1) + "}"
        else :
            texte = "Les solutions sont : {" + str(x1) \
                + ";" + str(x2) + "}"
        return texte
    elif discriminant < 0:
        texte = "Il n'y a pas de solution"
        return texte

print (str(polynome(a, b, c)))

    
