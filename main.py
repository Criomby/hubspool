import tkinter as tk
from tkinter import filedialog as fd
import os.path
from functions import *

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
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Lead categories sorted by size:')
        textbox.insert('end', '\n')
        textbox.insert('end', leads_disordered)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Industries sorted by size:')
        textbox.insert('end', '\n')
        textbox.insert('end', cats_disordered)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', total)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: No file opened. Select a file first.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')

def start_topleads():
    global table_savestate1
    global company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(company_data_filepath):
        result = get_topleads(company_data_filepath)
        table_savestate1 = result
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', result)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: No file opened. Select a file first.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')

def printall_button():
    global company_data_filepath
    x = company_data_filepath
    #x = entry_filepath_open.get()
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        result = printall_org_table(x)
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', result)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: No file opened. Select a file first.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')

def start_leadsbyindustry():
    global table_savestate1
    global company_data_filepath
    x = company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        result = leadsbyindustry(x)
        table_savestate1 = result
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', result)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: No file opened. Select a file first.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')

def start_pitches():
    global table_savestate1
    global company_data_filepath
    x = company_data_filepath
    textbox.delete('1.0', tk.END)
    if os.path.isfile(x):
        result = pitches(x)
        table_savestate1 = result
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', result)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: No file opened. Select a file first.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')

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
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'No file selected.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Opened file:')
        textbox.insert('end', '\n')
        textbox.insert('end', filename)
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')

def save_file():
    global table_savestate1
    filetypes = (
        ('Excel files', '*.xlsx'),
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    textbox.delete('1.0', tk.END)
    if table_savestate1.empty == True:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: Execute a function first to save it.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        filename = fd.asksaveasfilename(
            title='Save a file',
            initialdir='/',
            filetypes=filetypes)
        if filename == '':
            textbox.insert('1.0', '--------------------------------------------------------------------------------')
            textbox.insert('end', '\n')
            textbox.insert('end', 'No file saved.')
            textbox.insert('end', '\n')
            textbox.insert('end', '--------------------------------------------------------------------------------')
            textbox.insert('end', '\n')
        else:
            table_savestate1.to_excel(filename + '.xlsx')
            textbox.insert('1.0', '--------------------------------------------------------------------------------')
            textbox.insert('end', '\n')
            textbox.insert('end', 'Saved file: ' + filename)
            textbox.insert('end', '\n')
            textbox.insert('end', '--------------------------------------------------------------------------------')
            textbox.insert('end', '\n')

def exex_all():
    global company_data_filepath
    x = company_data_filepath
    new_filepath = x[:-4] + '_Hubspool.xlsx'
    textbox.delete('1.0', tk.END)
    if os.path.isfile(new_filepath) == True:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: File already exists. ')
        textbox.insert('end', '\n')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Open another file for analysis or delete existing file.')
        textbox.insert('end', '\n')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Existing file:')
        textbox.insert('end', '\n')
        textbox.insert('end', new_filepath)
        textbox.insert('end', '\n')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    elif os.path.isfile(x) == True:
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
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Counts (ordered) done.')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Counts (raw / size sorted) done.')
        textbox.insert('end', '\n')
        # leads by industry
        table_savestate4 = leadsbyindustry(x)
        textbox.insert('end', 'Leads by industry done.')
        textbox.insert('end', '\n')
        # pitches
        table_savestate5 = pitches(x)
        textbox.insert('end', 'Pitches done.')
        textbox.insert('end', '\n')
        # topleads
        table_savestate6 = get_topleads(x)
        textbox.insert('end', 'Topleads done.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        with pd.ExcelWriter(new_filepath) as writer:
            table_savestate1.to_excel(writer, sheet_name='Counts+Industries')
            table_savestate2.to_excel(writer, sheet_name='Counts_raw')
            table_savestate3.to_excel(writer, sheet_name='Industries_raw')
            table_savestate4.to_excel(writer, sheet_name='Leads_by_industries')
            table_savestate5.to_excel(writer, sheet_name='Pitches')
            table_savestate6.to_excel(writer, sheet_name='Topleads')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Excel file generated and saved to:')
        textbox.insert('end', '\n')
        textbox.insert('end', new_filepath[:-5])
        textbox.insert('end', '\n')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
    else:
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')
        textbox.insert('end', 'Error: Open a file first.')
        textbox.insert('end', '\n')
        textbox.insert('end', '--------------------------------------------------------------------------------')
        textbox.insert('end', '\n')

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
label5 = tk.Label(text='                                                                            Version: 2.4.1',
                  width=50, height=1, master=frame_0)
# define textbox
textbox = tk.Text(width=100, height=200, master=frame_d)
# define buttons
button_open = tk.Button(text='Open file', width=15, height=2, bg='LightSkyBlue1', command=select_file,
                         master=frame_buttons1, relief='flat') #groove
button_safe = tk.Button(text='Safe to Excel', width=15, height=2, bg='DarkSeaGreen1', command=save_file, master=frame_buttons1,
                        relief='flat')
button_delete = tk.Button(text='Delete', width=15, height=2, bg='RosyBrown1', command=delete_text,
                          master=frame_buttons1, relief='flat')
button_all = tk.Button(text='ALL', width=15, height=2, command=exex_all, bg='gray39', fg='white',
                         master=frame_buttons1, relief='flat')
button_printall = tk.Button(text='Print all', width=15, height=2, bg='gray70', command=printall_button,
                            master=frame_buttons1, relief='flat')
button_counts = tk.Button(text='Counts', width=15, height=2, bg='gray75', command=start_counts, master=frame_buttons1,
                          relief='flat')
button_leadsbyindustry = tk.Button(text='Leads by industry', width=15, height=2, bg='gray80',
                                   command=start_leadsbyindustry, master=frame_buttons1, relief='flat')
button_topleads = tk.Button(text='Topleads', width=15, height=2, bg='gray85', command=start_topleads,
                            master=frame_buttons1, relief='flat')
button_pitches = tk.Button(text='Pitches', width=15, height=2, command=start_pitches, bg='gray89',
                        master=frame_buttons1, relief='flat')

# PACKS
label4.pack(side=tk.LEFT)
label5.pack(side=tk.RIGHT)
label_space_top.pack(pady='10')
label_space3.pack()
#button grid layout
button_open.grid(row=0, column=0, pady='10')
button_safe.grid(row=0, column=1, pady='10')
button_delete.grid(row=0, column=2, pady='10')
button_all.grid(row=1, column=0)
button_printall.grid(row=1, column=1)
button_counts.grid(row=1, column=2)
button_leadsbyindustry.grid(row=2, column=0)
button_topleads.grid(row=2, column=1)
button_pitches.grid(row=2, column=2)

label_space2.pack()
textbox.pack()
window.mainloop()
