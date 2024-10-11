import os

def operaciones(num1, operador, num2):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Error: No se puede dividir por cero"
    else:
        return "Error: Opción inválida"

    operacion = f"{num1} {operador} {num2} = {resultado}"
    guardar_en_archivo(operacion)
    return operacion

def guardar_en_archivo(operacion):
    with open("historial.txt", "a") as archivo:
        archivo.write(operacion + "\n")

def mostrar_historial():
    try:
        with open("historial.txt", "r") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return "No hay historial disponible."

def calculadora():
    while True:
        print("\n1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Ver historial")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
    
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except:
                print("Error: Ingrese un número válido.")
            
            if opcion == '1':
                operador = '+'
            elif opcion == '2':
                operador = '-'
            elif opcion == '3':
                operador = '*'
            elif opcion == '4':
                operador = '/'
            
            print(operaciones(num1, operador, num2))
        elif opcion == '5':
            print("\nHistorial de operaciones:")
            print(mostrar_historial())
        elif opcion == '6':
            print("Saliendo de la calculadora")
            break
        else:
            print("Opción invalida. Intente de nuevo.")

