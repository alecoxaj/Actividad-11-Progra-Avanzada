propietarios = {}

print("¡BIENVENIDO!")
cantidad_propietarios = int(input("¿Cuántos propietarios quieres ingresar?: "))

for i in range(cantidad_propietarios):
    print(f"Propietario {i+1}")
    nit = input("Ingresa tu NIT: ")
    name = input("Ingresa tu nombre: ")
    phone = input("Ingresa tu teléfono: ")


cantidad_vehículos = int(input("Ingresa la cantidad de vehículos: "))
vehicles = {}

for j in range(cantidad_vehículos):
    print(f"Vehículo {j+1}")
    plate = input("Ingresa tu placa: ")
    brand = input("Ingresa la marca: ")
    model = input("Ingresa el modelo: ")
    year = int(input("Ingresa el año: "))
    tax_payed = input("¿Pagaste el impuesto? (si/no): ")

    vehicles[plate] = {
        "plate": plate,
        "brand": brand,
        "model": model,
        "year": year,
        "tax": tax_payed,
    }


    propietarios[nit] = {
        "name": name,
        "phone ": phone,
    }

print("\nResumen de propietarios: ")
for nit, datos in propietarios.items():
    print(f"\nNúmero de NIT: {nit}")

