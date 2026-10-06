# Angela Correa NC = 0037
# Número de lista =  14
print("EJEMPLO 1 — Detección de bordes con Canny")
print("+--++-+-+-+-+-+-")
import cv2

# Cargar la imagen
imagen = cv2.imread("jaguar.jpg")

# Comprobar que la imagen fue cargada
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes mediante Canny
bordes = cv2.Canny(gris, 100, 200)

# Mostrar resultados
cv2.imshow("Imagen original jaguar 0037", imagen)
cv2.imshow("Imagen en escala de grises jaguar 0037", gris)
cv2.imshow("Bordes Canny jaguar 0037", bordes)

# Guardar resultado
cv2.imwrite("jaguar resultado ejemplo 1.jpg", bordes)

print("Detección de bordes completada.")
print("Resultado guardado en jaguar resultado ejemplo 1.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Angela Correa NC = 0037")