import time
### CODE

# Función para imprimir el menú
def menu():
    print("")
    print("----------------- Contactos ---------------")
    print("What you want to do?")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Delete contact")
    

# Función para preguntar si quiere ver el menú de nuevo
def mostrar_menu():
    print("Do you want to see the menu again?")
    print("Yes/No")
    show_menu = input("--> ")
    if show_menu == ("yes"):
        menu()

    if show_menu == ("no"):
        pass


##Fase 1:
# Estructura de contactos
contactos = []

# Función para añadir contacto (ADD CONTACTS)
def add_contact(nombre, apellido, telefono):
    contactos.append({"Nombre": nombre, "Apellido": apellido, "Teléfono": telefono})
    


# Pretty print (LIST CONTACT)
def listcontacts():
    print("Contactos:")
    for i in contactos:
        print("---------------------------")
        print(i["Nombre"], i["Apellido"])
        print(i["Teléfono"])

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
		print("-----------------\n", i["Nombre"], i["Apellido"], i["Telefono"])
#listcontacts_or()

#CONTACT ID
id_contactos = {}
def contact_id():
	num_id = 1
	for i in contactos:
		id_contactos[num_id] = i
		num_id = num_id +1
	print(id_contactos)

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
	num = 0
	for i in id_contactos:
		for k,v in i.items():
			if v == list_msg[num]:
				print("a")
			num += 1

#Fase 4 
