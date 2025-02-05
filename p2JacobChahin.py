palabra = input()
suma = 0
vocales = ["a","e","i","o","u"]
for i in palabra:
    if i in vocales:
        suma+=1

print("Numero de vocales ",suma)