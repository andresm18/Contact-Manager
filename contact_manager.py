### CODE

##Fase 1:
# Estructura de contactos
contactos = []

# Función para añadir contacto 
def add_contact(nombre, apellido, telefono):
    contactos.append({"Nombre": nombre, "Apellido": apellido, "Teléfono": telefono})
    print(contactos)

def listcontacts():
	print("Contactos:")
	for i in contactos:
		print("\n{}\n".format(i))
listcontacts()