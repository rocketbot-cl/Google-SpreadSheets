



# Google SpreadSheet
  
Módulo to handle Google SpreadSheet from Rocketbot  
  
![banner](/docs/imgs/Banner_C:\Users\jmsir\Desktop\RB\Rocketbot\modules\Google-SpreadSheets.png)
## Howto install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



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
  
Create a new sheet in SpreadSheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Name|

### Delete Sheet
  
Delete a sheet from SpreadSheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name for delete||Sheet Name|

### Set cells
  
Set a cell or range of cells from spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Enter cell ||A1|
|Text ||[["data","data"],["data","data"]]|

### Read cells
  
Read a cell or range of cells from SpreadSheet selected, eg. A1 or A1:B5
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Enter cell or range of cells ||A1|
|Result||Variable|

### Get sheets
  
Get list of sheets with your id from a spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Result||Variable|

### Contar filas
  
Count rows
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Result||Variable|

### Add column
  
Add a column from spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Column||A|
|Quantity||Quantity|
|Keep format|||

### Add row
  
Add a row from spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Row||5|
|Quantity||Quantity|
|Keep format|||

### Delete column
  
Delete a column from spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Column||A|
|Blank|||

### Delete row
  
Delete a row from spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Row||5-7|
|Blank|||

### Filter data
  
Filter data in a spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|
|Column name||Column|
|Ingrese el valor||Value to filter|

### Unfilter data
  
Filter data in a spreadsheet selected
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet|

### Get cells filtered
  
Get cells filtered
|Parameters|Description|example|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Sheet name||Sheet:|
|Range ||A1:B2|
|Result||Variable|
