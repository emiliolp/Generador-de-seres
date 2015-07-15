#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convertir(posicion,accesorio,fisico,musculo,cola,ojo):
	if posicion==0:
		atacarBrazos()
	elif posicion==1:
		atacarPiernas()
	elif posicion==2:
		defender()

	if accesorio==2:
		encanonar(posicion)
	elif accesorio==3:
		insertarSierra(posicion)

	modelarFisico(fisico)
	modelarCola(cola)
	modelarOjos(ojo)
	if musculo==2:
		modelarMusculos(posicion,musculo)


def atacarBrazos():
 	print("Ha seleccionado ataque de brazos\n")

 	f=open('willy/willy.wrl','r')
 	contenido=''

 	for line in f:
 		linea=line.split('_')
 		directriz=linea[0]
		if directriz=="#brazo1":
			contenido +='	rotation 1 0 0 1.5708 #brazo1_\n'
		elif directriz=="	rotation 1 0 0 3.1416	#brazo2":
			contenido+='	rotation 1 0 0 1.5708 #brazo2_\n'
 		else:
			contenido += line

	f.close()
	f=open('changed/willy.wrl','w')
	f.write(contenido)
	f.close()

def atacarPiernas():
	print("Ha seleccionado ataque de piernas\n")
		
	f=open('willy/willy.wrl','r')
 	contenido=''
	for line in f:
		linea=line.split('_')
		directriz=linea[0]
		if directriz=="	rotation 1 0 0 3.1416	#pierna":
			contenido+='	rotation 1 0 0 2.25	#pierna\n'
		else:
			contenido +=line

	f.close()
	f=open('changed/willy.wrl','w')
	f.write(contenido)
	f.close()

def defender():
	print("Ha seleccionado posición de defensa\n")
	f=open('willy/willy.wrl','r')
	contenido=''
	for line in f:
		linea=line.split('_')
		directriz=linea[0]

		if directriz=="#brazo1":
			contenido+='	rotation 1 0 0 0.5236 #brazo1_\n'
		elif directriz=="	rotation 1 0 0 3.1416	#brazo2":
			contenido+='	rotation 1 0 0 0.5236 #brazo2_\n'
		else:
			contenido+=line

	f.close()
	f=open('changed/willy.wrl','w')
	f.write(contenido)
	f.close()

	#modificamos brazo.wrl
	g=open('willy/brazo.wrl','r')
	contenido=''
	for lined in g:
		linea=lined.split('_')
		directriz=linea[0]
		if directriz=="spine[-1 2.25 0,-1 1.5 0,-1 0.75 0,-0.5 0 0, 0.5 0 0] #defensa":
			contenido+='spine [0.95 2.95 1,0.9 2.8 1,0.7 2.1 1,0.5 1.4 1,0.3 0.7 1,0.3 0.7 1,-0.1 0 0,0.2 0 0,0.5 0 0]\n'
		else:
			contenido+=lined

	g.close()
	g=open('changed/brazo.wrl','w')
	g.write(contenido)
	g.close()

	#modificamos dedo.wrl
	f=open('willy/dedo.wrl','r')
	contenido=''
	for line in f:
		linea=line.split('[')
		directriz=linea[0]
		if directriz=="                spine ":
			contenido+='                spine [-0.12 0.3 0,-0.08 0.2 0,-0.04 0.1 0,0 0 0]\n'
		else:
			contenido+=line
	f.close()
	f=open('changed/dedo.wrl','w')
	f.write(contenido)
	f.close()

	#modificamos situación en el espacio de dedo en brazo.wrl
	f=open('changed/brazo.wrl','r')
	contenido=''
	for line in f:
		linea=line.split('_')
		directriz=linea[0]
		if directriz=="      translation -0.9 2.55 0.08 #rdedo":
			contenido+='		translation 0.96 3.27 1.08\n'
		elif directriz=="      translation -1.1 2.55 0.08 #rdedo":
			contenido+="		translation 1.16 3.2 1.08\n"
		elif directriz=="      translation -1 2.55 -0.1 #rdedo":
			contenido+='		translation 1.05 3.245 0.90\n'
		else:
			contenido+=line
	f.close()
	f=open('changed/brazo.wrl','w')
	f.write(contenido)
	f.close()

	# #modificamos brazo2.wrl
	f=open('willy/brazo2.wrl','r')
	contenido=''
	for line in f:
		linea=line.split('[')
		directriz=linea[0]
		if directriz=="spine":
			contenido+='            spine [-0.95 2.95 1,-0.9 2.8 1,-0.7 2.1 1,-0.5 1.4 1,-0.3 0.7 1,-0.3 0.7 1,0.1 0 0,-0.2 0 0,-0.5 0 0]\n'
		else:
			contenido+=line
	f.close()
	f=open('changed/brazo2.wrl','w')
	f.write(contenido)
	f.close()

	# #modificamos dedo2.wrl
	f=open('willy/dedo2.wrl','r')
	contenido=''
	for line in f:
		linea=line.split('[')
		directriz=linea[0]
		if directriz=="                spine ":
			contenido+='                spine [0.12 0.3 0,0.08 0.2 0,0.04 0.1 0,0 0 0]\n'
		else:
			contenido+=line
	f.close()
	f=open('changed/dedo2.wrl','w')
	f.write(contenido)
	f.close()

	#modificamos situación en el espacio de dedo en brazo.wrl
	f=open('changed/brazo2.wrl','r')
	contenido=''
	for line in f:
		linea=line.split('_')
		directriz=linea[0]
		if directriz=="      translation 0.9 2.55 0.08 #rdedo":
			contenido+='		translation -0.96 3.27 1.08\n'
		elif directriz=="      translation 1.1 2.55 0.08 #rdedo":
			contenido+="		translation -1.16 3.2 1.08\n"
		elif directriz=="      translation 1 2.55 -0.1 #rdedo":
			contenido+='		translation -1.05 3.245 0.90\n'
		else:
			contenido+=line
	f.close()
	f=open('changed/brazo2.wrl','w')
	f.write(contenido)
	f.close()

