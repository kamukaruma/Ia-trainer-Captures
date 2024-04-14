import cv2
import imutils
import os

DatosP = "p"
DatosN = "n"

if not os.path.exists(DatosP):
    print("Carpeta creada", DatosP)
    os.mkdir(DatosP)

if not os.path.exists(DatosN):
    print("Carpeta creada", DatosN)
    os.mkdir(DatosN)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0

while True:
    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto, width=38)

    cv2.imshow('frame' ,frame)
    cv2.imshow('objeto' ,objeto)

    k = cv2.waitKey(1)
    if k ==  27:
        break

    if k == ord('p'):
        cv2.imwrite(DatosP+'/objeto_{}.jpg'.format(count), objeto)
        print('Imagen almacenada positiva: ', '/objeto_{}.jpg'.format(count))
        count = count + 1

    if k == ord('n'):
        cv2.imwrite(DatosN+'/objeto_{}.jpg'.format(count), objeto)
        print('Imagen almacenada negativa: ', '/objeto_{}.jpg'.format(count))
        count = count + 1

cap.release()
cv2.destroyAllWindows()
