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
def remove_contact(nombre,apellido):
	for i in contactos:
		for (k,v) in i.items():
			if v == nombre:
				a = contactos.index(i)
				print(a)
			if v == apellido:
				b = contactos.index(i)
				print(b)
				contactos.pop(b)
	listcontacts()

					
			#if casilla == nombre:
	