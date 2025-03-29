import cv2
import numpy as np
from PIL import Image
import math
import openpyxl

# Frekfencija vraca broj koji se nalazi na slici
def prepoznajBroj(frame, x1, y1, x2, y2):
        slika = kropujSliku(frame, x1, y1, x2, y2)
        broj = pogodiBroj(slika)
        return broj
    

# Funkcija koja za unetu sliku pogadja koji je broj
def pogodiBroj(slika):
    slika = cv2.cvtColor(slika, cv2.COLOR_BGR2GRAY)
    slika = np.array(slika)

    res1 = cv2.matchTemplate(slika, broj1, cv2.TM_CCOEFF_NORMED)
    minVal1, maxVal1, minLoc1, maxLoc1 = cv2.minMaxLoc(res1)
    res2 = cv2.matchTemplate(slika, broj2, cv2.TM_CCOEFF_NORMED)
    minVal2, maxVal2, minLoc2, maxLoc2 = cv2.minMaxLoc(res2)
    res3 = cv2.matchTemplate(slika, broj3, cv2.TM_CCOEFF_NORMED)
    minVal3, maxVal3, minLoc3, maxLoc3 = cv2.minMaxLoc(res3)
    res4 = cv2.matchTemplate(slika, broj4, cv2.TM_CCOEFF_NORMED)
    minVal4, maxVal4, minLoc4, maxLoc4 = cv2.minMaxLoc(res4)
    res5 = cv2.matchTemplate(slika, broj5, cv2.TM_CCOEFF_NORMED)
    minVal5, maxVal5, minLoc5, maxLoc5 = cv2.minMaxLoc(res5)
    res6 = cv2.matchTemplate(slika, broj6, cv2.TM_CCOEFF_NORMED)
    minVal6, maxVal6, minLoc6, maxLoc6 = cv2.minMaxLoc(res6)
    res7 = cv2.matchTemplate(slika, broj7, cv2.TM_CCOEFF_NORMED)
    minVal7, maxVal7, minLoc7, maxLoc7 = cv2.minMaxLoc(res7)
    res8 = cv2.matchTemplate(slika, broj8, cv2.TM_CCOEFF_NORMED)
    minVal8, maxVal8, minLoc8, maxLoc8 = cv2.minMaxLoc(res8)
    res9 = cv2.matchTemplate(slika, broj9, cv2.TM_CCOEFF_NORMED)
    minVal9, maxVal9, minLoc9, maxLoc9 = cv2.minMaxLoc(res9)
    res0 = cv2.matchTemplate(slika, broj0, cv2.TM_CCOEFF_NORMED)
    minVal0, maxVal0, minLoc0, maxLoc0 = cv2.minMaxLoc(res0)

    maxVal = {maxVal1, maxVal2, maxVal3, maxVal4, maxVal5, maxVal6, maxVal7, maxVal8, maxVal9, maxVal0}


    if max(maxVal) == maxVal0 or max(maxVal) < 0.75:
         return '0'
    elif max(maxVal) == maxVal5:
         return '5'
    elif max(maxVal) == maxVal1:
         return '1'
    elif max(maxVal) == maxVal2:
         return '2'
    elif max(maxVal) == maxVal3:
         return '3'
    elif max(maxVal) == maxVal4:
         return '4'
    elif max(maxVal) == maxVal6:
         return '6'
    elif max(maxVal) == maxVal7:
         return '7'
    elif max(maxVal) == maxVal8:
         return '8'
    elif max(maxVal) == maxVal9:
         return '9'


# Cuva kropovanu sliku krpopvanu sliku, za date kordinate
def kropujSliku(slika,x1,y1,x2,y2):
    slika1 = Image.fromarray(slika)
    kropovanaSlika = slika1.crop((x1,y1,x2,y2))
    kropovanaSlika = np.array(kropovanaSlika)
    cv2.imwrite('kropovanaSlika.jpg', kropovanaSlika)
    return kropovanaSlika

