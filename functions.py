import os.path
import numpy as np
import pandas as pd

# global variables for data storage across functions
table_savestate1 = 0

# data analysis functions
def lead_count(inputfile): #sort according to size
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Name', 'Lead Status', 'Industry']].groupby('Lead Status').size() #.sort(1, descending=True)
    return csv1.to_frame()

def industry_count(inputfile): #sort according to size
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Name', 'Lead Status', 'Industry']].groupby('Industry').size()
    return csv1.to_frame()

def get_topleads(inputfile):
    global table_savestate1
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Name', 'Lead Status', 'Industry', 'Company owner']]
    tanalysis_topleads_followup = csv1[csv1['Lead Status'] == 'Follow-up']
    tanalysis_topleads_qualified = tanalysis_topleads_followup.append(csv1[csv1['Lead Status'] == 'Qualified Lead'])
    tanalysis_topleads = tanalysis_topleads_qualified.append(csv1[csv1['Lead Status'] == 'Contract'])
    table_savestate1 = tanalysis_topleads
    return tanalysis_topleads

def printall_org_table(inputfile):
    global table_savestate1
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Name', 'Lead Status', 'Industry', 'Create Date']] # sort date descending? -> usually not necessary bc. already done by HubSpot at export
    table_savestate1 = csv1
    return csv1

def leadsbyindustry(inputfile): #create 'for' loop to make function smaller
    global table_savestate1
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Lead Status', 'Industry']]
    """
    # test for function and get it right (decreased code size (speed?))
    CATEGORIES = ['Insurance', 'Financial Services', 'Mobility', 'Health', 'Telecommunications', 'eCommerce',
                  'Online Broker', 'Education',
                  'Banking', 'Government', 'nan']
    VARIABLES = [insurance, finance, mobility, health, telecomm, ecommerce, broker, edu, banking, government, nan]
    for i in VARIABLES:
        i = csv1[csv1['Industry'] == i].groupby('Lead Status').size().to_frame()
        df1 = pd.DataFrame([['i', '']], columns=i.columns)
        total = df1.append(finance).append(df1).append(insurance).append(df1).append(mobility).append(df1).append(
            health).append(df1).append(telecomm).append(df1).append(ecommerce).append(
            df1).append(broker).append(df1).append(edu).append(df1).append(banking).append(df1).append(government).append(
            df1).append(nan)
    """
    insurance = csv1[csv1['Industry'] == 'Insurance'].groupby('Lead Status').size().to_frame().reset_index()
    finance = csv1[csv1['Industry'] == 'Financial Services'].groupby('Lead Status').size().to_frame().reset_index()
    mobility = csv1[csv1['Industry'] == 'Mobility'].groupby('Lead Status').size().to_frame().reset_index()
    health = csv1[csv1['Industry'] == 'Health'].groupby('Lead Status').size().to_frame().reset_index()
    telecomm = csv1[csv1['Industry'] == 'Telecommunications'].groupby('Lead Status').size().to_frame().reset_index()
    ecommerce = csv1[csv1['Industry'] == 'eCommerce'].groupby('Lead Status').size().to_frame().reset_index()
    broker = csv1[csv1['Industry'] == 'Online Broker'].groupby('Lead Status').size().to_frame().reset_index()
    edu = csv1[csv1['Industry'] == 'Education'].groupby('Lead Status').size().to_frame().reset_index()
    #banking = csv1[csv1['Industry'] == 'Banking'].groupby('Lead Status').size().to_frame().reset_index() # depreciated
    government = csv1[csv1['Industry'] == 'Government'].groupby('Lead Status').size().to_frame().reset_index()
    nan = csv1[csv1['Industry'] == 'nan'].groupby('Lead Status').size().to_frame().reset_index()
    df0 = pd.DataFrame([['', '']], columns=insurance.columns)
    df1 = pd.DataFrame([['Insurance', '']], columns=insurance.columns) # add 'for' function for each category in 'Industries' respectively
    df2 = pd.DataFrame([['Financial Services', '']], columns=insurance.columns)
    df3 = pd.DataFrame([['Mobility', '']], columns=insurance.columns)
    df4 = pd.DataFrame([['Health', '']], columns=insurance.columns)
    df5 = pd.DataFrame([['Telecommunications', '']], columns=insurance.columns)
    df6 = pd.DataFrame([['eCommerce', '']], columns=insurance.columns)
    df7 = pd.DataFrame([['Online Broker', '']], columns=insurance.columns)
    df8 = pd.DataFrame([['Education', '']], columns=insurance.columns)
    #df8 = pd.DataFrame([['Banking', '']], columns=insurance.columns) # depreciated
    df9 = pd.DataFrame([['Government', '']], columns=insurance.columns)
    df10 = pd.DataFrame([['NaN', '']], columns=insurance.columns)
    total = df1.append(insurance).append(df0).append(df2).append(finance).append(df0).append(df3).append(mobility).append(
        df0).append(df4).append(health).append(df0).append(df5).append(telecomm).append(df0).append(df6).append(
        ecommerce).append(df0).append(df7).append(broker).append(df0).append(df8).append(edu).append(df0).append(
        df9).append(government).append(df0).append(df10).append(nan).rename(columns={0: 'Count'})
    table_savestate1 = total
    return total

# // not yet translated into pandas //
"""def join_contacts(companies, contacts):
    global table_savestate1
    hubspot_comp = pd.read_csv(companies)
    hubspot_pers = pd.read_csv(contacts)
    # joint = hubspot_pers.join(hubspot_comp, 'Company ID')
    total = hubspot_comp.join('Company ID', hubspot_pers, 'Associated Company ID').select('Name', 'First Name',
                                                                                          'Last Name', 'Job Title',
                                                                                          'Lead Status', 'Industry',
                                                                                          'Number of times contacted')
    table_savestate1 = total
    return total"""
