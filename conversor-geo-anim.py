it1=0
Ficheiro = [0]
unida=str(1000) #1000=metros, 1=mm

from tkinter import filedialog
from tkinter import Tk
from tkinter import *
import os

def root(what):

    root = Tk()
    # root.iconbitmap("c:/...") # Defenição Icon
    root.fileName = filedialog.askopenfilename(title=what)

    return root.fileName

#### TENTAR

Lista = root("Select Geometry file")
cor=root("Select Color file")
anima=root("Select Animation file")

open(str(Lista),"r") # MANDA ERRO CASO NÃO HAJA FI
open(str(cor),"r")
open(str(anima),"r")

abrir_lista = open(str(Lista), "r")

#####SEPARÇÃO ENTRE CAMINHO E NOME DE FICHEIRO ##################
path, filename = os.path.split(Lista)

vetor1 = [0]
it5=0
it51 = 0
it512 = 0
for abrir1 in abrir_lista.readlines():
    vetor1.insert(it5, abrir1.split(' '))
    vetor1[it5][:] = [x for x in vetor1[it5] if x]  # REMOÇÃO DE CÉLULAS VAZIAS
    if len(vetor1[it5]) == 1:
        it51 = it5 - it512
        it512 = it512 + 1
    it5 = it5 + 1
Ficheiro = vetor1[it51:it51+it512]

#FUNCÃO DE SELEÇÃO DE COR
def selcolor(num):
   import colorsys
   abrir_cores = open(cor, "r")
   vetor2 = [0]
   it2 = 0
   it21 = 0
   it212 = 0
   for abrir2 in abrir_cores.readlines():
       vetor2.insert(it2, abrir2.split(','))
       vetor2[it2][:] = [x for x in vetor2[it2] if x]  # REMOÇÃO DE CÉLULAS VAZIAS
       if len(vetor2[it2]) == 4:
           it21 = it2 - it212
           it212 = it212 + 1
       it2 = it2 + 1
   vetorcolor = vetor2[it21:it21+it212]

   it23=-1

   for selec in range(len(vetorcolor)):
       it23=it23+1
       if (abs(num)-90000) == int(vetorcolor[it23][0]):
           red = vetorcolor[it23][-3]
           green = vetorcolor[it23][-2]
           blue = vetorcolor[it23][-1]

   return (round((int(red)/255),2),round((int(green)/255),2),round((int(blue)/255),2))

Nome1=os.path.basename(Lista)
correc3=""
for carac3 in (Nome1):
    if carac3 in ".":
        correc3 = correc3 + ""
    else:
        correc3 = correc3 + carac3
Nome1=correc3+"global"

novo_ficheiro = open(path+Nome1 + "conv.FCMacro", "w")
novo_ficheiro.write("Gui.activateWorkbench(\"Assembly4Workbench\")")
novo_ficheiro.write("\nApp.newDocument(\"" + Nome1 + "\")")
novo_ficheiro.write("\nimport Mesh")
itit = -1
novo_ficheiro.write("\nprint(\"Progresso... " + str(itit+1) + " de "+ str(len(Ficheiro)) +"\")")

#POSICIONAMENTO INICIAL



novo_ficheiro1 = open(Nome1 + "anim.FCMacro", "w")
abrir_lista2 = open(str(anima), "r")

vetor15 = [0]
it55=0

for abrir2 in abrir_lista2.readlines():
    vetor15.insert(it55, abrir2.split(' '))
    vetor15[it55][:] = [x for x in vetor15[it55] if x]  # REMOÇÃO DE CÉLULAS VAZIAS

    it55 = it55 + 1
vetorm = vetor15[1:-1]

