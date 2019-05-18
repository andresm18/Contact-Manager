### CODE

##Fase 1:
# Estructura de contactos
contactos = []

# Función para añadir contacto 
def add_contact(nombre, apellido, telefono):
    contactos.append({"Nombre": nombre, "Apellido": apellido, "Teléfono": telefono})

def listcontacts():
	print("Contactos:")
	for i in contactos:
		print("-----------------\n", i["Nombre"], i["Apellido"], i["Teléfono"])
listcontacts()

#Remover contactos
def remove_contact(nom_ap):
	list_nom_ap = nom_ap.split(" ")
	ult_list = len(list_nom_ap)
	for i in contactos:
		for (k,v) in i.items():
			if v == list_nom_ap[0]:
				a = contactos.index(i)
				print(a, "a")
		for (k,v) in i.items():
			if v == nom_ap[ult_list]:
				b = contactos.index(i)
				print(b, "b")
	if a == b:
		contactos.pop(b)
				
	listcontacts()

##Fase 2:
filename = "InitialContacts.txt"
def lee_file(filename):
	with open(filename) as f:
		fcont = f.readlines()
		for i in fcont:
			info = i.split(',')
			nombre = info[0]
			apellido = info[1]
			telefono = info[2]
			contactos.append({"Nombre": nombre, "Apellido": apellido, "Telefono": telefono})
lee_file(filename)

##Funcion para listar contactos en orden alfabetico con base a apellido
def listcontacts_or():
	print("Contactos:")
	contactos_ordenado = sorted(contactos, key=lambda k: k['Apellido']) 
	for i in contactos_ordenado:
		print("-----------------\n", i["Nombre"], i["Apellido"], i["Telefono"])
listcontacts_or()