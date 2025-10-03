#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dyma'r modiwl ychwanegu_stoc o'r Rhaglen Siop Tkinter LLAWN. Mae'r modiwl yma'n
rheoli y ffenestr i ychwanegu eitemau newydd i'r rhestr stoc y siop. I rhedeg y
rhaglen yma redeg y modiwl "LLAWN_main.py".

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
from LLAWN_siop import *
from LLAWN_ffeiliau import ysgrifennu_stoc


def creu_ychwanegu_stoc(diweddaru_tabl_stoc, stoc):
	"""
	Dyma'r ffwythiant i greu'r ffenestr ychwanegu stoc

	Args:
		diweddaru_tabl_stoc (Function): Y ffwythiant i ddiweddaru'r tabl stoc
										yn y ffenestr siop
		stoc (Dict): Geiriadur yn cynnwys yr holl eitemau sydd ar werth
	"""

	# Creu y Tkinter root ar gyfer y ffenestr ychwanegu stoc,
	# creu teitl i'r ffenestr, a ffrâm newydd tu fewn,
	# a'i osod gan ddefnyddio'r rheolwr grid
	root_ychwanegu = Tk()
	root_ychwanegu.title("Rhaglen Siop - Ychwanegu Stoc")
	ffram_ychwanegu = Frame(root_ychwanegu)
	ffram_ychwanegu.grid(row = 0, column = 0)

	# Creu teitl ar frig y ffenestr,
	# Gosodwch ef yn ei le gyda'r rheolwr grid a chanoli
	label_teitl = Label(ffram_ychwanegu, 
						text = "Ychwanegu eitem newydd i'r rhestr stoc:")
	label_teitl.grid(row = 0, column = 0, sticky="ew")
	label_teitl.grid_columnconfigure(0, weight=1)

	# Creu label a maes ar gyfer Rhif yr eitem,
	# Gosodwch nhw yn eu lle gyda'r rheolwr grid
	label_id = Label(ffram_ychwanegu, text = "Rhif Eitem")
	label_id.grid(row = 1, column = 0)
	maes_id = Entry(ffram_ychwanegu)
	maes_id.grid(row = 1, column = 1)

	# Creu label a maes ar gyfer Enw'r eitem,
	# Gosodwch nhw yn eu lle gyda'r rheolwr grid
	label_enw = Label(ffram_ychwanegu, text = "Enw")
	label_enw.grid(row = 2, column = 0)
	maes_enw = Entry(ffram_ychwanegu)
	maes_enw.grid(row = 2, column = 1)

	# Creu label a maes ar gyfer Pris yr eitem,
	# Gosodwch nhw yn eu lle gyda'r rheolwr grid
	label_pris = Label(ffram_ychwanegu, text = "Pris")
	label_pris.grid(row = 3, column = 0)
	maes_pris = Entry(ffram_ychwanegu)
	maes_pris.grid(row = 3, column = 1)

	# Creu label a maes ar gyfer Nifer yr eitem mewn stoc,
	# Gosodwch nhw yn eu lle gyda'r rheolwr grid
	label_nifer = Label(ffram_ychwanegu, text = "Nifer")
	label_nifer.grid(row = 4, column = 0)
	maes_nifer = Entry(ffram_ychwanegu)
	maes_nifer.grid(row = 4, column = 1)

	# Creu botwm i ychwanegu'r eitem i stoc,
	# Defnyddio ffwythiant lambda fel bod prosesu_ychwanegu_eitem yn rhedeg pan
	# gaiff y botwm ei wasgu yn unig
	botwm_ychwanegu = Button(ffram_ychwanegu, text = "Ychwanegu Eitem",
							bg = "White", fg = "Green",
							command = lambda: prosesu_ychwanegu_eitem(
										root_ychwanegu, diweddaru_tabl_stoc,
										stoc, maes_id, maes_enw,
										maes_pris, maes_nifer))
	botwm_ychwanegu.grid(row = 5, column = 1)

	# Ffenestr newydd, felly mainloop newydd!
	root_ychwanegu.mainloop()


