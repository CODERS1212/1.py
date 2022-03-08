# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:16:02 2022

@author: Jay Ambe
"""

from tkinter import *
import random

prateek = Tk()

prateek.title("List")
prateek.geometry("500x500")

label1 = Label(prateek)
label1["text"] = "Listed items: " + str(list1)

list1 = ["Het", "Mitansha" , "Anuraj",  "Hetarth", "prtham"]
label1["text"] = "Put the item no." + str(rendom_number) +" in the bag"

def put():
    random_number = random.sample(range(0, 7),1)
    label2["text"] = "Put the item no. "+ str(rendom_number) +" in the bsg"


btn = Button(prateek, text="Which item to put in the bag?", command = put, bg ="red", fg="bla")
btn.Place(relx=0.5, rely=0.5 ancho=CENTER)
btn1.Place(relx=0.5, rely=0.4 ancho=CENTER)
btn2.Place(relx=0.5, rely=0.6 ancho=CENTER)


prateek.mainloop()