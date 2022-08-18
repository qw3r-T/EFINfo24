def nullstellen_suche(a, b, c):
    positiv = ((-b + (b*b - 4*a*c)**0.5))/(2*a)
    negativ = ((-b - (b*b - 4*a*c)**0.5))/(2*a)
    return [positiv,negativ]

a = int(input('a > '))
b = int(input('b > '))
c = int(input('c > '))

resultat = nullstellen_suche(a,b,c)
print(resultat)
