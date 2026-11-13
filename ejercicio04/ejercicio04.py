Marca = float(input("que nota tienes en Marca?:"))

Redes = float(input("que nota tienes en Redes?:"))

IPE = float(input("que nota tienes en IPE?:"))

media = (Marca + Redes + IPE) / 3

print(f"tienes una media de {media}")

if media == 10:

    print("matricula de honor")

elif media >= 9:

    print("sobresaliente")

elif media >= 7:

    print("notable")

elif media >= 5:

    print("aprobado")

elif media < 5 and media > 0:

    print("suspenso")

else:

    print("ERROR")

    #te pongo aqui un textito.