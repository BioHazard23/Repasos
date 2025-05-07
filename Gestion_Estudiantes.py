                                                        #Gestion de estudiantes

#Colors
DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

#Initial Students
students = [
    {"id": "001", "name": "Natasha Lopez", "age": 22, "note": 4.5},
    {"id": "002", "name": "Charlie Arango", "age": 20, "note": 4.8},
    {"id": "003", "name": "Susana Perez", "age": 21, "note": 3.0},
    {"id": "004", "name": "Anthony Torres", "age": 25, "note": 3.7},
    {"id": "005", "name": "Adolf Hittler", "age": 56, "note": 5.0}
]
#Find student by ID
def find_student_by_id(student_id):
    for student in students:
        if student ["id"] == student_id:
            return student
    return None

#Add New Student
def add_student(student_id, name, age, note):
    if find_student_by_id(student_id):
        print (DANGER + "Ya existe un estudiante con ese ID." + RESET)
        return
    if not (0.0 <= note <= 5.0):
        print (DANGER + "La nota debe estar entre 0.0 y 5.0." + RESET)
        return
    if age <= 0:
        print (DANGER + "La edad debe ser un numero positivo." + RESET)
        return
    students.append({"id": student_id, "name": name, "age": age, "note": note})
    print (SUCCESS + "Estudiante Agregado correctamente." + RESET)

#Search by ID
def search_by_id(student_id):
    student = find_student_by_id(student_id)
    if student:
        print(student)
    else:
        print (WARNING + "No se encontro al estudiante." + RESET)

#Search by name (partial)
def search_by_name(name):
    found = False
    for student in students:
        if name.lower() in student["name"].lower():
            print(student)
            found = True
    if not found:
        print (WARNING + "No se encontro ningun estudiante con ese nombre." + RESET)

#Update Student
def update_student(student_id, new_age=None, new_note=None):
    student = find_student_by_id(student_id)
    if not student:
        print (WARNING + "No se encontro al estudiante." + RESET)
        return
    if new_note is not None:
        if not (0.0 <= new_note <= 5.0):
            print (DANGER + "La nota debe estar entre 0.0 y 5.0." + RESET)
            return
        student["note"] = new_note
    if new_age is not None:
        if new_age <= 0:
            print (DANGER + "La edad debe ser un numero positivo." + RESET)
            return
        student["age"] = new_age
    print (SUCCESS + "Se actualizo la informacion del estudiante." + RESET)

#Delete Student
def delete_student(student_id):
    student = find_student_by_id(student_id)
    if not student:
        print(WARNING + "No se encontro al estudiante." + RESET)
        return
    students.remove(student)
    print(SUCCESS + "El estudiante se ha eliminado correctamente." + RESET)

#Calculate Average Note
def calculate_average ():
    if not students:
        print (WARNING + "No hay estudiantes registrados." + RESET)
        return
    total = sum(student["note"] for student in students)
    average = total / len(students)
    print (f"El promedio general de notas es: {SUCCESS}{average:.2f}{RESET}")

#List Students With Note Below Threshold
def list_below_threshold(threshold=3.0):
    low_students = [student for student in students if student["note"] < threshold]
    if not low_students:
        print(SUCCESS + "No hay estudiantes con notas menores al umbral." + RESET)
        return
    for student in low_students:
        print(student)

#Main Options
def menu():
    while True:
        print("\n----------Menu del sistema de gestion de alumnos----------")
        print("1. Agregar estudiante.")
        print("2. Buscar estudiante por ID.")
        print("3. Buscar estudiante por nombre.")
        print("4. Actualizar informacion de un estudiante")
        print("5. Eliminar estudiante")
        print("6. Calcular promedio de notas")
        print("7. Lista de estudiants con notas inferiores al umbral")
        print("8. Salir")

        opcion = input("\nSelecciona una opcion (1 - 8): ")

        if opcion == "1":
            nombre = input("Nombre completo del estudiante: ")
            edad = int(input("Edad del estudiante: "))
            id_estudiante = input("ID del estudiante: ")
            nota = float(input("Nota del estudiante (0.0 - 5.0): "))
            add_student(id_estudiante, nombre, edad, nota)
        
        elif opcion == "2":
            id_estudiante = input("ID del estudiante: ")
            search_by_id(id_estudiante)

        elif opcion == "3":
            nombre = input("Nombre del estudiante: ")
            search_by_name(nombre)

        elif opcion == "4":
            id_estudiante = input("ID del estudiante: ")
            actualizar_edad = input("¿Actualizar edad? (s/n): ").lower() == "s"
            actualizar_nota = input("¿Actualizar nota? (s/n): ").lower() == "s"
            nueva_edad = int(input("Nueva edad: ")) if actualizar_edad else None
            nueva_nota = float(input("Nueva nota (0.0 - 5.0): ")) if actualizar_nota else None
            update_student(id_estudiante, nueva_edad, nueva_nota)

        elif opcion == "5":
            id_estudiante = input("ID del estudiante a eliminar: ")
            delete_student(id_estudiante)

        elif opcion == "6":
            calculate_average()

        elif opcion == "7":
            entrada = input("Umbral de nota (Presiona enter para usar 3.0): ")
            umbral = float(entrada) if entrada else 3.0
            list_below_threshold(umbral)

        elif opcion == "8":
            print(SUCCESS + "Saliendo del sistema. ¡Hasta Pronto!" + RESET)
            break
        
        else:
            print(DANGER + "Opcion invalida" + RESET)

#Start Program
menu()
            
