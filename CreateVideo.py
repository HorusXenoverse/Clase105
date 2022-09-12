from email.mime import image
import os
from tkinter import Frame
from turtle import shape, width
import cv2


path = "D:/Proyectos de la escuela/Quinta etapa/Clase 105/PROC105-V1-actividad-alumno1-main/PROC105-V1-actividad-alumno1-main/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

readPrimeraImagen = cv2.imread(images[0])
height, width, channels = readPrimeraImagen.shape
size = (width, height)
print(size)
      
     #LLeva 4 parámetros  "Nombre.mp4"    cv2.VideoWriter_fourcc(*"DIVX") fotogramas size(El tamaño guardado)
writeVideo = cv2.VideoWriter("Video.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 10, size)

                    #Primer valor, desde donde empieza, hasta donde termina o hasta donde se va a repetir, de cuanto en cuanto se va a ir repitiendo
for amanecer in range(0, count, 1):
    frame = cv2.imread(images[amanecer])
    writeVideo.write(frame)
writeVideo.release()
print("Listo")