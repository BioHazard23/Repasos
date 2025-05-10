#Ejercicio 1
def saludo():
    nombre = input("Ingresa tu nombre: ")    
    print (f"Hola {nombre} como estas")

#Ejercicio 2
def suma():
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    resultado = num1+num2
    print(resultado)

#Ejercicio 3
def par_impar ():
    numero = int(input("Digite un numero: "))

    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

#Ejercicio 4
def mayor_edad():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad") 

#Ejercicio 5
def grados_fahrenheit (celsius):
    print("Convertir de grados Celsius a Fahrenheit.")

    celsius = float(input("Temperatura en °C: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} °C = {fahrenheit:.2f}")

#Ejercicio 6
def area_triangulo (base, altura):
    base = float(input("Base del triangulo: "))
    altura = float(input("Altura del triangulo: "))
    area = (base * altura) / 2
    print(f"El area del triangulo con base {base:.2f} y altura {altura:.2f} es: {area:.2f}")
    return area

#Ejercicio 7
lista_numeros = []
def mayor_lista ():
    agregar = input("Ingresa una secuencia de numeros separadas por comas: ")
    lista_numeros.append (agregar)
    mayor = max(lista_numeros)
    print(mayor)

#Ejercicio 8
def contar_letras():
    palabra = input("Ingresa una palabra: ")
    cantidad = len(palabra)
    print(f"Hay {cantidad} de letras en la palabra {palabra}")
