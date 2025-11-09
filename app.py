#Importo librerías
import utiles

#Defino variables 
monstruos = { 'vampiro': 3, 'momia': 2, 'bruja': 4, 'esqueleto': 1, 'fantasma': 5 } 
objetos = ['estaca', 'poción mágica', 'hechizo']

#Lógica del programa
mounstro = utiles.mostrar_mounstro(monstruos)

utiles.elegir_objeto(objetos,mounstro,monstruos)
