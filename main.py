import contact_manager

### MENÚ
print("")
print("------ Contactos ------")
print("\n")
cant_new_contacts = int(input("Ingrese la cantidad de contactos que desea añadir: "))
print("")

for agregar in range(cant_new_contacts):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el telefono: ")
    print("\n")
    contact_manager.add_contact(nombre, apellido, telefono)
    print("\n\n")

