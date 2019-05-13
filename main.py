import contact_manager

### MENÚ
print("")
print("------ Contactos ------")
print("\n")
#print("Presione 1 para añadir un contacto ")
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
telefono = input("Ingrese eñ telefono: ")
print("\n")
    
contact_manager.add_contact(nombre,apellido,telefono)
print("")
