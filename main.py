import tkinter as tk
import os.path
import numpy as np
import pandas as pd
from functions import *

pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 4)
#pd.set_option('display.width', 100)

# global variables for data storage across functions
table_savestate1 = pd.DataFrame()

# button functions
def delete_text():
    textbox.delete('1.0', tk.END)

def start_counts():
    global table_savestate1
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result_lead = lead_count(x)
        result_industries = industry_count(x)
        df0 = pd.DataFrame([['', '']], columns=result_lead.columns)
        df1 = pd.DataFrame([['Lead', '']], columns=df0.columns)
        df2 = pd.DataFrame([['Industry', '']], columns=df0.columns)
        total = df1.append(result_lead).append(df0).append(df2).append(result_industries)
        table_savestate1 = total
        textbox.insert('1.0', total)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def start_topleads():
    global table_savestate1
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result = get_topleads(x)
        table_savestate1 = result
        # textbox.insert('1.0', 'Our top leads are:')
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def printall_button():
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result = printall_org_table(x)
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def save():
    global table_savestate1
    s = entry_filepath_save.get()
    if table_savestate1.empty == True:
        textbox.insert('1.0', 'Print something first. The button saves the last table you have printed.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    elif os.path.isfile(s):
        textbox.insert('1.0', 'File already exists. Define new name for save file above or delete existing file.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        table_savestate1.to_csv(s)
        textbox.insert('1.0', 'File created!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        table_savestate1 = pd.DataFrame()

def start_leadsbyindustry():
    global table_savestate1
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result = leadsbyindustry(x)
        table_savestate1 = result
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def start_pitches():
    global table_savestate1
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result = pitches(x)
        table_savestate1 = result
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

# 'join' feature, feature has been suspended until further notice
"""
def start_join():
    x = entry_filepath_open.get()
    y = entry_filepath_open_cont.get()
    if os.path.isfile(entry_filepath_open.get()):
        result = join_contacts(x,y)
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
"""

def check_files():
    x = entry_filepath_open.get()
    #y = entry_filepath_open_cont.get()
    s = entry_filepath_save.get()
    textbox.delete('1.0', tk.END)
    if os.path.isfile(s) == True:
        textbox.insert('1.0', 'Savefile already exists. Please specfy new save path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:  # os.path.isfile(s)==False:
        textbox.insert('1.0', 'Save path is still available.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    """if os.path.isfile(y) == True: #function for old contacts.csv
        textbox.insert('1.0', 'Contacts file found!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:  # os.path.isfile(y)==False:
        textbox.insert('1.0', 'Contacts file NOT found!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')"""
    if os.path.isfile(x) == True:
        textbox.insert('1.0', 'Companies file found!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:  # os.path.isfile(x)==False:
        textbox.insert('1.0', 'Companies file NOT found!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

# GUI
window = tk.Tk()
window.title('Hubspool')
window.geometry('660x700')
window.resizable(False, True)
# window.rowconfigure([0,1])
# window.columnconfigure([0,1])
# DEFINITIONS
# basic layout
frame_0 = tk.Frame()
frame_0.pack()
frame_a = tk.Frame()
frame_a.pack()
frame_buttons1 = tk.Frame()
frame_buttons1.pack()
# frame_buttons2 = tk.Frame()
# frame_buttons2.pack()
frame_c = tk.Frame()
frame_c.pack()
frame_d = tk.Frame()
frame_d.pack()
# define labels
label_open_comp = tk.Label(text='Open COMPANIES.csv file from:', width=30, height=1, master=frame_a)
#label_open_cont = tk.Label(text='Open CONTACTS.csv file from:', width=30, height=1, master=frame_a)
label_save = tk.Label(text='Safe .csv file to:', width=30, height=1, master=frame_a)
label_space_top = tk.Label(text='Hubspool', width=30, height=1, master=frame_a)
label_space_top.config(font=("Courier", 44))
label_space = tk.Label(text='', width=30, height=2, master=frame_a)
label_space2 = tk.Label(text='', width=30, height=1, master=frame_c)
label_space3 = tk.Label(text='', width=30, height=0, master=frame_a)
#label_space4 = tk.Label(text='', width=30, height=0, master=frame_a)
#label3 = tk.Label(text='Output:', width=30, height=2, master=frame_c)
label4 = tk.Label(text='Copyright 2021 Braum                                                                            ',
                  width=50, height=1, master=frame_0)
label5 = tk.Label(text='                                                                            Version: 2.2.0',
                  width=50, height=1, master=frame_0)
#label_empt = tk.Label(text='', width=40, height=1, master=frame_0)
# define entries
entry_filepath_open = tk.Entry(width=80, master=frame_a)
entry_filepath_open.insert(0, 'C:/Users/NAME/Downloads/DATA.csv')
#entry_filepath_open_cont = tk.Entry(width=80, master=frame_a)
#entry_filepath_open_cont.insert(0, 'C:/Users/NAME/Downloads/CONTACTS_DATA.csv')
entry_filepath_save = tk.Entry(width=80, master=frame_a)
entry_filepath_save.insert(0, 'C:/Users/NAME/Downloads/OUTPUT.csv')
# define textbox
textbox = tk.Text(width=100, height=200, master=frame_d)
# define buttons
button_counts = tk.Button(text='Counts', width=15, height=2, bg='gray85', command=start_counts, master=frame_buttons1)
# button_open = tk.Button(text='open file', width=15, height=2, command=openfile,  master=frame_buttons1)
button_topleads = tk.Button(text='Topleads', width=15, height=2, bg='gray85', command=start_topleads,
                            master=frame_buttons1)
button_safe = tk.Button(text='Safe to .csv', width=15, height=2, bg='DarkSeaGreen1', command=save, master=frame_buttons1)
button_delete = tk.Button(text='Delete', width=15, height=2, bg='RosyBrown1', command=delete_text,
                          master=frame_buttons1)
button_printall = tk.Button(text='Print all', width=15, height=2, bg='gray85', command=printall_button,
                            master=frame_buttons1)
button_leadsbyindustry = tk.Button(text='Leads by industry', width=15, height=2, bg='gray85',
                                   command=start_leadsbyindustry, master=frame_buttons1)
button_pitches = tk.Button(text='Pitches', width=15, height=2, command=start_pitches, bg='gray85',
                        master=frame_buttons1)
button_check = tk.Button(text='Check files', width=15, height=2, bg='alice blue', command=check_files,
                         master=frame_buttons1)

# PACKS
label4.pack(side=tk.LEFT)
label5.pack(side=tk.RIGHT)
#label_empt.pack(side=tk.RIGHT)
label_space_top.pack(pady='20')
label_open_comp.pack()
entry_filepath_open.pack()
#label_space4.pack()
#label_open_cont.pack()
#entry_filepath_open_cont.pack()
label_space3.pack()
label_save.pack()
entry_filepath_save.pack()
label_space.pack()
button_printall.grid(row=1, column=0)
button_counts.grid(row=0, column=1)
#button_open.grid(row=0, column=1)
button_topleads.grid(row=1, column=1)
button_safe.grid(row=1, column=3)
button_leadsbyindustry.grid(row=0, column=2)
button_pitches.grid(row=1, column=2)
button_check.grid(row=0, column=0)

button_delete.grid(row=0, column=3)
label_space2.pack()

#label3.pack()
textbox.pack()

window.mainloop()
