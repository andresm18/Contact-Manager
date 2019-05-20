import contact_manager
import time

contact_manager.menu()
try:
    opt = int(input("--> "))
except ValueError:
    print("Error ingrese una opcion")
    opt = int(input("--> "))


while opt != 14:
    if opt == 1:
        try:
            cant_new_contacts = int(input("\n Ingrese la cantidad de contactos que desea añadir: "))
        except ValueError:
            print("ERROR, ingrese una cantidad")
            cant_new_contacts = int(input("\n Ingrese la cantidad de contactos que desea añadir: "))
        print("")
        for agregar in range(cant_new_contacts):
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            try:
                telefono = int(input("Ingrese el telefono: "))
            except ValueError:
                print("ERROR, no ingreso numeros")
                telefono = int(input("Ingrese el telefono: "))
            print("\n")
            contact_manager.add_contact(nombre, apellido, telefono)    


    if opt == 2:
        print("")
        contact_manager.listcontacts()


    if opt == 3:
        print("")
        nom_ap = input("Ingrese el nombre y apellido del contacto a eliminar: ")
        print("")
        contact_manager.remove_contact(nom_ap)


    if opt == 4:
        print("")
        file_name = input("Ingrese el nombre del documento: ")
        contact_manager.lee_file(file_name)


    if opt == 5:
        print("")
        contact_manager.listcontacts_or()


    if opt == 6:
        print("")
        contact_manager.contact_id()   


    if opt == 7:
        print("")
        call_cont = int(input("A que usuario desea llamar? ingrese el contactID: "))
        contact_manager.call_contact(call_cont)

    if opt == 8:
        print("")
        msg_cont = input("A quienes desea enviar un mensaje? ")
        contact_manager.msg_contact(msg_cont)
        mensaje = input("Ingresa el mensaje: ")
        time.sleep(1)
        print("Listo! Enviado \n")
        time.sleep(0.5)

    if opt == 9:
        print("")
        try:
            cant_new_contacts2 = int(input("\n Ingrese la cantidad de contactos que desea añadir: "))
        except ValueError:
            print("ERROR, ingrese una cantidad")
            cant_new_contacts2 = int(input("\n Ingrese la cantidad de contactos que desea añadir: "))
        print("")
        for agregar in range(cant_new_contacts2):
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            try:
                telefono = int(input("Ingrese el telefono: "))
            except ValueError:
                print("ERROR, no ingreso numeros")
                telefono = int(input("Ingrese el telefono: "))
            print("\n")
            contact_manager.add_favorite(nombre, apellido, telefono)


    if opt == 10:
        print("")
        contact_manager.get_favorite()
    
    if opt == 11:
        print("")
        nom_ap = input("Ingrese el nombre y apellido del contacto a eliminar: ")
        print("")
        contact_manager.remove_favorite_contact(nom_ap)
    
    if opt == 12:
        print("")
        gid = input("Ingrese gid: ")
        URL = "https://tinyurl.com/yygujcbg"
        contact_manager.get(URL,gid)
    
    if opt == 13:
        print("")
        URL = "https://tinyurl.com/yygujcbg"
        contact_manager.post(URL)

    if opt == 14:
        print("")
        exit()

    contact_manager.mostrar_menu()

    try:
        opt = int(input("--> "))
    except ValueError:
        print("ERROR, ingrese una opcion")
        opt = int(input("--> "))
print("Nos vemos!")
exit()