import os.path
from datascience import *
import tkinter as tk

# global variables for data storage across functions
table_savestate1 = 0

# data analysis functions
def lead_count(inputfile):  # sample filepath: 'C:/Users/phili/Downloads/hubspot_qundo_20210526.csv'
    hubspot_org = Table.read_table(inputfile)  # , file read before via text imput
    # hubspot_org = inputfile
    # get table with rows 'Name', 'Lead Status', 'industry' out of Hubspot .csv file
    csv1 = hubspot_org.select('Name', 'Lead Status', 'Industry').group('Lead Status').sort(1, descending=True)
    return csv1

def industry_count(inputfile):
    hubspot_org = Table.read_table(inputfile)
    # hubspot_org = inputfile
    # get table with rows 'Name', 'Lead Status', 'industry' out of Hubspot .csv file
    csv1 = hubspot_org.select('Name', 'Lead Status', 'Industry').group('Industry').sort(1, descending=True)
    return csv1

def get_topleads(inputfile):
    global table_savestate1
    hubspot_org = Table.read_table(inputfile)
    # get table with rows 'Name', 'Lead Status', 'industry' out of Hubspot .csv file
    csv1 = hubspot_org.select('Name', 'Lead Status', 'Industry', 'Company owner')
    # create new table with industry counts
    tanalysis_topleads_followup = csv1.where('Lead Status', 'Follow-up')
    tanalysis_topleads_qualified = tanalysis_topleads_followup.append(csv1.where('Lead Status', 'Qualified Lead'))
    tanalysis_topleads_contract = tanalysis_topleads_qualified.append(csv1.where('Lead Status', 'Contract'))
    tanalysis_topleads = tanalysis_topleads_contract
    table_savestate1 = tanalysis_topleads
    return tanalysis_topleads

def printall_org_table(inputfile):
    global table_savestate1
    hubspot_org = Table.read_table(inputfile)
    csv1 = hubspot_org.select('Name', 'Lead Status', 'Industry', 'Create Date').sort(3, descending=True)
    table_savestate1 = csv1
    return csv1

def leadsbyindustry(
        inputfile):  # integrate 'for' function to define industries in beginning and let it run through for each industry to reduce redundancy
    global table_savestate1
    hubspot_org = Table.read_table(inputfile)
    csv1 = hubspot_org.select('Name', 'Lead Status', 'Industry')
    basetable = Table(make_array('Lead Status', 'count'))
    insurance = csv1.where('Industry', 'Insurance').group(1)
    finance = csv1.where('Industry', 'Financial Services').group(1)
    mobility = csv1.where('Industry', 'Mobility').group(1)
    health = csv1.where('Industry', 'Health').group(1)
    telecomm = csv1.where('Industry', 'Telecommunications').group(1)
    ecommerce = csv1.where('Industry', 'eCommerce').group(1)
    broker = csv1.where('Industry', 'Online Broker').group(1)
    edu = csv1.where('Industry', 'Education').group(1)
    banking = csv1.where('Industry', 'Banking').group(1)
    government = csv1.where('Industry', 'Government Relations').group(1)
    nan = csv1.where('Industry', 'nan').group(1)
    total = basetable.with_row(make_array('', '')).with_row(make_array('Insurance', '')).append(insurance).with_row(
        make_array('', '')).with_row(make_array('Financial Services', '')).append(finance).with_row(
        make_array('', '')).with_row(make_array('Mobilty', '')).append(mobility).with_row(make_array('', '')).with_row(
        make_array('Health', '')).append(health).with_row(make_array('', '')).with_row(
        make_array('Telecommunications', '')).append(telecomm).with_row(make_array('', '')).with_row(
        make_array('eCommerce', '')).append(ecommerce).with_row(make_array('', '')).with_row(
        make_array('Broker', '')).append(broker).with_row(make_array('', '')).with_row(
        make_array('Education', '')).append(edu).with_row(make_array('', '')).with_row(
        make_array('Banking', '')).append(banking).with_row(make_array('', '')).with_row(
        make_array('Other', '')).append(nan)
    table_savestate1 = total
    return total

def join_contacts():
    global table_savestate1
    x = entry_filepath_open.get()
    y = entry_filepath_open_cont.get()
    # join contact persons with company
    hubspot_comp = Table.read_table(x)
    hubspot_pers = Table.read_table(y)
    # joint = hubspot_pers.join(hubspot_comp, 'Company ID')
    total = hubspot_comp.join('Company ID', hubspot_pers, 'Associated Company ID').select('Name', 'First Name',
                                                                                          'Last Name', 'Job Title',
                                                                                          'Lead Status', 'Industry',
                                                                                          'Number of times contacted')
    table_savestate1 = total
    return total

# button functions
def delete_text():
    textbox.delete('1.0', tk.END)

