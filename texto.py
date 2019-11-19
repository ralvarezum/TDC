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
print(resultid, "\n\n",resultusr, "\n\n",resultidc, "\n\n",resultfdc, "\n\n",resultio, "\n\n",resultoo, "\n\n",resultma, "\n\n",resultmc, "\n")

#INFO DE CADA USUARIO
print("\nINFO DETALLADA")#imprime info de cada usuario con sus resp. etiqueta.
print("----------------------------------------------------------------------------------------------------------\n")
for x in range(1,10): 
    print("USUARIO", x)
    print("\n", resultid[0],": ",resultid[x], "\n",resultusr[0],": ",resultusr[x], "\n",resultidc[0],": ",resultidc[x], "\n",resultfdc[0],": ",resultfdc[x], "\n",resultio[0],": ",resultio[x], "\n",resultoo[0],": ",resultoo[x], "\n",resultma[0],": ",resultma[x], "\n",resultmc[0],": ",resultmc[x], "\n")
    print("----------------------------------------------------------------------------------------------------------\n")

#20 usuarios
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
print(resultid, "\n\n",resultusr, "\n\n",resultidc, "\n\n",resultfdc, "\n\n",resultio, "\n\n",resultoo, "\n\n",resultma, "\n\n",resultmc, "\n")

#INFO DE CADA USUARIO
print("\nINFO DETALLADA")#imprime info de cada usuario con sus resp. etiqueta.
print("----------------------------------------------------------------------------------------------------------\n")
for x in range(1,21): #range(x,x) --> cambiar en caso de que haya mas usuarios.
    print("USUARIO", x)
    print("\n", resultid[0],": ",resultid[x], "\n",resultusr[0],": ",resultusr[x], "\n",resultidc[0],": ",resultidc[x], "\n",resultfdc[0],": ",resultfdc[x], "\n",resultio[0],": ",resultio[x], "\n",resultoo[0],": ",resultoo[x], "\n",resultma[0],": ",resultma[x], "\n",resultmc[0],": ",resultmc[x], "\n")
    print("----------------------------------------------------------------------------------------------------------\n")