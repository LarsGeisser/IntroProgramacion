num = int(input("ingresa un numero: "))
nombre = str(input("¿Cual es tu nombre? "))
if num % 7 == 0 and (nombre == "leo" or nombre == "pepe"):
    print("acabaste!")
else:
    print("fin")