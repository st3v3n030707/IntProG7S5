rango_inicial = int(input("Escribe el inicio del rango: "))
rango_final = int(input("Escribe el final del rango: "))
numero = int(input("Dime un numero: "))
if(rango_inicial < rango_final):
    numero = int(input("Dime un numero: "))
    if(numero >= rango_inicial and numero <= rango_final):
        print("El numero esta dentro del rango")
    else:
        print("El numero esta fuera del rango")
else:
    print("El rango inicial no puede se mayor que el rango final")    
