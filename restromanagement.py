# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:16:45 2020

@author: birla
"""

from tkinter import *
from tkinter import messagebox
import random
import time
import datetime

root = Tk() # creates new window
root.geometry("1465x770+0+0") # to set screen size
root.title("RESTAURANT MANAGEMENT SYSTEM") # to give title
root.configure(background='black') # used to configure widgets
#root.iconbitmap(r'C:\Users\birla\OneDrive\Desktop\PYHTON VS\restro_icon.ico') # used to add icon to the window

#========================================FRAMES=================================

Tops = Frame(root, width=1465, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=670, bd=8, relief="raise")
f1.pack(side=LEFT)

# creating child frames of 'f1'
f1_top = Frame(f1, width=900 , height=330 , bd=8 , relief="raise")
f1_top.pack(side=TOP)

# creating child frames of 'f1_top'
f1_top_left = Frame(f1_top, width=400 , height=330 , bd=16 , relief="raise")
f1_top_left.pack(side=LEFT)

f1_top_right = Frame(f1_top, width=400 , height=330 , bd=16 , relief="raise")
f1_top_right.pack(side=RIGHT)
# end of child frames of 'f1_top'

f1_bottom = Frame(f1, width=900 , height=340 , bd=6 , relief="raise")
f1_bottom.pack(side=BOTTOM)

# creating child frames of 'f1_bottom'
f1_bottom_left = Frame(f1_bottom, width=450 , height=340 , bd=14 , relief="raise")
f1_bottom_left.pack(side=LEFT)

f1_bottom_right = Frame(f1_bottom, width=450 , height=340 , bd=14 , relief="raise")
f1_bottom_right.pack(side=RIGHT)
# end of child frames of 'f1_bottom'

# end of child frames of 'f1'

f2 = Frame(root, width=565 , height=670, bd=8, relief="raise")
f2.pack(side=RIGHT)

# creating child frames of 'f2'
f2_top = Frame(f2, width=565 , height=520 , bd=12 , relief="raise")
f2_top.pack(side=TOP)

f2_bottom = Frame(f2, width=565 , height=150 , bd=16 , relief="raise")
f2_bottom.pack(side=BOTTOM)
# end of child frames of 'f2'

Tops.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

lbl_info = Label(Tops , text="RESTAURANT MANAGEMENT SYSTEM" , bd=10 , font="Consolas 68 bold italic")
lbl_info.grid(row=0 , column=0)

#=======================================EXIT METHOD=======================================

def qExit():
    qExit = messagebox.askyesno("Quit System" , "Do you want to quit?")
    if qExit > 0 :
        root.destroy()
        return

#=======================================END OF EXIT METHOD=======================================

#=======================================RESET METHOD=======================================
def Reset():
    tax_paid.set("")
    sub_total.set("")
    total_cost.set("")
    cost_of_soups.set("")
    cost_of_snacks.set("")
    cost_of_main.set("")
    txt_recipt.delete("1.0",END)
    
    e_tea.set("0")
    e_coffee.set("0")
    
    e_soup1.set("0")
    e_soup2.set("0")
    
    e_fries.set("0")
    e_manchurian.set("0")
    e_vpizza.set("0")
    e_cpizza.set("0")
    e_mpizza.set("0")
    e_burger.set("0")
    
    e_dosa.set("0")
    e_idli.set("0")
    
    e_frice.set("0")
    e_trice.set("0")
    
    e_handi.set("0")
    e_paneer.set("0")
    
    e_roti.set("0")
    
    e_buttermilk.set("0")
                
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    
    txt_tea.configure(state=DISABLED)
    txt_coffee.configure(state=DISABLED)
    txt_soup_1.configure(state=DISABLED)
    txt_soup_2.configure(state=DISABLED)
    txt_fries.configure(state=DISABLED)
    txt_manchurian.configure(state=DISABLED)
    txt_burger.configure(state=DISABLED)
    txt_vpizza.configure(state=DISABLED)
    txt_cpizza.configure(state=DISABLED)
    txt_mpizza.configure(state=DISABLED)
    txt_dosa.configure(state=DISABLED)
    txt_idli.configure(state=DISABLED)
    txt_handi.configure(state=DISABLED)
    txt_panner.configure(state=DISABLED)
    txt_roti.configure(state=DISABLED)
    txt_rice.configure(state=DISABLED)
    txt_srice.configure(state=DISABLED)
    txt_buttermilk.configure(state=DISABLED)

#=======================================END OF RESET METHOD=======================================

#=======================================CHECKBUTTON METHOD=======================================
    
def chkbutton_value():
    if(var1.get()==1):
        txt_tea.configure(state=NORMAL)
    elif var1.get()==0:
        txt_tea.configure(state=DISABLED)
        e_tea.set("0")
    if(var2.get()==1):
        txt_coffee.configure(state=NORMAL)
    elif var2.get()==0:
        txt_coffee.configure(state=DISABLED)
        e_coffee.set("0")
    if(var3.get()==1):
        txt_soup_1.configure(state=NORMAL)
    elif var3.get()==0:
        txt_soup_1.configure(state=DISABLED)
        e_soup1.set("0")
    if(var4.get()==1):
        txt_soup_2.configure(state=NORMAL)
    elif var4.get()==0:
        txt_soup_2.configure(state=DISABLED)
        e_soup2.set("0")
    if(var5.get()==1):
        txt_fries.configure(state=NORMAL)
    elif var5.get()==0:
        txt_fries.configure(state=DISABLED)
        e_fries.set("0")
    if(var6.get()==1):
        txt_manchurian.configure(state=NORMAL)
    elif var6.get()==0:
        txt_manchurian.configure(state=DISABLED)
        e_manchurian.set("0")
    if(var7.get()==1):
        txt_dosa.configure(state=NORMAL)
    elif var7.get()==0:
        txt_dosa.configure(state=DISABLED)
        e_dosa.set("0")
    if(var8.get()==1):
        txt_idli.configure(state=NORMAL)
    elif var8.get()==0:
        txt_idli.configure(state=DISABLED)
        e_idli.set("0")
    if(var9.get()==1):
        txt_vpizza.configure(state=NORMAL)
    elif var9.get()==0:
        txt_vpizza.configure(state=DISABLED)
        e_vpizza.set("0")
    if(var10.get()==1):
        txt_cpizza.configure(state=NORMAL)
    elif var10.get()==0:
        txt_cpizza.configure(state=DISABLED)
        e_cpizza.set("0")
    if(var11.get()==1):
        txt_mpizza.configure(state=NORMAL)
    elif var11.get()==0:
        txt_mpizza.configure(state=DISABLED)
        e_mpizza.set("0")
    if(var12.get()==1):
        txt_rice.configure(state=NORMAL)
    elif var12.get()==0:
        txt_rice.configure(state=DISABLED)
        e_frice.set("0")
    if(var13.get()==1):
        txt_srice.configure(state=NORMAL)
    elif var13.get()==0:
        txt_srice.configure(state=DISABLED)
        e_trice.set("0")
    if(var14.get()==1):
        txt_burger.configure(state=NORMAL)
    elif var14.get()==0:
        txt_burger.configure(state=DISABLED)
        e_burger.set("0")
    if(var15.get()==1):
        txt_handi.configure(state=NORMAL)
    elif var15.get()==0:
        txt_handi.configure(state=DISABLED)
        e_handi.set("0")
    if(var16.get()==1):
        txt_panner.configure(state=NORMAL)
    elif var16.get()==0:
        txt_panner.configure(state=DISABLED)
        e_paneer.set("0")
    if(var17.get()==1):
        txt_roti.configure(state=NORMAL)
    elif var17.get()==0:
        txt_roti.configure(state=DISABLED)
        e_roti.set("0")
    if(var18.get()==1):
        txt_buttermilk.configure(state=NORMAL)
    elif var18.get()==0:
        txt_buttermilk.configure(state=DISABLED)
        e_buttermilk.set("0")    

#=======================================END OF CHECKBUTTON METHOD=======================================
        
#=======================================COST OF ITEMS METHODS=====================================
def cost():
    item1 = float(e_tea.get())
    item2 = float(e_coffee.get())
    item3 = float(e_soup1.get())
    item4 = float(e_soup2.get())
    item5 = float(e_fries.get())
    item6 = float(e_manchurian.get())
    item7 = float(e_dosa.get())
    item8 = float(e_idli.get())
    item9 = float(e_vpizza.get())
    item10 = float(e_cpizza.get())
    item11 = float(e_mpizza.get())
    item12 = float(e_frice.get())
    item13 = float(e_trice.get())
    item14 = float(e_burger.get())
    item15 = float(e_handi.get())
    item16 = float(e_paneer.get())
    item17 = float(e_roti.get())
    item18 = float(e_buttermilk.get())
    
    price_bev = (item1 * 10) + (item2 * 15) + (item18 * 20)
    price_soup = (item3 * 70) + (item4 * 50)
    price_snacks = (item5 * 50) + (item6 * 50) + (item14 * 50) + (item7 * 50) + (item8 * 30)
    price_main = (item9 * 80) + (item10 * 120) + (item11 * 150) + (item15 * 180) + (item16 * 180) + (item17 * 20) + (item12 * 100) + (item13 * 120)
    
    SoupPrice = str('%.2f'%(price_soup)) + "Rs"
    SnacksPrice = str('%.2f'%(price_snacks)) + "Rs"
    MainPrice = str('%.2f'%(price_main)) + "Rs"
    
    cost_of_soups.set(SoupPrice)
    cost_of_snacks.set(SnacksPrice)
    cost_of_main.set(MainPrice)
    
    price_sub = price_soup + price_snacks + price_main + price_bev
    SubPrice = str('%.2f'%(price_sub)) + "Rs"
    sub_total.set(SubPrice)
    
    price_tax = 0.05 * price_sub
    Tax = str('%.2f'%(price_tax)) + "Rs"
    tax_paid.set(Tax)
    
    TotalPrice = str('%.2f'%(price_sub + price_tax)) + "Rs"
    total_cost.set(TotalPrice)

#=======================================END OF COST OF ITEMS METHOD=======================================
    
#=======================================RECIPT METHOD=======================================

def Recipt_btn():
    txt_recipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    recipt_ref.set("BILL" + randomRef)

    txt_recipt.insert(END, 'Receipt Ref: \t\t\t'+recipt_ref.get()+"\t\t\t"+date_of_order.get()+"\n")
    txt_recipt.insert(END, 'Items\t\t\t'+'Quantity\t\t'+"Price \n\n")
    
    if int(e_tea.get()) > 0:
        txt_recipt.insert(END, 'Tea:\t\t\t'+str(e_tea.get())+'\t\t'+str('Rs%.2f'%(int(e_tea.get())*10))+'\n')
    if int(e_coffee.get()) > 0:
        txt_recipt.insert(END, 'Coffee:\t\t\t'+str(e_coffee.get())+'\t\t'+str('Rs%.2f'%(int(e_coffee.get())*15))+'\n')
    if int(e_soup1.get()) > 0:
        txt_recipt.insert(END, 'Manchow Soup :\t\t\t'+str(e_soup1.get())+'\t\t'+str('Rs%.2f'%(int(e_soup1.get())*70))+'\n')
    if int(e_soup2.get()) > 0:
        txt_recipt.insert(END, 'Thai Soup :\t\t\t'+str(e_soup2.get())+'\t\t'+str('Rs%.2f'%(int(e_soup2.get())*50))+'\n')
    if int(e_fries.get()) > 0:
        txt_recipt.insert(END, 'Fries:\t\t\t'+str(e_fries.get())+'\t\t'+str('Rs%.2f'%(int(e_fries.get())*50))+'\n')
    if int(e_manchurian.get()) > 0:
        txt_recipt.insert(END, 'Dry Manchurian :\t\t\t'+str(e_manchurian.get())+'\t\t'+str('Rs%.2f'%(int(e_manchurian.get())*50))+'\n')
    if int(e_burger.get()) > 0:
        txt_recipt.insert(END, 'Burger :\t\t\t'+str(e_burger.get())+'\t\t'+str('Rs%.2f'%(int(e_burger.get())*50))+'\n')
    if int(e_dosa.get()) > 0:
        txt_recipt.insert(END, 'Masala Dosa :\t\t\t'+str(e_dosa.get())+'\t\t'+str('Rs%.2f'%(int(e_dosa.get())*50))+'\n')
    if int(e_idli.get()) > 0:
        txt_recipt.insert(END, 'Idli:\t\t\t'+str(e_idli.get())+'\t\t'+str('Rs%.2f'%(int(e_idli.get())*30))+'\n')
    if int(e_vpizza.get()) > 0:
        txt_recipt.insert(END, 'Veg Pizza:\t\t\t'+str(e_vpizza.get())+'\t\t'+str('Rs%.2f'%(int(e_vpizza.get())*80))+'\n')
    if int(e_cpizza.get()) > 0:
        txt_recipt.insert(END, 'Cheese Corn Pizza:\t\t\t'+str(e_cpizza.get())+'\t\t'+str('Rs%.2f'%(int(e_cpizza.get())*120))+'\n')
    if int(e_mpizza.get()) > 0:
        txt_recipt.insert(END, 'Mix Veg Pizza:\t\t\t'+str(e_mpizza.get())+'\t\t'+str('Rs%.2f'%(int(e_mpizza.get())*150))+'\n')
    if int(e_frice.get()) > 0:
        txt_recipt.insert(END, 'Fried Rice:\t\t\t'+str(e_frice.get())+'\t\t'+str('Rs%.2f'%(int(e_frice.get())*100))+'\n')
    if int(e_trice.get()) > 0:
        txt_recipt.insert(END, 'Triple Schezwan Rice:\t\t\t'+str(e_trice.get())+'\t\t'+str('Rs%.2f'%(int(e_trice.get())*120))+'\n')
    if int(e_handi.get()) > 0:
        txt_recipt.insert(END, 'Paneer Handi:\t\t\t'+str(e_handi.get())+'\t\t'+str('Rs%.2f'%(int(e_handi.get())*180))+'\n')
    if int(e_paneer.get()) > 0:
        txt_recipt.insert(END, 'Panner Butter Masala:\t\t\t'+str(e_paneer.get())+'\t\t'+str('Rs%.2f'%(int(e_paneer.get())*180))+'\n')
    if int(e_roti.get()) > 0:
        txt_recipt.insert(END, 'Chapatti:\t\t\t'+str(e_roti.get())+'\t\t'+str('Rs%.2f'%(int(e_roti.get())*20))+'\n')
    if int(e_buttermilk.get()) > 0:
        txt_recipt.insert(END, 'Buttermilk:\t\t\t'+str(e_buttermilk.get())+'\t\t'+str('Rs%.2f'%(int(e_buttermilk.get())*20))+'\n')
    
    txt_recipt.insert(END, '\nCost of Drinks:\t'+cost_of_soups.get()+'\nCost of Cakes:\t'+cost_of_snacks.get()+"\n")
    txt_recipt.insert(END, "Tax Paid:\t"+ tax_paid.get()+"\nSubTotal:\t"+ sub_total.get()+"\n")
    txt_recipt.insert(END, "Total Cost:\t"+ total_cost.get()+"\n")
#=======================================END OF RECIPT METHOD METHOD=======================================

#=======================================VARIABLES=======================================
    
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()

date_of_order = StringVar()
recipt_ref = StringVar()
tax_paid = StringVar()
sub_total = StringVar()
total_cost = StringVar()
cost_of_soups = StringVar()
cost_of_snacks = StringVar()
cost_of_main = StringVar()

e_tea = StringVar()
e_coffee = StringVar()

e_soup1 = StringVar()
e_soup2 = StringVar()

e_fries = StringVar()
e_manchurian = StringVar()
e_vpizza = StringVar()
e_cpizza = StringVar()
e_mpizza = StringVar()
e_burger = StringVar()

e_dosa = StringVar()
e_idli = StringVar()

e_frice = StringVar()
e_trice = StringVar()

e_handi = StringVar()
e_paneer = StringVar()

e_roti = StringVar()

e_buttermilk = StringVar()

e_tea.set("0")
e_coffee.set("0")

e_soup1.set("0")
e_soup2.set("0")

e_fries.set("0")
e_manchurian.set("0")
e_vpizza.set("0")
e_cpizza.set("0")
e_mpizza.set("0")
e_burger.set("0")

e_dosa.set("0")
e_idli.set("0")

e_frice.set("0")
e_trice.set("0")

e_handi.set("0")
e_paneer.set("0")

e_roti.set("0")

e_buttermilk.set("0")

date_of_order.set(time.strftime("%d/%m/%Y"))

#====================LEFT========================
tea = Checkbutton(f1_top_left , text="Tea\t\t\t" , variable=var1 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
tea.grid(row=0 , column=0)
txt_tea = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_tea , state=DISABLED)
txt_tea.grid(row=0 , column=1)

coffee = Checkbutton(f1_top_left , text="Coffee\t\t\t" , variable=var2 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
coffee.grid(row=1 , column=0)
txt_coffee = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_coffee, state=DISABLED)
txt_coffee.grid(row=1 , column=1)

soup_1 = Checkbutton(f1_top_left , text="Manchow Soup\t\t" , variable=var3 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
soup_1.grid(row=2 , column=0)
txt_soup_1 = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_soup1, state=DISABLED)
txt_soup_1.grid(row=2 , column=1)

soup_2 = Checkbutton(f1_top_left , text="Thai Soup\t\t" , variable=var4 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
soup_2.grid(row=3 , column=0)
txt_soup_2 = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_soup2, state=DISABLED)
txt_soup_2.grid(row=3 , column=1)

fries = Checkbutton(f1_top_left , text="French Fries\t\t" , variable=var5 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
fries.grid(row=4 , column=0)
txt_fries = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_fries, state=DISABLED)
txt_fries.grid(row=4 , column=1)

manchurian = Checkbutton(f1_top_left , text="Dry Manchurian\t\t" , variable=var6 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
manchurian.grid(row=5 , column=0)
txt_manchurian = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_manchurian, state=DISABLED)
txt_manchurian.grid(row=5 , column=1)

dosa = Checkbutton(f1_top_left , text="Masala Dosa\t\t" , variable=var7 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
dosa.grid(row=6 , column=0)
txt_dosa = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_dosa, state=DISABLED)
txt_dosa.grid(row=6 , column=1)

idli = Checkbutton(f1_top_left , text="Idli\t\t\t" , variable=var8 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
idli.grid(row=7 , column=0)
txt_idli = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_idli, state=DISABLED)
txt_idli.grid(row=7 , column=1)

vpizza = Checkbutton(f1_top_left , text="Veg Pizza\t\t" , variable=var9 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
vpizza.grid(row=8 , column=0)
txt_vpizza = Entry(f1_top_left , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_vpizza, state=DISABLED)
txt_vpizza.grid(row=8 , column=1)

#====================RIGHT========================
cpizza = Checkbutton(f1_top_right , text="Cheese Corn Pizza\t\t" , variable=var10 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
cpizza.grid(row=0 , column=0)
txt_cpizza = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_cpizza, state=DISABLED)
txt_cpizza.grid(row=0 , column=1)

mpizza = Checkbutton(f1_top_right , text="Mix Veg Pizza\t\t\t" , variable=var11 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
mpizza.grid(row=1 , column=0)
txt_mpizza = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_mpizza, state=DISABLED)
txt_mpizza.grid(row=1 , column=1)

rice = Checkbutton(f1_top_right , text="Fried Rice\t\t\t" , variable=var12 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
rice.grid(row=2 , column=0)
txt_rice = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_frice, state=DISABLED)
txt_rice.grid(row=2 , column=1)

srice = Checkbutton(f1_top_right , text="Triple Schezwan Rice\t\t" , variable=var13 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
srice.grid(row=3 , column=0)
txt_srice = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_trice, state=DISABLED)
txt_srice.grid(row=3 , column=1)

burger = Checkbutton(f1_top_right , text="Burger\t\t\t\t" , variable=var14 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
burger.grid(row=4 , column=0)
txt_burger = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_burger, state=DISABLED)
txt_burger.grid(row=4 , column=1)

handi = Checkbutton(f1_top_right , text="Panner Handi\t\t\t" , variable=var15 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
handi.grid(row=5 , column=0)
txt_handi = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_handi, state=DISABLED)
txt_handi.grid(row=5 , column=1)

panner = Checkbutton(f1_top_right , text="Panner Butter Masala\t\t" , variable=var16 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
panner.grid(row=6 , column=0)
txt_panner = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_paneer, state=DISABLED)
txt_panner.grid(row=6 , column=1)

roti = Checkbutton(f1_top_right , text="Chappati\t\t\t" , variable=var17 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
roti.grid(row=7 , column=0)
txt_roti = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_roti, state=DISABLED)
txt_roti.grid(row=7 , column=1)

buttermilk = Checkbutton(f1_top_right , text="Buttermilk\t\t\t" , variable=var18 , onvalue=1 , offvalue=0 , command=chkbutton_value , font="Consolas 16 bold italic")
buttermilk.grid(row=8 , column=0)
txt_buttermilk = Entry(f1_top_right , font="Consolas 16 bold" , bd=8 , width=6 , justify='left' , textvariable=e_buttermilk, state=DISABLED)
txt_buttermilk.grid(row=8 , column=1 )

#==================================INFORMATION=====================================
lbl_recipt = Label(f2_top , font="Consolas 14 bold" , text="Recipt" , bd=2 , anchor='w')
lbl_recipt.grid(row=0 , column=0 , sticky=W)

txt_recipt = Text(f2_top , font="Consolas 11 bold" , bd=8 , width=46 , height=24 , bg="white")
txt_recipt.grid(row=1 , column=0)

#==================================COST OF ITEMS INFORMATION=====================================
lbl_cost_soup = Label(f1_bottom_left , font="Consolas 17 bold" , text="Cost of Soups" , bd=8)
lbl_cost_soup.grid(row=0 , column=0 , sticky=W)
txt_soup = Entry(f1_bottom_left , font="Consolas 17 bold" , bd=8 , justify='left' , textvariable=cost_of_soups)
txt_soup.grid(row=0 , column=1 , sticky=W)

lbl_cost_snacks = Label(f1_bottom_left , font="Consolas 17 bold" , text="Cost of Snacks" , bd=8)
lbl_cost_snacks.grid(row=1 , column=0 , sticky=W)
txt_snacks = Entry(f1_bottom_left , font="Consolas 17 bold" , bd=8 , justify='left' , textvariable=cost_of_snacks)
txt_snacks.grid(row=1 , column=1 , sticky=W)

lbl_cost_main = Label(f1_bottom_left , font="Consolas 17 bold" , text="Cost of Main Course" , bd=8)
lbl_cost_main.grid(row=2 , column=0 , sticky=W)
txt_main = Entry(f1_bottom_left , font="Consolas 17 bold" , bd=8 , justify='left' , textvariable=cost_of_main)
txt_main.grid(row=2 , column=1 , sticky=W)

#==================================PAYMENT INFORMATION=====================================
lbl_cost_tax = Label(f1_bottom_right , font="Consolas 17 bold" , text="Tax" , bd=8)
lbl_cost_tax.grid(row=0 , column=0 , sticky=W)
txt_tax = Entry(f1_bottom_right , font="Consolas 17 bold" , bd=8 , justify='left' , insertwidth=2 , textvariable=tax_paid)
txt_tax.grid(row=0 , column=1 , sticky=W)

lbl_sub_total = Label(f1_bottom_right , font="Consolas 17 bold" , text="Sub Total" , bd=8)
lbl_sub_total.grid(row=1 , column=0 , sticky=W)
txt_sub_total = Entry(f1_bottom_right, font="Consolas 17 bold" , bd=8 , justify='left' , insertwidth=2 , textvariable=sub_total)
txt_sub_total.grid(row=1 , column=1 , sticky=W)

lbl_total = Label(f1_bottom_right , font="Consolas 17 bold" , text="Total" , bd=8)
lbl_total.grid(row=2 , column=0 , sticky=W)
txt_total = Entry(f1_bottom_right , font="Consolas 17 bold" , bd=8 , justify='left' , insertwidth=2 , textvariable=total_cost)
txt_total.grid(row=2 , column=1 , sticky=W)

#==================================BUTTONS=====================================
btn_total = Button(f2_bottom , padx=16 , pady=3 , bd=4 , fg="black" , font="Consolas 14 bold" , width=5 , text="Total" , command=cost)
btn_total.grid(row=0 , column=0)

btn_recipt = Button(f2_bottom , padx=16 , pady=3 , bd=4 , fg="black" , font="Consolas 14 bold" , width=5 , text="Recipt" , command=Recipt_btn)
btn_recipt.grid(row=0 , column=1)

btn_reset = Button(f2_bottom , padx=16 , pady=3 , bd=4 , fg="black" , font="Consolas 14 bold" , width=5 , text="Reset" , command=Reset)
btn_reset.grid(row=0 , column=2)

btn_exit = Button(f2_bottom , padx=16 , pady=3 , bd=4 , fg="black" , font="Consolas 14 bold" , width=5 , text="Exit" , command=qExit)
btn_exit.grid(row=0 , column=3)

root.mainloop()
