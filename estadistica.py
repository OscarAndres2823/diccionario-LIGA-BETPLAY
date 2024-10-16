def mostrar_estadistica_equipos(datos):
    if not datos["equipos"]:
        print("No hay equipos registrados.")
        return

    if all(equipo["goles_favor"] == 0 for equipo in datos["equipos"].values()):
        print("No hay estadísticas disponibles. Ningún equipo ha marcado goles.")
        return

    equipo_mas_goles = max(datos["equipos"].values(), key=lambda x: x["goles_favor"])
    equipo_mas_goles_contra = max(datos["equipos"].values(), key=lambda x: x["goles_contra"])
    equipo_ultimo = min(datos["equipos"].values(), key=lambda x: x["puntos"])

    print("\nEstadísticas de equipos:")
    print(f"Equipo con más goles a favor: {equipo_mas_goles['nombre']} ({equipo_mas_goles['goles_favor']} goles)")
    print(f"Equipo con más goles en contra: {equipo_mas_goles_contra['nombre']} ({equipo_mas_goles_contra['goles_contra']} goles)")
    print(f"Equipo en último lugar: {equipo_ultimo['nombre']} ({equipo_ultimo['puntos']} puntos)")

    if datos["jugadores"]:
        jugador_mas_faltas = max(datos["jugadores"].values(), key=lambda x: x["faltas"])
        jugador_mas_amarillas = max(datos["jugadores"].values(), key=lambda x: x["tarjetas_amarillas"])

        print(f"\nJugador con más faltas: {jugador_mas_faltas['nombre']} ({jugador_mas_faltas['faltas']} faltas)")
        print(f"Jugador con más tarjetas amarillas: {jugador_mas_amarillas['nombre']} ({jugador_mas_amarillas['tarjetas_amarillas']} tarjetas)")
    else:
        print("\nNo hay jugadores registrados para mostrar estadísticas individuales.")