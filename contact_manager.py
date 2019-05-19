import time
import os
### CODE

# Función para imprimir el menú
def menu():
    print("------------ Contacts ------------\n")
    print("What do you want to do?")
    print("1. Add Contact")
    print("2. List Contact")
    print("3. Remove Contact")
    print("4. Initialize with File")
    print("5. Alphabetic Contacts")
    print("6. ID your Contacts")
    print("7. Call Contact")
    print("8. Message Contacts")

# Función para preguntar si quiere ver el menú de nuevo
def mostrar_menu():
	print("Do you want to see the manu again? ")
	print("Yes/No")
	show_menu = input("--> ")
	show_menu.lower()
	print("")
	
	if show_menu == ("yes"):
		menu()
	
	elif show_menu == ("no"):
		exit()
	
	else:
		print("ERROR, 'Yes/No'")
		show_menu = input("--> ")
		print("")
		show_menu.lower()
		menu()


##Fase 1:
# Estructura de contactos
contactos = []

# Función para añadir contacto (ADD CONTACTS)
def add_contact(nombre,apellido,telefono):
    if nombre == "":
        print("No hay nombre")
    nombre.title()
    if apellido == "":
        print("No hay apellido")
    apellido.title()
    contactos.append({"Nombre": nombre, "Apellido": apellido, "Telefono" :telefono})

# Pretty print (LIST CONTACT)
def listcontacts():
	print("Contactos:")
	for i in contactos:
		print("----------------------------")
		print(i["Nombre"])
		print(i["Apellido"])
		print(i["Telefono"])
		print("")

#Remover contactos (DELETE CONTACT)
def remove_contact(nom_ap):
    list_nom_ap = nom_ap.split(" ")
    ult_list = len(list_nom_ap)
    for i in contactos:
        for (k,v) in i.items():
            if v == list_nom_ap[0]:
                a = contactos.index(i)
        for (k,v) in i.items():
            if v == nom_ap[ult_list]:
                b = contactos.index(i)
    if a == b:
        contactos.pop(b)
                
    listcontacts()
   


##Fase 2:
filename = "InitialContacts.txt"
def lee_file(file_name = "InitialContacts.txt"):
    file_name = file_name 
    with open(file_name) as f:
        fcont = f.readlines()
        for i in fcont:
            info = i.split(',')
            nombre = info[0]
            apellido = info[1]
            telefono = info[2]
            contactos.append({"Nombre": nombre, "Apellido": apellido, "Telefono": telefono})
#lee_file(filename)


##Funcion para listar contactos en orden alfabetico con base a apellido
def listcontacts_or():
	print("Contactos:")
	lista_a_ordenar = contactos
	contactos_ordenado = sorted(lista_a_ordenar, key=lambda k: k['Apellido'])
	for i in contactos_ordenado:
		print("----------------------------")
		print(i["Nombre"], i["Apellido"])
		print(i["Telefono"])
		print("")

#listcontacts_or()


## Fase 3

#CONTACT ID
id_contactos = {}
def contact_id():
	num_id = 0
	print("Contactos:")
	for i in contactos:
		id_contactos[num_id] = i
		num_id = num_id + 1
		print("----------------------------")
		print(num_id,i["Nombre"],",",i["Apellido"],",",i["Telefono"] )
		print("")
		
    #print(id_contactos)


# CALL CONTACT
def call_contact(call_cont):
    for i in id_contactos:
        if i == call_cont:
            contact = id_contactos[i]
            try:
                print("\n    Llamando...")
                print(contact["Nombre"], contact["Apellido"])
                print(contact["Telefono"])
                time.sleep(60)
            except KeyboardInterrupt:
                pass


# MESSAGE CONTACT
def msg_contact(msg_cont):
    list_msg = msg_cont.split(" ")
    msg = []
    num = 0
    for i in id_contactos:
        print(i)
        if i == list_msg[num]:
            msg.append(i)
            print(msg, "g")
        num += 1
        # for k,v in i.items():
        #   if v == list_msg[num]:
        #       print("a")
        #   num += 1

#Fase 4 
def loadFromFile():
	externalfile = input("Escriba el nombre exacto del archivo con un backslash al principio: ")
	try:
		nombre_compelto_de_file = "C:\\Users\\Andres M\\Desktop"
		path = nombre_compelto_de_file + externalfile
		with open(path, 'r') as f:
			fcont = f.readlines()
			for i in fcont:
				info = i.split(',')
				nombre = info[0]
				apellido = info[1]
				telefono = info[2]
				contactos.append({"Nombre": nombre, "Apellido": apellido, "Telefono": telefono})
	except:
		print("Error el archivo de existe o no fue encontrado")
	else:
		listcontacts_or()
#loadFromFile()

# List all files in a directory using os.listdir
# basepath = 'C:\\Users\\Andres M\\Desktop'
# for entry in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath, entry)):
#         print(entry)

# filename_prueb = "maspruebas.txt"
# exists=os.path.isfile(filename_prueb)
# if exists:
# 	print("s")
# else:
# 	print('n')