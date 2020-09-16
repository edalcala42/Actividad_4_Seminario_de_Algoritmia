print("Hola, mundo!")

def area_cuadrado(lado = int)->int:
    return lado * lado

def area_triangulo(base = int, altura = int)->int:
    return (base*altura)/2

def area_circulo(radio = float)->float:
    return (radio*radio)*3.1416

def signo_zodiacal(dia, mes):
    if mes == "1":
        if dia < "21":
            print("Eres Capricornio")
        else:
            print("Eres Acuario")
    elif mes == "2":
        if dia < "20":
            print("Eres Acuario")
        else:
            print("Eres Piscis")
    elif mes == "3":
        if dia < "21":
            print("Eres Piscis")
        else:
            print("Eres Aries")
    elif mes == "4":
        if dia < "20":
            print("Eres Aries")
        else:
            print("Eres Tauro")    
    elif mes == "5":
        if dia < "21":
            print("Eres Tauro")
        else:
            print("Eres Géminis")
    elif mes == "6":
        if dia < "22":
            print("Eres Géminis")
        else:
            print("Eres Cáncer")
    elif mes == "7":
        if dia < "24":
            print("Eres Cáncer")
        else:
            print("Eres Leo")
    elif mes == "8":
        if dia < "24":
            print("Eres Leo")
        else:
            print("Eres Virgo")
    elif mes == "9":
        if dia < "23":
            print("Eres Virgo")
        else:
            print("Eres Libra")
    elif mes == "10":
        if dia < "23":
            print("Eres Libra")
        else:
            print("Eres Escorpión")
    elif mes == "11":
        if dia < "23":
            print("Eres Escorpión")
        else:
            print("Eres Sagitario")
    elif mes == "12":
        if dia < "23":
            print("Eres Sagitario")
        else:
            print("Eres Acuario")
    else:
        print("Mes no valido")

signo_zodiacal(input("Dia: "),input("Mes: "))

def determinar_factorial(numero)->int:
    total = 1
    i = numero
    while i > 0:
        total *= i
        i = i-1

    return total

print("Factorial de 3: ", determinar_factorial(5))

def calcular_e(limite):
    n = 0
    e = 0
    while n < limite:
	    e += 1/determinar_factorial(n)
	    n = n + 1
    print("El valor de e con 3 es: ",e)

calcular_e(3)