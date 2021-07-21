<p align='center'><img src="https://user-images.githubusercontent.com/86114549/126486866-b0074940-70ff-4ecb-8747-7af48b6a8540.png" alt="Hubspool_Logo_Complete" width="300"></p>

#### A data analysis program for .csv database files exported from HubSpot CRM, calculating and exporting several quantitative and qualitative metrics via a simple GUI.

<br>

## Download Info: <br>
<h3> Ready-to-use version (Windows only):</h3><br>
The latest release can be found on the right under 'Releases'. <br>
Download the .exe and execute it as an administrator.<br>
<br>
Your antivirus might flag the program when trying to open it for the first time.
<h3>Be reassured: It's open source and safe for you and your data!</h3><br>

## Getting started:
<img src="https://user-images.githubusercontent.com/86114549/126452821-72b10b3c-3653-48f2-8050-bf79eca6ff61.png" alt="Hubspool_v2.2.0_screenshot_counts" width="630">
<br>
_______________________________________________________________________________________________________________
<strong><h3>The easiest & quickest way:</h3></strong><br>
<ul>
<li><strong>Open file:</strong><br>
Select your HubSpot exported .csv file.<br>
<li><strong>'ALL':</strong><br>
Press 'ALL' and you'll have an Excel file with all analyses next to your source file within one second.<br>
</ul>
<br>
<strong>-> Done!</strong><br>
_______________________________________________________________________________________________________________<br>
<br>
(See below for detailed descriptions)<br>
<br>
<br>
<br>

## Function descriptions:
Usually you won't need any other function but 'ALL'.<br>
Each other function prints the output tables into the text box for manual inspection and can be exported separately to Excel.<br>
<br>

> <strong>General workflow:</strong><br>
> 
> <strong>1.</strong> Press 'Open' and select the .csv data file you want to analyse. <br>
> <strong>2.</strong> Press the desired function (grey buttons).<br>
> <strong>3.</strong> Save the result via 'Save'. <br>
> <strong>4.</strong> Repeat for required functions. <br>
> 
> Steps 3 & 4 not required for 'ALL' function, since it exports all functions automatically.

<br>
<ul>
<li><strong>Open file:</strong><br>
Open a .csv file exported from HubSpot.<br>
The imported file has to be in the .csv format.</li>
<br>
<li><strong>Save to Excel:</strong><br>
Saves the last printed function which is seen in the text box as Excel (.xlsx) file.<br>
(not required for 'ALL')</li>
<li><strong>Delete:</strong><br>
Deletes all output within the text box.<br></li>
<br>
_________________________________________________________________________________________________________________________<br>
<br>
<li><strong>ALL:</strong><br>
All metrics are taken and exported into one Excel file within different sheets, each named accordingly.<br>
The exported file will be automatically saved at the filepath where the original file is saved, with '_Hubspool' added to the filename.<br>
<br>
<img src="https://user-images.githubusercontent.com/86114549/126341569-1a3578f2-9284-4e4a-8af4-af3fee6386f4.png" alt="textbox output ALL function" width="630"><br>
<br>
Folder with original file (left) and created file (right):
<br>
<img src="https://user-images.githubusercontent.com/86114549/125850530-87264001-8089-447f-9634-bedebf6516ed.png" alt="output folder" width="200"><br>
<br>
The generated Excel file will contain the worksheets:<br>
<img width="630" alt="Screenshot worksheets" src="https://user-images.githubusercontent.com/86114549/126385893-1007b189-208b-41f1-bd75-bb50382a1b01.png">
<br>
<br>

> <strong>Categories:</strong> Predefined leads and industries custom sorted & analyzed (see below for categories).<br>
> <strong>Leads_raw:</strong> ALL lead categories displayed, counted size and sorted by size descending.<br>
> <strong>Industries_raw:</strong> ALL industries displayed, counted size and sorted by size descending.<br>
> <strong>Leads_by_industries:</strong> All the leads categories and counts sorted by industry (predifined industries only, see below).<br>
> <strong>Pitches:</strong> All data entries with sales pitches info dispayed and sorted by status and date (see below).<br>
> <strong>Rejection reasons:</strong> Companies with lead status 'Rejected' & 'Ineligible' and the data which is given as reason for the status in the data column 'Reason for rejection / unuitability'. (Also all companies with an entry in the 'Reason' column are shown)
> <strong>Topleads:</strong> All data entries with the status 'Follow-up', 'Qualified Lead', or 'Contract'.<br>

