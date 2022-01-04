<strong>2.6.0</strong><br>
Function 'Leads by industries' (incl. in 'ALL') now automatically gets the available industries from the imported dataset,<br>
counts the lead categories of each individual industry and outputs it;<br>
Catgeories xls sheet removed,<br>
leads now always logically ordered / industries categories now always size-ordered;<br>
Same changes applied to textbox output with function 'Counts';<br>
Filename output via function 'ALL' changed to 'Hubspool_{current_date}.xslx';<br>
Changed GUI background color from grey to white;<br>
Replaced written logo with round graphical logo in GUI.<br>
<strong>2.5.1</strong><br>
Analysis 'Reason for rejection / unsuitability' implemented and added to function 'ALL';<br>
'Open file' dialog opens in Download directory;<br>
resolved issue tickets #8 & 9;<br>
chart axis' labeled & named accordingly, dropped legends for bar charts;<br>
window & taskbar logo changed from tkinter default logo to Hubspool logo image;<br>
new written logo font.<br>
<strong>2.5.0</strong><br>
Charts are generated with each analysis directly in the Excel file sheets,<br>
types: bar / pie charts;<br>
Excel column widths are fitted in width to content;<br>
The redundant indexes from the DataFrames have been removen and are not saved in the Excel anymore,<br>
they are now numbered from 0 to n when manually exporting to Excel (any function besides 'ALL') where they are still included.<br>
<strong>2.4.1</strong><br>
New minimalistic button design, logical button code order;<br>
optimized imports (reduced number of imported packages);<br>
text message output optimized for error message with spaces and save paths with spaces for better readability.<br>
<strong>2.4.0</strong><br>
Drastically reduced filesize of the executable from ~250mb to ~30mb;<br>
textbox output optimized (separation rows above and below every printout + no empty first line),<br>
also code for textbox output optimized for easier human reading;<br>
'ALL' function checks for existing file before running;<br>
new button layout: 'ALL' first button in functions block;<br>
added new error messages.<br>
<strong>2.3.0</strong><br>
Implemented system file dialog to open & save files (replaces the text label file path input);<br>
'ALL' function implemented: executes every function and saves the table in an Excel file in a separate sheet in it named respectively,<br>
the newly generated file is called after the imported file with '_Hubspool' added the filename and saved at the same path;<br>
the 'delete' butoon now not only deletes the output in the textbox, but also resets the savestate.<br>
<strong>2.2.1</strong><br>
Updated 'Pitch' function with sort, closed pitches are on top now; <br>
'count_leads' & 'count_industries' output changes: 'Counts' now returns three tables: <br>
A table with all lead status' categories sorted by size, a table with all industries sorted by size,<br>
and a joint table with the leads and industries joined together and sorted in a custom order for export,<br>
Industries not included in the custom order are displayed as 'NaN' and can be viewed in the disordered table below if needed;<br>
code cleaned from depreciated rows and annotations.<br>
<strong>2.2.0</strong><br>
Suspended 'join' feature;<br>
new feature: Pitches list generation;<br>
contacts file entry suspended, Hubspot written logo created;<br>
Table printout size shows now 4 columns in width and printout box size optimized for split view of larger tables in width in second column supported now.<br>
<strong>2.1.2</strong><br>
Updated feature list, slightly smaller .exe file; new logo.<br>
<strong>2.1.1</strong><br>
Updated error feature and instructions given by program during input / output.<br>
<strong>2.1.0</strong><br>
Added 'leadsbyindustry' feature.<br>
<strong>2.0</strong><br>
Working prototype rewritten in pandas & numpy only.<br>
<strong>1.0</strong><br>
First working prototype written in datascience module.<br>
