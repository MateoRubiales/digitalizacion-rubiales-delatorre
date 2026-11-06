compra = ["pan", "leche", "huevos"]

pedido = input("que deseas (principio)?: ")
pedido2 = input("que deseas (final)?: ")

compra.insert(0, pedido)
compra.append(pedido2)

print(compra)

quitar = input("que producto deseas eliminar?: ")
compra.remove(quitar)

print(compra)

print("se va a eliminar el ultimo producto: ")
compra.pop()

print(compra)
