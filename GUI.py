import tkinter as tk

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