vetormat=[0]*int(len(vetorm)/4)
Matrix=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
#print(Matrix)
#print(vetorm)
it9=-1
it93=0
for itm in range(len(vetormat)):
    Matrix = [["", "", "", str(unida)+"*"], #MATRIZ DO FREECAD TEM AS LINHA TROCADAS COM AS COLUNAS
              ["", "", "", str(unida)+"*"],
              ["", "", "", str(unida)+"*"],
              ["", "", "", ""]]
    it91=-1

    for itm2 in range(0,4):
        it91 = it91 + 1
        it92 = -1
        for itm3 in range(0,4):
            it92 = it92 + 1
            Matrix[it91][it92]=Matrix[it91][it92]+vetorm[it92+it93][it91]
    it9=it9+1
    it93 = it93 + 4

    correc3 = ""
    for carac3 in str(Matrix):
        if carac3 in "[":
            correc3 = correc3 + ""
        elif carac3 in "]":
            correc3 = correc3 + ""
        elif carac3 in "\\":
            correc3 = correc3 + ""
        elif carac3 in "n":
            correc3 = correc3 + ""
        elif carac3 in "''":
            correc3 = correc3 + ""
        else:
            correc3 = correc3 + carac3
    Matrix = correc3

    vetormat[it9]=Matrix

