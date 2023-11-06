#Fn para agregar compra a la lista "Compras"
def agregar_compra(compras):
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    print("Compra agregada correctamente.")


#Fn que muestra las compras ya registradas
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: ${compra:.2f}")


#Fn que suma lo gastado
def mostrar_total(compras):
    total_gastado = sum(compras)
    print(f"Total gastado: ${total_gastado:.2f}")


#Main ()
def main():
    compras = []

    while True:
        print("Menú:")
        print("1. Agregar compras")
        print("2. Mostrar compras")
        print("3. Mostrar gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("Programa terminado ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Seleccione del 1 al 4, por favor.")


if __name__ == "__main__":
    main()
