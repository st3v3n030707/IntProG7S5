import datetime as dt

fecha_inicio_sesion = input("El ultimo inicio de sesion en formato YYYY-MM-DD: ")
fecha_inicio_sesion = dt.datatime.strptime(fecha_inicio_sesion, "%Y-%m-%d")

fecha_actual = dt.datatime.now()

contar_dias = (fecha_actual- fecha_inicio_sesion).days
if contar_dias > 30:
    print("Inactivo por mas de 30 dias.")
else: 
    print("Estamos bien.")