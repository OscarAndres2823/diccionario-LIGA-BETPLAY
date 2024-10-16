def registrar_equipo(datos):
    nombre = input("Ingrese el nombre del equipo: ").strip()
    if not nombre:
        print("El nombre del equipo no puede estar vacío.")
        return
    if nombre.lower() in datos["equipos"]:
        print(f"El equipo '{nombre}' ya existe.")
        return
    
    datos["equipos"][nombre.lower()] = {
        "nombre": nombre,
        "goles_favor": 0,
        "goles_contra": 0,
        "puntos": 0
    }
    print(f"Equipo '{nombre}' registrado con éxito.")

def obtener_equipo(datos, nombre):
    return datos["equipos"].get(nombre.lower())

def listar_equipos(datos):
    if not datos["equipos"]:
        print("No hay equipos registrados.")
        return False
    print("\nEquipos registrados:")
    for nombre in datos["equipos"]:
        print(f"- {datos['equipos'][nombre]['nombre']}")
    return True