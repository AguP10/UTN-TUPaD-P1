#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
edad = int(input("Escriba su edad: "))
if edad > 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad> 0 and edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 12:
    print("Adolescente")
elif edad >=18 and edad < 30:
    print("Adulto joven")
elif edad >= 30:
    print("Adulto mayor")
else:
    print("Valor de edad no válido")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

pasw = input("Ingrese contraseña: ")
long = len(pasw)
if long >= 8 and long <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

from statistics import mode, median, mean
import random
numeros_aleatoreos = [random.randint(1, 100) for i in range (50)]
if mean (numeros_aleatoreos) > median (numeros_aleatoreos) and median (numeros_aleatoreos) > mode(numeros_aleatoreos):
    print("Sesgo positivo")
if mean (numeros_aleatoreos) < median (numeros_aleatoreos) and median (numeros_aleatoreos) < mode (numeros_aleatoreos):
    print("Sesgo negativo")
if mean (numeros_aleatoreos) == median (numeros_aleatoreos) == mode (numeros_aleatoreos):
    print("Sin sesgo")
 
 
 #7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#pantalla.
vocal = ["a", "e", "i", "o", "u"]
frase = input("Ingrese una palabra o frase: ")
if frase[-1] in vocal:
    print(f"{frase}!")
else:
    print(frase)
    
    
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas. 

nombre = input("ingrese su nombre: ")
op = input("Seleccione la opcion 1, 2 o 3: ")
if op == "1":
    nombre = nombre.upper()
    print(nombre)
elif op == "2":
    nombre = nombre.lower()
    print(nombre)
elif op == "3":
    nombre = nombre.title()
    print(nombre)
else:
    print("opcion no valida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla

mg = int(input("Ingrese la magnitud del terremoto: "))
cat = ""
if mg < 3:
    cat = "Muy leve"
    print(cat)
if mg >= 3 and mg < 4:
    cat = "Leve"
    print(cat)
if mg >= 4 and mg < 5:
    cat = "Moderado"
    print(cat)
if mg >= 5 and mg < 6:
    cat = "Fuerte"
    print(cat)
if mg >= 6 and mg < 7:
    cat = "Muy Fuerte"
    print(cat)
if mg >= 7:
    cat = "Extremo"
    print(cat)    

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.

mes = int(input("Ingrese el numero de mes: "))
dia = int(input("Ingrese el dia: "))
hemisferio = input("Ingrese N si esta en el hemisferio norte o S si esta en el sur: "). upper()

if mes < 1 or mes > 12:
    print("Mes inválido")
elif dia < 1 or dia > 31:
    print("Día inválido")
elif hemisferio not in ("N", "S"):
    print("Hemisferio inválido")
else:
    estacion = ""

    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 22):
            estacion = "Verano"
        elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
            estacion = "Otoño"
    else:
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 22):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 23) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
            estacion = "Primavera"

    print(f"La estación es: {estacion}")