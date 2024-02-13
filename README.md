Please check out the successor of Hubspool, Skidra here: https://github.com/Criomby/Skidra

<br>

---

<p align='center'><img src="https://user-images.githubusercontent.com/86114549/126486866-b0074940-70ff-4ecb-8747-7af48b6a8540.png" alt="Hubspool_Logo_Complete" width="300"></p>

#### A data analysis program for .csv database files exported from HubSpot CRM, calculating and exporting several quantitative and qualitative metrics to Excel via a simple GUI.

<br>

## Download Info: <br>
<h3> Latest ready-to-use version (Windows only):</h3>
<h3><a href='https://github.com/Criomby/hubspool/releases/download/v2.6.0/Hubspool_v2.6.0.exe'>Download Hubspool_v2.6.0.exe</a><br></h3>
<br>
Download the .exe and execute it as an administrator.<br>
<br>
Your antivirus might flag the program when trying to open it for the first time.
<h3>Be reassured: It's open source and safe for you and your data!</h3><br>

Verify your download:<br>
(SHA256sum) 4a54fdcd02b9cc66f5435d630764c132c2f953f9e2587f4d54a739c548c0f460<br>
(To verify your download you can use the <a href='https://github.com/Criomby/AutoHasher'>AutoHasher</a>)
<br>
<br>

## Getting started:
<img src="https://user-images.githubusercontent.com/86114549/148035625-6f5acfec-d127-44b2-8934-b5e9d43453e3.png" alt="Hubspool_v2.2.0_screenshot_counts" width="630">
<br>
_______________________________________________________________________________________________________________
<strong><h3>The intended way:</h3></strong><br>
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
<li><strong>Save to Excel:</strong><br>
Saves the last printed function which is seen in the text box as Excel (.xlsx) file.<br>
(not required for 'ALL')</li>
<li><strong>Delete:</strong><br>
Deletes all output within the text box.<br></li>
<br>
<br>
<br>
<li><strong>ALL:</strong><br>
All metrics are taken and exported into one Excel file within different sheets, each named accordingly.<br>
The exported file will be automatically saved at the filepath where the original file is saved, with '_Hubspool' added to the filename.<br>
<br>
<img src="https://user-images.githubusercontent.com/86114549/148035828-7e3d8601-ac9c-4a92-9ae1-2bdb277332b0.png" alt="textbox output ALL function" width="630"><br>
<br>
Folder with original file (right) and created file (left):
<br>
<img src="https://user-images.githubusercontent.com/86114549/148035875-46cc633b-350e-4edb-a3cb-d3fcce84ffc4.png" alt="output folder" width="200"><br>
<br>
The generated Excel file will contain the worksheets:<br>
<img width="630" alt="Screenshot worksheets" src="https://user-images.githubusercontent.com/86114549/148036302-9f53401f-cf78-42ff-8efa-175b39c113b6.png">
<br>
<br>

> <strong>Leads:</strong> ALL lead categories, size and logically sorted.<br>
>
> <strong>Industries:</strong> ALL industries, size and sorted by size descending.<br>
>
> <strong>Leads_by_industries:</strong> Lead category counts sorted by industry.<br>
>
> <strong>Pitches:</strong> All data entries with sales pitches info dispayed and sorted by status and date (see below).<br>
> 
> <strong>Rejection reasons:</strong> Companies with lead status 'Rejected' & 'Ineligible' and the data which is given as reason for the status in the data column 'Reason for rejection / unuitability'. (Also all companies with an entry in the 'Reason' column are shown)<br>
> 
> <strong>Topleads:</strong> All data entries with the lead status 'Follow-up', 'Qualified Lead', or 'Contract'.<br>

<br>
The created Excel also contains charts of the data for the sheets 'Leads' & 'Industries':<br>
<br>
<img width="630" alt="Screenshot Excel output ALL leads" src="https://user-images.githubusercontent.com/86114549/148036876-e4d6ec85-3715-4fc9-92f1-caf13d18e9ce.png">
<br>
<br>
<img width="630" alt="Screenshot Excel output ALL industries" src="https://user-images.githubusercontent.com/86114549/148036920-e8bdb6b5-eae1-465e-8c8f-3883f074cdd3.png">
<br>
<br>
(Only function 'ALL' creates charts).<br>
<br>
<br>
<li><strong>Print all:</strong><br>
Prints out the first 5 top and bottom rows, to see if the file contains the latest information.<br</li>
<li><strong>Counts:</strong><br>
1. Counts the all different lead categorie and number of entries in them.<br></li>
2. Counts all industries and number of entries in them.<br>
  <i>(See screenshots above from Excel sheets 'Leads' & 'Industries')</i>
