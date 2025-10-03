#Hangman
import os

#Import dependencies
from random import randint
import tkinter as tk
from tkinter import messagebox


def main():

    global root, canfas
      
    # Creu y prif ffenestr
    root = tk.Tk()
    root.title("Hangman")

    # Ymgychwyn gem
    dechrau_gem()
    root.mainloop()


def dechrau_gem():
    global bywydau, dyfaliadau, gair

    # Diffinio bywydau, rhestr gwag o ddyfaliadau, a'r gair i ddyfalu
    bywydau = 6
    dyfaliadau = []
    gair = gair_ar_hap()

    dechrau_gui()


def gair_ar_hap():

    ffeil_geiriau = open(os.path.dirname(os.path.abspath(__file__)) +
                            "/wordlist.txt","r")
    data_geiriau = ffeil_geiriau.read()
    rhestr_geiriau = data_geiriau.split("\n")

    rhif = randint(0, len(rhestr_geiriau))
    gair = rhestr_geiriau[rhif]
    return gair


def dechrau_gui():
    global root, bywydau, dyfaliadau, gair, canfas,
            label_gair, label_bywydau, label_dyfaliadau, maes_dyfaliad

    # Creu'r canfas am lunio'r hangman
    canfas = tk.Canvas(root, width=300, height=300)
    canfas.grid(column=0, row=0)

    # Creu botymau Ail-Geisio and Allan
    botwm_ail = tk.Button(root, text="Ail-Geisio", command=lambda:ail_geisio())
    botwm_ail.grid(column=0, row=5)
    botwm_allan = tk.Button(root, text="Allan", command=lambda:adael_gem())
    botwm_allan.grid(column=0, row=6)

    # Alluogi'r defnyddiwr i ddefnyddio'r allwedd dychwelyd i ddyfalu
    root.bind("<Return>", lambda event: gwirio())

    # Lunio'r crocbren
    canfas.create_line(20, 280, 120, 280)
    canfas.create_line(70, 280, 70, 20)
    canfas.create_line(70, 20, 170, 20)
    canfas.create_line(170, 20, 170, 50)

    # Creu label i ddangos y gair
    label_gair = tk.Label(root, text=" ".join(["_" for llythyren in gair]))
    label_gair.grid(column=0, row=1)

    # Creu label i ddangos bywydau ar ôl
    label_bywydau = tk.Label(root, text="Bywydau: {}".format(lives))
    label_bywydau.grid(column=0, row=2)

    # Creu label i ddangos y dyfaliadau
    label_dyfaliadau = tk.Label(root, text="Wedi dyfalu: ")
    label_dyfaliadau.grid(column=0, row=3)

    # Creu maes i'r defnyddiwr dyfalu llythyren
    maes_dyfaliad = tk.Entry(root)
    maes_dyfaliad.grid(column=0, row=4)



def gwirio():
    global root, bywydau, dyfaliadau, gair,
            label_gair, label_bywydau, label_dyfaliadau, maes_dyfaliad
    
    dyfaliad = maes_dyfaliad.get().lower()
    maes_dyfaliad.delete(0, tk.END)
    
    # Gwirio a yw'r dyfaliad yn un llythyren, neu a yw'r dyfaliad eisoes wedi'i dyfalu 
    if len(dyfaliad) != 1 or not dyfaliad.isalpha() or dyfaliad in dyfaliadau:
        return
    
    # Ychwanegu dyfaliad i dyfaliadau
    dyfaliadau.append(dyfaliad)
    label_dyfaliadau.config(text="Wedi dyfalu: {}".format(" ".join(guessed)))
    
    # Gwirio fod y dyfaliad yn y gair
    if dyfaliad in gair:
        rhestr_llyth = list(label_gair["text"])
        for i in range(len(gair)):
            if gair[i] == dyfaliad:
                rhestr_llyth[2*i] = dyfaliad

        word_label.config(text="".join(rhestr_llyth))

        # Gwiriwch a yw'r defnyddiwr wedi ennill
        if "_" not in rhestr_llyth:
            messagebox.showinfo("Hangman","Ennill!")
            maes_dyfaliad.config(state=tk.DISABLED)
            return
    
    #Os nad yw dyfaliad yn y gair, lleihau bywydau
    else:
        bywydau -= 1
        label_ bywydau.config(text="Bywydau: {}".format(bywydau))
        
        # Llunio'r hangman
        if bywydau == 5:
            canfas.create_oval(140, 50, 200, 110)
        elif bywydau == 4:
            canfas.create_line(170, 110, 170, 170)
        elif bywydau == 3:
            canfas.create_line(170, 130, 140, 140)
        elif bywydau == 2:
            canfas.create_line(170, 130, 200, 140)
        elif bywydau == 1:
            canfas.create_line(170, 170, 140, 190)
        elif bywydau == 0:
            canfas.create_line(170, 170, 200, 190)
            messagebox.showinfo("Hangman", "Methu! Roedd '{}' y gair!".format(gair))
            maes_dyfaliad.config(state=tk.DISABLED)


def ail_geisio():
    global canfas, label_dyfaliadau, label_gair, label_bywydau

    # Dileu'r canfas a chlirio'r labelai    
    canfas.destroy()
    label_dyfaliadau.config(text="")
    label_gair.config(text="")
    label_bywydau.config(text="")

    #Ail-ddechrau Game
    dechrau_gem()
  

def adael_gem():
    global root

    #Dileu'r root (h.y. y GUI llawn)
    root.destroy()


main()
