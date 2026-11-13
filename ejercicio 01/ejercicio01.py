t = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
p = input("dime un dia de la semana: ").strip().lower()

if p  in t:
    print("está en el índice:", t.index(p))
else:
    print("ese dia no existe")