def start_counts():  # write (copy&paste) second function for counts_industries and add another button for it
    global table_savestate1
    # global table_savestate2
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result_lead = lead_count(x).relabel(0, 'Description')
        result_industries = industry_count(x).relabel(0, 'Description')
        total = result_lead.with_row(make_array('', '')).append(result_industries)
        table_savestate1 = total
        textbox.insert('1.0', total)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        """#old version history
        #textbox.insert('1.0', 'Lead Funnel:')
        textbox.insert('1.0', result_lead)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        #textbox.insert('1.0', 'Industry Count:')
        textbox.insert('1.0', result_industries)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        """
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def start_topleads():
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result = get_topleads(x)
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
        result = printall_org_table(x).select('Name', 'Industry', 'Create Date').sort(2, descending=True)
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

def save():
    global table_savestate1
    s = entry_filepath_save.get()
    if table_savestate1 == 0:
        textbox.insert('1.0', 'Print something first. The button saves the last table you have printed.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:  # define printout if save file already exists and save path has to be renamed first (as in f{check file})
        table_savestate1.to_csv(s)
        textbox.insert('1.0', 'File created!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
        table_savestate1 = 0

def start_leadsbyindustry():
    x = entry_filepath_open.get()
    if os.path.isfile(x):
        result = leadsbyindustry(x)
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def start_join():
    if os.path.isfile(entry_filepath_open.get()):
        result = join_contacts()
        textbox.insert('1.0', result)
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:
        textbox.insert('1.0', 'File not found. Check file path.')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')

def check_files():
    x = entry_filepath_open.get()
    y = entry_filepath_open_cont.get()
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
    if os.path.isfile(y) == True:
        textbox.insert('1.0', 'Contacts file found!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
    else:  # os.path.isfile(y)==False:
        textbox.insert('1.0', 'Contacts file NOT found!')
        textbox.insert('1.0', '\n')
        textbox.insert('1.0', '--------------------------------------------------------------------------------')
        textbox.insert('1.0', '\n')
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
window.title('Hub Data Tool')
window.geometry('660x700')
window.resizable(False, True)
# window.rowconfigure([0,1])
# window.columnconfigure([0,1])
# DEFINITIONS
# basic layout
frame_0 = tk.Frame()
frame_0.pack(side='top', anchor='nw')
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
label_open_cont = tk.Label(text='Open CONTACTS.csv file from:', width=30, height=1, master=frame_a)
label_save = tk.Label(text='Safe .csv file to:', width=30, height=1, master=frame_a)
#label_space_top = tk.Label(text='', width=30, height=1, master=frame_a)
label_space = tk.Label(text='', width=30, height=2, master=frame_a)
label_space2 = tk.Label(text='', width=30, height=1, master=frame_c)
label_space3 = tk.Label(text='', width=30, height=0, master=frame_a)
label_space4 = tk.Label(text='', width=30, height=0, master=frame_a)
#label3 = tk.Label(text='Output:', width=30, height=2, master=frame_c)
label4 = tk.Label(text='Copyright (c) 2021 Braum                                                                        ',
                  width=50, height=1, master=frame_0)
#label_empt = tk.Label(text='', width=40, height=1, master=frame_0)
# define entries
entry_filepath_open = tk.Entry(width=80, master=frame_a)
entry_filepath_open.insert(0, 'C:/Users/phili/Downloads/hubspot-crm-exports-all-companies-2021-06-17.csv')
entry_filepath_open_cont = tk.Entry(width=80, master=frame_a)
entry_filepath_open_cont.insert(0, 'C:/Users/phili/Downloads/hubspot-crm-exports-all-contacts-2021-06-17.csv')
entry_filepath_save = tk.Entry(width=80, master=frame_a)
entry_filepath_save.insert(0, 'C:/Users/phili/Downloads/hubspot_analysis_OUTPUT_1.csv')
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
button_join = tk.Button(text='Join cont. & comp.', width=15, height=2, command=start_join, bg='gray85',
                        master=frame_buttons1)
button_check = tk.Button(text='Check files', width=15, height=2, bg='alice blue', command=check_files,
                         master=frame_buttons1)

# PACKS
label4.pack()
#label_empt.pack(side=tk.RIGHT)
#label_space_top.pack()
label_open_comp.pack()
entry_filepath_open.pack()
label_space4.pack()
label_open_cont.pack()
entry_filepath_open_cont.pack()
label_space3.pack()
label_save.pack()
entry_filepath_save.pack()
label_space.pack()
button_printall.grid(row=1, column=0)
button_counts.grid(row=0, column=1)
# button_open.grid(row=0, column=1)
button_topleads.grid(row=1, column=1)
button_safe.grid(row=1, column=3)
button_leadsbyindustry.grid(row=0, column=2)
button_join.grid(row=1, column=2)
button_check.grid(row=0, column=0)

button_delete.grid(row=0, column=3)
label_space2.pack()

#label3.pack()
textbox.pack()

window.mainloop()
