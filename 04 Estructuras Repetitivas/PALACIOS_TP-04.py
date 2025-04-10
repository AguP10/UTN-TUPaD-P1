# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for x in range (101):
    print(x)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 
from math import trunc
dig = 0
num = float(input("Ingrese un numero "))
while num > 0:
    num = num / 10
    num = trunc(num)
    dig += 1
print(dig)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 
suma = 0
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
for x in range(num1+1,num2):
    suma = suma + x
print(suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 
suma = 0
num = int(input("Ingrese un numero: "))
while num != 0:
    suma += num
    num = int(input("Ingrese otro numero: "))    
print("El resultado de la suma es: ", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num = random.randint(0,10)
num2 = 0
num2 = int(input("Adivine el numero: "))
while num2 != num:
    num2 = int(input("Incorrecto. Ingrese otro numero: "))
print("¡Correcto! El numero era ",num)


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.
for i in range (-100,0,2):
    print(abs(i))


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.
num = int(input("Ingrese un numero: "))
suma = 0
if num > 0:
    for i in range(0,num):
        suma += i
print("Resultado: ", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
num = 0
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(0,100):
    num = int(input("Ingrese un numero: "))
    if num >= 0:
        positivos += 1
    else:
        negativos += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Números pares: {pares}\n"
      f"Números impares: {impares}\n"
      f"Números negativos: {negativos}\n"
      f"Números positivos: {positivos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).
suma = 0
media = 0
for i in range (0,100):
    num = int(input("Ingrese un numero: "))
    suma += num
media = suma/100
print("La media es: ", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
num = input("Ingrese un numero: ")
invertido = ""
for i in num:
    invertido = i + invertido
print(int(invertido))

