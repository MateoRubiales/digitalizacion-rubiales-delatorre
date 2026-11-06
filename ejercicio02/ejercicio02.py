dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
l = list(dias)
dias = tuple(l)

if "martes" in dias:
    print("martes si esta")
else:
    print("martes no esta")
    
if "marzo" in dias:
    print("marzo si esta")
else:
    print("marzo no esta")