def dilysu_ychwanegu(maes_id, maes_enw, maes_pris, maes_nifer):
	"""
	Mae'r ffwythiant hwn yn dilysu cynnwys y meysydd mewnbwn
	NODYN: Os yw hyn yn llwyddiannus bydd gan bob gwerth a ddychwelir eu mathau
	angenrheidiol, ond os yw'n aflwyddiannus bydd y gwerth aflwyddiannus yn
	dychwelyd yn False.

	Args:
		maes_id (String): Y maes mewnbwn ar gyfer y Rhif Eitem newydd
		maes_enw (String): Y maes mewnbwn ar gyfer Enw yr eitem newydd
		maes_pris (String): Y maes mewnbwn ar gyfer Pris yr eitem newydd
		maes_nifer (String): Y maes mewnbwn ar gyfer Nifer o'r eitem newydd sydd
						 	 mewn stoc

	Return:
		id_eitem (False / int): Gwerth Rhif yr Eitem
		enw (False / String): Gwerth Enw'r eitem
		pris (False / float): Gwerth Pris yr eitem
		nifer (False / int): Gwerth Nifer yr eitem mewn stoc
	"""

	id_eitem, enw, pris, nifer = False, False, False, False

	if ((maes_id.get() == "") or (maes_enw.get() == "") or
		(maes_pris.get() == "") or (maes_nifer.get() == "")):
		messagebox.showwarning("Gwall", "Rhaid i bob maes gynnwys gwerthoedd!")
	else:
		try:
			id_eitem = int(maes_id.get())
		except ValueError:
			messagebox.showwarning("Gwall", 
									"Rhaid i Rhif Eitem fod yn gyfanrif!")
			return id_eitem, enw, pris, nifer

		try:
			pris = float(maes_pris.get())
		except ValueError:
			messagebox.showwarning("Gwall", "Rhaid i'r pris fod yn rhif!")
			return id_eitem, enw, pris, nifer

		try:
			nifer = int(maes_nifer.get())
		except ValueError:
			messagebox.showwarning("Gwall", "Rhaid i Nifer fod yn gyfanrif!")
			return id_eitem, enw, pris, nifer

		enw = maes_enw.get()

	return id_eitem, enw, pris, nifer


def prosesu_ychwanegu_eitem(root_ychwanegu, diweddaru_tabl_stoc, stoc,
					 		maes_id, maes_enw, maes_pris, maes_nifer):
	"""
	Dyma'r ffwythiant prosesu_ychwanegu_eitem sy'n ceisio ychwanegu eitem os
	yw'r meysydd mewnbwn wedi'u dilysu'n llwyddiannus.
	Mae'r eitem yn cael ei hychwanegu at stoc, mae'r stoc yn cael ei
	hailysgrifennu i ffeil, ac mae'r tabl yn cael ei ddiweddaru. Yn ogystal,
	mae'r ffenestr ychwanegu stoc yn cael ei dinistrio.

	Args:
		root_ychwanegu (Tkinter Window): Y ffenestr i'w dinistrio
		diweddaru_tabl_stoc (Function): Y ffwythiant i ddiweddaru'r tabl stoc
		stoc (Dict): Geiriadur yr holl eitemau sydd ar werth
		maes_id (String): Y maes mewnbwn ar gyfer y Rhif Eitem newydd
		maes_enw (String): Y maes mewnbwn ar gyfer Enw yr eitem newydd
		maes_pris (String): Y maes mewnbwn ar gyfer Pris yr eitem newydd
		maes_nifer (String): Y maes mewnbwn ar gyfer Nifer o'r eitem newydd
							 sydd mewn stoc
	"""

	id_eitem, enw, pris, nifer = dilysu_ychwanegu(maes_id, maes_enw, 
													maes_pris, maes_nifer)

	if ((id_eitem != False) and (enw != False) and 
			(pris != False) and (nifer != False)):

		stoc[id_eitem] = {	"Enw": enw,
							"Pris": pris,
							"Stoc": nifer
							}
		ysgrifennu_stoc(stoc)
		diweddaru_tabl_stoc()
		root_ychwanegu.destroy()