<li><strong>Topleads:</strong><br>
Counts the compnaies in the top 3 lead categories: 'Follow-up', 'Qualified Lead' & 'Contract'<br></li>
<li><strong>Leads by industries:</strong><br>
Counts the industries and each respective indiv. lead status counts.<br></li>
<img width='300' alt='Hubspool_Excel_Topleads' src='https://user-images.githubusercontent.com/86114549/148038422-dee8371a-2c21-4bf4-a7ed-01e2a82c6f47.png'><br>
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
Additionally, with the following lead status categories configured in HubSpot, the function puts out a custom sorted table that can be exported:<br>
<br>
<strong>(If you use different lead categories, they will still be analyzed, but sorted by size and not custom sorted as shown below)</strong><br>

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
If a company / contact person rejects your offer, the reason for the rejection must be entered under "Company Information" under "Reason for rejection / unsuitability"<br>
within HubSpot. This category has to be manually added to the HubSpot database default configuration.<br>
This sheet is only generated using the function button 'ALL'.<br>

<h2>FAQ:</h2><br>
Regarding questions or other inquiries message me at:<br>
<br>
<strong>philippebraum@pm.me</strong><br>
<br>
<br>
<ul><li><strong>Data import requirements for database files:</strong><br></ul></li>
The imported data has to be in the .csv file format.<br>
When exporting the database file from from HubSpot select the following options:<br>
<br>
<img width="293" alt="Screenshot 2022-01-04 103955" src="https://user-images.githubusercontent.com/86114549/148040649-c8fdf626-d23f-46d6-951c-bba83a0b6f6d.png">
<br>
<img width='450' alt='HubSpot_export_view_settings' src='https://user-images.githubusercontent.com/86114549/148040296-97d8de17-5f73-4bcc-b23b-4eccf7dc8671.png'>
<br>
<i>For files not from HubSpot:</i><br>
The file has to contain the following columns:<br>
Name (of the company), Lead Status, Create Date, Industry, Company owner (internally responsible person), Pitch, Reason for rejection / unsuitability.<br>
<br>
<ul><li><strong>I have an Apple computer, can I use the ready-to-use release, too?</strong><br></ul></li>
The ready-to-use-version is Windows only atm.<br>
To run the program on MacOS, download the two scripts and run them in your local Python distribution, IDE or compile them yourself.<br>
<br>
<ul><li><strong>Windows Defender doesn't let me run the program:</strong><br></ul></li>
MS Windows' built-in antivirus Windows Defender automatically blocks any kind of unknown programs by default.<br>
<br>
<b>&nbsp&nbsp&nbsp&nbsp&nbspBe reassured:</b> Everything takes place on your local machine without access to the internet.<br>
<br>
You can still check the source code of the executable yourself if you want to: https://github.com/Criomby/hubspool/archive/refs/tags/v2.5.2.zip<br>
<br>

To run the program, follow the process below:<br>

<img src="https://user-images.githubusercontent.com/86114549/141657595-cb6240a0-5fc0-4dd0-969f-70d4a958207e.png" alt="defender_run"></a>

<img src="https://user-images.githubusercontent.com/86114549/141657566-c661a1bd-5918-43c5-b8e3-3b61f14e79e0.png" alt="defender_more_details"></a>

<br>
<ul><li><strong>Dependencies?</strong><br></ul></li>
See requirements.txt.<br>
<br>

<h2>Support the project:</h2><br>
<p float='left'>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/123052110-be243880-d402-11eb-9f0b-77df24874278.png" alt="tether-usdt-logo" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/122908329-4a2b5700-d354-11eb-8ba9-4fa8d2c76ed6.png" alt="usdc-large" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/122908250-35e75a00-d354-11eb-8be1-243fcecc93c6.png" alt="dai-large" height="50"></a>
<a href='https://basicattentiontoken.org/'>
<img src="https://user-images.githubusercontent.com/86114549/132904922-1921973e-13f0-40e5-a912-2180fe2b1485.png" alt="bat_token" height="50"></a>
<a href='https://ethereum.org/en/stablecoins/'>
<img src="https://user-images.githubusercontent.com/86114549/122967139-7235ad00-d38a-11eb-86e9-b6e634a5fc75.png" alt="ETH-logo-round" height="50"></a>
</p>
Wallet adress:<br> 
0xfC56bfc44E5671fD689331490D8e6Fa5B121474F<br>
<br>
<img width="116" alt="ether_wallet_qr_code" src="https://user-images.githubusercontent.com/86114549/122909208-3f24f680-d355-11eb-88b9-c49afb867a98.png"><br>
Supported currencies: USDT, USDC, DAI, BAT, ETH <br>
<br>
<br>
© 2021 Criomby
