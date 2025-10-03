#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dyma'r modiwl mewngofnodi o'r Rhaglen Siop Tkinter LLAWN. Mae'r modiwl yma'n
rheoli y rhesymeg a'r ffenestr mewngofnodi. I rhedeg y rhaglen yma redeg y 
modiwl "LLAWN_main.py".

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

from tkinter import *
from tkinter import messagebox


def creu_mewngofnodi(newid_i_siop):
	"""
	Dyma'r ffenestr mewngofnodi i ganiatáu mynediad i'r siop

	Args:
		newid_i_siop (Function): Yn caniatáu i'r mewngofnodwr alw newid_i_siop
								 ar ôl mewngofnodi'n llwyddiannus
	"""

	def prosesu_mewngofnodi():
		"""
		Mae'r ffwythiant hwn yn prosesu'r mewngofnodi a'r dilysu, ar ôl pwyso'r
		botwm. Os oedd y mewngofnodi'n llwyddiannus yna rydym yn galw
		newid_i_siop i ddileu'r ffenestr hon a galw'r rhaglen siop.

		NODYN: Mae'n rhyfedd gweld ffwythiannau o fewn ffwythiannau, ac fel
		arfer mae'n ddiangen, er y gallech ei weld o bryd i'w gilydd. Yn yr
		achos hwn, bydd yn atal ein botwm rhag rhedeg yn awtomatig wrth gychwyn
		"""

		# Storio'r manylion mewngofnodi
		enw_stor = "Fy.Enw"
		cyfrinair_stor = "cyfr1n41rDa"

		# Gwiriwch a yw manylion mewngofnodi'r defnyddiwr yn cyfateb i fewnbwn
		# y defnyddiwr
		if ((enw_mewn.get() == enw_stor) and
			(cyfrinair_mewn.get() == cyfrinair_stor)):

			# Nawr rydym yn galw newid_i_siop i lansio'r rhaglen shopface
			newid_i_siop(root_mewngofnodi)

		else:
			messagebox.showwarning("Wedi methu!", "Wedi methu!")


	# Creu y Tkinter root ar gyfer y ffenestr mewngofnodi,
	# creu teitl i'r ffenestr, a ffrâm newydd tu fewn,
	# a'i osod gan ddefnyddio'r rheolwr pack
	root_mewngofnodi = Tk()
	root_mewngofnodi.title("Rhaglen Siop - Mewngofnodi")
	ffram_mewngofnodi = Frame(root_mewngofnodi)
	ffram_mewngofnodi.pack()

	# O fewn y ffrâm_mewngofnodi, crëwch deitl a'i bacio
	label_teitl = Label(ffram_mewngofnodi, text = "Croeso i'r Siop!")
	label_teitl.pack()

	# O fewn y ffrâm_mewngofnodi, crëwch ffrâm, label a'r maes mewnbwn ar gyfer
	# enw defnyddiwr, paciwch nhw i gyd
	ffram_enw = Frame(ffram_mewngofnodi)
	ffram_enw.pack()
	label_enw = Label(ffram_enw, text = "enw")
	label_enw.pack(side = LEFT)
	maes_enw = Entry(ffram_enw)
	maes_enw.pack(side = RIGHT)

	# O fewn y ffrâm_mewngofnodi, crëwch ffrâm, label a'r maes mewnbwn ar gyfer
	# y cyfrinair, paciwch nhw i gyd
	ffram_cyfrinair = Frame(ffram_mewngofnodi)
	ffram_cyfrinair.pack()
	label_cyfrinair = Label(ffram_cyfrinair, text = "cyfrinair")
	label_cyfrinair.pack(side=LEFT)
	maes_cyfrinair = Entry(ffram_cyfrinair)
	maes_cyfrinair.pack(side=RIGHT)

	#O fewn y ffrâm_mewngofnodi, creu botwm sy'n galw prosesu_mewngofnodi,
	# a'i bacio
	botwm_cyflwyno = Button(ffram_mewngofnodi, text = "cyflwyno", 
							bg = "White", fg = "Red", 
							command = prosesu_mewngofnodi)
	botwm_cyflwyno.pack()

	# Mae'r ffwythiant mainloop yn cadw'r GUI hwn mewn dolen (h.y. yn ei gadw'n
	# weithredol) ac yn aros am fewnbwn gan y defnyddiwr - mae angen hwn arnom
	# ar ddiwedd pob ffenestr newydd
	root_mewngofnodi.mainloop()