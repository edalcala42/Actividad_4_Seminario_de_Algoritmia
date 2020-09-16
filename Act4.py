print("Hola, mundo!")

def area_cuadrado(lado = int)->int:
    return lado * lado

def area_triangulo(base = int, altura = int)->int:
    return (base*altura)/2

def area_circulo(radio = float)->float:
    return (radio*radio)*3.1416

print("El area de un cuadrado con lados de valor 2 es: ", area_cuadrado(2))
print("El area de un triangulo de base 3 y altura 5 es de: ", area_triangulo(3,5))
print("El area de un circulo con radio de 4.5 es de: ", area_circulo(4.5))