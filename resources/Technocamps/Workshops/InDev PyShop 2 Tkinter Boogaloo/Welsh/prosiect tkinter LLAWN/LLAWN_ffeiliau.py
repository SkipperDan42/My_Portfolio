#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dyma'r modiwl ffeiliau o'r Rhaglen Siop Tkinter LLAWN. Mae'r modiwl yma'n
rheoli darllen o ac ysgrifennu i ffeiliau allanol. I rhedeg y rhaglen yma redeg
y modiwl "LLAWN_main.py".

Bwriadwyd y rhaglen hon fel ymarfer ar gyfer cwricwlwm Cyfrifiadureg CBAC 2025
(yn benodol yr arddull arholiad newydd ar gyfer Uned 2).

Nod y dasg yw deall y rhaglen a thrwsio'r holl wallau sy'n bresennol, wrth wella
gallu'r dysgwyr i ddarparu sylwadau a dogfennaeth dda.

NODYN: Dyma fersiwn LLAWN o'r rhaglen heb unrhyw wallau, i ddefnyddiwyd gan yr
       athro i gefnogi'r dysgwyr!
       Nid yw'r ddogfennaeth yn y rhaglen hon yn ofyniad TGAU CBAC, ond mae
       wedi'i chynnwys er mwyn cyflawnrwydd. Mae rhai o'r sylwadau'n rhy
       ddisgrifiadol, ond wedi'u cynnwys i fod o gymorth.
"""
__author__ = "Dan North"
__maintainer__ = "Technocamps"
__date__ = "2025/08/27"
__deprecated__ = False

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os


def ol_ffeil_stoc(modd):
	"""
	Dyma'r ffwythiant i ôl y ffeil stoc o'r cyfeiriadur. Dyle'r ffwythiant yma
	gweithio hyd yn oed ar ôl symud y cyfeiriadur (os yw'r strwythur y tu mewn
	i'r cyfeiriadur yn gyson).

	Args:
		modd (String): Y modd i agor y ffeil stoc (e.e. darllen/ysgrifennu)

	Return: 
		ffeil_stoc (File): yn dychwelyd y ffeil agored yn y modd a ddymunir
	"""

	cyfeiriadur = os.path.dirname(os.path.abspath(__file__))
	llwybr_stoc = os.path.join(cyfeiriadur,'LLAWN_eitemau.csv')
	ffeil_stoc = open(os.path.abspath(llwybr_stoc), modd)

	return ffeil_stoc


def llwytho_stoc():
	"""
	Dyma'r ffwythiant i llwytho stoc o ffeil

	Return:
		stoc (Dict): Geiriadur yn cynnwys yr holl eitemau sydd ar werth
	"""

	ffeil_stoc = ol_ffeil_stoc('r')
	stoc = {}

	for llinell in ffeil_stoc:
		
		eitem = []
		for col in llinell.strip().split(','):
			eitem.append(col)

		id_eitem = int(eitem[0].strip())
		enw = eitem[1].strip().replace('"','')
		pris = float(eitem[2].strip())
		nifer = int(eitem[3].strip())

		stoc[id_eitem] = {
						"Enw": enw,
						"Pris": pris,
						"Stoc": nifer
						}
	ffeil_stoc.close()

	return stoc


def ysgrifennu_stoc(stoc):
	"""
	Dyma'r ffwythiant i ysgrifennu stoc i ffeil

	Args:
		stoc (Dict): Geiriadur yn cynnwys yr holl eitemau sydd ar werth
	"""

	ffeil_stoc = ol_ffeil_stoc('w')

	for id_eitem, eitem in stoc.items():
		llinell =  str(str(id_eitem) + ', "' + item["Enw"] + '", ' +
	    		str(item["Pris"]) + ', ' + str(item["Stoc"]) + '\n')
		ffeil_stoc.write(llinell)

	ffeil_stoc.close()

