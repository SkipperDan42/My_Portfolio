from tkinter import *
from tkinter import messagebox


def creu_mewngofnodi():
	"""
	Dyma'r ffenestr mewngofnodi i ganiatáu mynediad i'r siop

	Args: ...
		
	"""


	def ffwythiant_dibwrpas():
		"""
		Mae'r ffwythiant hwn yn gwbl ddibwrpas.
		Ei unig ddefnydd go iawn fydd dangos pam y byddwn yn pasio ffwythiannau
		fel newidynnau.
		"""
		
		print("This functions is pointless.")


	def prosesu_mewngofnodi():
		"""
		Mae'r ffwythiant hwn ...
		"""

		# Storio'r manylion mewngofnodi
		enw_stor = ""
		cyfrinair_stor = ""

		# Gwiriwch a yw manylion mewngofnodi'r defnyddiwr yn cyfateb i fewnbwn
		# y defnyddiwr
		if ((enw_mewn.get() == enw_stor) or
				(cyfrinair_mewn.get() == cyfrinair_stor)):

			# Nawr rydym yn galw newid_i_siop i lansio'r rhaglen shopface
			print("I'r Siop!")

		else:
			# ...
			messagebox.showwarning("Wedi methu!", "Wedi methu!")


	# Creu y Tkinter root ar gyfer y ffenestr mewngofnodi,
	# creu teitl i'r ffenestr, a ffrâm newydd tu fewn,
	# a'i osod gan ddefnyddio'r rheolwr pack
	root_mewngofnodi = Tk()
	root_mewngofnodi.title("01")
	ffram_mewngofnodi = Frame(root_mewngofnodi)
	ffram_mewngofnodi.pack()


	# O fewn y ffrâm_mewngofnodi, crëwch deitl a'i bacio
	label_teitl = Label(ffram_mewngofnodi, text = "Croeso i'r Siop!")


	# O fewn y ffrâm_mewngofnodi, crëwch ffrâm, label a'r maes mewnbwn ar gyfer
	# enw defnyddiwr, paciwch nhw i gyd
	ffram_enw = Frame(ffram_mewngofnodi)
	ffram_enw.pack()
	label_enw = Label(ffram_enw, text = "enw")
	label_enw.pack(side = LEFT)
	maes_enw = Entry(ffram_enw)
	maes_enw.pack(side = RIGHT)

	# ...
	ffram_cyfrinair = Frame(ffram_mewngofnodi)
	ffram_cyfrinair.pack()
	label_cyfrinair = Label(ffram_cyfrinair, text = "cyfrinair")
	label_cyfrinair.pack(side=RIGHT)
	maes_cyfrinair = Entry(ffram_cyfrinair)
	maes_cyfrinair.pack(side=LEFT)


	#O fewn y ffrâm_mewngofnodi, creu botwm sy'n galw prosesu_mewngofnodi,
	# a'i bacio
	botwm_cyflwyno = Button(ffram_mewngofnodi, text = "cyflwyno",
							bg = "White", fg = "Red",
							command = ffwythiant_dibwrpas)
	botwm_cyflwyno.pack()

	# Mae'r ffwythiant mainloop yn cadw'r GUI hwn mewn dolen (h.y. yn ei gadw'n
	# weithredol) ac yn aros am fewnbwn gan y defnyddiwr - mae angen hwn arnom
	# ar ddiwedd pob ffenestr newydd
	root_mewngofnodi.mainloop()