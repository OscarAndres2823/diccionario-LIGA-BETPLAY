import equipos
import jugadores
import estadistica

def mostrar_menu():
    titulo="""
    ****************************************************
    *  ⚽🥅🫵        LIGA BETPLAY          ⚽🥅🫵   *
    ****************************************************
    """
    print(titulo)
    print("1. Registrar equipo")
    print("2. Registrar integrante de equipo")
    print("3. Ver estadísticas de equipos")
    print("4. Registrar estadísticas de jugador")
    print("5. Salir")

def main():
    datos = {
        "equipos": {},
        "jugadores": {},
        "cuerpo_tecnico": {}
    }
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            equipos.registrar_equipo(datos)
        elif opcion == "2":
            jugadores.registrar_integrante(datos)
        elif opcion == "3":
            estadistica.mostrar_estadisticas_equipos(datos)
        elif opcion == "4":
            jugadores.registrar_estadisticas_jugador(datos)
        elif opcion == "5":
            print("Gracias por usar el programa")
            print("✡︎¡Hasta luego!✡︎")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()