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
        return "Error: Opción inválida"

    operacion = f"{num1} {operador} {num2} = {resultado}"
    historial.append(operacion)
    return operacion

def mostrar_historial(historial):
    return "\n".join(historial)

def calculadora():
    historial = []

    while True:
        print("\n1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Ver historial")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                operador = '+'
            elif opcion == '2':
                operador = '-'
            elif opcion == '3':
                operador = '*'
            elif opcion == '4':
                operador = '/'
            
            print(operaciones(num1, operador, num2, historial))
        elif opcion == '5':
            print("\nHistorial de operaciones:")
            print(mostrar_historial(historial))
        elif opcion == '6':
            print("Saliendo de la calculadora")
            break
        else:
            print("Opción invalida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora()
