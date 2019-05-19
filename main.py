import contact_manager

## MENU
contact_manager.menu()
opt = input("--> ")

# ADD CONTACT
if opt == ("1"):
    print("\n")
    cant_new_contacts = int(input("Ingrese la cantidad de contactos que desea añadir: "))
    print("")

for agregar in range(cant_new_contacts):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = input("Ingrese el telefono: ")
    print("\n")
    # llamar la función para agregar el nuevo contacto
    contact_manager.add_contact(nombre, apellido, telefono)

contact_manager.mostrar_menu()
opt = input("--> ")

# LIST CONTACT
if opt == ("2"):
    print("")
    contact_manager.listcontacts()
contact_manager.mostrar_menu()
opt = input("--> ")

# DELETE CONTACT
if opt == ("3"):
    nom_ap = input("Ingrese el nombre y apellido del contacto a eliminar: ")
    contact_manager.remove_contact(nom_ap)
    
contact_manager.mostrar_menu()
opt = input("--> ")


