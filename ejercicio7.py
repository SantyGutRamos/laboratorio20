estudiantes = []

def agregar_estudiante():
    print("\n1-.Agregar estudiante")
    
    nombre = input("Ingresa el nombre: ").strip()
    
    while True:
        try:
            edad = int(input("Ingresa la edad : "))
            break
        except ValueError:
            print("No valido")

    while True:
        try:
            promedio = float(input("Ingresa el promedio : "))
            break
        except ValueError:
            print("No valido")

    nuevo_estudiante = {
        "nombre": nombre, 
        "edad": edad, 
        "promedio": promedio
    }
    
    estudiantes.append(nuevo_estudiante)
    print(f"\nEstudiante '{nombre}' registrado.")

def mostrar_estudiantes():
    print("\n2-.Mostrar estudiantes")
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
        
    for i in range(len(estudiantes)):
        est = estudiantes[i]
        print(f"[{i+1}] Nombre: {est['nombre']}, Edad: {est['edad']}, Promedio: {est['promedio']:.2f}")

def mostrar_mejor_promedio():
  
    print("\n3.-Estudiante con mejor promedio")
    if not estudiantes:
        return
        
    mejor_promedio = -1.0 
    mejor_estudiante = None
    
    for est in estudiantes:
        if est['promedio'] > mejor_promedio:
            mejor_promedio = est['promedio']
            mejor_estudiante = est

    if mejor_estudiante:
        print(f"Nombre: {mejor_estudiante['nombre']}")
        print(f"Promedio: {mejor_estudiante['promedio']:.2f}")

def buscar_por_nombre():
    print("\n4-.buscar por nombre")
    if not estudiantes:
        return
        
    nombre_buscado = input("Ingresa el nombre a buscar: ").strip().lower()
    encontrado = False
    
    for est in estudiantes:
        if est['nombre'].strip().lower() == nombre_buscado:
            print(f"Encontrado: Nombre: {est['nombre']}, Edad: {est['edad']}, Promedio: {est['promedio']:.2f}")
            encontrado = True
    
    if not encontrado:
        print(f"No se encontró el estudiante '{nombre_buscado}'.")

def eliminar_por_nombre():
    print("\n5-.Eliminar por nombre")
    if not estudiantes:
        return

    nombre_eliminar = input("Ingresa el nombre a eliminar: ").strip().lower()
    eliminado = False
    
    for i in range(len(estudiantes) - 1, -1, -1):
        if estudiantes[i]['nombre'].strip().lower() == nombre_eliminar:
            del estudiantes[i]
            eliminado = True
            
    if eliminado:
        print(f"Estudiante(s) con el nombre '{nombre_eliminar}' eliminado(s).")
    else:
        print(f"No se encontró el estudiante '{nombre_eliminar}' para eliminar.")


def menu_principal():
    while True: 
        print("\n Registro ")
        print("1. agregar estudiante")
        print("2. mostrar estudiantes")
        print("3. mostrar estudiante con mejor promedio")
        print("4. buscar por nombre")
        print("5. eliminar por nombre")
        print("6. salir")
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            mostrar_mejor_promedio()
        elif opcion == '4':
            buscar_por_nombre()
        elif opcion == '5':
            eliminar_por_nombre()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("No valido")

if __name__ == "__main__":
    menu_principal()