lista = []

for i in range (6):
    palabras = input("dime una palabra: ").strip().lower()
    lista.append(palabras)
    lista.sort()
    
print(lista)

word = input("dime una palabra para verificvar si esta en la lista: ").strip().lower()
if word in lista:
    print("si esta en la lista")
    print("aparece en la lista este numero de veces: ", lista.count(word))
else:
    print("no esta en la lista")
    
lista2 = []

for palabras in lista:
    if len(palabras) > 4:
        lista2.append(palabras)
    
lista2.reverse()

print("a continuacion se mostrara la lista2 con las palbras que contengan mas de 4 caracteres")
print(lista2)