def main(): 
    wedi_mewngofnodi = False
    while not wedi_mewngofnodi:
        wedi_mewngofnodi = mewngofnodi()

    llwytho_eitemau()

    mewn_dewislen = True
    while mewn_dewislen:
        dewislen()


def mewngofnodi():
    enw_stor = "gweinyddwr"
    cyfrinair_stor = "12345"

    enw_mewn = input("Rhowch enw defnyddiwr: ")
    cyfrinair_mewn = input("Rhowch cyfrinair: ")

    if (enw_stor == enw_mewn) and (cyfrinair_stor == cyfrinair_mewn):
        print("Croeso!")
        return True
    else:
        print("Mewngofnodiad wedi Methu!")
        return False


def dewislen():
    dewis = input("""
    Dewis opsiwn:
    1. Gweld
    2. Ychwanegu
    3. Dileu
    """)

    try:
        dewisiad = int(dewis)

        if dewisiad == 1:
            gweld_eitemau()

        elif dewisiad == 2:
            ychwanegu_eitem()

        elif dewisiad == 3:
            dileu_eitem()

        else:
            print("Dewisiad annilys!")

    except ValueError:
        print("Rhaid derbyn cyfanrif dilys!")


def llwytho_eitemau():
    global eitemau

    ffeil_stoc = open('stoc.csv','r')
    eitemau = []

    for llinell in ffeil_stoc:
        eitem = []

        for colofn in llinell.strip().split(','):
            eitem.append(colofn)

        eitemau.append({ 
                        "Enw": eitem[0],
                        "Pris": int(eitem[1]),
                        "MewnStoc": int(eitem[2])
                        })
    ffeil_stoc.close()


def cadw_eitemau():
    global eitemau

    ffeil_stock = open('stock.csv','w')

    for eitem in eitemau:
        llinell = eitem["Enw"] + "," + str(eitem["Pris"]) + "," + str(eitem["MewnStoc"]) + "\n"

        ffeil_stock.write(llinell)

    ffeil_stock.close() 


def gweld_eitemau(): 
    global eitemau 

    for eitem in eitemau:
        print("Enw: " + eitem["Enw"])
        print("Pris: " + str(eitem["Pris"]))
        print("Stoc: " + str(eitem["MewnStoc"]) + "\n")


def ychwanegu_eitem():
    global eitemau
    eitem_newydd = dict()
    eitem_newydd["Enw"] = input("Enw'r eitem: ")
    eitem_newydd["Pris"] = float(input("Pris yr eitem: "))
    eitem_newydd["MewnStoc"] = int(input("Nifer mewn stoc: "))

    eitemau.append(eitem_newydd)
    cadw_eitemau()
    
def dileu_eitem():
    global eitemau

    enw_eitem = input("Enw'r eitem i ddileu: ")

    for eitem in eitemau:
        if eitem["Enw"] == enw_eitem:
            print("Enw: " + eitem["Enw"]) 
            print("Pris: " + str(eitem["Pris"]))
            print("Stoc: " + str(eitem["MewnStock"]) + "\n")

            cadarnhau = input("Dileu'r eitem? Y/N: ")
            if cadarnhau == "Y":
                eitemau.remove(eitem)
                cadw_eitemau()
