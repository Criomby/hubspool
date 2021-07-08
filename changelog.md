<strong>1.0</strong> First working prototype written in datascience module.<br>
<strong>2.0</strong> Working prototype rewritten in pandas & numpy only.<br>
<strong>2.1.0</strong> Added 'leadsbyindustry' feature.<br>
<strong>2.1.1</strong> Updated error feature and instructions given by program during input / output.<br>
<strong>2.1.2</strong> Updated feature list, slightly smaller .exe file; new logo.<br>
<strong>2.2.0</strong> Suspended 'join' feature;<br>
new feature: Pitches list generation;<br>
contacts file entry suspended, Hubspot written logo created;<br>
Table printout size shows now 4 columns in width and printout box size optimized for split view of larger tables in width in second column supported now.<br>
<strong>2.2.1</strong> Updated 'Pitch' function with sort, closed pitches are on top now; <br>
'count_leads' & 'count_industries' output changes: 'Counts' now returns three tables: <br>
A table with all lead status' categories sorted by size, a table with all industries sorted by size,<br>
and a joint table with the leads and industries joined together and sorted in a custom order for export,<br>
Industries not included in the custom order are displayed as 'NaN' and can be viewed in the disordered table below if needed;<br>
code cleaned from depreciated rows and annotations.<br>
<strong>2.3.0</strong> Implemented system file dialog to open & save files (replaces the text label file path input);<br>
'ALL' function implemented: executes every function and saves the table in an Excel file in a separate sheet in it named respectively,<br>
the newly generated file is called after the imported file with '_Hubspool' added the filename and saved at the same path;<br>
the 'delete' butoon now not only deletes the output in the textbox, but also resets the savestate.<br>
<strong>2.4.0</strong> Drastically reduced filesize of the executable from 250mb to 30mb;<br>
textbox output optimized (separation rows above and below every printout + no empty first line),<br>
also code for textbox output optimized for easier human reading;<br>
'ALL' function checks for existing file before running;<br>
new button layout: 'ALL' first button in functions block;<br>
added new error messages.<br>