def encanonar(posicion):
	print "Ha seleccionado accesorio cañón\n"

	if posicion==3 or posicion==0 or posicion==1:
		#brazo 1
		f=open('willy/brazo.wrl','r')
 		contenido=''

 		for line in f:
 			linea=line.split('_')
 			directriz=linea[0]
			if directriz=="      translation -0.9 2.55 0.08 #rdedo":
				contenido +='      translation -1 2.8 0 #rdedo_la\n'
			elif directriz=="    #fin":
				contenido+=']}\n'
				break
 			else:
				contenido += line

		f.close()
		f=open('changed/brazo.wrl','w')
		f.write(contenido)
		f.close()

		#transformar dedo1
		f=open('willy/dedo.wrl','r')
		contenido=''

		for line in f:
			linea=line.split('[')
			directriz=linea[0]
			if directriz=="                scale":
				contenido+='                  scale[ 0.2 0.2, 0.2 0.2, 0.07 0.07,0.07 0.07]\n'
			elif directriz=="                spine ":
				contenido+='                spine [0 0.6 0, 0 0.25 0, 0 0.25 0,0 0.6 0]\n'
			else:
				contenido+=line
		f.close()
		f=open('changed/dedo.wrl','w')
		f.write(contenido)
		f.close()

		#brazo2
		f=open('willy/brazo2.wrl','r')
 		contenido=''

 		for line in f:
 			linea=line.split('_')
 			directriz=linea[0]
			if directriz=="      translation 0.9 2.55 0.08 #rdedo":
				contenido +='      translation 1 2.8 0 #rdedo\n'
			elif directriz=="    #fin":
				contenido+=']}\n'
				break
 			else:
				contenido += line

		f.close()
		f=open('changed/brazo2.wrl','w')
		f.write(contenido)
		f.close()

		#dedo2
		f=open('willy/dedo2.wrl','r')
		contenido=''

		for line in f:
			linea=line.split('[')
			directriz=linea[0]
			if directriz=="            scale":
				contenido+='                  scale[ 0.2 0.2, 0.2 0.2, 0.07 0.07,0.07 0.07]\n'
			elif directriz=="                spine ":
				contenido+='                spine [0 0.6 0, 0 0.25 0, 0 0.25 0,0 0.6 0]\n'
			else:
				contenido+=line
		f.close()
		f=open('changed/dedo2.wrl','w')
		f.write(contenido)
		f.close()

