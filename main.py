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
#Lista de conatctos 
contact_manager.listcontacts()
### BORRAR CONTACTOS 
print("Borrar contactos")
nom_ap = input("Ingrese el nombre y apellido: ")
contact_manager.remove_contact(nom_ap)
