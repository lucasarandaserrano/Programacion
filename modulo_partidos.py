#Importación de librerias
import modulo_utiles
import modulo_equipos
import tabulate
lista_id_p = []
lista_jornadas = []
def crear_partido(equipos):
    partido = {}
    jornada = int(input('Introduce un número de jornada: '))
    while (jornada <1):
        print('La jornada debe ser mayor o igual a 1 o no debe estar establecida ya.')
        jornada = int(input('Introduce un número de jornada: '))

    local_id = int(input('Introduce el id del equipo local: '))
    while (local_id not in modulo_equipos.lista_id_e) or (equipos[local_id - 1]['Activo'] == False):
        print('El equipo no existe o esta inactivo.')
        local_id = int(input('Introduce el id del equipo local: '))

    visitante_id = int(input('Introduce el id del equipo visitante: '))
    while (visitante_id not in modulo_equipos.lista_id_e) or (equipos[visitante_id - 1]['Activo'] == False) or (local_id == visitante_id):
        if (visitante_id not in modulo_equipos.lista_id_e) or (equipos[visitante_id - 1]['Activo'] == False):
            print('El equipo no existe o esta inactivo.')
        else:
            print('El equipo visitante no puede ser el mismo que el local.')
        visitante_id = int(input('Introduce el id del equipo visitante: '))
    fecha = input('Introduzca la fecha en formato(DD/MM/AAAA): ')
    hora = input('Introduce la hora en formato (HH:MM): ' )

    partido['ID'] = modulo_utiles.generar_id(lista_id_p)
    partido['Jornada'] = jornada
    partido['local_id'] = local_id
    partido['visitante_id'] = visitante_id
    partido['Fecha'] = fecha
    partido['Hora'] = hora
    partido['Jugado'] = False
    partido['Resultado'] = None

    lista_jornadas.append(jornada)
    lista_id_p.append(partido['ID'])
    return partido

def listar_partidos(partidos):
    menu_filtrar = [
        '1. Filtrar por jornada',
        '2. Mostrar todos',
        '3. Salir'
    ]

    opcion_filtrar = modulo_utiles.mostrar_menu(menu_filtrar)
    while (opcion_filtrar != 3):
        match opcion_filtrar:
            case 1:
                buscar_jornada = int(input('Introduzca la jornada para ver sus partidos: '))
                if buscar_jornada not in lista_jornadas:
                    print('Jornada no encontrada.')
                else:
                    filtro_lista = []
                    for filtro in partidos:
                        if filtro['Jornada'] == buscar_jornada:
                            filtro_lista.append(filtro)
                    print(tabulate.tabulate(filtro_lista, headers=['ID', 'Jornada', 'Local', 'Visitante', 'Fecha', 'Hora', 'Jugado', 'Resultado']))
            case 2:
                print(tabulate.tabulate(partidos, headers=['ID', 'Jornada', 'Local', 'Visitante', 'Fecha', 'Hora', 'Jugado', 'Resultado']))
            case _ :
                print('Opción no disponible.')
        opcion_filtrar = modulo_utiles.mostrar_menu(menu_filtrar)
    print('Saliendo al menú PARTIDOS...')

def reprogramar_partido(partidos,id_busqueda):
    while (id_busqueda not in lista_id_p):
        print('Partido no encontrado.')
    menu_reprogramar = [
        '1. Cambiar fecha',
        '2. Cambiar hora',
        '3. Salir'
    ]

    opcion_reprogramar = modulo_utiles.mostrar_menu(menu_reprogramar)
    while (opcion_reprogramar != 3):
        match opcion_reprogramar:
            case 1:
               nueva_fecha = input('Introduzca la nueva fecha en formato(DD/MM/AAAA): ')
               partidos[id_busqueda - 1]['Fecha'] = nueva_fecha
               print('Se actualizó la fecha del partido')
            case 2:
                nueva_hora = input('Introduce la nueva hora en formato (HH:MM): ' ) 
                partidos[id_busqueda - 1]['Hora'] = nueva_hora
                print('Se actualizó la hora del partido')
            case _:
                print('Opción no encontrada.')
        opcion_reprogramar = modulo_utiles.mostrar_menu(menu_reprogramar)
    print('Saliendo al menú PARTIDOS...')

def eliminar_partido(partidos,id_busqueda):
    while (id_busqueda not in lista_id_p) or (partidos[id_busqueda - 1]['Jugado'] == True):
        print('Partido no encontrado.')
    
    print(f'Se eliminó el siguiente partido {partidos[id_busqueda - 1]}')
    partidos.remove(id_busqueda - 1)
    lista_id_p.remove(id_busqueda - 1)

    
