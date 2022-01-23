"""
PARTE 1
a. Desarrolla un algoritmo que imprima los números del 0 al 100. Adicionalmente debe
imprimirse en la misma línea la palabra buzz en caso de que el número sea par. Sí el
número es múltiplo de 5 debe imprimirse en la misma línea la palabra bazz.
"""

for i in range(0, 101):
    if (i%2)==0:
        if (i%5)==0:
          print(f"{i}  buzz   bazz")
        else:
          print(f"{i}  buzz")
    elif (i%5)==0:
        print(f"{i}  bazz")
    else:
        print(i)