for fic in Ficheiro:
    itit = itit +1

    #open(Ficheiro[itit][0].rstrip(), "r") # rstrip remove careter de mudança de linha \n e similares # Manda error no caso de existir o ficheiro antes de criar um ficheiro

    abrir_file = open(path+"/"+Ficheiro[itit][0].rstrip(), "r")
    it = 0
    it221 = 0
    it222 = 0
    it223 = 0
    vetor = [0]
    vetorp = [""]
    for abrir in abrir_file.readlines():
        vetor.insert(it,abrir.split(' '))
        vetor[it][:]=[x for x in vetor[it] if x]# REMOÇÃO DE CÉLULAS VAZIAS

        coord=0

        #GERAÇÃO DO VETOR PONTOS SEM ESPAÇOS
        for carac in vetor[it][0]: #SE EXIXTIR UM PONTO "." ASSUMIR PARA VETOR DOS PONTOS
            if carac in ".":
                coord=1
        if coord == 1:
            vetorp.insert(it222,abrir.split(' '))
            vetorp[it222][:]=[x for x in vetorp[it222] if x]# REMOÇÃO DE CÉLULAS VAZIAS
            it0222 = 0
            for see in range(len(vetorp[it222])):
                correc = ""
                for carac in vetorp[it222][it0222]:
                    if carac in "D":
                        correc = correc + "E"
                    else:
                        correc = correc + carac
                vetorp[it222][it0222]=correc
                it0222 = it0222 + 1
            it222 = it222+1


        if coord == 0:
            inic = it221 - it223
            it223 = it223 + 1

        if it == 0: #SALTAR A PRIMEIRA LINHA DO Nº DE PONTOS E CONECTIVIDADES
            it221 = 0
            it222 = 0
            it223 = 0
        it = it + 1
        it221 = it221 + 1
    #print(vetor)
    #npontos = eval(vetor[0][0]) #  ATUALMENTE NÃO TEM QQ INFLUENCIA NO CÓDIGO
    #nconec = eval(vetor[0][1])

    vetorp[:] = [x for x in vetorp if x]  # REMOÇÃO DE CÉLULAS VAZIAS
    vetorc10 = vetor[inic:it223 + inic]  # it-2  inic+2


    #JUNTAR TODAS AS CONETIVIDADES REMOVENDO OS ESPAÇOS
    itis = 0
    vetorc1=[""]*(len(vetorc10))
    for se in range(len(vetorc10)):
        verf=0
        for carac1 in vetorc10[itis][0]: #SE EXIXTIR UM PONTO "." ASSUMIR PARA VETOR DOS PONTOS
            if carac1 in ".":
                verf=1
        if len(vetorc10[itis]) >= 4 and verf == 0: #!!!!!!!!! MEXER NESTE PARAMETRO REMOVE MESHES INDESEJADAS
            vetorc1[itis] = vetorc10[itis]
            if len(vetorc10[itis+1]) <= 3 and verf == 0: #!!!!!!!!!!!!!!AQUI TAMBEM
                vetorc1[itis+1] = vetorc10[itis+1]
        itis = itis + 1

    vetorc1[:] = [x for x in vetorc1 if x]  # REMOÇÃO DE CÉLULAS VAZIAS

    vetorc10 = vetor[inic:it223+inic+1]#it-2  inic+2
    #print(vetorp)
    #print(vetorc1)
    #VETOR CONECTIVIDADES POR EXTENSO
    Nc=0
    for it0 in range(len(vetorc1)):
        Nc = Nc + len(vetorc1[it0])

    vetorcext=[0]*Nc
    it4q = 0
    it44q = 0
    for it444 in range(len(vetorc1)):
        it444q = 0
        for it441 in range(len(vetorc1[it44q])):
            vetorcext[it4q] = vetorc1[it44q][it444q].rstrip()
            it4q = it4q + 1
            it444q = it444q + 1
        it44q = it44q + 1
    vetorcext[:] = [x for x in vetorcext if x]  # REMOÇÃO DE CÉLULAS VAZIAS

    #VETOR DE ETAPAS PARA CADA MESH
    #print(vetorcext)
    Ncor = 0 #NUMERO DE MESH DO FICHEIRO ORIGINAL
    for it00 in range(len(vetorcext)):
        if int(vetorcext[it00]) <= 0:
            Ncor = Ncor + 1

    vetorcet = [0] * Ncor

    Ncolu=0
    Ncor1=0
    Ntri=0
    for it001 in range(len(vetorcext)):
        Ncolu = Ncolu + 1
        if int(vetorcext[it001]) <= 0:
            vetorcet[Ncor1] = [0] * Ncolu
            Ntri = Ntri + Ncolu - 3 #numero de triangulos para o Vetorc
            Ncor1 = Ncor1 + 1
            Ncolu=0

    it4q = 0
    it44q = 0
    it444q = -1
    for it444 in range(len(vetorcext)):
        it444q = it444q + 1
        vetorcet[it44q][it444q] = vetorcext[it4q]
        if int(vetorcext[it4q]) <= 0:
            it444q = -1
            it44q = it44q + 1
        it4q = it4q + 1

    #VETORC
    vetorc=[0]*Ntri
    it4q = 0
    it44q = 0
    for it444 in range(len(vetorcet)):
        it444q = -1
        for tda in range(0,len(vetorcet[it44q])-3):
                it444q = it444q + 1
                vetorc[it4q] = [0] * 4
                vetorc[it4q][0] = vetorcet[it44q][0]
                vetorc[it4q][1] = vetorcet[it44q][1+it444q]
                vetorc[it4q][2] = vetorcet[it44q][2+it444q]
                vetorc[it4q][-1] = vetorcet[it44q][-1]
                it4q = it4q + 1
        it44q = it44q + 1
    #print(vetorp)
    #print(vetorc)
    itq=-1
    novo_ficheiro.write("\nApp.activeDocument().Tip = App.activeDocument().addObject('App::Part','Part_"+str(itit +1)+"')")

    for it3 in range(len(vetorc)-1): #CICLO DE CONECTIVIDADES
        itq=itq+1
        novo_ficheiro.write("\n#Conectividade " + str(itq))
        novo_ficheiro.write("\ntriangles=[")
        itq1=-1
        for it4 in range(len(vetorc[itq]) - 1): # CICLO PARA O
            itq1 = itq1 + 1
            vx = str(vetorp[int(vetorc[itq][itq1])-1][0])
            vy = str(vetorp[int(vetorc[itq][itq1])-1][1])
            vz = str(vetorp[int(vetorc[itq][itq1])-1][2])
            if itq1 == (len(vetorc[itq]) - 2):
                novo_ficheiro.write("["+unida+"*"+vx+","+unida+"*"+vy+","+unida+"*"+vz+"]]")
            else:
                novo_ficheiro.write("[" + unida + "*" + vx + "," + unida + "*" + vy + "," + unida + "*" + vz + "],")
        novo_ficheiro.write("\nmeshObject = Mesh.Mesh(triangles)")
        novo_ficheiro.write("\nmesh = App.ActiveDocument.addObject(" + "\"Mesh::Feature\""+")")
        novo_ficheiro.write("\nmesh.Mesh = meshObject")
        novo_ficheiro.write("\nmesh.ViewObject.ShapeColor = " + str(selcolor(int(vetorc[itq][-1]))))
        novo_ficheiro.write("\nGui.Selection.clearSelection()")
        novo_ficheiro.write("\nGui.Selection.addSelection(\""+Nome1+"\", 'Part_"+str(itit +1)+"', mesh.Label)")
        novo_ficheiro.write("\nGui.Selection.clearSelection()")
        novo_ficheiro.write("\nGui.Selection.addSelection(\""+Nome1+"\",mesh.Label)")
        novo_ficheiro.write("\nApp.getDocument(\""+Nome1+"\").getObject(mesh.Label).adjustRelativeLinks(App.getDocument(\""+Nome1+"\").getObject('Part_"+str(itit +1)+"'))")
        novo_ficheiro.write("\nApp.getDocument(\""+Nome1+"\").getObject('Part_"+str(itit +1)+"').addObject(App.getDocument(\""+Nome1+"\").getObject(mesh.Label))")
        novo_ficheiro.write("\nGui.Selection.clearSelection()")
        novo_ficheiro.write("\nGui.Selection.addSelection(\""+Nome1+"\",'Part_"+str(itit +1)+"', mesh.Label)")
        novo_ficheiro.write("\nApp.ActiveDocument.recompute()")
    novo_ficheiro.write("\nApp.getDocument(\"" + Nome1 + "\").Part_" + str(itit + 1) + ".Placement=App.Matrix(" + str(vetormat[itit])+")")
    novo_ficheiro.write("\nprint(\"Progresso... " + str(itit+1) + " de "+ str(len(Ficheiro)) +"\")")
