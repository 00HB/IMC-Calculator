def pedir_texto(campo):
    while True:
        dato = input(f"Ingresa {campo}: ").strip()

        if dato == "":
            print(f"Error: {campo} no puede quedar vacío.")
        else:
            return dato


def pedir_entero(campo):
    while True:
        dato = input(f"Ingresa {campo}: ").strip()

        if dato == "":
            print(f"Error: {campo} no puede quedar vacío.")
            continue

        try:
            numero = int(dato)

            if numero <= 0:
                print(f"Error: {campo} debe ser mayor que cero.")
            else:
                return numero

        except ValueError:
            print(f"Error: {campo} debe ser un número entero válido.")


def pedir_numero(campo):
    while True:
        dato = input(f"Ingresa {campo}: ").strip()

        if dato == "":
            print(f"Error: {campo} no puede quedar vacío.")
            continue

        try:
            numero = float(dato)

            if numero <= 0:
                print(f"Error: {campo} debe ser mayor que cero.")
            else:
                return numero

        except ValueError:
            print(f"Error: {campo} debe ser un número válido.")


# Datos personales
nombre = pedir_texto("tu nombre")
apellido_paterno = pedir_texto("tu apellido paterno")
apellido_materno = pedir_texto("tu apellido materno")

edad = pedir_entero("tu edad")
peso = pedir_numero("tu peso en kilogramos")
estatura = pedir_numero("tu estatura en metros, por ejemplo 1.70")

# Cálculo del IMC
imc = peso / (estatura ** 2)

# Resultados
print("\n--- DATOS CAPTURADOS ---")
print("Nombre:", nombre)
print("Apellido paterno:", apellido_paterno)
print("Apellido materno:", apellido_materno)
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
print("Estatura:", estatura, "m")

print("\n--- RESULTADO ---")
print("IMC calculado:", round(imc, 2))
