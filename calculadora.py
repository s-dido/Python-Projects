# Pedir al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Pedir al usuario que elija una operación aritmética
print("Seleccione una operación aritmética:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")
print("5. Módulo (%)")
print("6. División entera (//)")
print("7. Exponentiación (**)")
opcion = int(input("Ingrese el número de la operación: "))

# Realizar la operación aritmética seleccionada
if opcion == 1:
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == 2:
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == 3:
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir por cero")
elif opcion == 5:
    resultado = num1 % num2
    print("El resultado del módulo es:", resultado)
elif opcion == 6:
    resultado = num1 // num2
    print("El resultado de la división entera es:", resultado)
elif opcion == 7:
    resultado = num1 ** num2
    print("El resultado de la exponentiación es:", resultado)
else:
    print("Error: Opción no válida")