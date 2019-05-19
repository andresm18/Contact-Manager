import contact_manager
contact_manager.menu()
opt = int(input(" opcion "))
while opt != 10:
    if opt == 1:
        cant_new_contacts = int(input("Ingrese la cantidad de contactos que desea añadir: "))
        print("")
        for agregar in range(cant_new_contacts):
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            try:
                telefono = int(input("Ingrese el telefono: "))
            except ValueError:
                print("Error no ingreso numeros")
                telefono = int(input("Ingrese el telefono: "))
            print("\n")
            contact_manager.add_contact(nombre, apellido, telefono)    
    if opt == 2:
        print("")
        contact_manager.listcontacts()
    if opt == 3:
        nom_ap = input("Ingrese el nombre y apellido del contacto a eliminar: ")
        contact_manager.remove_contact(nom_ap)
    if opt == 4:
        print("AAAAAAAAAAAAAAAAAAAA")
        file_name = input("Ingrese el nombre del documento: ")
        contact_manager.lee_file(file_name)
    if opt == 5:
        contact_manager.listcontacts_or()
    if opt == 6:
        contact_manager.contact_id()   
    if opt == 7:
        call_cont = int(input("A que usuario desea llamar? "))
        contact_manager.call_contact(call_cont)
    if opt == 8:
        msg_cont = input("A quienes desea enviar un mensaje? ")
        contact_manager.msg_contact(msg_cont)

    contact_manager.mostrar_menu()
    opt = int(input(" opcion "))
print("Nos vemos!")