#Importo librerias
import modulo_equipos
import modulo_utiles
import modulo_jugadores
import modulo_partidos
#Defino variables
menu_principal = [
    '1. Gestión equipos',
    '2. Gestión de jugadores',
    '3. Calendarios de partidos',
    '4. Resultados y clasificación',
    '5. Salir'
]
menu_equipos = [
    '1. Crear equipo',
    '2. Listar equipos',
    '3. Buscar equipo por id',
    '4. Actualizar equipo',
    '5. Eliminar equipo',
    '6. Salir a menu principal'
]
menu_jugadores = [
    '1. Dar de alta a jugador',
    '2. Listar jugadores',
    '3. Buscar jugador por ID',
    '4. Actualizar jugador',
    '5. Eliminar jugador',
    '6. Salir a menu principal'
]
menu_partidos = [
    '1. Crear partido.',
    '2. Listar partidos',
    '3. Reprogramar partido',
    '4. Eliminar partido',
    '5. Salir a menu principal'
]
equipos = []
jugadores = []
partidos = []

#Lógica dek programa

#Guardamos la funcion de mostrar menú en una variable para crear un bucle y un match case con ella.
opcion = modulo_utiles.mostrar_menu(menu_principal)

while (opcion != 5):
    #En cada case de este match haremos otros while con match para cada menú.
    match opcion:
        #Menú equipos
        case 1:
            opcion_equipos = modulo_utiles.mostrar_menu(menu_equipos)
            while (opcion_equipos != 6):
                match opcion_equipos:
                    #Crear equipo
                    case 1:
                       crear_equipo = modulo_equipos.crear_equipo()
                       equipos.append(crear_equipo)
                    #Listar equipos
                    case 2:
                        modulo_equipos.listar_equipos(equipos)
                    #Buscar equipo
                    case 3:
                        id_busqueda = int(input('Introduzca el id de búsqueda: '))
                        modulo_equipos.buscar_id_equipo(equipos, id_busqueda)
                    #Actualizar equipo
                    case 4:
                        id_busqueda = int(input('Introduzca el id de búsqueda: '))
                        modulo_equipos.actualizar_equipo(equipos, id_busqueda)
                    #Eliminar equipo
                    case 5:
                        id_busqueda = int(input('Introduzca el id de búsqueda: '))
                        modulo_equipos.eliminar_equipo(equipos, id_busqueda)
                    case _:
                        print('Opción incorrecta.')
                opcion_equipos = modulo_utiles.mostrar_menu(menu_equipos)
            print('Saliendo del menú de equipos.')
        #Menú jugadores
        case 2:
            opcion_jugadores = modulo_utiles.mostrar_menu(menu_jugadores)
            while(opcion_jugadores != 6):
                match opcion_jugadores:
                    #Crear jugador
                    case 1:
                        jugador = modulo_jugadores.crear_jugador(equipos)
                        jugadores.append(jugador)
                        print(f'Se añadió {jugador} correctamente')
                    #Listar jugadores
                    case 2:
                        modulo_jugadores.listar_jugadores(jugadores)
                    #Buscar jugador
                    case 3:
                        id_busqueda = int(input('Introduzca el id de búsqueda: '))
                        modulo_jugadores.buscar_jugador(jugadores,id_busqueda)
                    #Actualizar jugador
                    case 4:
                        id_busqueda = int(input('Introduzca el id de búsqueda: '))
                        modulo_jugadores.actualizar_jugador(jugadores,id_busqueda,equipos)
                    #Eliminar jugador
                    case 5:
                        id_busqueda = int(input('Introduzca el id de búsqueda: '))
                        modulo_jugadores.eliminar_jugador(jugadores,id_busqueda)
                    case _:
                        print('Opción incorrecta.')
                opcion_jugadores = modulo_utiles.mostrar_menu(menu_jugadores)
            print('Saliendo a menu principal...')    
        #Menú partidos
        case 3:
            opcion_partidos = modulo_utiles.mostrar_menu(menu_partidos)
            while (opcion_partidos != 5):
                match opcion_partidos:
                    #Crear partrido
                    case 1:
                        nuevo_partido = modulo_partidos.crear_partido(equipos)
                        partidos.append(nuevo_partido)
                        print(f'Se añadio correctamente ---> {nuevo_partido}')
                    #Listar partidos
                    case 2:
                        modulo_partidos.listar_partidos(partidos)
                    #Reprogramar partido
                    case 3:
                        id_busqueda = int(input('Introduzca el id de búsqueda para reprogramar: '))
                        modulo_partidos.reprogramar_partido(partidos,id_busqueda)
                    #Eliminar partido
                    case 4:
                       id_busqueda = int(input('Introduzca el id de búsqueda para eliminar: '))
                       modulo_partidos.eliminar_partido(partidos,id_busqueda)
                    case _:
                        print('Opción incorrecta') 
                opcion_partidos = modulo_utiles.mostrar_menu(menu_partidos)
        #Menú resultados



