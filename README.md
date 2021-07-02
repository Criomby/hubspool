# Hubspool
#### A data analysis program for .csv database files exported from HubSpot CRM, calculating and exporting several quantitative and qualitative metrics, operated via a simple GUI. 

## Download Info: <br>
<h3> Ready-to-use version: <br>
The latest release can be found on the right, under 'Releases'. <br>
Download the .exe and execute it as an administrator. </h3> <br>
Your antivirus might flag the program when trying to open it for the first time. <br>
<strong>Be reassured: It's open source and safe for you and your data!</strong><br>

## Documentation: <br>
<img src="https://user-images.githubusercontent.com/86114549/123169716-ee5aee00-d479-11eb-8fb1-cc90e99c0be4.png" alt="Hubspool_v2.2.0_screenshot_printall" height="650">
<br>
<strong>1.</strong> Open a .csv datafile: Enter filepath to your .csv file in the top textfield(s). <br>
<strong>2.</strong> Click 'Check files' (the printout will indicate, whether the files are found). <br>
<strong>3.</strong> Print desired function (grey buttons). <br>
<strong>4.</strong> Save printout via 'Save' to the specified path in the textfield above. <br>
<strong>5.</strong> Repeat. <br>
(Print a metric and save, print the next metric and save. <br>
Be sure to change the name for the save file above for each metric you save).<br>
<br>
<h3>Functions overview:</h3>
Each function prints out a table of the specified information below, which is displayed in the output text field and can be exported as .csv file / table.<br>
<br>
<ul>
<li><strong>Check files:</strong><br>
  Checks if the data (companies) file under the specified path can be found and accessed.<br></li>
<li><strong>Print all:</strong><br>
Prints out the top and bottom rows, to see if the file is correct.<br</li>
<li><strong>Counts:</strong><br>
1. Counts the all different lead categorie and number of entries in them.<br></li>
2. Counts all industries and number of entries in them.<br>
<li><strong>Topleads:</strong><br>
Counts the compnaies in the top 3 lead categories, closest to a deal: 'Follow-up', 'Qualified Lead' & 'Contract'<br></li>
<li><strong>Leads by industries:</strong><br>
Counts the industries and the different lead status in them and ho many companies in each industry belong to each lead status respectively.<br></li>
<li><strong>Pitches:</strong><br>
Prints a table of each company that has a pitch scheduled and the data within the pitch information entry.<br></li>
<li><strong>Delete:</strong><br>
Deletes all output in the text box.<br></li>
<li><strong>Save:</strong><br>
Saves the last printed function which is seen in the text box as .csv to the save path specified above.<br></li>
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

<h2>Support:</h2><br>
<strong>I don't know where to find my filepath:</strong><br>
Go to your targetfile > open properties > details > copy the folder path + add the name of your file to the end of it + .csv. <br>
<br>
<strong>The file is not saved when I press 'Safe to .csv':</strong><br>
You have probably forgotten to change the name for the next savefile after your last safe.<br>
Since the program does not override existing fles, it prints an error message, stating that the file already exists.<br>
In that case you have two options: 1. Define a new save path / name for your new file, or 2. delete the existing file.<br>
<br>
<strong>The wrong table is exported when I press 'save to':</strong><br>
The program always saves the last function you have printed / pressed. <br>
Make sure the right table is shown in the textfield on top before you save.<br>
<br>
<strong>There is only one table printed when I press 'save to':</strong><br>
Currently the program only saves the last function / table you have pressed. <br>
If you want to save multiple functions, you have to press the button, save it and repeat with each other function.<br>
The ability to save multiple tables at once will be included in a future version. <br>
<br>

<h2>Donations:</h2><br>
<p float='left'>
<img src="https://user-images.githubusercontent.com/86114549/123052110-be243880-d402-11eb-9f0b-77df24874278.png" alt="tether-usdt-logo" height="50">
<img src="https://user-images.githubusercontent.com/86114549/122908329-4a2b5700-d354-11eb-8ba9-4fa8d2c76ed6.png" alt="usdc-large" height="50">
<img src="https://user-images.githubusercontent.com/86114549/122908250-35e75a00-d354-11eb-8be1-243fcecc93c6.png" alt="dai-large" height="50">
<img src="https://user-images.githubusercontent.com/86114549/122967139-7235ad00-d38a-11eb-86e9-b6e634a5fc75.png" alt="ETH-logo-round" height="50">
</p>
Wallet adress:<br> 
0xfC56bfc44E5671fD689331490D8e6Fa5B121474F<br>
<br>
<img width="116" alt="ether_wallet_qr_code" src="https://user-images.githubusercontent.com/86114549/122909208-3f24f680-d355-11eb-88b9-c49afb867a98.png">
Supported currencies: USDT, USDC, DAI, ETH <br>
<br>
© 2021 Braum
