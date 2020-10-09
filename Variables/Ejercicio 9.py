cumple = input("¿cuando es tu cumpleaños? ")
a = int(input("¿En que año naciste? "))
aa = int(input("¿En que año estamos? "))
edad = (aa-a)

if edad >= 18:
    print("El usuario en mayor de edad con ", edad, "años")
else:
    print("el usuario es menor de e edad con ", edad, "años")