#Importación de librerías
import tabulate
import modulo_utiles
import modulo_jugadores
#Defino variables
lista_id_e = [0]
#Defino funciones
def crear_equipo():
    equipo = {}
    #Pido nombre y ciudad y guardo en variables
    nombre_equipo = input('Introduzca el nombre del equipo: ') 
    ciudad_equipo = input('Introduzca de que ciudad es este equipo: ')
    
    #Creo claves y valores del diccionario
    equipo['ID'] = modulo_utiles.generar_id(lista_id_e)
    equipo['Nombre'] = nombre_equipo
    equipo['Ciudad'] = ciudad_equipo
    equipo['Activo'] = True
    lista_id_e.append(equipo['ID'])
    return equipo

def listar_equipos(equipos):
    equipo_actv = []
    for actv in equipos:
        if actv['Activo'] == True:
            equipo_actv.append(actv)
    print(tabulate.tabulate(equipo_actv))

def buscar_id_equipo(equipos, id_busqueda):
    #Comprobamos si el id pedido en el main esta en la lista de ids.
    if (id_busqueda in lista_id_e) and (id_busqueda != 0):
        print(f'Su equipo buscado: {equipos[id_busqueda - 1]}')
    else:
        print('No encontrado')

def actualizar_equipo(equipos, id_busqueda):
    #Condición para saber si el id esta en la lista
    if (id_busqueda in lista_id_e) and (id_busqueda != 0):
        #Creamos menú para actualizar y preguntamos opción
        menu_actualizar = [
            '1. Nombre',
            '2. Ciudad'
            '3. Salir'
        ]
        opcion_actualizar = modulo_utiles.mostrar_menu(menu_actualizar)
        #Bucle para actualizar 
        while (opcion_actualizar != 3):
            match opcion_actualizar:
                case 1:
                    nuevo_nombre = input('Introduce el nuvo nombre del equipo: ')
                    equipos[id_busqueda - 1]['Nombre'] = nuevo_nombre
                case 2: 
                    nueva_ciudad = input('Introduce la nueva ciudad: ')
                    equipos[id_busqueda - 1]['Ciudad'] = nueva_ciudad
                case _:
                    print('Introduzca una opción del menú.')
    else: 
        print('No encontrado.')
def eliminar_equipo(equipos,id_busqueda,jugadores):
    while (id_busqueda not in lista_id_e) or (equipos[id_busqueda - 1]['Activo'] == False):
        print('ID no encontrado o ya eliminado.')
        id_busqueda = int(input('Introduzca el id para eliminar: '))
    #Bucle para comprobar si el equipo tiene jugadores
    while (id_busqueda in modulo_jugadores.lista_equipos):
        print('Este equipo tiene jugadores y no puede ser borrado.')
        id_busqueda = int(input('Introduzca el id para eliminar: '))
    equipos[id_busqueda - 1]['Activo'] = False
    print(f'Se ha eliminado el equipo: {equipos[id_busqueda - 1]}')

        
    

