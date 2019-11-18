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
print("\nINFO GENERAL") #imprime los valores de cada lista
print("\n", resultid, "\n",resultusr, "\n",resultidc, "\n",resultfdc, "\n",resultio, "\n",resultoo, "\n",resultma, "\n",resultmc, "\n")

#INFO DE CADA USUARIO
for x in range(1,10): 
    print("USUARIO", x) #imprime info de cada usuario con sus resp. etiqueta.
    print("\n", resultid[0],": ",resultid[x], "\n",resultusr[0],": ",resultusr[x], "\n",resultidc[0],": ",resultidc[x], "\n",resultfdc[0],": ",resultfdc[x], "\n",resultio[0],": ",resultio[x], "\n",resultoo[0],": ",resultoo[x], "\n",resultma[0],": ",resultma[x], "\n",resultmc[0],": ",resultmc[x], "\n")