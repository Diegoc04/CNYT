import math
#suma de dos numeros complejos
def Suma(X,Y):
    Suma = X + Y
    A = print(f"La suma de los numeros complejos introducidos es {Suma}")
    return A

#resta de dos numeros complejos
def Resta(X,Y):
    Resta = X - Y
    A = print(f"La resta de los numeros complejos introducidos es {Resta}")
    return A

#multiplicacion de dos numeros complejos
def Multiplicacion(X,Y):
    Multiplicacion = X * Y
    A = print(f"La multiplicacion de los numeros complejos introducidos es {Multiplicacion}")
    return A
#division de dos numeros complejos
def Division(X,Y):
    Division = X / Y
    A = print(f"La division de los numeros complejos introducidos es {Division}")
    return A


#Modulo de un numero complejo
def Modulo(Z):
    a = Z.real
    b = Z.imag
    t = math.sqrt(a**2 + b**2)
    A = print(f"El modulo del numero complejo introducido es {t}")
    return A

#Conjugado de un numero complejo
def Conjugado(Z):
    c = Z.imag
    c = c*-1
    A = print(f"El conjugado del numero complejo introducido es {Z.real} + ({c})j")
    return A

#Conversión entre representaciones polar y cartesiano

#cartesiano a polar
def Car_Pol(Z):
    a = Z.real
    b = Z.imag
    r = math.sqrt(a**2 + b**2)
    θ = math.atan(b/a)
    θ = θ * 180/3.14
    A = print(f"La representacion polar del numero complejo introducido es {r}[{θ}]°")
    return A
"""""
#polar a cartesiano ///
a = r * math.cos(θ)
b = r * math.sin(θ)

print(f"{a} + {b}j")
"""""
#fase de un numero complejo
def Fase(Z):
    a = Z.real
    b = Z.imag
    r = math.sqrt(a**2 + b**2)
    θ = math.atan(b/a)
    θ = θ * 180/3.14
    A = print(f"La fase del numero complejo introducido es {θ}")
    return A

def main():
    X = input("introduzca el primer numero complejo en la forma (a+bj): ")
    Y = input("introduzca el segundo numero complejo en la forma (a+bj): ")
    X = complex(X)
    Y = complex(Y)
    result= Suma(X,Y)
    result= Resta(X,Y)
    result= Multiplicacion(X,Y)
    result= Division(X,Y)
    Z = input("introduzca el tercer numero complejo en la forma (a+bj): ")
    Z = complex(Z)
    result= Modulo(Z)
    result= Conjugado(Z)
    result= Car_Pol(Z)
    result= Fase(Z)
    

main()
"""""
X = input("introduzca el primer numero complejo en la forma (a + bi): ")
Y = input("introduzca el segundo numero complejo en la forma (a + bi): ")
"""""