
"""
#9 usuarios
#SEPARACION DE CADA ETIQUETA
f=open('text.txt',"r")
linesf=f.readlines()
resultid=[]
resultusr=[]
resultidc=[]
resultfdc=[]
resultst=[]
resultio=[]
resultoo=[]
resultma=[]
resultmc=[]
for x in linesf: #Guardo la info. en diferentes listas
    resultid.append(x.split(';')[0])
    resultusr.append(x.split(';')[1])
    resultidc.append(x.split(';')[2])
    resultfdc.append(x.split(';')[3])
    resultst.append(x.split(';')[4])
    resultio.append(x.split(';')[5])
    resultoo.append(x.split(';')[6])
    resultma.append(x.split(';')[7])
    resultmc.append(x.split(';')[8])
f.close()
print("INFO GENERAL") #imprime los valores de cada lista
print("----------------------------------------------------------------------------------------------------------\n")
print(resultid, "\n\n",resultusr, "\n\n",resultidc, "\n\n",resultfdc, "\n\n",resultst, "\n\n",resultio, "\n\n",resultoo, "\n\n",resultma, "\n\n",resultmc, "\n")
print("----------------------------------------------------------------------------------------------------------\n")

#INFO DE CADA USUARIO
print("\nINFO DETALLADA")#imprime info de cada usuario con sus resp. etiqueta.
print("----------------------------------------------------------------------------------------------------------\n")
for x in range(1,len(linesf),1):
    print("USUARIO", x)
    print("\n" + resultid[0] + ": " + resultid[x] + "\n" + resultusr[0] + ": " + resultusr[x] +  "\n" + resultidc[0] + ": " + resultidc[x] + "\n" + resultfdc[0] + ": " + resultfdc[x] + "\n" + resultst[0] + ": " + resultst[x] +  "\n" + resultio[0] + ": " + resultio[x] + "\n" + resultoo[0] + ": " + resultoo[x] + "\n" + resultma[0] + ": " + resultma[x] +  "\n" + resultmc[0] + ": " + resultmc[x] +  "\n")
    print("----------------------------------------------------------------------------------------------------------\n")

#29 usuarios
#SEPARACION DE CADA ETIQUETA
f=open('text2.txt',"r")
linesf=f.readlines()
resultid=[]
resultusr=[]
resultidc=[]
resultfdc=[]
resultst=[]
resultio=[]
resultoo=[]
resultma=[]
resultmc=[]
for x in linesf: #Guardo la info. en diferentes listas
    resultid.append(x.split(';')[0])
    resultusr.append(x.split(';')[1])
    resultidc.append(x.split(';')[2])
    resultfdc.append(x.split(';')[3])
    resultst.append(x.split(';')[4])
    resultio.append(x.split(';')[5])
    resultoo.append(x.split(';')[6])
    resultma.append(x.split(';')[7])
    resultmc.append(x.split(';')[8])
f.close()
print("INFO GENERAL") #imprime los valores de cada lista
print("----------------------------------------------------------------------------------------------------------\n")
print(resultid, "\n\n",resultusr, "\n\n",resultidc, "\n\n",resultfdc, "\n\n",resultst, "\n\n",resultio, "\n\n",resultoo, "\n\n",resultma, "\n\n",resultmc, "\n")
print("----------------------------------------------------------------------------------------------------------\n")

#INFO DE CADA USUARIO
print("\nINFO DETALLADA")#imprime info de cada usuario con sus resp. etiqueta.
print("----------------------------------------------------------------------------------------------------------\n")
for x in range(1,len(linesf),1):
    print("USUARIO", x)
    print("\n" + resultid[0] + ": " + resultid[x] + "\n" + resultusr[0] + ": " + resultusr[x] +  "\n" + resultidc[0] + ": " + resultidc[x] + "\n" + resultfdc[0] + ": " + resultfdc[x] + "\n" + resultst[0] + ": " + resultst[x] +  "\n" + resultio[0] + ": " + resultio[x] + "\n" + resultoo[0] + ": " + resultoo[x] + "\n" + resultma[0] + ": " + resultma[x] +  "\n" + resultmc[0] + ": " + resultmc[x] +  "\n")
    print("----------------------------------------------------------------------------------------------------------\n")
"""
#Funciona con cualquier cantidad de usuarios
text = input("Ingrese el nombre del archivo: ")
f=open(text,"r")
linesf=f.readlines()
resultid=[]
resultusr=[]
resultidc=[]
resultfdc=[]
resultst=[]
resultio=[]
resultoo=[]
resultma=[]
resultmc=[]
for x in linesf: #Guardo la info. en diferentes listas
    resultid.append(x.split(';')[0])
    resultusr.append(x.split(';')[1])
    resultidc.append(x.split(';')[2])
    resultfdc.append(x.split(';')[3])
    resultst.append(x.split(';')[4])
    resultio.append(x.split(';')[5])
    resultoo.append(x.split(';')[6])
    resultma.append(x.split(';')[7])
    resultmc.append(x.split(';')[8])
f.close()
print("INFO GENERAL") #imprime los valores de cada lista
print("----------------------------------------------------------------------------------------------------------\n")
print(resultid, "\n\n",resultusr, "\n\n",resultidc, "\n\n",resultfdc, "\n\n",resultst, "\n\n",resultio, "\n\n",resultoo, "\n\n",resultma, "\n\n",resultmc, "\n")
print("----------------------------------------------------------------------------------------------------------\n")

#INFO DE CADA USUARIO
print("\nINFO DETALLADA")#imprime info de cada usuario con sus resp. etiqueta.
print("----------------------------------------------------------------------------------------------------------\n")
for x in range(1,len(linesf),1):
    print("USUARIO", x)
    print("\n" + resultid[0] + ": " + resultid[x] + "\n" + resultusr[0] + ": " + resultusr[x] +  "\n" + resultidc[0] + ": " + resultidc[x] + "\n" + resultfdc[0] + ": " + resultfdc[x] + "\n" + resultst[0] + ": " + resultst[x] +  "\n" + resultio[0] + ": " + resultio[x] + "\n" + resultoo[0] + ": " + resultoo[x] + "\n" + resultma[0] + ": " + resultma[x] +  "\n" + resultmc[0] + ": " + resultmc[x] +  "\n")
    print("----------------------------------------------------------------------------------------------------------\n")
