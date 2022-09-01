



# Google SpreadSheet
  
Módulo para manejar Google SpreadSheet desde Rocketbot  
  
![banner](imgs/Banner_Google-SpreadSheets.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

## How to use this module

Before using this module, you must register your app into the Google Cloud Portal.

1. Sign in with a google account to the following link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete the form and then press Create
3. Within the Navigation Menu (Left), enter API and Services
4. In the upper section, go to "+ ENABLE API AND SERVICES"
5. Search for "Google Sheets API", select it and finally enable it
6. Again, go to the Navigation Menu (Left) > API and Services > Credentials
7. Press Create Credentials > OAuth Client ID, select Application Type: Desktop App, enter a name and create.
8. Download the credentials JSON file.
9. Finally go to the Navigation Menu (Left) > Consent Screen and add a user in the "Test Users" section


## Description of the commands

### Setup G-Suite credentials
  
Get permissions to handle Google SpreadSheet with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Path||C:/path/to/credentials.json|

### Create SpreadSheet
  
Create a new spreadsheet in Google SpreadSheet
|Parameters|Description|example|
| --- | --- | --- |
|SpreadSheet name||Name|
|Variable where the ID will be saved||Variable|

### Create Sheet
  
Create a new sheet in selected SpreadSheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Name|

### Delete Sheet
  
Delete a sheet from selected SpreadSheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Name of the sheet to delete||Sheet Name|

### Write cells
  
Write to a cell or range of cells in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Cell to write ||A1|
|Text ||[["data","data"],["data","data"]]|

### Read cells
  
Read a cell or range of cells from the selected Spreadsheet, example A1 or A1:B5
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Cell or range of cells ||A1|
|Result||Variable|

### Get sheets
  
Get list of sheets with their ID of the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Result||Variable|

### Contar filas
  
Count the rows of the selected sheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Result||Variable|

### Add column
  
Add Columns to Selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Column||A|
|Quantity||Quantity|
|Keep format|||

### Add row
  
Add rows to the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Row||5|
|Quantity||Quantity|
|Keep format|||

### Delete column
  
Delete a column from a selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Column||A|
|Blank|||

### Delete row
  
Delete a row from a selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Row||5-7|
|Blank|||

### Filter data
  
Filter data in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Column||Column|
|Value||Value to filter|

### Unfilter data
  
Unfilter data in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|

### Get filtered cells
  
Get the filtered cells
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet:|
|Range ||A1:B2|
|Result||Variable|