<br>
The created Excel also contains charts of the data for the sheets 'Leads+Industries', 'Leads_raw' & 'Industries_raw':<br>
<br>
<img width="630" alt="Screenshot Excel output categories" src="https://user-images.githubusercontent.com/86114549/126545995-59325403-29d4-4194-b14d-f553d183cf20.png">
<br>
<br>
<img width="630" alt="Screenshot Excel output ALL leads_raw" src="https://user-images.githubusercontent.com/86114549/126546050-f27748cd-5485-40d7-81d7-62ce19351794.png">
<br>
<br>
<img width="630" alt="Screenshot Excel output ALL industries_raw" src="https://user-images.githubusercontent.com/86114549/126546112-b015ba8a-01f7-4e3f-98c7-1b6e396561ac.png">
<br>
<br>
(Only function 'ALL' creates charts).<br>
_________________________________________________________________________________________________________________________<br>
<br>
<li><strong>Print all:</strong><br>
Prints out the first 5 top and bottom rows, to see if the file contains the latest information.<br</li>
<li><strong>Counts:</strong><br>
1. Counts the all different lead categorie and number of entries in them.<br></li>
2. Counts all industries and number of entries in them.<br>
3. Puts out an additional custom sorted table with the leads and industries counted as specified by the categories below.<br>
<li><strong>Topleads:</strong><br>
Counts the compnaies in the top 3 lead categories, closest to a deal: 'Follow-up', 'Qualified Lead' & 'Contract'<br></li>
<li><strong>Leads by industries:</strong><br>
Counts the industries and the different lead status in them and ho many companies in each industry belong to each lead status respectively.<br></li>
<li><strong>Pitches:</strong><br>
Prints a table of each company that has a pitch scheduled and the data within the pitch information entry.<br></li>
</ul>
<br>

## Recommendations: <br>
The program gets every industry and lead status from HubSpot without any changes to the initial setup required.<br>
Should you import data from a different tool, read below for the requirements.<br>
<br>
However, some functions can perform additional analyses through changes to the HubSpot data structure / setup.<br>
The function 'Counts' automatically gets every industry and lead status from HubSpot and counts their occurrence.<br>
Additionally, with the following lead status & industry categories configured in HubSpot, the function puts out a custom sorted table that can be exported:<br>
<br>
<strong>(If you use different categories, they will still be analyzed, but sorted by size and not custom sorted as shown below)</strong><br>

<br>
<strong>Industries:</strong>
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
<strong>Lead status:</strong>
<ul>
  <li>Cold</li>
  <li>Cold Contacted</li>
  <li>Warm</li>
  <li>Follow-up</li>
  <li>Qualified Lead</li>
  <li>Contract</li>
  <li>Rejected</li>
  <li>Ineligible</li>
</ul>
<br>
Of course you are free to change the categories for custom sort in the source code should you require different ones.<br>
<br>
<strong>Pitches:</strong><br>
For the function 'Pitches', a company information entry has to be set up in HubSpot, where the pitch information is inserted with the following structure:<br>
<br>

> (Closed / Open) YYYY.MM.DD, time, location

(again, you are free to enter whatever you like here and the function still works, the output just might not be ideal without changes to the sort command)<br>
<br>
<strong>Rejection:</strong><br>
If a company / contact person rejects Qundo's offer, the reason for the rejection must be entered under "Company Information" under "Reason for rejection / unsuitability".<br>

<strong>Reference contacts:</strong><br>
Reference contacts are created as contacts under the respective company.<br>
The lead status "Reference" is then selected under the respective contact.<br>
<br>

<h2>FAQ:</h2><br>
Regarding questions or other inquiries message me at:<br>
<br>
<strong>criomby@pm.me</strong><br>
<br>
<br>
<strong>What are the empty cells in the sheet 'Leads+Industries' below 'Industry'?</strong><br>
Those cells are industries in your data that are not included in the predefined categories above.<br>
To see those industry names, go to the sheet 'Industries_raw' and they will be shown there.<br>
<br>
<strong>Data import requirements for files not from HubSpot:</strong><br>
The imported data has to be in the .csv file format.<br>
The file has to contain the following columns:<br>
Name (of the company), Lead Status, Create Date, Industry, Company owner (internally responsible person), Pitch, Reason for rejection / unsuitability.<br>
<br>

<h2>Support the project:</h2><br>
<p float='left'>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/123052110-be243880-d402-11eb-9f0b-77df24874278.png" alt="tether-usdt-logo" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/122908329-4a2b5700-d354-11eb-8ba9-4fa8d2c76ed6.png" alt="usdc-large" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/122908250-35e75a00-d354-11eb-8be1-243fcecc93c6.png" alt="dai-large" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/122967139-7235ad00-d38a-11eb-86e9-b6e634a5fc75.png" alt="ETH-logo-round" height="50"></a>
</p>
Wallet adress:<br> 
0xfC56bfc44E5671fD689331490D8e6Fa5B121474F<br>
<br>
<img width="116" alt="ether_wallet_qr_code" src="https://user-images.githubusercontent.com/86114549/122909208-3f24f680-d355-11eb-88b9-c49afb867a98.png">
Supported currencies: USDT, USDC, DAI, ETH <br>
<br>
<br>
© 2021 Braum