def insertarSierra(posicion):
	if posicion==1 or posicion==3 or posicion==0:
		f=open('willy/brazo.wrl','r')
		contenido=''

		for line in f:
			linea=line.split('"')
			directriz=linea[0]
			if directriz=="          url ":
				contenido+='		url "cuchilla.wrl"'
			else:
				contenido+=line
		f.close()
		f=open('changed/brazo.wrl','w')
		f.write(contenido)
		f.close()

		f=open('changed/brazo.wrl','r')
		contenido=''
		for line in f:
			linea=line.split('_')
			directriz=linea[0]
			if directriz=="      rotation 1 0 0 3.1416 #rdedo":
				contenido+='	rotation 1 0 0 -1.5708\n'
			elif directriz=="      translation -0.9 2.55 0.08 #rdedo":
				contenido+='  		translation -0.3 3.75 0\n'
			elif directriz=="    #fin":
				contenido+=']}'
				break
			else:
				contenido+=line
		f.close()
		f=open('changed/brazo.wrl','w')
		f.write(contenido)
		f.close()

def modelarFisico(fisico):
	f=open('changed/willy.wrl','r')
	contenido=''

	for line in f:
		linea=line.split("_")
		directriz=linea[0]
		if directriz=="				scale [0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3,0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5,1.7 1.7,2.15 2.15,2.4 2.4,2.5 2.5,2.4 2.4,2.15 2.15,1.7 1.7] #fisico":
			if fisico==1:
				contenido+='				scale [0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3,0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5,1.7 0.7,2.15 1.15,2.4 1.4,2.5 1.5,2.4 1.4,2.15 1.15,1.7 0.7] #fisico'
			elif fisico==2:
				contenido+='				scale [0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3,0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5,1.7 1.2,2.15 1.65,2.4 1.9,2.5 2,2.4 1.9,2.15 1.65,1.7 1.2] #fisico'
			elif fisico==3:
				contenido+='				scale [0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3, 0.3 0.3,0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5, 0.5 0.5,1.7 1.7,2.15 2.15,2.4 2.4,2.5 2.5,2.4 2.4,2.15 2.15,1.7 1.7] #fisico'
		elif directriz=="	translation 0 1.285714281 -2.5 #":
			if fisico==1:
				contenido+='	translation 0 1.285714281 -1.5\n'
			elif fisico==2:
				contenido+='	translation 0 1.285714281 -2\n'
			elif fisico==3:
				contenido+='	translation 0 1.285714282 -2.5\n'
		else:
			contenido+=line
	f.close()
	f=open('changed/willy.wrl','w')
	f.write(contenido)
	f.close()

def modelarCola(cola):
	f=open('willy/cola.wrl','r')
	contenido=''

	for line in f:
		linea=line.split("[")
		directriz=linea[0]
		if cola==2:
			if directriz=="            scale":
				contenido+="		            scale[0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15]"
			elif directriz=="#final":
				contenido+='Transform{\n    translation 0 8 0\n    children [\n    Inline {\n    url "elice.wrl"\n}]\n}'
			elif directriz=="                spine ":
				contenido+='                spine [0 8 0,0 2.4 0, 0 2.2 0, 0 2 0, 0 1.8 0, 0 1.6 0, 0 1.4 0, -0.5 1.2 0,-0.5 1 0,-0.5 0.5 0,-0.25 0 0, 0.25 0 0]\n'
			else:
				contenido+=line
		elif cola==3:
			if directriz=="            scale":
				contenido+="					scale[0.3 0.3,0.5 0.5, 0.5 0.5, 0.5 0.5,0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15, 0.15 0.15]"
			elif directriz=="                spine ":
				contenido+='				spine[3 8 0,2 8 0,3 8 0, 2 8 0, 1 8 0, 0.75 7 0, 0.5 6 0, 0.25 5 0,0 2.4 0, 0 2.2 0, 0 2 0, 0 1.8 0, 0 1.6 0, 0 1.4 0, -0.5 1.2 0,-0.5 1 0,-0.5 0.5 0,-0.25 0 0, 0.25 0 0]\n'
			else:
				contenido+=line
		else:
			contenido+=line

	
	f.close()
	f=open('changed/cola.wrl','w')
	f.write(contenido)
	f.close()

def modelarOjos(ojo):
	if ojo==1:
		f=open('changed/willy.wrl','r')
		contenido=''
		#modifica ojo

		for line in f:
			linea=line.split('_')
			directriz=linea[0]
			
			if directriz=='			url "ojo.wrl"	#ojo2':
				contenido+=' '
			elif directriz=='			url "antena.wrl"	#antena2':
				contenido+=' '
			elif directriz=='	translation 1 7.75 0 #centra':
				contenido+='	translation 0 7.75 0\n'
			else:
				contenido+=line

		f.close()
		f=open('changed/willy.wrl','w')
		f.write(contenido)
		f.close()

		#modifica antena
		f=open('changed/antena.wrl','r')
		contenido=''

		for line in f:
			linea=line.split('_')
			directriz=linea[0]
			if directriz=='    			spine [0.75 1 0, 0 0 0]  #antena':
				contenido+='    			spine [0 1 0, 0 0 0]  #antena\n'
			else:
				contenido+=line

		f.close()
		f=open('changed/antena.wrl','w')
		f.write(contenido)
		f.close()

