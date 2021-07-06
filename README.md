# Hubspool
#### A data analysis program for .csv database files exported from HubSpot CRM, calculating and exporting several quantitative and qualitative metrics, operated via a simple GUI. 

## Download Info: <br>
<h3> Ready-to-use version (Windows only):</h3><br>
The latest release can be found on the right, under 'Releases'. <br>
Download the .exe and execute it as an administrator.<br>
<br>
Your antivirus might flag the program when trying to open it for the first time.
<h3>Be reassured: It's open source and safe for you and your data!</h3><br>

## Documentation: <br>
<img src="https://user-images.githubusercontent.com/86114549/124588954-b54b5200-de59-11eb-9aed-63bdae6f2f3e.png" alt="Hubspool_v2.2.0_screenshot_printall" height="650">
<br>
<strong>1.</strong> Press 'Open' and select the .csv data file you want to analyse. <br>
<strong>2.</strong> Press the desired function (grey buttons).<br>
<strong>3.</strong> Save the result via 'Save'. <br>
<strong>4.</strong> Repeat fore required functions. <br>
<br>
<strong>Alternatively:</strong> Press 'ALL' to execute all analyses at once.<br>
<br>
<strong>If you want to have all analyses at once and within one file, press 'ALL'.</strong><br>
All metrics will be taken and exported into one Excel file within different sheets, each named accordingly.<br>
The exported file will be automatically saved at the filepath where the original file is saved, with '_Hubspool' added to the filename.<br>
<br>
<h3>Functions overview:</h3>
Each function prints out a table of the specified information below, which is displayed in the output text field and can be exported as an Excel file / sheet.<br>
<br>
<ul>
<li><strong>Open file:</strong><br>
Open a .csv file exported from HubSpot.<br>
The imported file has to be in the .csv format.</li>
<li><strong>Save to Excel:</strong><br>
Saves the last printed function which is seen in the text box as Excel (.xlsx) file.<br></li>
<li><strong>Delete:</strong><br>
Deletes all output within the text box.<br></li>
<br>
<li><strong>ALL:</strong><br>
Executes every analysis and saves them into one Excel file in a separate worksheet, each respectively.<br>
The new file is saved in the same path as the original file with '_Hubspool' at the end.<br> 
<br>
<li><strong>Print all:</strong><br>
Prints out the first 5 top and bottom rows, to see if the file is correct.<br</li>
<li><strong>Counts:</strong><br>
1. Counts the all different lead categorie and number of entries in them.<br></li>
2. Counts all industries and number of entries in them.<br>
<li><strong>Topleads:</strong><br>
Counts the compnaies in the top 3 lead categories, closest to a deal: 'Follow-up', 'Qualified Lead' & 'Contract'<br></li>
<li><strong>Leads by industries:</strong><br>
Counts the industries and the different lead status in them and ho many companies in each industry belong to each lead status respectively.<br></li>
<li><strong>Pitches:</strong><br>
Prints a table of each company that has a pitch scheduled and the data within the pitch information entry.<br></li>
</ul>


## Recommendations: <br>
The program gets every industry and lead status from HubSpot without any changes to the initial setup required. <br>
However, some functions can perform additional analyses through changes to the HubSpot data structure / setup.<br>
The function 'Counts' automatically gets every industry and lead status from HubSpot and counts their occurrence.<br>
Additionally, with the following lead status & industry categories configured in HubSpot, the function puts out a custom sorted table that can be exported:<br>
<br>
<strong>(If you use different categories, they will still be shown and analyzed, but sorted by size and not custom sorted as shown below)</strong><br>
- Cold
- Cold Contacted
- Warm
- Follow-up
- Qualified Lead
- Contract
- Rejected
<br>
<ul>
<li>Insurance</li>
<li>Financial Services</li>
<li>Mobility</li>
<li>Health</li>
<li>Telecommunications</li>
<li>eCommerce</li>
<li>Online Broker</li>
<li>Education</li>
<li>Government</li>
</ul>
<br>
Of course you are free to change the categories for custom sort in the source code should you require different ones.<br>
For the function 'Pitches', a company information entry has to be set up in HubSpot, where the pitch information is inserted with the following structure:<br>
<br>
<em>(Closed / Open) date, time, location</em><br>
(again, you are free to enter whatever you like here and the function still works, the output just might not be ideal without changes to the sort command)<br>
<br>

<h2>FAQ:</h2><br>
<strong>I don't know where to find the generated file with 'ALL':</strong><br>
The file is saved under the same path as the .csv data file, with the same name, but '_Hubspool' added to the end of the filename.<br>
<br>
<strong>The wrong table is exported when I press 'Save to Excel':</strong><br>
The program always saves the last function you have printed / pressed. <br>
Make sure the right table is shown in the textfield before you save.<br>
<br>
<strong>There is only one table saved when I press 'Save to Excel':</strong><br>
If you want to have all analyses in one Excel file at once, press 'ALL'.<br>
Otherwise, the program saves the last function / table you have pressed.<br>
<br>

<h2>Support the project:</h2><br>
<p float='left'>
<a href='https://ethereum.org/en/stablecoins/#explore'>
<img src="https://user-images.githubusercontent.com/86114549/123052110-be243880-d402-11eb-9f0b-77df24874278.png" alt="tether-usdt-logo" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/#explore'>
<img src="https://user-images.githubusercontent.com/86114549/122908329-4a2b5700-d354-11eb-8ba9-4fa8d2c76ed6.png" alt="usdc-large" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/#explore'>
<img src="https://user-images.githubusercontent.com/86114549/122908250-35e75a00-d354-11eb-8be1-243fcecc93c6.png" alt="dai-large" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/#explore'>
<img src="https://user-images.githubusercontent.com/86114549/122967139-7235ad00-d38a-11eb-86e9-b6e634a5fc75.png" alt="ETH-logo-round" height="50"></a>
</p>
Wallet adress:<br> 
0xfC56bfc44E5671fD689331490D8e6Fa5B121474F<br>
<br>
<img width="116" alt="ether_wallet_qr_code" src="https://user-images.githubusercontent.com/86114549/122909208-3f24f680-d355-11eb-88b9-c49afb867a98.png">
Supported currencies: USDT, USDC, DAI, ETH <br>
<br>
© 2021 Braum
