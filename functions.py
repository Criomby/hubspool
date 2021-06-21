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
#print(lead_count('C:/Users/phili/Downloads/hubspot-crm-exports-all-companies-2021-06-18.csv'))

def industry_count(inputfile): #sort according to size
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Name', 'Lead Status', 'Industry']].groupby('Industry').size()
    return csv1.to_frame()
#print(industry_count('C:/Users/phili/Downloads/hubspot-crm-exports-all-companies-2021-06-18.csv'))

def get_topleads(inputfile):
    global table_savestate1
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Name', 'Lead Status', 'Industry', 'Company owner']]
    tanalysis_topleads_followup = csv1[csv1['Lead Status'] == 'Follow-up']
    tanalysis_topleads_qualified = tanalysis_topleads_followup.append(csv1[csv1['Lead Status'] == 'Qualified Lead'])
    tanalysis_topleads = tanalysis_topleads_qualified.append(csv1[csv1['Lead Status'] == 'Contract'])
    table_savestate1 = tanalysis_topleads
    return tanalysis_topleads
#print(get_topleads('C:/Users/phili/Downloads/hubspot-crm-exports-all-companies-2021-06-18.csv'))

def printall_org_table(inputfile):
    global table_savestate1
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Name', 'Lead Status', 'Industry', 'Create Date']] # sort date descending? -> usually not necessary bc. already done by HubSpot on export
    table_savestate1 = csv1
    return csv1
#print(printall_org_table('C:/Users/phili/Downloads/hubspot-crm-exports-all-companies-2021-06-18.csv'))

# // not yet translated into pandas //
"""
def leadsbyindustry(inputfile): #create 'for' loop to avoid redundancy
    global table_savestate1
    hubspot_org = pd.read_csv(inputfile)
    csv1 = hubspot_org[['Lead Status', 'Industry']]
    basetable = pd.DataFrame(data = {'Lead Status': [''], 'count': ['']})
    insurance = csv1[csv1['Industry'] == 'Insurance'].groupby('Lead Status').size()
    finance = csv1[csv1['Industry'] == 'Financial Services'].groupby('Lead Status').size()
    mobility = csv1[csv1['Industry'] == 'Mobility'].groupby('Lead Status').size()
    health = csv1[csv1['Industry'] == 'Health'].groupby('Lead Status').size()
    telecomm = csv1[csv1['Industry'] == 'Telecommunications'].groupby('Lead Status').size()
    ecommerce = csv1[csv1['Industry'] == 'eCommerce'].groupby('Lead Status').size()
    broker = csv1[csv1['Industry'] == 'Online Broker'].groupby('Lead Status').size()
    edu = csv1[csv1['Industry'] == 'Education'].groupby('Lead Status').size()
    banking = csv1[csv1['Industry'] == 'Banking'].groupby('Lead Status').size()
    government = csv1[csv1['Industry'] == 'Government'].groupby('Lead Status').size()
    nan = csv1[csv1['Industry'] == 'nan'].groupby('Lead Status').size()
    #total = basetable.append(insurance)
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
    return insurance #total"""
#print(leadsbyindustry('C:/Users/phili/Downloads/hubspot-crm-exports-all-companies-2021-06-18.csv'))
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