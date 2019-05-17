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
		print("\n{}\n".format(i))
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

	