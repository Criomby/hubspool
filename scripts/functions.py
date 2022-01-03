# Copyright 2022 Braum
# philippebraum@pm.me
# www.philippebraum.de

import pandas as pd
from pandas.api.types import CategoricalDtype
import os
import sys


# data analysis functions
def lead_count(inputfile):
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Company name', 'Lead Status', 'Industry']].groupby(
        'Lead Status').size().to_frame().reset_index()
    csv1 = csv1.rename(columns={'Lead Status': 'Description', 0: 'Count'})
    lead_cat_order = CategoricalDtype(['Cold', 'Cold Contacted', 'Warm', 'Follow-up', 'Qualified Lead',
                                       'Contract', 'Rejected', 'Ineligible'], ordered=True)
    csv1['Description'] = csv1['Description'].astype(lead_cat_order)
    leads_inorder = csv1.sort_values('Description')
    return leads_inorder


def industry_count(inputfile):
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Company name', 'Lead Status', 'Industry']].groupby('Industry').size().to_frame().reset_index()
    csv1 = csv1.rename(columns={'Industry': 'Description', 0: 'Count'})
    cats_disordered = csv1.sort_values(by='Count', ascending=False)
    return cats_disordered


def get_topleads(inputfile):
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Company name', 'Lead Status', 'Industry', 'Company owner']]
    tanalysis_topleads_followup = csv1[csv1['Lead Status'] == 'Follow-up']
    tanalysis_topleads_qualified = tanalysis_topleads_followup.append(csv1[csv1['Lead Status'] == 'Qualified Lead'])
    tanalysis_topleads = tanalysis_topleads_qualified.append(csv1[csv1['Lead Status'] == 'Contract'])
    return tanalysis_topleads


def printall_org_table(inputfile):
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Company name', 'Lead Status', 'Industry', 'Create Date']]
    return csv1


def leadsbyindustry(inputfile):
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Lead Status', 'Industry']]
    total = pd.DataFrame([['', '']], columns=pd.Index(['Lead Status', 0], dtype='object'))
    empt = pd.DataFrame([['', '']], columns=pd.Index(['Lead Status', 0], dtype='object'))
    industries = csv1['Industry'].unique().tolist()
    for i in industries:
        x = csv1[csv1['Industry'] == i].groupby(
            'Lead Status').size().to_frame().reset_index().sort_values(by=[0], ascending=False)
        dfx = pd.DataFrame([[i, '']], columns=x.columns)
        total = total.append(dfx).append(x).append(empt)
    total.rename(columns={'Lead Status': 'Description', 0: 'Count'}, inplace=True)
    return total


def pitches(inputfile):
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Company name', 'Pitch']]
    filtered_csv1 = csv1[csv1['Pitch'].notnull()]
    result = filtered_csv1.sort_values(by='Pitch')
    return result


def reasons(inputfile):
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Company name', 'Industry', 'Lead Status', 'Reason for rejection / unsuitability']]
    filtered_csv1 = csv1[csv1['Reason for rejection / unsuitability'].notnull()]
    result = filtered_csv1.sort_values(by='Lead Status')
    return result


# function to get the .ico file found in the pyinstaller --onefile exe,
# which sets the path not as 'env' anymore, but as sys._MEIPASS
# this code snippet was copied from:
# https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
