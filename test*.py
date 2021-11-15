def trouver_pair(tableau):
    pair=0
    for entier in tableau:
        if entier % 2 == 0:
            pair = pair + 1
           
        else:print('faux')
    return pair

nombre_pair = trouver_pair([1,3,6,4, 8])
print(nombre_pair)