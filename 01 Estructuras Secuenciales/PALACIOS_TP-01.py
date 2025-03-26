#Fernando Agustin Palacios

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

nombre = input("Escriba su nombre: ") 
print(f"Hola {nombre}, bienvenido.")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados

nombre = input("Ingrese su nombre: ")
apelldio = input("Ingrese su apelldo: ")
res = input("ingrese su lugar de residencia: ")

print(f"Su nombre es {nombre} {apelldio} y vive en {res}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = int(input("ingrese el radio del circulo: "))
pi = 3.1459
area = pi * radio**2
perimetro = 2 * pi * radio

print(f"El area es:{area}")
print(f"El perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 

seg = int(input("ingrese los segudons: "))
hora = (seg/60)/60
print(f"Equivale a {hora} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese un numero: "))

print(f"{num} x 1 =",(num*1))
print(f"{num} x 2 =",(num*2))
print(f"{num} x 3 =",(num*3))
print(f"{num} x 4 =",(num*4))
print(f"{num} x 5 =",(num*5))
print(f"{num} x 6 =",(num*6))
print(f"{num} x 7 =",(num*7))
print(f"{num} x 8 =",(num*8))
print(f"{num} x 9 =",(num*9))
print(f"{num} x 10 =",(num*10))

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 and num2 != 0:
    print("Suma: ",(num1 + num2))
    print("Divisió: ",(num1 / num2))
    print("Multiplicación: ",(num1 * num2))
    print("Resta: ",(num1 - num2))
else:
    print("El numero debe ser distinto a 0")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

peso = float(input("Por favor indiquie su peso en Kg: "))
altura = float(input("Por favor indique su altura en m: "))
print("Su índice de masa corporal es:",(peso/(altura**2)))

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

tempC = float(input("Ingrese la temperatura en celcius: "))
tempF = (9/5) * tempC + 32
print ("La temperatura en Kelvin es: ", tempF)

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.
num1 = float(input("Ingrese el primer numero: " ))
num2 = float(input("Ingrese el segundo numero: " ))
num3 = float(input("Ingrese el tercer numero: " ))

prom = (num1 + num2 + num3)/3
print("El promedio es:",prom)
