class usuarios: #Clase para datos de usuario
    def __init__(self, nombre, correo, codigo):
        self.nombre = nombre
        self.correo = correo
        self.codigo = codigo
    
    def __str__(self): #Identificar al usuario
        print (f"{self.nombre} ID:  {self.codigo} CORREO:  {self.correo}")

class libro: #Clase para datos del libro
    def __init__(self, tema, name, cod, autor):
        self. tema = tema
        self.name = name
        self.cod = cod
        self.autor = autor

    def __str__(self): #Identificar al libro
        print (f"{self.name} Tema: {self.tema} COD: {self.cod}")

class Biblio: #Clase para las funciones del menú
    def __init__(self):
        self.libros = [] #lista para guardar el libro
        self.usuarios = [] #lista para guardar el usuario
        self.temas = ["Romance", "Ciencia ficción", "Historia"]

    def r_libro(self): #Registrar un nuevo libro según sus tema
        print ("\n -----Registro de Libro-----")
        name = input("Título: ")
        cod = input("Código del Libro: ")
        autor = input("Autor del Libro: ")

        print ("\n Temas Disponibles")
        cont = 1
        for tema in self.temas:
            print (f"{cont}. {tema}")
            cont +=1
        op = int(input("Seleccione el tema: "))

        if 1<=op<=len(self.temas): #da las opciones de los temas de los libros
            tema = self.temas[op-1]
            libroo = libro(tema, name, cod, autor)
            self.libros.append(libroo) #agregar el libro a la lista
            print ("El libro fue agregado de forma correcta.")
        else:
            print ("No se puedo agregar el libro.")

    def r_usuario(self): #registrar un nuevo usuario
        print ("\n -----Registro de Usuarios-----")
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        codigo = input("Código: ")
        user = usuarios(nombre, correo, codigo)
        self.usuarios.append(user) #agregar al usuario a la lista
        print ("El usuario fue agregado de forma correcta.")

    def m_libros(self): #mostrar los libros registrados
        print ("\n -----Libros Registrados-----")
        if not self.libros: #mostrar si hay o no libros
            print ("No hay ningún libro registrado")
        else:
            for libroo in self.libros:
                print (libroo)

    def m_users(self): #mostrar los usuarios registrados
        print ("\n -----Usuarios Registrados-----")
        if not self.libros: #mostrar si hay o no un usuario registrado
            print ("No está registrado el usuario")
        else:
            for user in self.usuarios:
                print (user)

def main():
    biblioteca = Biblio()

    while True: #mostrar el menú al usuario
        print ("\n -----Menú de la Biblioteca Universitaria-----")
        print ("1. Registrar un nuevo libro.")
        print ("2. Registrar un nuevo usuario.")
        print ("3. Ver libro.")
        print ("4. Ver usuario.")
        print ("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1": #selección de la opción a trabajar
            biblioteca.r_libro()
        elif opcion == "2":
            biblioteca.r_usuario()
        elif opcion == "3":
            biblioteca.m_libros()
        elif opcion == "4":
            biblioteca.m_users()
        elif opcion =="5":
            print ("\n -----Saliendo del Programa-----") #cerrar el programa
            break
        else: 
            print ("\ -----OPCIÓN INVÁLIDA-----")

if __name__ == "__main__":
    main()







