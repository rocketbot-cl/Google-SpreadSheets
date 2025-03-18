



# Google SpreadSheet
  
This module allows you to read, write and update Google spreadsheets. You can add, delete, duplicate or even hide sheets; filter data; add or delete rows and columns; modify cells format, copy/cut and paste them; and more.  

*Read this in other languages: [English](Manual_Google-SpreadSheets.md), [Português](Manual_Google-SpreadSheets.pr.md), [Español](Manual_Google-SpreadSheets.es.md)*
  
![banner](imgs/Banner_Google-SpreadSheets.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## How to use this module

Before using this module, you must register your app into Google Cloud Portal.

1. Sign in with a google account and get into the following link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete the form to create a new proyect and then press "Create".
3. Within the Navigation Menu (Left), get into API and Services.
4. Go to the upper section and press "+ ENABLE API AND SERVICES".
5. Search for "Google Sheets API", select it and then press "ENABLE".
6. Go back to the Navigation Menu, go to API and Services and then get into Credentials.
7. Press Create Credentials and select OAuth Client ID. Then select Application Type: Desktop App, give it a name and press Create.
8. Download the credentials JSON file.
9. Finally, go back to the Navigation Menu, go to Consent Screen and add your user in the "Test Users" section (even if it is the same that is creating the app).

Note: When the first connection is made, a .pickle 
file will be created in the Rocketbot root folder, to connect to the same service with another account you must give each session a name. If credentials expire you must delete the .pickle file and create and download a nwe credentials (JSON) file.

## ERROR REDIRECT_URI_MISMATCH

If you receive the following error when using a previously functional credentials .json file:

![error](imgs/redirect_uri_mismatch_Error.png)

Credentials will need to be created again. Before step 6 of the previous section 'How to use this module', the following must be configured:
- Go to 'OAuth Consent Screen' from the left menu
- Choose the User Type:
    1. Internal: Projects associated with a Google Cloud organization can configure internal users to limit authorization requests to members of the organization.
    2. External: available to any user with a Google account.
       
        Click on Create
- Complete the mandatory data marked with an asterisk (*) on the Application Information page, such as 
the Application Name, the user's support Email, and the developer's contact information. Click Save and continue.
- Continue from step 6 indicated in this section to conclude.

## Description of the commands

### Setup G-Suite credentials
  
Get permissions to handle Google SpreadSheet with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path|JSON file with the credentials to access the Google SpreadSheets API.|C:/path/to/credentials.json|
|Port (Optional)||8080|
|Session||session|

### Login without json file
  
Login to Google Drive without json file
|Parameters|Description|example|
| --- | --- | --- |
|Client ID|Client ID from Google Cloud Platform console.|123456789012-xxxxxxxxxxxxxxx.apps.googleusercontent.com|
|Client Secret|Client Secret from Google Cloud Platform console.|GOCSPX-xxxxxxxxx_Dc9TGFy32_xxxxxxxx|
|Port (Optional)||8080|
|Session||session|

### Create SpreadSheet
  
Create a new spreadsheet in Google SpreadSheet
|Parameters|Description|example|
| --- | --- | --- |
|SpreadSheet name||Name|
|Variable where the ID will be saved||Variable|
|Session||session|

### Create Sheet
  
Create a new sheet in selected SpreadSheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Name|
|Session||session|

### Update Sheet properties
  
Update a sheet properties from selected SpreadSheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Name of the sheet to update||Sheet Name|
|New Name (Optional)||New|
|Hide sheet||False|
|Session||session|

### Delete Sheet
  
Delete a sheet from selected SpreadSheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Name of the sheet to delete||Sheet Name|
|Session||session|

### Write cells
  
Write to a cell or range of cells in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Cell to write ||A1|
|Text ||[["data","data"],["data","data"]]|
|Type of data sending||USER_ENTERED|
|Session||session|

### Format cells
  
Change format of a cell or range of cells in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Cells to format ||A1:C1|
|Merge cells|||
|Unmerge cells|||
|Adjust columns size|||
|Format type||---- Select type ----|
|Format pattern ||yyyy-mm-dd hh:mm A/P".M."|
|Font color ||255,0,0|
|Font family ||Open Sans|
|Font size ||12|
|Bold|||
|Italic|||
|Strikethrough|||
|Underline|||
|Session||session|

### Read cells
  
Read a cell or range of cells from the selected Spreadsheet, example A1 or A1:B5
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Cell or range of cells ||A1|
|Result||Variable|
|Session||session|

### Copy/Cut and paste
  
Copy or cut and paste a cell or range of cells in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Source sheet name||Sheet1|
|Source cells ||A1:C1|
|Destination sheet name||Sheet2|
|Destination cells ||A2:C2|
|Paste type||---- Select type ----|
|Transponse|||
|Cut|||
|Session||session|

### Get sheets
  
Get list of sheets with their ID of the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Result||Variable|
|Session||session|

### Count rows and/or columns
  
Count the used rows and/or columns of the selected sheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Range ||A1:A100|
|Variable where to store result of rows||Variable|
|Variable where to store result of columns||Variable|
|Session||session|

### Add column
  
Add Columns to Selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Column||A|
|Quantity||Quantity|
|Keep format|||
|Session||session|

### Add row
  
Add rows to the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Row||5|
|Quantity||Quantity|
|Keep format|||
|Session||session|

### Delete column
  
Delete a column from a selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Column/s||A:C|
|Blank|||
|Session||session|

### Delete row
  
Delete a row from a selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Row||5:7|
|Blank|||
|Session||session|

### Filter data
  
Filter data in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Column||Column|
|Value||Value to filter|
|Session||session|

### Unfilter data
  
Unfilter data in the selected Spreadsheet
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Session||session|

### Get filtered cells
  
Get the filtered cells
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Range ||A1:B2|
|Get data with row number|||
|Result||Variable|
|Session||session|

### Duplicate sheet
  
Duplicates the selected sheet to the same or another workbook
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|Spreadsheet ID||Spreadsheet ID|
|Result||Variable|
|Session||session|

### Text to columns
  
Splits a column of text into multiple columns, based on a delimiter in each cell.
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet1|
|separator||---- Select separator ----|
|Result||Variable|
|Session||session|
