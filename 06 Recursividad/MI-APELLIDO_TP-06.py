# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario.
 
def factorial (num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial (num -1)
numero = int(input("Ingrese un numero: "))    
for i in range(1, numero +1):
    print(f"El factorial de {i} es: {factorial(i)}")

# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 
    
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
for i in range(1, (int(input("Ingrese la posición: ")) + 1)):
    print(fibonacci(i))

# Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base,exponente-1)

B = int(input("Ingrese la base: "))
P = int(input("Ingrese la potencia: "))

print(f"El resultado es: {potencia(B,P)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.


def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
    

def es_palindromo(palabra: str) -> bool:
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

# 6)Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
# 7)Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

def contar_bloques(n: int) -> int:
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero: int, digito: int) -> int:
    if numero == 0:
        return 1 if digito == 0 else 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)
