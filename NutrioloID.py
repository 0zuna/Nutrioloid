#!/usr/bin/env python
# -*- coding: utf-8 -*-
#################################################################################
#  				     Modulo del conocimiento 			#
#################################################################################
#  referencia http://www.mujerdeelite.com/guia_de_alimentos
class Alimento(object):
	"""docstring for Alimento"""
	def __init__(self, nombre, caloria, proteina, hidratos, grasa,indiceglicemico, tipo):
		super(Alimento, self).__init__()
		self.nombre = nombre
		self.caloria = caloria
		self.proteina = proteina
		self.hidratos = hidratos
		self.grasa = grasa
		self.indiceglicemico=indiceglicemico
		self.tipo = tipo
	def mostrarAlimento(self):
		print "%s %s %s %s %s %s %s" %(self.nombre, self.caloria, self.proteina, self.hidratos, self.grasa, self.indiceglicemico, self.tipo)
Alimentos=[]
def cargaConocimiento():
	n=0
	file = open('conocimiento','r')
	while True:
		pass
		n=n+1
		linea = file.readline()
		if not linea: break
		alim=linea.split('|')
		Alimentos.append(Alimento(alim[0], alim[1], alim[2], alim[3], alim[4], alim[5], 'Verduras'))

#################################################################################
#  				     Modulo de Inferencia			#
#################################################################################
def pesoIdeal(sexo, altura):
    if (sexo=='hombre'):
        return ((altura - 150)* 0.75)+50
    elif (sexo=='mujer'):
        return ((altura - 150)* 0.6)+50
#################################################################################
#  				     Modulo de explicacion			#
#################################################################################
def valoracion(masa):
	if (masa<=18):
		return """Tu peso es insuficiente
Bajo Peso

por lo que debererías seguir un plan encaminado a obtener un peso apto para ti y una correcta nutrición."""
	elif(masa>18 and masa <=24.9):
            return """En este momento te encuentras en una situacion de Normo Peso
				Tu peso es adecuado u optimo para tu estatura"""
	elif (masa>=25 and masa<=26.9):
            return """
					En este momento te encuentras en una situación de
			Sobrepeso I
			
			Ello quiere decir que tu peso está por encima del recomendado para tu estatura. Accede cuanto antes a inciciar tu plan y verás qué sencillo te resulta"""
	elif (masa>=27 and masa<=29.9):
            return """
					En este momento te encuentras en una situación de
			Sobrepeso II
			
			p>Pre-obesidad. Ello quiere decir que tu peso está por encima del recomendado para tu estatura. Accede cuanto antes a inciciar tu plan y verás qué sencillo te resulta."""
	elif (masa>=30 and masa<= 34.9):
            return """
					En este momento te encuentras en una situación de
			Obesidad Tipo I
			
			Ello significa que tu peso está por encima del recomendado para tu estatura, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud."""
	elif (masa>=35 and masa<=39.9):
            return """
					En este momento te encuentras en una situación de
			Obesidad Tipo II
			
			Ello significa que tu peso está por encima del recomendado para tu estatura, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud."""
	elif (masa>=40 and masa <= 49.9):
            return """
					En este momento te encuentras en una situación de
			Obesidad Tipo III
			
			Ello significa que tu peso está por encima del recomendado para tu estatura, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud."""
	elif (masa>=50):
            return """
					En este momento te encuentras en una situación de
			Obesidad Extrema
			
			Ello significa que tu peso está por encima del recomendado para tu estatura, y que además tienes probabilidades de que vaya asociado todo ello a la aparición de patologías (colesterol, Trigliéridos, hipertensión, diabetes tipoII, etc). Por todo esto, accede a iniciar plan, y te ayudaremos a bajar de peso y mejorar tu salud."""
class Perfil(object):
	"""docstring for Perfil"""
	def __init__(self, nombre, peso, altura):
		super(Perfil, self).__init__()
		self.nombre = nombre
		self.peso = peso
		self.altura = altura
	def imc(self):
		return self.peso/pow(self.altura,2)

		
def main():
	print "##############################################################"
	print "#			    NUTRIOLOID                      #"
	print "##############################################################"
	print "Hola antes de empezar porfavor contastame unas preguntas"
	nombre=raw_input('Cual es tu Nombre>:')
	peso=raw_input('Cual es tu Peso en kilogramos>:')
	altura=raw_input('Cual es tu altura en metros>:')
        sexo=raw_input('Cual es tu sexo>:')

	perfil=Perfil(nombre, float(peso), float(altura))
	print "%s %s" %(nombre,valoracion(perfil.imc()))
	cargaConocimiento()
	Alimentos[0].mostrarAlimento()
	print pesoIdeal('hombre',1.72)
	input() 

if __name__ == '__main__':
	main()
