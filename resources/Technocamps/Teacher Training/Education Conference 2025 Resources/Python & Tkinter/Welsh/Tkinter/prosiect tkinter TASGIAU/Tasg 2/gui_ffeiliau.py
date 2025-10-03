import os


def ol_ffeil_stoc(modd):
	"""
	Dyma'r ffwythiant i ôl y ffeil stoc o'r cyfeiriadur. Dyle'r ffwythiant yma
	gweithio hyd yn oed ar ôl symud y cyfeiriadur (os yw'r strwythur y tu mewn
	i'r cyfeiriadur yn gyson).

	Args:
		modd (String): Y modd i agor y ffeil stoc (e.e. darllen/ysgrifennu)

	Dychwelyd: 
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
		pris = int(eitem[2].strip())
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