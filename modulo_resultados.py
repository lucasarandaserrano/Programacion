#Importo librerias
import tabulate
import modulo_utiles
import modulo_equipos
import modulo_partidos
#defino variables

#Defino funciones
def registrar_resultado(resultados,partidos,id_busqueda):
    while (id_busqueda not in modulo_partidos.lista_id_p) or (partidos['Jugado'] == True):
        print('Este partido no existe o ya ha sido jugado.')
        id_busqueda = int(input('Introduce el id de búsqueda para poner resultado: '))
    resultado = (
        int(input('Introduce los goles del equipo local: ')), 
        int(input('Introduce los goles del equipo visitante: '))
        )
    while (resultado[0] < 0):
        print('El contador debe ser positivo.')
        resultado[0] = int(input('Introduce los goles del equipo local: '))
    while (resultado [1] < 0):
        print('El contador debe ser positivo.')
        resultado[1] = int(input('Introduce los goles del equipo visitante: '))
    partidos[id_busqueda - 1]['Resultado'] = resultado
    partidos[id_busqueda - 1]['Jugado'] = True

def clasificar(clasificacion, partidos, equipos):
    estadisticas = {}
    PJ = 0
    G = 0
    E = 0
    P = 0
    GF = 0
    GC = 0
    DG = 0
    PTS = 0
    for partido in partidos:
        if 