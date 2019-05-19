import contact_manager

### MENÚ


# Función para opcion del menu

# ADD CONTACT
contact_manager.menu()
opt = input("--> ")
if opt == ("1"):
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

#  LISTA INICIALIZADA
if opt == ("4"):
    print("AAAAAAAAAAAAAAAAAAAA")
    file_name = input("Ingrese el nombre del documento: ")
    contact_manager.lee_file(file_name)
contact_manager.mostrar_menu()
opt = input("--> ")

# CONTACTOS ORDENADOS
if opt == ("5"):
    contact_manager.listcontacts_or()
contact_manager.mostrar_menu()
opt = input("--> ")

# CONTACT ID
if opt == ("6"):
    contact_manager.contact_id()
contact_manager.mostrar_menu()
opt = input("--> ")

# CALL CONTACT
if opt == ("7"):
    call_cont = int(input("A que usuario desea llamar? "))
    contact_manager.call_contact(call_cont)
contact_manager.mostrar_menu()
opt = input("--> ")

if opt == ("8"):
    msg_cont = input("A quienes desea enviar un mensaje? ")
    contact_manager.msg_contact(msg_cont)
contact_manager.mostrar_menu()
opt = input("--> ")
