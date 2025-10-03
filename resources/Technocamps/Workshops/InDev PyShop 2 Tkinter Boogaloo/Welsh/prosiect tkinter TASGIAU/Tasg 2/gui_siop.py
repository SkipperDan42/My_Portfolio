from tkinter import *
from tkinter import messagebox
from gui_ffeiliau import *


def creu_siop(newid_i_mewngofnodi):
	"""
	Dyma'r ffwythiant i greu ffenestr y siop sy'n cynnwys prif swyddogaeth y
	rhaglen.

	Args: 
		newid_i_mewngofnodi (Function): Yn caniatáu i'r siop alw
										newid_i_mewngofnodi ar ôl pwyso
										allgofnodi
	"""

	# Rhaid diffinio stoc a gwerthiannau fel newidynnau eang er mwyn caniatáu
	# iddynt gael eu diweddaru o fewn y GUI


	# Diffinnir ffram_siop fel eang er mwyn symlrwydd,
	# NODYN: mae hwn yn arfer gwael
	global ffram_siop

	# Cychwyn geiriadur stoc trwy lwytho o ffeil

	
	# Creu y Tkinter root ar gyfer ffenestr y siop,
	# creu teitl i'r ffenestr, a ffrâm newydd tu fewn,
	# a'i osod gan ddefnyddio'r rheolwr grid
	root_siop = Tk()
	root_siop.title("Rhaglen Siop")
	ffram_siop = Frame(root_siop)
	ffram_siop.grid(row = 0, column = 0)

	# Cychwyn gwerthiannau gan ddefnyddio Newidyn Tkinter
	gwerthiannau = DoubleVar(root_siop)
	gwerthiannau.set(0.0)

	# Galw ffwythiannau i greu'r elfennau o fewn y ffram_siop
	creu_bar_dewislen(newid_i_mewngofnodi, root_siop)
	creu_tabl_stoc()
	creu_bar_prynu()

	# Gan mai ffenestr newydd yw hon, mae angen i ni nodi ei bod mainloop()
	root_siop.mainloop()


def creu_bar_dewislen(newid_i_mewngofnodi, root_siop):
	"""
	Mae'r ffwythiant hyn yn creu'r bar dewislen ar gyfer ffenestr y siop

	Args:
		newid_i_mewngofnodi (Function): ...

		root_siop (Tkinter Window): Rhaid pasio'r ffenestr i'w dinistrio
	"""

	# Rhaid ailddiffinio mynediad eang i newidynnau bob tro y cânt eu defnyddio
	global stoc
	global ffram_siop

	# Create the menu frame within the shopface frame and configure the columns
	ffram_dewislen = Frame(ffram_siop, bd=5, relief=RIDGE)
	ffram_dewislen.grid(row = 0, column = 0, sticky="ew")

	# Creu botwm i allgofnodi yn ffrâm y ddewislen. Bydd y botwm hwn yn galw
	# newid_i_mewngofnodi i allgofnodi o'r siop
	# NODYN: mae'r gan y ffwythiabt lambda yr un pwrpas
	botwm_allgofnodi = Button(ffram_dewislen, text ="Allgofnodi",
						  bg = "White", fg = "Red",
						  command = lambda: print("Allgofnodi?"))
	botwm_allgofnodi.grid(row = 3, column = 3)


def creu_tabl_stoc():
	"""
	Mae'r ffwythiant hyn yn creu'r tabl stoc ar gyfer ffenestr y siop
	"""

	# ...
	global stoc
	global ffram_siop

	# Diffinnir ffram_tabl fel eang er mwyn symlrwydd diweddaru ffram_tabl
	# NODYN: mae hwn yn arfer gwael
	global ffram_tabl

	# Creu'r ffrâm tabl o fewn ffrâm y siop a ffurfweddu'r colofnau i arddangos
	# yn iawn
	ffram_tabl = Frame(ffram_siop, bd=5, relief=RIDGE)
	ffram_tabl.grid(row = 1, column = 0, sticky="ew")
	ffram_tabl.grid_columnconfigure(0, weight=1)
	ffram_tabl.grid_columnconfigure(1, weight=1)
	ffram_tabl.grid_columnconfigure(2, weight=1)
	ffram_tabl.grid_columnconfigure(3, weight=1)

	# Llenwi ffrâm y tabl gyda phenawdau
	label_id = Label(ffram_tabl, text ="Rhif Eitem").grid(row = 1, column = 0)
	label_enw = Label(ffram_tabl, text ="Enw").grid(row = 2, column = 1)
	label_pris = Label(ffram_tabl, text ="Pris (£)").grid(row = 0, column = 2)
	quantity_label = Label(ffram_tabl, text ="Mewn Stoc").grid(row = 0, column = 3)

	# Llenwch y tabl gyda gwerthoedd *cyfredol* eitemau
	for i, eitem in enumerate(stoc):
		label_id = Label(ffram_tabl, text=eitem).grid(row=i + 3, column=1)
		label_enw = Label(ffram_tabl, text=stock[eitem]["Enw"]).grid(row=i + 2, column=0)
		label_pris = Label(ffram_tabl, text=stock[eitem]["Pris"]).grid(row=i + 1, column=2)
		label_nifer = Label(ffram_tabl, text=stock[eitem]["Stoc"]).grid(row=i + 1, column=3)


