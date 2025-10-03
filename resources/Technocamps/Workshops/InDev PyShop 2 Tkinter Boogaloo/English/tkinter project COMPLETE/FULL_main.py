#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the main module of the FULL Tkinter Shop Program. Run this module to
run the program.

This program was intended as an exercise for the WJEC 2025 Computing curriculum
(specifically the new exam style for Unit 2).

The aim of the task is to understand the program and fix all the errors that
are present, while improving the learners' ability to provide good comments and
documentation.

NOTE: This is a FULL version of the program without any errors, to be used by
      the teacher to support the learners! 
      The documentation in this program is not a WJEC GCSE requirement, but it
      is included for completeness. Some of the comments are too descriptive, 
      but are included to be helpful.
"""
__author__ = "Dan North"
__maintainer__ = "Technocamps"
__date__ = "2025/08/27"
__deprecated__ = False

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from FULL_login import create_login
from FULL_shopface import create_shopface


def switch_to_shop(login_root):
    """
    This function switches windows by destroying the login window and
    creating the shopface window.

    NOTE: the function switch_to_login is passed to create_shopface
      so that create_shopface can later call switch_to_login
        
    Args: 
        login_root (Tkinter Window): Passes the Tkinter root to be destroyed
    """
    login_root.destroy()
    create_shopface(switch_to_login)


def switch_to_login(shopface_root):
    """
    This function switches windows by destroying the shopface window and
    creating the login window.

    NOTE: the function switch_to_shop is passed to create_login
      so that create_login can later call switch_to_shop
        
    Args: 
        shopface_root (Tkinter Window): Passes the Tkinter root to be destroyed
    """
    shopface_root.destroy()
    create_login(switch_to_shop)


# We kick off our program by calling the create_login function
create_login(switch_to_shop)