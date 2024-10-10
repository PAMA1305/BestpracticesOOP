class Alumno:
    #crea la funcion constructor con atributos vasioas#
    def __init__(self):
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para agregar valores a los atributos
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores almacenados
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre



    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}"

    # Método para mostrar información completa del alumno
    def mostrar_info(self):
        return f"Nombre: {self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}, No. Control: {self.__no_control}, Semestre: {self.__semestre}"

# Crear una instancia de Alumno
alumno1 = Alumno()
alumno1.set_nombre("Pedro")
alumno1.set_apellido_paterno("Morales")
alumno1.set_apellido_materno ("Lopez")
alumno1.set_no_control(12345678)
alumno1. set_semestre (5)

alumno = Alumno()
registro_alumnos = {}
alumnos_dict = {}

registro_alumnos [0] = alumno1
print (f"Nombre: {registro_alumnos [0].get_nombre()}")


# Obtener información del alumno
print(alumno1.mostrar_info())
print( "Nombre:", alumno1.get_nombre())
print("Apellido Paterno:", alumno1.get_apellido_paterno())
print("Apellido Materno:", alumno1.get_apellido_materno())
print("No. Control:", alumno1.get_no_control())
print ("Semestre:", alumno1.get_semestre())
print ("Nombre Completo:", alumno1.get_nombre_completo())



for i in range(1, 51):
    nombre = f"Nombre{i}"
    apellido_paterno = f"Apellido Paterno{i}"
    apellido_materno = f"Apellido Materno{i}"
    no_control = f"20{i:02d}00{i}"  # Ejemplo de no. control
    semestre = i % 8 + 1  # Semestre de 1 a 8




for no_control, alumno in alumnos_dict.items():
    print(alumno.mostrar_info())

for i in range(3):
    alumno1.set_nombre (input("introduce el Nombre: "))
    alumno1.set_apellido_paterno (input("introduce el apellidopaterno: "))
    alumno1.set_apellido_materno (input("introduce el apellido materno: "))
    alumno1.set_no_control (input("introduce el numero de control: "))
    alumno1.set_semestre (int(input("Semestre: ")))

    registro_alumnos[i] = alumno1
for i in range (3):
    print(f"nombre:{registro_alumnos[i].get_nombre()}")