novo_ficheiro.write("\nApp.ActiveDocument.recompute()")
import pathlib
Nomef=path+"\\"+Nome1+".FCStd"
correc3=""
for carac3 in (Nomef):
    if carac3 in "\\":
        correc3 = correc3 + "/"
    else:
        correc3 = correc3 + carac3
Nomef=correc3
novo_ficheiro.write("\nApp.getDocument(\""+str(Nome1)+"\").saveAs(u\""+Nomef+"\")")
print
############ A N I M A Ç Ã O ################################
#print(vetormat)
itwq=-1
novo_ficheiro1.write("vetormat=[0]*int("+str(len(vetorm)/4)+")")
for it3 in range(len(vetormat)):  # CICLO DE CONECTIVIDADES
    itwq = itwq + 1
    novo_ficheiro1.write("\nvetormat["+str(itwq)+"]=["+vetormat[itwq]+"]") #GRAVAR VETOR DE MATRIZES
novo_ficheiro1.write("\nfrom PySide2 import QtCore")
#EXECUTÁVEL
novo_ficheiro1.write("\nitit99=0")
novo_ficheiro1.write("\ni=0")
novo_ficheiro1.write("\ndef update():")
novo_ficheiro1.write("\n    global i, itit99")
itit9=-1
for it43 in Ficheiro:
    itit9 = itit9 + 1
    novo_ficheiro1.write("\n    App.getDocument(\"" + Nome1 + "\").Part_" + str(itit9 + 1) + ".Placement=App.Matrix(")
    itit98=-1
    for it47 in range(0,16):
        itit98=itit98+1
        if itit98==15:
            novo_ficheiro1.write("vetormat[itit99+" + str(itit9) +"]["+str(itit98)+"])")
        else:
            novo_ficheiro1.write("vetormat[itit99+"+str(itit9)+"]["+str(itit98)+"],")

novo_ficheiro1.write("\n    itit99 = itit99 + "+str(len(Ficheiro)))
novo_ficheiro1.write("\n    if itit99 == "+str(len(vetormat))+":")
novo_ficheiro1.write("\n        i=0")
novo_ficheiro1.write("\n        itit99=0")
novo_ficheiro1.write("\n    i+=2")
novo_ficheiro1.write("\ntimer = QtCore.QTimer()")
novo_ficheiro1.write("\ntimer.timeout.connect(update)")
novo_ficheiro1.write("\ntimer.start(1)")