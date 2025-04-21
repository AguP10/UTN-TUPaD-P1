# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

#Definición de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

#Definición de funciones
def saludar_ususario(nombre):
    return(f"Hola, {nombre}!")

#Programa principal
usuario = input("Ingrese su nombre: ")
saludo = saludar_ususario(usuario)
print(saludo)


# 3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.

#Definición de funciones
def información_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa principal
nombre = input("Ingrese su nombre: ")
apelldio = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugrar de residencia: ")

información_personal(nombre, apelldio, edad, residencia)


#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

#Definición de funciones
def calcular_area_circulo(radio):
    return 3.1416 * radio **2
def calcular_perímetro_círculo(radio):
    return 2*3.1416*radio

#Programa principal
radio = int(input("Ingrese el radio: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perímetro_círculo(radio)
print(f"El area es {area} y el perimetro es {perimetro}")  


#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

#Definición de funciones
def segundos_a_horas(segundos):
    print((segundos/60)/60)

#Programa principal
segundos = int(input("Ingrese los segundos: "))

segundos_a_horas(segundos)


#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
#  ción.

# Definicion de funciones
def tabla_demultiplicar(numero):
    for i in range(1,11):
        print(f"{i} * {numero} = {i*numero}")

#Programa principal
numero = int(input("Ingrese el número: "))
tabla_demultiplicar(numero)


#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

#Definicion de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a/b
    return (suma, resta, multiplicacion, division)
#Programa principal
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
resultados = operaciones_basicas(a,b)
print("Resultados:")
print(f"Suma = {resultados[0]}")
print(f"Resta = {resultados[1]}")
print(f"Multiplicación = {resultados[2]}")
print(f"División = {resultados[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

#Definir funciones
def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    return imc
#Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
resultados = calcular_imc(peso,altura)
print(f"Su IMC es:{resultados}")


#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

#Definir funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
#Programa principal
temp_cel = float(input("Ingrese los grados celcius: "))
temp_f = celsius_a_fahrenheit(temp_cel)
print(f"La temeperatura en fahrenheit es: {temp_f}") 


#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

#Definir funciones
def calcular_promedio(a, b, c):
    prom = (a+b+c)/3
    return prom
#Programa principal
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = calcular_promedio(num1,num2,num3)
print(f"El promedio es: {promedio}")


