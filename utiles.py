#Importación de librerías
import random
#Defino variables
suma_objetos = {
    'estaca':0.4,
    'poción mágica':0.2,
    'hechizo':0.1
}

#Definición de funciones
def mostrar_mounstro(mounstros):
    monstruo = random.choice(list(mounstros.keys()))
    print('-------------------------------------------------')
    print(f'Te has encontrado con un {monstruo} con dificultad {mounstros[monstruo]} |')
    print('-------------------------------------------------')
    return monstruo

def elegir_objeto(objetos,mounstro,mounstros):
    print('\n')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(f'Tienes 3 intentos restantes')
    objeto = input(f'Elige un objeto para cazar a {mounstro}(estaca, poción mágica, hechizo): ')
    while (objeto not in objetos):
        print('Objeto incorrecto.')
        objeto = input(f'Elige un objeto para cazar a {mounstro}(estaca, poción mágica, hechizo): ')
    #Divido la dificultad de captura entre uno para que cuanto más dificil menor sea el número
    probabilidad = float(1 / mounstros[mounstro])
    #Uso min con un 0,95 por si sale 1 de dificultad no sea mas de 100% de probabilidad
    prob_final = min(probabilidad + suma_objetos[objeto],0.95)
    if random.random() < prob_final:
        print(f'Felicidades!!! Has cazado a {mounstro} con {objeto}.')
    else:
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(f'No has podido cazar a {mounstro} con {objeto}')
        print('Tienes 2 intentos restantes')
        objeto = input(f'Elige un objeto para cazar a {mounstro}(estaca, poción mágica, hechizo): ')
        while (objeto not in objetos):
            print('Objeto incorrecto.')
            objeto = input(f'Elige un objeto para cazar a {mounstro}(estaca, poción mágica, hechizo): ')
        #Divido la dificultad de captura entre uno para que cuanto más dificil menor sea el número
        probabilidad = float(1 / mounstros[mounstro])
        #Uso min con un 0,95 por si sale 1 de dificultad no sea mas de 100% de probabilidad
        prob_final = min(probabilidad + suma_objetos[objeto],0.95)
        if random.random() < prob_final:
            print(f'Felicidades!!! Has cazado a {mounstro} con {objeto}.')
        else:
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(f'No has podido cazar a {mounstro} con {objeto}')
            print('Tienes 1 intento restantes')
            objeto = input(f'Elige un objeto para cazar a {mounstro}(estaca, poción mágica, hechizo): ')
            while (objeto not in objetos):
                print('Objeto incorrecto.')
                objeto = input(f'Elige un objeto para cazar a {mounstro}(estaca, poción mágica, hechizo): ')
            #Divido la dificultad de captura entre uno para que cuanto más dificil menor sea el número
            probabilidad = float(1 / mounstros[mounstro])
            #Uso min con un 0,95 por si sale 1 de dificultad no sea mas de 100% de probabilidad
            prob_final = min(probabilidad + suma_objetos[objeto],0.95)
            if random.random() < prob_final:
                print(f'Felicidades!!! Has cazado a {mounstro} con {objeto}.')
            else:
                print('No has podidio cazar el mounstro. Otra vez será!')
        
    
