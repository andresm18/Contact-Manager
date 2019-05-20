import time
import os
import requests

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
	print("6. ID your Contact")
	print("7. Call Contact")
	print("8. Message Contacts")
	print("9. Add to Favorite")
	print("10. List Favorites")
	print("11. Remove Favorite Contact")
	print("12. HTTP Request GET")
	print("13. HTTP Request POST")
	print("14. Exit")


# Función para preguntar si quiere ver el menú de nuevo
def mostrar_menu():
    try:
        print("Do you want to see the menu again? ")
        print("Yes/No")
        show_menu = input("--> ")
        show_menu.lower()
        print("")
    except ValueError:
        print("ERROR, ingrese un numero")
        show_menu = input("--> ")
        show_menu.lower()
        print("")
    if show_menu == ("yes"):
        menu()
    elif show_menu == ("no"):
        pass 
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
		print(i["Nombre"], i["Apellido"])
		print(i["Telefono"])
		print("")

#Remover contactos (DELETE CONTACT)
def remove_contact(nom_ap):
    list_nom_ap = nom_ap.split(" ")
    ult_list = len(list_nom_ap)
    try:
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
    except UnboundLocalError and IndexError:
        print("\nERROR, usuario no enontrado\n")
        mostrar_menu()

##Fase 2:
def lee_file(file_name = "InitialContacts.txt"):
    try:
        with open(file_name) as f:
            fcont = f.readlines()
            for i in fcont:
                info = i.split(',')
                nombre = info[0]
                apellido = info[1]
                telefono = info[2]
                contactos.append({"Nombre": nombre, "Apellido": apellido, "Telefono": telefono})
    except FileNotFoundError:
        print("\nERROR, Documento No Encotrado")
        mostrar_menu()

##Funcion para listar contactos en orden alfabetico con base a apellido
def listcontacts_or():
	print("Contactos:")
	contactos_ordenado = sorted(contactos, key=lambda k: k['Apellido'])
	for i in contactos_ordenado:
		print("----------------------------")
		print(i["Nombre"], i["Apellido"])
		print(i["Telefono"])
		print("")


## Fase 3

#CONTACT ID
id_contactos = {}
def contact_id():
	num_id = 1
	print("Contactos:")
	for i in contactos:
		id_contactos[num_id] = i
		print("----------------------------")
		print(num_id,i["Nombre"],i["Apellido"],"--> ",i["Telefono"] )
		num_id = num_id + 1
		print("")
	


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
    list_msgs = msg_cont.split()
    msg = []
    num = 0
    print("Enviando mensaje a...")
    for k,v in id_contactos.items():
        print(k,v)
        if k == list_msgs[num]:
            msg.append(v["Nombre"])
            print(msg)
            num += 1





# ADD FAVORITE
# Estructura de contactos favoritos
favoritos = []

# Función para añadir contactos a favoritos
def add_favorite(nombre,apellido,telefono):
	if nombre == "":
		print("No hay nombre")
	nombre.title()
	if apellido == "":
		print("No hay apellido")
	apellido.title()
	favoritos.append({"Nombre": nombre, "Apellido": apellido, "Telefono" :telefono})
	contactos.append({"Nombre": nombre, "Apellido": apellido, "Telefono" :telefono})


# Get Favorite (pretty print with ID)
id_contactos_favoritos = {}
def get_favorite():
	num_id_favorites = 0
	print("Favoritos:")
	for i in favoritos:
		id_contactos_favoritos[num_id_favorites] = i
		num_id_favorites = num_id_favorites + 1
		print("----------------------------")
		print(num_id_favorites, i["Nombre"], i["Apellido"],"--> ", i["Telefono"])
		print("")

# Remove from favorites
def remove_favorite_contact(nom_ap):
    list_nom_ap = nom_ap.split(" ")
    ult_list = len(list_nom_ap)
    try:
        for i in favoritos:
            for (k,v) in i.items():
                if v == list_nom_ap[0]:
                    a = favoritos.index(i)
            for (k,v) in i.items():
                if v == nom_ap[ult_list]:
                    b = favoritos.index(i)
                    if a == b:
                        favoritos.pop(b)
        get_favorite()
    except UnboundLocalError and IndexError:
        print("\nERROR, usuario no enontrado\n")
        mostrar_menu()


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
		print("ERROR, el archivo al que quiere acceder no existe o no fue encontrado")
	else:
		listcontacts_or()

##Fase 6
#GET
def get(URL,gid):
    payload = {"gid":gid}
    response = requests.get(URL,params= payload)
    print(response.text)

def post(URL):
	response = requests.post(URL, json= contactos)
	print(response.text)

