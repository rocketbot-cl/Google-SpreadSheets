



# Google SpreadSheet
  
Módulo para manejar Google SpreadSheet desde Rocketbot  

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

Note: When the first connection is made, a .pickle file will be created in the Rocketbot root folder, to connect to the same service from another account you must delete
that file. Do the same procedure for the case in which the credentials expire.

## Overview

1. Setup G-Suite credentials  
Get permissions to handle Google SpreadSheet with Rocketbot

2. Create SpreadSheet  
Create a new spreadsheet in Google SpreadSheet

3. Create Sheet  
Create a new sheet in selected SpreadSheet

4. Delete Sheet  
Delete a sheet from selected SpreadSheet

5. Write cells  
Write to a cell or range of cells in the selected Spreadsheet

6. Read cells  
Read a cell or range of cells from the selected Spreadsheet, example A1 or A1:B5

7. Get sheets  
Get list of sheets with their ID of the selected Spreadsheet

8. Contar filas  
Count the rows of the selected sheet

9. Add column  
Add Columns to Selected Spreadsheet

10. Add row  
Add rows to the selected Spreadsheet

11. Delete column  
Delete a column from a selected Spreadsheet

12. Delete row  
Delete a row from a selected Spreadsheet

13. Filter data  
Filter data in the selected Spreadsheet

14. Unfilter data  
Unfilter data in the selected Spreadsheet

15. Get filtered cells  
Get the filtered cells  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)- [**google-auth-httplib2**](https://pypi.org/project/google-auth-httplib2/)- [**google-auth-oauthlib**](https://pypi.org/project/google-auth-oauthlib/)- [**gspread**](https://pypi.org/project/gspread/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)