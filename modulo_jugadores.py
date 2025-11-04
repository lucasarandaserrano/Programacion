#Importación de librerías
import tabulate
import modulo_utiles
import modulo_equipos
#Defino variables
lista_id_j = [0]
lista_equipos = []
#Defino funciones
def crear_jugador(equipos):
    jugador = {}
    #Pido nombre,posicion y id de equipo.
    nombre_jugador = input('Introduzca el nombre del jugador: ') 
    posicion_jugador = input('Introduzca la posición: ')
    id_equipo = int(input('Intropduzca el id del equipo de este jugador: '))
    #Bucle para comprobar que el id existe o si el equipo esta inactivo
    while (id_equipo not in modulo_equipos.lista_id_e) or (equipos[id_equipo - 1]['Activo'] == False):
        print('Este id de equipo no existe o esta inactivo.')
        id_equipo = input('Intropduzca el id del equipo de este jugador: ')
    
    #Al acabar el bucle añadimos los registros al diccionario y devolvemos el diccionario entero
    jugador['ID'] = modulo_utiles.generar_id(lista_id_j)
    jugador['Nombre'] = nombre_jugador
    jugador['Posición'] = posicion_jugador
    jugador['Equipo_ID'] = id_equipo
    jugador['Activo'] = True
    lista_id_j.append(jugador['ID'])
    lista_equipos.append(jugador['Equipo_ID'])
    return jugador

def listar_jugadores(jugadores):
    #Creamos un menú para las opciones de filtrado
    menu_listar = [
        '1. Listar por equipo',
        '2. Listar todos',
        '3. Salir'
    ]
    opción_listar = modulo_utiles.mostrar_menu(menu_listar)
    while (opción_listar != 3):
        match opción_listar:
            #Para filtrar preguntamos primero el id y comprobamos si es correcto y mostramos los jugadores con ese equipo
            case 1:
                id_busqueda = int(input('Introduce el id del equipo por el que quieres filtrar: '))
                while id_busqueda not in lista_equipos:
                    print('ID no encontrado.')
                    id_busqueda = int(input('Introduce el id del equipo por el que quieres filtrar: '))
                filtro = []
                for xequipo in jugadores:
                    if xequipo['Equipo_ID'] == id_busqueda:
                        filtro.append(xequipo)
                print(tabulate.tabulate(filtro))
            #Mostramos todos
            case 2:
                print(tabulate.tabulate(jugadores))
            case _:
                print('Opción incorrecta.')
        opción_listar = modulo_utiles.mostrar_menu(menu_listar)
    print('Saliendo al menú')

def buscar_jugador(jugadores,id_busqueda):
    while (id_busqueda not in lista_id_j):
        print('ID no encontrado')
        id_busqueda = int(input('Introduzca el id de búsqueda: '))
    print(f'Usuario encontrado ---> {jugadores[id_busqueda - 1]}')

def actualizar_jugador(jugadores, id_busqueda, equipos):
    while (id_busqueda not in lista_id_j):
        print('ID no encontrado')
        id_busqueda = int(input('Introduzca el id de búsqueda: '))
    menu_actualizar = [
        '1. Cambiar nombre',
        '2. Cambiar posición',
        '3. Cambiar equipo',
        '4. Salir '
    ]
    opcion_actualizar = modulo_utiles.mostrar_menu(menu_actualizar)
    while (opcion_actualizar != 4):
        match opcion_actualizar:
            case 1:
                nuevo_nombre = input('Introduzca el nuevo nombre para el jugador: ')
                jugadores[id_busqueda - 1]['Nombre'] = nuevo_nombre
                
            case 2:
                nueva_posicion = input('Introduzca la nueva posición para el jugador: ')
                jugadores[id_busqueda - 1]['Posición'] = nueva_posicion
            case 3:
                nuevo_equipo = int(input('Introduce el nuevo id de equipo: '))
                while (nuevo_equipo not in modulo_equipos.lista_id_e) or (equipos[nuevo_equipo - 1]['Activo'] == False):
                    print('Este id de equipo no existe o esta inactivo.')
                    nuevo_equipo = input('Intropduzca el id del equipo de este jugador: ')
                jugadores[id_busqueda -1]['Equipo_ID'] = nuevo_equipo
            case _:
                print('Opción incorrecta.')
        opcion_actualizar = modulo_utiles.mostrar_menu(menu_actualizar)
    print('Saliendo al menú principal...')

def eliminar_jugador(jugadores,id_busqueda):
    while (id_busqueda not in lista_id_j) or (jugadores[id_busqueda - 1]['Activo'] == False):
        print('ID no encontrado o ya eliminado')
        id_busqueda = int(input('Introduzca el id para eliminar: '))
    jugadores[id_busqueda - 1]['Activo'] = False
    print(f'Se ha eliminado el jugador: {jugadores[id_busqueda - 1]}')





        
