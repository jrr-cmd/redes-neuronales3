#------------------------------Se importan las librerias -----------------------
from xml.etree.ElementTree import tostring
import cv2
import Informacion_manos as im #Programa el cual contiene la deteccion y seguimiento de manos
import os

#---------------------------------------Se crea la carpeta donde se almacenara el entrenamiento ----------------
nombre = input('Ingrese el nombre del objeto: ')
direccion = 'Fotos/Entrenamiento'
carpeta = direccion + '/' + nombre
if not os.path.exists(carpeta):
    print('carpeta creada: ', carpeta)
    os.makedirs(carpeta)

#Se asigna un contador para el nombre de la fotos
cont = 0

#---------------------------------- Declaracion de variables -------------------------
anchocam, altocam = 640, 480


#--------------------------------- Lectura de Camara -----------------------------------
cap = cv2.VideoCapture(0)
cap.set(3,anchocam) # Se define el ancho y alto definido para siempre
cap.set(4,altocam)


#-----------------------------------------Se declara el detector -----------------------
detector = im.detectormanos(maxManos=1, Confdeteccion=0.7)  #Solo se utilizara una mano


while True:
    #------------------------------------ Vamos a encontrar los puntos de la mano---------------------
    ret, frame = cap.read()
    manos = detector.encontrarmanos(frame) # Encontramos las manos
    lista, bbox = detector.encontrarposicion(frame) # Se muestra las posiciones
    if len(lista) != 0:
        x1 = bbox[0]
        y1 = bbox[1]
        x2 = bbox[2]
        y2 = bbox[3]
        data = frame[y1:y2,x1:x2]
        obje = cv2.resize(data, (200,200), interpolation=cv2.INTER_CUBIC) # Se redimenciona las fotos
        cv2.imwrite(carpeta + "/Objeto_{}.jpg".format(cont), obje)
        cont = cont + 1




        cv2.imshow("Base Datos", frame)
        k = cv2.waitKey(1)
        if k == 27 or cont >= 300:
            break
cap.release()
cv2.destroyAllWindows()