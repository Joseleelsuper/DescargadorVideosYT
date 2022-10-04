from pytube import YouTube

#Main
def main():
	#Mensaje de bienvenida
	x = int(input("¿Qué quieres hacer?\n1. Elegir ruta de descarga (obligatorio 1º vez)\n2. Descargar varios vídeos\n3. Salir\n\nElige: "))

	#Elección de lo que hará el programa
	if x == 1:
		ruta_vídeo()
		main()
	elif x == 2:
		descarga_vídeo()
		final()
	elif x == 3:
		exit()
	else:
		print("Opción no válida. Elige un número del 1 al 3.")
		input("Presiona enter para continuar...")
		main()

#Ruta de descarga
def ruta_vídeo():
	SAVE_PATH = input("Introduce la ruta de descarga del vídeo (Ej: C:/Users/Admin User/Downloads): ")
	#crear fichero .txt con la ruta de descarga
	f = open("Ruta de descarga.txt", "w")
	f.write(SAVE_PATH)
	f.close()

#Descargar vídeo
def descarga_vídeo():
	#Creo una lista para guardar los links
	links = []
	#Abrir fichero .txt con la ruta de descarga
	f = open("Ruta de descarga.txt", "r")
	SAVE_PATH = f.read()
	f.close()

	#Preguntar cuántos vídeos se van a descargar
	y = int(input("Número de videos que se van a descargar: "))

	#Preguntar por los links de los vídeos
	for i in range(y):
		x = input(f"Pon el link del vídeo {i+1}: ")
		links.append(x)

	print("\nRecuerda que la descarga puede tardar un rato.")
	
	#Descargar los vídeos
	for i in links:
		try:
			#Comprobar si el vídeo existe o si Youtube está caído
			yt = YouTube(i)
		except:
			print("Hubo algún error bro, pero tiene que ver con la conexión a YouTube o con el link, prueba más tarde.")
			input("Presiona enter para continuar...")
			break
		
		try:
			#Conseguir la resolución de vídeo más alta disponible
			stream = yt.streams.get_highest_resolution()
			#Descargar el video
			print("Descargando: ",yt.title)
			stream.download(SAVE_PATH)
			print("Descarga de "+yt.title+" completada!\n")
		except:
			print("\nHubo algún error bro, mira a ver si el enlace está bien puesto.")
			input("Presiona enter para continuar...")
			break

#Descarga completada
def final():
	#Mensaje de descarga completada
	print("Ya se han descargado todos los vídeos que has puesto.")
	input("Presiona enter para continuar...")
	#Salir del programa
	exit()

#Ejecutar el programa
main()