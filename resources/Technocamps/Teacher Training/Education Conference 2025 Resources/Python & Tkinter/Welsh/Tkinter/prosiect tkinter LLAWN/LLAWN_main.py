#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dyma prif modiwl y Rhaglen Siop Tkinter LLAWN. Rhedwch y modiwl yma i redeg y
rhaglen.

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

from LLAWN_mewngofnodi import creu_mewngofnodi
from LLAWN_siop import creu_siop


def newid_i_siop(root_mewngofnodi):
    """
    Mae'r ffwythinat hon yn newid ffenestri drwy ddinistrio'r ffenestr
    mewngofnodi a chreu'r ffenestr siop.

    NODYN: mae'r ffwythiant newid_i_mewngofnodi yn cael ei basio i creu_siop
    fel y gall creu_siop alw newid_i_mewngofnodi yn ddiweddarach
        
    Args: 
        root_mewngofnodi (Ffenestr Tkinter): Yn pasio'r gwreiddyn Tkinter i
                                             gael ei ddinistrio
    """
    root_mewngofnodi.destroy()
    creu_siop(newid_i_mewngofnodi)


def newid_i_mewngofnodi(root_siop):
    """
    Mae'r ffwythinat hon yn newid ffenestri drwy ddinistrio'r ffenestr siop a
    chreu'r ffenestr mewngofnodi.

    NODYN: mae'r ffwythiant newid_i_siop yn cael ei basio i creu_mewngofnodi
           fel y gall creu_mewngofnodi alw newid_i_siop yn ddiweddarach
        
    Args: 
        root_siop (Ffenestr Tkinter): Yn pasio'r gwreiddyn Tkinter i gael ei
                                      ddinistrio
    """
    root_siop.destroy()
    creu_mewngofnodi(newid_i_siop)


# Rydym yn cychwyn ein rhaglen drwy alw'r ffwythiant creu_mewngofnodi
creu_mewngofnodi(newid_i_siop)