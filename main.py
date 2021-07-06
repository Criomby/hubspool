import tkinter as tk
from tkinter import filedialog as fd
import os.path
import numpy as np
import pandas as pd
from functions import *
import openpyxl

# global variables for data storage across functions
table_savestate1 = pd.DataFrame()
company_data_filepath = 'none'

# button functions
def delete_text():
    global table_savestate1
    textbox.delete('1.0', tk.END)
    table_savestate1 = pd.DataFrame()

def start_counts():
    global table_savestate1
    global company_data_filepath
    x = company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        leads_disordered, leads_inorder = lead_count(x)
        cats_disordered, cats_inorder = industry_count(x)
        df0 = pd.DataFrame([['', '']], columns=leads_disordered.columns)
        df1 = pd.DataFrame([['Lead', '']], columns=df0.columns)
        df2 = pd.DataFrame([['Industry', '']], columns=df0.columns)
        total = df1.append(leads_inorder).append(df0).append(df2).append(cats_inorder)
        table_savestate1 = total
        textbox.insert('1.0', leads_disordered)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', 'Lead categories sorted by size:')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', cats_disordered)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', 'Industries sorted by size:')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', total)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'No file opened. Select a file first.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def start_topleads():
    global table_savestate1
    global company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(company_data_filepath):
        result = get_topleads(company_data_filepath)
        table_savestate1 = result
        # textbox.insert('1.0', 'Our top leads are:')
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'No file opened. Select a file first.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def printall_button():
    global company_data_filepath
    x = company_data_filepath
    #x = entry_filepath_open.get()
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        result = printall_org_table(x)
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'No file opened. Select a file first.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def start_leadsbyindustry():
    global table_savestate1
    global company_data_filepath
    x = company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        result = leadsbyindustry(x)
        table_savestate1 = result
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'No file opened. Select a file first.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def start_pitches():
    global table_savestate1
    global company_data_filepath
    x = company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        result = pitches(x)
        table_savestate1 = result
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'No file opened. Select a file first.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def select_file():
    global company_data_filepath
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    company_data_filepath = filename
    textbox.delete('1.0', tk.END)
    if filename == '':
        textbox.insert('1.0', 'No file opened.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'Opened file: ' + filename)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def save_file():
    global table_savestate1
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    filename = fd.asksaveasfilename(
        title='Save a file',
        initialdir='/',
        filetypes=filetypes)
    #textbox.delete('1.0', tk.END)
    if table_savestate1.empty == True:
        textbox.insert('1.0', 'Execute a function first to save it.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    elif filename == '':
        textbox.insert('1.0', 'No file saved.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        table_savestate1.to_excel(filename + '.xlsx')
        textbox.insert('1.0', 'Saved file: ' + filename)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def exex_all():
    global company_data_filepath
    x = company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        # counts
        leads_disordered, leads_inorder = lead_count(x)
        cats_disordered, cats_inorder = industry_count(x)
        df0 = pd.DataFrame([['', '']], columns=leads_disordered.columns)
        df1 = pd.DataFrame([['Lead', '']], columns=df0.columns)
        df2 = pd.DataFrame([['Industry', '']], columns=df0.columns)
        total = df1.append(leads_inorder).append(df0).append(df2).append(cats_inorder)
        table_savestate1 = total
        table_savestate2 = leads_disordered
        table_savestate3 = cats_disordered
        textbox.insert('1.0', 'Topleads done.')
        textbox.insert('1.0', '\n')
        # leads by industry
        table_savestate4 = leadsbyindustry(x)
        textbox.insert('1.0', 'Pitches done.')
        textbox.insert('1.0', '\n')
        # pitches
        table_savestate5 = pitches(x)
        textbox.insert('1.0', 'Leads by industry done.')
        textbox.insert('1.0', '\n')
        # topleads
        table_savestate6 = get_topleads(x)
        textbox.insert('1.0', 'Counts (ordered & raw) done.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        with pd.ExcelWriter(x + '_Hubspool.xlsx') as writer:
            table_savestate1.to_excel(writer, sheet_name='Counts+Industries')
            table_savestate2.to_excel(writer, sheet_name='Counts_raw')
            table_savestate3.to_excel(writer, sheet_name='Industries_raw')
            table_savestate4.to_excel(writer, sheet_name='Leads_by_industries')
            table_savestate5.to_excel(writer, sheet_name='Pitches')
            table_savestate6.to_excel(writer, sheet_name='Topleads')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', x + 'Hubspool')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', 'Excel file generated and saved to:')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'Open a file first.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

# GUI
window = tk.Tk()
window.title('Hubspool')
window.geometry('660x700')
window.resizable(False, True)
# DEFINITIONS
# basic layout
frame_0 = tk.Frame()
frame_0.pack()
frame_a = tk.Frame()
frame_a.pack()
frame_buttons1 = tk.Frame()
frame_buttons1.pack()
frame_c = tk.Frame()
frame_c.pack()
frame_d = tk.Frame()
frame_d.pack()
# define labels
label_space_top = tk.Label(text='Hubspool', width=30, height=1, master=frame_a)
label_space_top.config(font=("Courier", 44))
label_space2 = tk.Label(text='', width=30, height=1, master=frame_c)
label_space3 = tk.Label(text='', width=30, height=0, master=frame_a)
label4 = tk.Label(text='Copyright 2021 Braum                                                                            ',
                  width=50, height=1, master=frame_0)
label5 = tk.Label(text='                                                                            Version: 2.3.0',
                  width=50, height=1, master=frame_0)
# define textbox
textbox = tk.Text(width=100, height=200, master=frame_d)
# define buttons
button_counts = tk.Button(text='Counts', width=15, height=2, bg='gray85', command=start_counts, master=frame_buttons1)
button_topleads = tk.Button(text='Topleads', width=15, height=2, bg='gray85', command=start_topleads,
                            master=frame_buttons1)
button_safe = tk.Button(text='Safe to Excel', width=15, height=2, bg='DarkSeaGreen1', command=save_file, master=frame_buttons1)
button_delete = tk.Button(text='Delete', width=15, height=2, bg='RosyBrown1', command=delete_text,
                          master=frame_buttons1)
button_printall = tk.Button(text='Print all', width=15, height=2, bg='gray85', command=printall_button,
                            master=frame_buttons1)
button_leadsbyindustry = tk.Button(text='Leads by industry', width=15, height=2, bg='gray85',
                                   command=start_leadsbyindustry, master=frame_buttons1)
button_pitches = tk.Button(text='Pitches', width=15, height=2, command=start_pitches, bg='gray85',
                        master=frame_buttons1)
button_open = tk.Button(text='Open file', width=15, height=2, bg='alice blue', command=select_file,
                         master=frame_buttons1)
button_empt0 = tk.Button(text='ALL', width=15, height=2, command=exex_all, bg='gray40', fg='white',
                         master=frame_buttons1)
# PACKS
label4.pack(side=tk.LEFT)
label5.pack(side=tk.RIGHT)
label_space_top.pack(pady='10')
label_space3.pack()
#button grid layout
button_open.grid(row=0, column=0, pady='10')
button_safe.grid(row=0, column=1, pady='10')
button_delete.grid(row=0, column=2, pady='10')
button_printall.grid(row=1, column=0)
button_counts.grid(row=1, column=1)
button_leadsbyindustry.grid(row=1, column=2)
button_topleads.grid(row=2, column=0)
button_pitches.grid(row=2, column=1)
button_empt0.grid(row=2, column=2)
label_space2.pack()
textbox.pack()
window.mainloop()
