# Copyright 2021 Criomby
# criomby@pm.me

import tkinter as tk
from tkinter import filedialog as fd
import os
from functions import *
import xlsxwriter

class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()
        # global variables for data storage across functions
        self.table_savestate1 = pd.DataFrame()
        self.company_data_filepath = 'none'

        # GUI
        #self.window = tk.Tk()
        self.title('Hubspool')
        #self.window.iconbitmap(resource_path('icon_in.ico'))
        self.geometry('660x700')
        self.resizable(False, True)
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
        label_space_top.config(font=("Bahnschrift Light", 44))
        label_space2 = tk.Label(text='', width=30, height=1, master=frame_c)
        label_space3 = tk.Label(text='', width=30, height=0, master=frame_a)
        label4 = tk.Label(
            text='Copyright 2021 Criomby                                                                           ',
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
        button_all = tk.Button(text='ALL', width=15, height=2, command=self.exex_all, bg='gray39', fg='white',
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
        label_space_top.pack(pady='10')
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
        # global table_savestate1
        self.textbox.delete('1.0', tk.END)
        self.table_savestate1 = pd.DataFrame()

    def start_counts(self):
        # global table_savestate1
        # global company_data_filepath
        x = self.company_data_filepath
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(x):
            leads_disordered, leads_inorder = lead_count(x)
            cats_disordered, cats_inorder = industry_count(x)
            df0 = pd.DataFrame([['', '']], columns=leads_disordered.columns)
            df1 = pd.DataFrame([['Lead', '']], columns=df0.columns)
            df2 = pd.DataFrame([['Industry', '']], columns=df0.columns)
            total = df1.append(leads_inorder).append(df0).append(df2).append(cats_inorder)
            self.table_savestate1 = total
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'All lead categories sorted by size:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', leads_disordered)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'All industries sorted by size:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', cats_disordered)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', total)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')

    def start_topleads(self):
        # global table_savestate1
        # global company_data_filepath
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
            self.textbox.insert('end', '\n')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')

    def printall_button(self):
        # global company_data_filepath
        x = self.company_data_filepath
        # x = entry_filepath_open.get()
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(x):
            result = printall_org_table(x)
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', result)
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
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
        # global table_savestate1
        # global company_data_filepath
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
            self.textbox.insert('end', '\n')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')

    def start_pitches(self):
        # global table_savestate1
        # global company_data_filepath
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
            self.textbox.insert('end', '\n')
        else:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: No file opened. Select a file first.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')

    def select_file(self):
        # global company_data_filepath
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
            self.textbox.insert('end', '\n')
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
            self.textbox.insert('end', '\n')

    def save_file(self):
        # global table_savestate1
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )
        self.textbox.delete('1.0', tk.END)
        if self.table_savestate1.empty == True:
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Error: Execute a function first to save it.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
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
                self.textbox.insert('end', '\n')
            else:
                self.table_savestate1.to_excel(filename + '.xlsx')
                self.textbox.insert('1.0',
                                    '--------------------------------------------------------------------------------')
                self.textbox.insert('end', '\n')
                self.textbox.insert('end', 'Saved file: ' + filename)
                self.textbox.insert('end', '\n')
                self.textbox.insert('end',
                                    '--------------------------------------------------------------------------------')
                self.textbox.insert('end', '\n')

    def exex_all(self):
        # global company_data_filepath
        x = self.company_data_filepath
        new_filepath = x[:-4] + '_Hubspool.xlsx'
        self.textbox.delete('1.0', tk.END)
        if os.path.isfile(new_filepath) == True:
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
            self.textbox.insert('end', '\n')
        elif os.path.isfile(x) == True:
            # counts
            leads_disordered, leads_inorder = lead_count(x)
            cats_disordered, cats_inorder = industry_count(x)
            df0 = pd.DataFrame([['', '']], columns=leads_disordered.columns)
            df1 = pd.DataFrame([['Lead', '']], columns=df0.columns)
            df2 = pd.DataFrame([['Industry', '']], columns=df0.columns)
            total = df1.append(leads_inorder).append(df0).append(df2).append(cats_inorder)
            total.reset_index(drop=True, inplace=True)
            leads_disordered.reset_index(drop=True, inplace=True)
            cats_disordered.reset_index(drop=True, inplace=True)
            table_savestate1 = total
            table_savestate2 = leads_disordered
            table_savestate3 = cats_disordered
            self.textbox.insert('1.0',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Counts (ordered) done.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Counts (raw / size sorted) done.')
            self.textbox.insert('end', '\n')
            # leads by industry
            df_leadsbyindustry = leadsbyindustry(x)
            df_leadsbyindustry.reset_index(drop=True, inplace=True)
            table_savestate4 = df_leadsbyindustry
            self.textbox.insert('end', 'Leads by industry done.')
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
            self.textbox.insert('end', 'Topleads done.')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end',
                                '--------------------------------------------------------------------------------')
            self.textbox.insert('end', '\n')
            with pd.ExcelWriter(new_filepath) as writer:
                # create Excel
                table_savestate1.to_excel(writer, sheet_name='Categories', index=False)
                table_savestate2.to_excel(writer, sheet_name='Leads_raw', index=False)
                table_savestate3.to_excel(writer, sheet_name='Industries_raw', index=False)
                table_savestate4.to_excel(writer, sheet_name='Leads_by_industries', index=False)
                table_savestate5.to_excel(writer, sheet_name='Pitches', index=False)
                table_savestate6.to_excel(writer, sheet_name='Rejection reasons', index=False)
                table_savestate7.to_excel(writer, sheet_name='Topleads', index=False)
                # create charts
                # counts leads uncategorized
                workbook = writer.book
                worksheet_leads_raw = writer.sheets['Leads_raw']
                chart_leads_raw = workbook.add_chart({'type': 'bar'})
                chart_leads_raw.add_series({
                    'categories': '=Leads_raw!$A$2:$A$9',
                    'values': '=Leads_raw!$B$2:$B$9',
                    'data_labels': {'value': True},
                    'points': [
                        {'fill': {'color': '#9da7b2'}},
                        {'fill': {'color': '#5c7f90'}},
                        {'fill': {'color': '#005778'}},
                        {'fill': {'color': '#f2a007'}},
                        {'fill': {'color': '#5b7b63'}},
                        {'fill': {'color': '#8c0410'}},
                        {'fill': {'color': '#a55b75'}}
                    ]
                })
                chart_leads_raw.set_x_axis({'name': 'Number of companies'})
                chart_leads_raw.set_y_axis({'name': 'Status', 'reverse': True})
                chart_leads_raw.set_legend({'none': True})
                chart_leads_raw.set_title({'name': 'All lead categories'})
                worksheet_leads_raw.insert_chart('E1', chart_leads_raw)
                # counts industries uncategorized
                worksheet_industries_raw = writer.sheets['Industries_raw']
                chart_industries_raw = workbook.add_chart({'type': 'pie'})
                chart_industries_raw.add_series({
                    'categories': '=Industries_raw!$A$2:$A$13',
                    'values': '=Industries_raw!$B$2:$B$13',
                    'data_labels': {'value': True}
                })
                chart_industries_raw.set_title({'name': 'All industries'})
                worksheet_industries_raw.insert_chart('E1', chart_industries_raw)
                # counts inorder charts
                worksheet_counts = writer.sheets['Categories']
                chart_leads_inorder = workbook.add_chart({'type': 'bar'})
                chart_leads_inorder.add_series({
                    'categories': '=Categories!$A$3:$A$10',
                    'values': '=Categories!$B$3:$B$10',
                    'data_labels': {'value': True},
                    'points': [
                        {'fill': {'color': '#9da7b2'}},
                        {'fill': {'color': '#5c7f90'}},
                        {'fill': {'color': '#005778'}},
                        {'fill': {'color': '#f2a007'}},
                        {'fill': {'color': '#5b7b63'}},
                        {'fill': {'color': '#8c0410'}},
                        {'fill': {'color': '#a55b75'}}
                    ]
                })
                chart_leads_inorder.set_x_axis({'name': 'Number of companies'})
                chart_leads_inorder.set_y_axis({'name': 'Status', 'reverse': True})
                chart_leads_inorder.set_legend({'none': True})
                chart_leads_inorder.set_title({'name': 'Lead categories'})
                worksheet_counts.insert_chart('E1', chart_leads_inorder)
                chart_industries_inorder = workbook.add_chart({'type': 'pie'})
                chart_industries_inorder.add_series({
                    'categories': '=Categories!$A$13:$A$21',
                    'values': '=Categories!$B$13:$B$21',
                    'data_labels': {'value': True}
                })
                chart_industries_inorder.set_title({'name': 'Industries'})
                worksheet_counts.insert_chart('E17', chart_industries_inorder)
                # set column width for Excel sheets
                worksheet_counts.set_column(0, 0, 19)
                worksheet_leads_raw.set_column(0, 0, 15)
                worksheet_industries_raw.set_column(0, 0, 22)
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
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', 'Excel file saved to:')
            self.textbox.insert('end', '\n')
            self.textbox.insert('end', new_filepath[:-5])
            self.textbox.insert('end', '\n')
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
    