def creu_bar_prynu():
	"""
		...
	"""

	# Rhaid ailddiffinio mynediad eang i newidynnau bob tro y cânt eu defnyddio
	global gwerthiannau
	global ffram_siop

	# Creu'r ffrâm prynu o fewn ffrâm y siop a ffurfweddu'r colofnau i arddangos
	# yn iawn
	ffram_prynu = Frame(ffram_siop, bd=5, relief=RIDGE)
	ffram_prynu.grid(row = 2, column = 0, sticky="ew")
	ffram_prynu.grid_columnconfigure(0, weight=1)
	ffram_prynu.grid_columnconfigure(1, weight=1)
	ffram_prynu.grid_columnconfigure(2, weight=1)

	# ...
	label_prynu = Label(ffram_prynu, text ="I Brynu: ")
	label_prynu.grid(row = 0, column = 0)
	maes_prynu = Entry(ffram_prynu)
	maes_prynu.grid(row = 0, column = 1)

	# ...
	label_gwerthiannau = Label(ffram_prynu, text ="Gwerthiannau:")
	label_gwerthiannau.grid(row = 1, column = 1)
	label_gwerth = Label(ffram_prynu, text = str(f"{gwerthiannau.get():.2f}"))
	label_gwerth.grid(row = 1,column = 2)

	# Creu botwm prynu i wneud pryniannau
	# NODYN: Mae'r ffwythiant lambda yn llawer mwy cymhleth yma, dim ond os yw
	# canlyniad cynning_pryniant yn True y caiff prosesu_pryniant ei alw
	# Dyma brif bwrpas ffwythiannau lambda, i weithredu sawl ffwythiant
	botwm_prynu = Button(ffram_prynu, text ="Prynu",
							bg = "White", fg = "Green",
							command = lambda: prosesu_pryniant(label_gwerth, 
													prosesu_pryniant.get())
							if cynning_pryniant(0)
							else None)
	botwm_prynu.grid(row = 0, column = 2)


def diweddaru_tabl_stoc():
	"""
	Dyma'r ffwythiant diweddaru stoc sy'n dinistrio'r ffram_tabl ac yn galw'r
	ffwythiant creu_tabl_stoc
	"""

	# Rhaid ailddiffinio mynediad eang i newidynnau bob tro y cânt eu defnyddio
	global table_frame

	# ...
	table_frame.destroy()
	

def cynning_pryniant(mewnbwn):
	"""
	Dyma'r ffwythiant cynning_pryniant sy'n gwirio a yw pryniant yn bosibl, os
	yw'n bosibl mae'n dychwelyd True, os nac ydy mae'n dangos rhybudd a
	ddychwelyd False

	Yn ogystal, os nad yw'r allwedd yn gyfanrif mae'n dangos rhybudd

	Args:
		mewnbwn (String): Y mewnbwn defnyddiwr ar gyfer rhif yr eitem i'w brynu

	Return: 
			...
	"""


	# Rhaid ailddiffinio mynediad eang i newidynnau bob tro y cânt eu defnyddio
	global stoc

	# ...
	try:
		allwedd = int(mewnbwn)

		if stock[allwedd]["Stoc"] > 0:
			return True
		else:
			messagebox.showwarning("Dim Stoc!", "Dim Stoc!")
			return False

	# ...
	except (ValueError, KeyError):
		messagebox.showwarning("Rhowch Allwedd Ddilys!", 
								"Rhowch Allwedd Ddilys!")
		return False


def prosesu_pryniant(label_gwerth, mewnbwn):
	"""
	Dyma'r ffwythiant prosesu_pryniant sy'n prosesu'r pryniant mewn gwirionedd.
	Mae nifer mewn stoc yn cael ei ddiweddaru, mae'r stoc yn cael ei
	hailysgrifennu i ffeil, mae'r tabl yn cael ei ddiweddaru, ac mae
	gwerthiannau yn cael ei gynyddu gan bris yr eitem.

	Args:
			...
	"""

	# Rhaid ailddiffinio mynediad eang i newidynnau bob tro y cânt eu defnyddio


	# ...
	allwedd = int(mewnbwn)
	stoc[allwedd]["Stoc"] -= 1
	ysgrifennu_stoc(stoc)
	diweddaru_tabl_stoc()

	# Mae hyn yn diweddaru'r gwerthiannau drwy olygu'r label_gwerth
	gwerthiannau.set(gwerthiannau.get() + stoc[allwedd]["Pris"])
	label_gwerth.config(text= str(f"{gwerthiannau.get():.2f}"))


