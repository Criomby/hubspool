# Copyright 2021 Criomby
# criomby@pm.me

import datetime
import tkinter as tk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from functions import *
import xlsxwriter
import os
import sys


class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.table_savestate1 = pd.DataFrame()
        self.company_data_filepath = 'none'

        # GUI
        self.title('Hubspool')
        self.iconbitmap(resource_path('icon_in.ico'))
        self.geometry('660x700')
        self.resizable(False, True)
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
        # logo image
        self.logo = 'logo_gui.jpg'
        self.logo_open = Image.open(self.logo)
        self.img_logo = ImageTk.PhotoImage(self.logo_open)
        self.label_logo = tk.Label(image=self.img_logo, master=frame_a)
        # define labels
        label_space2 = tk.Label(text='', width=30, height=1, master=frame_c)
        label_space3 = tk.Label(text='', width=30, height=0, master=frame_a)
        label4 = tk.Label(
            text='Copyright 2021 Braum                                                                             ',
            width=50, height=1, master=frame_0)
        label5 = tk.Label(
            text='                                                                            Version: 2.5.2',
            width=50, height=1, master=frame_0)
        # define textbox
        self.textbox = tk.Text(width=100, height=200, master=frame_d)
        # define buttons
        button_open = tk.Button(text='Open file', width=15, height=2, bg='LightSkyBlue1', master=frame_buttons1,
                                command=self.select_file, relief='flat')
        button_safe = tk.Button(text='Safe to Excel', width=15, height=2, bg='DarkSeaGreen1', command=self.save_file,
                                master=frame_buttons1,
                                relief='flat')
        button_delete = tk.Button(text='Delete', width=15, height=2, bg='RosyBrown1', command=self.delete_text,
                                  master=frame_buttons1, relief='flat')
        button_all = tk.Button(text='ALL', width=15, height=2, command=self.exec_all, bg='gray39', fg='white',
                               master=frame_buttons1, relief='flat')
        button_printall = tk.Button(text='Print all', width=15, height=2, bg='gray75', command=self.printall_button,
                                    master=frame_buttons1, relief='flat')
        button_counts = tk.Button(text='Counts', width=15, height=2, bg='gray79', command=self.start_counts,
                                  master=frame_buttons1,
                                  relief='flat')
        button_leadsbyindustry = tk.Button(text='Leads by industry', width=15, height=2, bg='gray80',
                                           command=self.start_leadsbyindustry, master=frame_buttons1, relief='flat')
        button_topleads = tk.Button(text='Topleads', width=15, height=2, bg='gray85', command=self.start_topleads,
                                    master=frame_buttons1, relief='flat')
        button_pitches = tk.Button(text='Pitches', width=15, height=2, command=self.start_pitches, bg='gray89',
                                   master=frame_buttons1, relief='flat')
        # PACKS
        label4.pack(side=tk.LEFT)
        label5.pack(side=tk.RIGHT)
        self.label_logo.pack()
        label_space3.pack()
        # button grid layout
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
        self.textbox.pack()

    # button functions
    def delete_text(self):
        self.textbox.delete('1.0', tk.END)
        self.table_savestate1 = pd.DataFrame()

    def start_counts(self):
        x = self.company_data_filepath
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(x):
            leads_inorder = lead_count(x)
            cats_disordered = industry_count(x)
            df0 = pd.DataFrame([['', '']], columns=leads_inorder.columns)
            df1 = pd.DataFrame([['Lead', '']], columns=df0.columns)
            df2 = pd.DataFrame([['Industry', '']], columns=df0.columns)
            total = df1.append(leads_inorder).append(df0).append(df2).append(cats_disordered)
            self.table_savestate1 = total
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Lead categories:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', leads_inorder)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Industries sorted by size:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', cats_disordered)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')

    def start_topleads(self):
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(self.company_data_filepath):
            result = get_topleads(self.company_data_filepath)
            self.table_savestate1 = result
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', result)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')

    def printall_button(self):
        x = self.company_data_filepath
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(x):
            dataset = printall_org_table(x)
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', dataset)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')

    def start_leadsbyindustry(self):
        x = self.company_data_filepath
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(x):
            result = leadsbyindustry(x)
            self.table_savestate1 = result
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', result)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')

    def start_pitches(self):
        x = self.company_data_filepath
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(x):
            result = pitches(x)
            self.table_savestate1 = result
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', result)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')

    def select_file(self):
        filetypes = (
            ('CSV files', '*.csv'),
        )
        username = os.getlogin()
        if os.path.isdir('C:/Users/' + username + '/Downloads'):
            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='C:/Users/' + username + '/Downloads',
                filetypes=filetypes)
        else:
            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)
        self.company_data_filepath = filename
        self.textbox.delete('1.0', tk.END)
        if filename == '':
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'No file selected.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Opened file:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', filename)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')

    def save_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )
        self.textbox.delete('1.0', tk.END)
        if self.table_savestate1.empty:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: Execute a function first to save it.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        else:
            filename = fd.asksaveasfilename(
                title='Save a file',
                initialdir='/',
                filetypes=filetypes)
            if filename == '':
                self.textbox.insert('1.0',
                                    '--------------------------------------------------------------------------------')
                self.textbox.insert('end', '\n')
                self.textbox.insert('end', 'No file saved.')
                self.textbox.insert('end', '\n')
                self.textbox.insert('end',
                                    '--------------------------------------------------------------------------------')
            else:
                self.table_savestate1.to_excel(filename + '.xlsx')
                self.textbox.insert('1.0',
                                    '--------------------------------------------------------------------------------')
                self.textbox.insert('end', '\n')
                self.textbox.insert('end', 'Saved file: ' + filename + '.xlsx')
                self.textbox.insert('end', '\n')
                self.textbox.insert('end',
                                    '--------------------------------------------------------------------------------')

    def exec_all(self):
        x = self.company_data_filepath
        date = datetime.date.today()
        new_filepath = x[:-48] + f'Hubspool_{date}.xlsx'
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(new_filepath):
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: File already exists. ')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Open another file for analysis or delete existing file.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Existing file:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', new_filepath)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
        elif os.path.isfile(x):
            # counts
            leads_inorder = lead_count(x)
            cats_disordered = industry_count(x)
            leads_inorder.reset_index(drop=True, inplace=True)
            cats_disordered.reset_index(drop=True, inplace=True)
            table_savestate2 = leads_inorder
            table_savestate3 = cats_disordered
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Lead count oho.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Industry count aha.')
            self.textbox.insert('end', '\n')
            # leads by industry
            df_leadsbyindustry = leadsbyindustry(x)
            df_leadsbyindustry.reset_index(drop=True, inplace=True)
            table_savestate4 = df_leadsbyindustry
            self.textbox.insert('end', 'Leads_by_industry done.')
            self.textbox.insert('end', '\n')
            # pitches
            df_pitches = pitches(x)
            df_pitches.reset_index(drop=True, inplace=True)
            table_savestate5 = df_pitches
            self.textbox.insert('end', 'Pitches pitched.')
            self.textbox.insert('end', '\n')
            # reasons for rejection / unsuitability
            df_reasons = reasons(x)
            df_reasons.reset_index(drop=True, inplace=True)
            table_savestate6 = df_reasons
            self.textbox.insert('end', 'Rejection reasons read.')
            self.textbox.insert('end', '\n')
            # topleads
            df_topleads = get_topleads(x)
            df_topleads.reset_index(drop=True, inplace=True)
            table_savestate7 = df_topleads
            self.textbox.insert('end', 'Topleads topped.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            with pd.ExcelWriter(new_filepath) as writer:
                # create Excel file
                table_savestate2.to_excel(writer, sheet_name='Leads', index=False)
                table_savestate3.to_excel(writer, sheet_name='Industries', index=False)
                table_savestate4.to_excel(writer, sheet_name='Leads_by_industries', index=False)
                table_savestate5.to_excel(writer, sheet_name='Pitches', index=False)
                table_savestate6.to_excel(writer, sheet_name='Rejection reasons', index=False)
                table_savestate7.to_excel(writer, sheet_name='Topleads', index=False)
                # create charts
                # counts leads uncategorized
                workbook = writer.book
                worksheet_leads = writer.sheets['Leads']
                chart_leads = workbook.add_chart({'type': 'bar'})
                chart_leads.add_series({
                    'categories': '=Leads!$A$2:$A$9',
                    'values': '=Leads!$B$2:$B$9',
                    'data_labels': {'value': True},
                    'points': [
                        {'fill': {'color': '#9da7b2'}},
                        {'fill': {'color': '#5c7f90'}},
                        {'fill': {'color': '#005778'}},
                        {'fill': {'color': '#f2a007'}},
                        {'fill': {'color': '#5b7b63'}},
                        {'fill': {'color': '#8c0410'}},
                        {'fill': {'color': '#a55b75'}},
                    ]
                })
                chart_leads.set_x_axis({'name': 'Number of companies'})
                chart_leads.set_y_axis({'name': 'Status', 'reverse': True})
                chart_leads.set_legend({'none': True})
                chart_leads.set_title({'name': 'All lead categories'})
                worksheet_leads.insert_chart('E2', chart_leads)
                # counts industries uncategorized
                worksheet_industries = writer.sheets['Industries']
                chart_industries = workbook.add_chart({'type': 'pie'})
                chart_industries.add_series({
                    'categories': '=Industries!$A$2:$A$16',
                    'values': '=Industries!$B$2:$B$16',
                    'data_labels': {'value': True}
                })
                chart_industries.set_title({'name': 'All industries'})
                worksheet_industries.insert_chart('E2', chart_industries)
                # set column width for Excel sheets
                worksheet_leads.set_column(0, 0, 15)
                worksheet_industries.set_column(0, 0, 22)
                worksheet_leadsbyindustries = writer.sheets['Leads_by_industries']
                worksheet_leadsbyindustries.set_column(0, 0, 19)
                worksheet_pitches = writer.sheets['Pitches']
                worksheet_pitches.set_column(0, 0, 21)
                worksheet_pitches.set_column(1, 1, 39)
                worksheet_reasons = writer.sheets['Rejection reasons']
                worksheet_reasons.set_column(0, 0, 37)
                worksheet_reasons.set_column(1, 1, 18)
                worksheet_reasons.set_column(2, 2, 12)
                worksheet_reasons.set_column(3, 3, 70)
                worksheet_topleads = writer.sheets['Topleads']
                worksheet_topleads.set_column(0, 0, 34)
                worksheet_topleads.set_column(1, 1, 14)
                worksheet_topleads.set_column(2, 2, 18)
                worksheet_topleads.set_column(3, 3, 20)
            self.textbox.insert('end', 'Charts generated.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            #self.textbox.insert('end', '\n')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Excel file saved to:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', new_filepath)
            #self.textbox.insert('end', '\n')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: Open a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')


if __name__ == '__main__':
    app = App()
    app.mainloop()
