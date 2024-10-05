def operaciones(num1, operador, num2, historial):
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
        return "Error: Opcion no valida"

    operacion = f"{num1} {operador} {num2} = {resultado}"
    historial.append(operacion)
    return operacion

def mostrar_historial(historial):
    return "\n".join(historial)

def calculadora():
    historial = []

    while True:
        print("\n1. Realizar operación")
        print("2. Ver historial")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            operador = input("Ingrese el operador (+, -, *, /): ")
            num2 = float(input("Ingrese el segundo número: "))
            print(operaciones(num1, operador, num2, historial))
        elif opcion == '2':
            print("\nHistorial de operaciones:")
            print(mostrar_historial(historial))
        elif opcion == '3':
            print("Saliendo de la calculadora")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora()