def modelarMusculos(posicion,musculo):
	if posicion==0 or posicion==1 or posicion==3:
		f=open('changed/brazo.wrl')
		contenido=''

		for line in f:
			linea=line.split('[')
			directriz=linea[0]
			if directriz=="            scale":
				contenido+='            scale[ 0.25 0.25, 0.32 0.25, 0.25 0.25, 0.25 0.25, 0.35 0.35,0.40 0.40,0.35 0.35,0.25 0.25,0.25 0.25]\n'
			elif directriz=="spine":
				contenido+='spine[-1 2.25 0,-1 1.5 0,-1 0.75 0,-0.5 0 0, -0.25 0.1 0,0 0.2 0,0.25 0.1 0,0.5 0 0,0.6 0 0]\n'
			else:
				contenido+=line

		f.close()
		f=open('changed/brazo.wrl','w')
		f.write(contenido)
		f.close()

		f=open('changed/brazo2.wrl')
		contenido=''
		for line in f:
			linea=line.split('[')
			directriz=linea[0]
			if directriz=="            scale":
				contenido+='            scale[ 0.25 0.25, 0.32 0.25, 0.25 0.25, 0.25 0.25, 0.35 0.35,0.40 0.40,0.35 0.35,0.25 0.25,0.25 0.25]\n\n'
			elif directriz=="spine":
				contenido+='spine[1 2.25 0,1 1.5 0,1 0.75 0,0.5 0 0, 0.25 0.1 0,0 0.2 0,-0.25 0.1 0,-0.5 0 0,-0.6 0 0]\n'
			else:
				contenido+=line

		f.close()
		f=open('changed/brazo2.wrl','w')
		f.write(contenido)
		f.close()

def error():
	print("error saliendo del programa")

#Copiamos todos los ficheros a la carpeta changed
import os, sys
os.mkdir('changed', 0777 );
fw=open('willy/willy.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/willy.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/brazo.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/brazo.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/brazo2.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/brazo2.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/cola.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/cola.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/dedo.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/dedo.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/dedo2.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/dedo2.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()

fw=open('willy/hombro.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/hombro.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/ojo.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/ojo.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/pierna.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/pierna.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/pierna2.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/pierna2.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()	

fw=open('willy/antena.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/antena.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/base.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/base.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/cuchilla.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/cuchilla.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero

fw=open('willy/elice.wrl','r')	#Abrimos el principal para lectura
c = fw.read()				#Leemos el fichero
fw.close()					#Cerramos el fichero
fw2=open('changed/elice.wrl','w')	#Abrimos el fichero copia para lectura
fw2.write(c)						#Escribimos el contenido en el fichero
fw2.close()							#Cerramos el fichero


pos= int(input("Introduce la posicion\n    1-Ataque\n    2-Defensa\n    3-Saludo\n"))	
if pos==1:
	ata=int(input("Seleccione tipo de ataque:\n    1-Brazos\n    2-Piernas\n"))
	if ata==1:
		pos=0	#posicion 0 es brazos
	else:
		pos=1   #posicion 1 es piernas
				#posicion 2:defensa, posicion 3: descanso, posicion 4: saludo
if pos!=2:
	acc=int(input("Introduce accesorio para brazos:\n    1-Dedos\n    2-Pistola\n    3-Sierra\n"))
fis=int(input("Introduce forma fisica del ser:\n    1-Delgado\n    2-Normal\n    3-Gordo\n"))
mus=int(input("Introduce fuerza del ser:\n    1-Debil\n    2-Fibroso\n"))
cola=int(input("Seleccione el tipo de cola:\n    1-Normal\n    2-Helice\n    3-Pistola\n"))
ojo=int(input("Seleccione el tipo de ojos:\n    1-Un ojo\n    2-Dos ojos\n"))
#fis1: obeso1, fis2: obeso2, fis3: obeso3, fis4: musculoso1, fis5: musculoso2, fis6: musculoso3, fis7: normal
if pos!=2:
	convertir(pos,acc,fis,mus,cola,ojo)
else:
	acc=0
	convertir(pos,acc,fis,mus,cola,ojo)