Fp = 93.1
Fm = 95.25

# Otvaranje video fajla
video = cv2.VideoCapture('video15fps.mp4')

# Provera da li je fajl uspešno otvoren
if not video.isOpened():
    print("Greška pri otvaranju fajla")

# Inicijalizacija listi za cuvanje vrednosti 
niz1 = [] 
niz2 = []

# Inicijalizacija mesta za cuvanje prethodnih brojeva
prethodniBroj1 = None
prethodniBroj2 = None

# Brojevi za poredjenje
broj1 = cv2.imread("broj1.jpg")
broj1 = cv2.cvtColor(broj1, cv2.COLOR_BGR2GRAY)
broj1 = np.array(broj1)
broj2 = cv2.imread('broj2.jpg')
broj2 = cv2.cvtColor(broj2, cv2.COLOR_BGR2GRAY)
broj2 = np.array(broj2)
broj3 = cv2.imread('broj3.jpg')
broj3 = cv2.cvtColor(broj3, cv2.COLOR_BGR2GRAY)
broj3 = np.array(broj3)
broj4 = cv2.imread('broj4.jpg')
broj4 = cv2.cvtColor(broj4, cv2.COLOR_BGR2GRAY)
broj4 = np.array(broj4)
broj5 = cv2.imread('broj5.jpg')
broj5 = cv2.cvtColor(broj5, cv2.COLOR_BGR2GRAY)
broj5 = np.array(broj5)
broj6 = cv2.imread('broj6.jpg')
broj6 = cv2.cvtColor(broj6, cv2.COLOR_BGR2GRAY)
broj6 = np.array(broj6)
broj7 = cv2.imread('broj7.jpg')
broj7 = cv2.cvtColor(broj7, cv2.COLOR_BGR2GRAY)
broj7 = np.array(broj7)
broj8 = cv2.imread('broj8.jpg')
broj8 = cv2.cvtColor(broj8, cv2.COLOR_BGR2GRAY)
broj8 = np.array(broj8)
broj9 = cv2.imread('broj9.jpg')
broj9 = cv2.cvtColor(broj9, cv2.COLOR_BGR2GRAY)
broj9 = np.array(broj9)
broj0 = cv2.imread('broj0.jpg')
broj0 = cv2.cvtColor(broj0, cv2.COLOR_BGR2GRAY)
broj0 = np.array(broj0)


# Inicijalizacija pozicija pravougaonika     /Podesiti vrednosti/

x11, y11, x12, y12 = 256, 41, 282, 90
x21, y21, x22, y22 = 284, 41, 310, 90
x31, y31, x32, y32 = 340, 41, 366, 90
x41, y41, x42, y42 = 368, 41, 394, 90
x51, y51, x52, y52 = 943, 40, 969, 89
x61, y61, x62, y62 = 971, 40, 997, 89
x71, y71, x72, y72 = 1027, 40, 1053, 89
x81, y81, x82, y82 = 1055, 40, 1081, 89
x91, y91, x92, y92 = 1083, 40, 1109, 89

