from equipos import obtener_equipo, listar_equipos

def registrar_integrante(datos):
    if not listar_equipos(datos):
        return

    nombre_equipo = input("Ingrese el nombre del equipo al que pertenece el integrante: ").strip()
    equipo = obtener_equipo(datos, nombre_equipo)
    if not equipo:
        print("Equipo no encontrado.")
        return

    nombre = input("Ingrese el nombre del integrante: ").strip()
    if not nombre:
        print("El nombre del integrante no puede estar vacío.")
        return

    roles_validos = ["jugador", "tecnico", "asistente", "preparador", "medico"]
    rol = input(f"Ingrese el rol ({'/'.join(roles_validos)}): ").lower().strip()
    if rol not in roles_validos:
        print("Rol no válido.")
        return

    if rol == "jugador":
        posicion = input("Ingrese la posición del jugador: ").strip()
        if not posicion:
            print("La posición del jugador no puede estar vacía.")
            return
        datos["jugadores"][nombre.lower()] = {
            "nombre": nombre,
            "equipo": nombre_equipo,
            "posicion": posicion,
            "goles": 0,
            "tarjetas_amarillas": 0,
            "tarjetas_rojas": 0,
            "faltas": 0
        }
    else:
        datos["cuerpo_tecnico"][nombre.lower()] = {
            "nombre": nombre,
            "equipo": nombre_equipo,
            "rol": rol
        }

    print(f"{rol.capitalize()} '{nombre}' registrado con éxito en el equipo '{equipo['nombre']}'.")

def registrar_estadisticas_jugador(datos):
    if not listar_equipos(datos):
        return

    nombre_equipo = input("Ingrese el nombre del equipo del jugador: ").strip()
    equipo = obtener_equipo(datos, nombre_equipo)
    if not equipo:
        print("Equipo no encontrado.")
        return

    jugadores_equipo = [j for j in datos["jugadores"].values() if j["equipo"].lower() == nombre_equipo.lower()]
    if not jugadores_equipo:
        print("Este equipo no tiene jugadores registrados.")
        return

    print("\nJugadores del equipo:")
    for jugador in jugadores_equipo:
        print(f"- {jugador['nombre']}")

    nombre_jugador = input("Ingrese el nombre del jugador: ").strip()
    jugador = datos["jugadores"].get(nombre_jugador.lower())
    if not jugador or jugador["equipo"].lower() != nombre_equipo.lower():
        print("Jugador no encontrado en este equipo.")
        return

    try:
        goles = int(input("Goles anotados: "))
        tarjetas_amarillas = int(input("Tarjetas amarillas recibidas: "))
        tarjetas_rojas = int(input("Tarjetas rojas recibidas: "))
        faltas = int(input("Faltas cometidas: "))

        if any(num < 0 for num in [goles, tarjetas_amarillas, tarjetas_rojas, faltas]):
            raise ValueError("Los valores no pueden ser negativos.")

        jugador["goles"] += goles
        jugador["tarjetas_amarillas"] += tarjetas_amarillas
        jugador["tarjetas_rojas"] += tarjetas_rojas
        jugador["faltas"] += faltas

        equipo["goles_favor"] += goles
        print("Estadísticas actualizadas con éxito.")
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese solo números enteros no negativos.")