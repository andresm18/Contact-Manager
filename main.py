import contact_manager

### MENÚ
# Función para imprimir el menú
def menu():
    print("")
    print("----------------- Contactos ---------------")
    print("What you want to do?")
    print("1. Add Contact")
    print("2. List Contactc")
    print("3. Delete contact")
menu()

# Función para preguntar si quiere ver el menú de nuevo
def mostrar_menu():
    print("Do you want to see the menu again?")
    print("Yes/No")
    show_menu = input("--> ")
    if show_menu == ("yes"):
        menu()
        opcion_menu()

    if show_menu == ("no"):
        exit()


# Función para opcion del menu
def opcion_menu():
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
        mostrar_menu()

    # LIST CONTACT
    if opt == ("2"):
        print("")
        contact_manager.listcontacts()
        mostrar_menu()

    # DELETE CONTACT
    if opt == ("3"):
        nom_ap = input("Ingrese el nombre y apellido del contacto a eliminar: ")
        contact_manager.remove_contact(nom_ap)
        mostrar_menu()

opcion_menu()