# Petlja koja se izvršava sve dok postoje frejmovi u videu
while video.isOpened():
    # Čitanje sledećeg frejma
    ret, frame = video.read()

    # Provera da li je frejm uspešno pročitan
    if ret:
        # Ocitavanje vrednosti sa frejma
        broj11 = prepoznajBroj(frame, x11, y11, x12, y12)
        broj12 = prepoznajBroj(frame, x21, y21, x22, y22)
        broj13 = prepoznajBroj(frame, x31, y31, x32, y32)
        broj14 = prepoznajBroj(frame, x41, y41, x42, y42)
        broj15 = prepoznajBroj(frame, x51, y51, x52, y52)
        broj16 = prepoznajBroj(frame, x61, y61, x62, y62)
        broj17 = prepoznajBroj(frame, x71, y71, x72, y72)
        broj18 = prepoznajBroj(frame, x81, y81, x82, y82)
        broj19 = prepoznajBroj(frame, x91, y91, x92, y92)
        
        vrednost1 = broj11 + broj12 + '.' + broj13 + broj14
        vrednost2 = broj15 + broj16 + '.' + broj17 + broj18 + broj19
        
        if (prethodniBroj1 is None or prethodniBroj1 != float(vrednost1)) and (prethodniBroj2 is None or prethodniBroj2 != float(vrednost2)):
            vrednost1 = float(vrednost1)
            vrednost2 = float(vrednost2)

            niz1.append(vrednost1)
            niz2.append(vrednost2)

            prethodniBroj1 = vrednost1
            prethodniBroj2 = vrednost2


        # Crtanje pravougaonika na brojevima
        cv2.rectangle(frame, (x11,y11), (x12,y12), (0 ,255, 0))
        cv2.rectangle(frame, (x21,y21), (x22,y22), (0 ,255, 0))
        cv2.rectangle(frame, (x31,y31), (x32,y32), (0 ,255, 0))
        cv2.rectangle(frame, (x41,y41), (x42,y42), (0 ,255, 0))
        cv2.rectangle(frame, (x51,y51), (x52,y52), (0 ,255, 0))
        cv2.rectangle(frame, (x51,y51), (x52,y52), (0 ,255, 0))
        cv2.rectangle(frame, (x61,y61), (x62,y62), (0 ,255, 0))
        cv2.rectangle(frame, (x71,y71), (x72,y72), (0 ,255, 0))
        cv2.rectangle(frame, (x81,y81), (x82,y82), (0 ,255, 0))
        cv2.rectangle(frame, (x91,y91), (x92,y92), (0 ,255, 0))


        # Prikaz frejma
        cv2.imshow('Automatsko prepoznavanje brojeva', frame)

        # Čekanje na pritisak tastera 'q' za izlazak iz petlje
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Oslobađanje resursa
video.release()
cv2.destroyAllWindows()

Lm = None
Lp = None

for i in range(len(niz1)):
     if(Fp == niz1[i]):
          Lp = niz2[i]
          break

     elif Fp < niz1[i]:
          k = round((niz2[i+1]-niz2[i])/(niz1[i+1]-niz1[i]),8)
          n = niz2[i+1]-k*niz1[i+1]
          Lp = k*Fp + n
          break

for i in range(len(niz1)):
     if(Fm == niz1[i]):
          Lm = niz2[i]
          break

     elif Fm < niz1[i]:
          k = round((niz2[i+1]-niz2[i])/(niz1[i+1]-niz1[i]),8)
          n = niz2[i+1]-k*niz1[i+1]
          Lm = k*Fm + n
          print(round(Lm,3))
          break

izv1 = []
izv2 = []

for j in range(1, math.floor(Fm/5) + 1):
     for i in range(len(niz1)):
          if(j*5 == niz1[i]):
               izv1.append(niz1[i])
               izv2.append(niz2[i])
               break

          elif j*5 < niz1[i]:
               k = round((niz2[i+1]-niz2[i])/(niz1[i+1]-niz1[i]),8)
               n = niz2[i+1]-k*niz1[i+1]
               izv1.append(j*5)
               izv2.append(round(k*j*5 + n,3))
               break

# Stvaramo novu radnu knjigu
wb1 = openpyxl.Workbook()
wb2 = openpyxl.Workbook()

# Odabiremo aktivni list u radnoj knjizi
sheet1 = wb1.active
sheet1.append(['Sila', 'Ugib'])
sheet1.append(['kN', 'mm'])

for i in range(len(izv1)):
     sheet1.append([izv1[i], izv2[i]])

sheet1.append([])
sheet1.append(['Fp'])
sheet1.append([Fp, Lp])
sheet1.append(['Fm'])
sheet1.append([Fm,Lm])

sheet2 = wb2.active

for i in range(len(niz1)):
     sheet2.append([niz1[i], niz2[i]])

wb1.save('Izvestaj.xlsx')
wb2.save('Kontrolna tabela.xlsx')