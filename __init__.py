# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os.path

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + \
           'Google-SpreadSheets' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

from googleapiclient import discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pickle
import json

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

global creds

if module == "GoogleSuite":
    cred = None
    credential_path = GetParams("credentials_path")

    try:
        print(credential_path)
        if not os.path.exists(credential_path):
            raise Exception(
                "El archivo de credenciales no existe en la ruta especificada")

        SCOPES = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/script.projects',
            'https://www.googleapis.com/auth/script.external_request',
            'https://www.googleapis.com/auth/drive.scripts'
        ]

        if os.path.exists('token_sheet.pickle'):
            with open('token_sheet.pickle', 'rb') as token:
                cred = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credential_path, SCOPES)
                cred = flow.run_local_server()
            # Save the credentials for the next run
            with open('token_sheet.pickle', 'wb') as token:
                pickle.dump(cred, token)
        creds = cred
    except Exception as e:
        PrintException()
        raise e

if module == "CreateSpreadSheet":

    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_name = GetParams('ss_name')
    result = GetParams('result')

    service = discovery.build('sheets', 'v4', credentials=creds)

    spreadsheet_body = {
        "properties": {
            "title": ss_name
        }
    }

    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    if result:
        SetVar(result, response["spreadsheetId"])
        
if module == "CreateSheet":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    name = GetParams('name')
    result = GetParams('result')

    service = discovery.build('sheets', 'v4', credentials=creds)

    body = {
        "requests": [
            {
                "addSheet": {
                    "properties": {
                        "title": name,
                    }
                }
            }
        ]
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=ss_id,
                                                 body=body)
    response = request.execute()
    print(response)
    if result:
        sheetId = response["replies"][0]["addSheet"]["properties"]["sheetId"]
        SetVar(result, sheetId)
if module == "DeleteSheet":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet_name = GetParams('sheetName')
    service = discovery.build('sheets', 'v4', credentials=creds)

    sheets = service.spreadsheets().get(
        spreadsheetId=ss_id).execute()["sheets"]

    for sheet in sheets:
        if sheet["properties"]["title"] == sheet_name:
            sheet_id = sheet["properties"]["sheetId"]

    body = {
        "requests": [
            {
                "deleteSheet": {
                    "sheetId": sheet_id
                }
            }

        ]
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=ss_id,
                                                 body=body)
    response = request.execute()

if module == "UpdateRange":

    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    range_ = GetParams('range')
    text = GetParams('text')

    try:
        if not text.startswith("["):
            text = text.replace('"', '\\\"')
            text = "[[ \"{}\" ]]".format(text)
        
               
        print(text)
        values = eval(text)
        print(values)
        
        service = discovery.build('sheets', 'v4', credentials=creds)

        # Checks existence of the given sheet name and update the range
        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()
        for element in data["sheets"]:
            if element["properties"]["title"] == sheet:
                range_ = sheet + "!" + range_ # Sheet1!A1:A10
        
        body = {
            "values": values
        }
        print(body)
        
        request = service.spreadsheets().values().update(spreadsheetId=ss_id, range=range_,
                                                         valueInputOption="USER_ENTERED",
                                                         body=body)
        response = request.execute()
    
    except Exception as e:
        PrintException()
        raise e

if module == "ReadCells":

    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    range_ = GetParams('range')
    result = GetParams('result')

    try:
        service = discovery.build('sheets', 'v4', credentials=creds)

        # Checks existence of the given sheet name and update the range
        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()
        for element in data["sheets"]:
            if element["properties"]["title"] == sheet:
                range_ = sheet + "!" + range_ # Sheet1!A1:A10
                
        request = service.spreadsheets().values().get(spreadsheetId=ss_id, range=range_)

        response = request.execute()
        try:
            value = response["values"]
        except:
            value = ""

        if result:
            SetVar(result, value)
    except Exception as e:
        PrintException()
        raise e

if module == "GetSheets":

    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams('sheetName')
    result = GetParams('result')
    
    service = discovery.build('sheets', 'v4', credentials=creds)
        
    request = service.spreadsheets().get(spreadsheetId=ss_id)
    response = request.execute()

    sheets = []
    for element in response["sheets"]:
        sheets.append(element["properties"]["title"])
    if result:
        SetVar(result, sheets)
        
if module == "CountCells":

    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    try:
        ss_id = GetParams('ss_id')
        sheet_name = GetParams('sheetName')
        result = GetParams('result')

        range_ = sheet_name + "!A1:ZZZ999999"

        service = discovery.build('sheets', 'v4', credentials=creds)
        
        # Checks existence of the given sheet name and update the range
        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()
        for element in data["sheets"]:
            if element["properties"]["title"] == sheet:
                range_ = sheet + "!" + range_ # Sheet1!A1:A10
                
        request = service.spreadsheets().values().get(spreadsheetId=ss_id, range=range_)
        response = request.execute()

        length = len(response["values"])
        if result:
            SetVar(result, length)

    except Exception as e:
        PrintException()
        raise e


def get_column_index(col):
    try:
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
        around_abc = len(col) - 1
        col = col[-1]
        col_index = around_abc * len(abc) + abc.index(col)
        return col_index
    except Exception as e:
        PrintException()
        raise e


if module == "DeleteColumn":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    col = GetParams('column').lower()
    blank = GetParams('blank')

    try:
        service = discovery.build('sheets', 'v4', credentials=creds)

        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()

        for element in data["sheets"]:
            if element["properties"]["title"] == sheet:
                sheet_id = element["properties"]["sheetId"]
        
        print("sheet id",sheet_id)

        col_index = get_column_index(col)
        print(col_index)

        if blank is not None:
            blank = eval(blank)

        if blank:
            shiftDimension = "ROWS"
        else:
            shiftDimension = "COLUMNS"

        body = {
            "requests": [{
                "deleteRange": {
                    "range": {
                        "sheetId": sheet_id,
                        "startColumnIndex": col_index,
                        "endColumnIndex": col_index + 1
                    },
                    "shiftDimension": shiftDimension
                }
            }]
        }

        request = service.spreadsheets().batchUpdate(spreadsheetId=ss_id, body=body)
        response = request.execute()

    except Exception as e:
        PrintException()
        raise e

if module == "DeleteRow":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    row = GetParams('row')
    blank = GetParams('blank')

    try:

        service = discovery.build('sheets', 'v4', credentials=creds)

        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()

        for element in data["sheets"]:
            if element["properties"]["title"] == sheet:
                sheet_id = element["properties"]["sheetId"]

        if blank is not None:
            blank = eval(blank)

        if blank:
            shiftDimension = "COLUMNS"
        else:
            shiftDimension = "ROWS"

        if row.find("-") == -1:
            row = int(row)
            body = {
                "requests": [{
                    "deleteRange": {
                        "range": {
                            "sheetId": sheet_id,
                            "startRowIndex": row - 1,
                            "endRowIndex": row
                        },
                        "shiftDimension": shiftDimension
                    }
                }]
            }
        else:
            row = row.split("-")
            body = {
                "requests": [{
                    "deleteRange": {
                        "range": {
                            "sheetId": sheet_id,
                            "startRowIndex": int(row[0]) - 1,
                            "endRowIndex": int(row[1])
                        },
                        "shiftDimension": shiftDimension
                    }
                }]
            }

        request = service.spreadsheets().batchUpdate(spreadsheetId=ss_id, body=body)
        response = request.execute()

    except Exception as e:
        PrintException()
        raise e

if module == "AddColumn":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    col = GetParams('column').lower()
    q = int(GetParams("q"))
    blank = GetParams('blank')

    try:
        service = discovery.build('sheets', 'v4', credentials=creds)

        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()

        for element in data["sheets"]:
            if element["properties"]["title"] == sheet:
                sheet_id = element["properties"]["sheetId"]

        col_index = get_column_index(col)
        
        if blank is not None:
            blank = eval(blank)

        if blank == False or col_index == 0:
            inheritance = "false"
        else:
            inheritance = "true"

        body = {
            "requests": [{
                "insertDimension": {
                    "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": col_index,
                    "endIndex": col_index + q
                },
                "inheritFromBefore": inheritance
                }
            }]
        }

        request = service.spreadsheets().batchUpdate(spreadsheetId=ss_id, body=body)
        response = request.execute()

    except Exception as e:
        PrintException()
        raise e

if module == "AddRow":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    row = int(GetParams('row'))
    q = int(GetParams("q"))
    blank = GetParams('blank')
    
    try:

        service = discovery.build('sheets', 'v4', credentials=creds)

        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()

        for element in data["sheets"]:
            if element["properties"]["title"] == sheet:
                sheet_id = element["properties"]["sheetId"]

        if blank is not None:
            blank = eval(blank)
            
        row_index = row - 1

        if blank == False or row_index == 0:
            inheritance = "false"
        else:
            inheritance = "true"

        body = {
            "requests": [{
                "insertDimension": {
                    "range": {
                    "sheetId": sheet_id,
                    "dimension": "ROWS",
                    "startIndex": row_index,
                    "endIndex": row_index + q
                },
                "inheritFromBefore": inheritance
                }
            }]
        }

        request = service.spreadsheets().batchUpdate(spreadsheetId=ss_id, body=body)
        response = request.execute()

    except Exception as e:
        PrintException()
        raise e

def get_existing_basic_filters(ss_id, service, startRow=0, endRow=1000) -> dict:
    params = {'spreadsheetId': ss_id,
              'fields': 'sheets(properties(sheetId,title),basicFilter)'}
    response = service.spreadsheets().get(**params).execute()
    print(response)
    data = service.spreadsheets().get(spreadsheetId=ss_id).execute()
    values_range = []
    for sheet in response['sheets']:
        if 'basicFilter' in sheet:
            values_range = list(sheet.values())[1]['range']
    # {'startRowIndex': startRow, 'endRowIndex': endRow, 'startColumnIndex': 4, 'endColumnIndex': 5}
    col = chr(values_range['startColumnIndex'] + 65)
    col = col + str(values_range['startRowIndex']+1) + ":" + col + str(values_range['endRowIndex']+1)
    return col



def apply_filters(ss_id, filters, service):
    try:
        # All requests are validated before any are applied, so bundling the set and clear filter
        # operations in the same request would fail: only 1 basic filter can exist at a time.

        def clear_filters(ss_id, known_filters, service):
            requests = []
            for sheetId, filter in known_filters.items():
                requests.append({'clearBasicFilter': {'sheetId': sheetId}})
            if not requests:
                return
            params = {'spreadsheetId': ss_id,
                      'body': {'requests': requests}}
            service.spreadsheets().batchUpdate(**params).execute()

        def removekey(d, key):
            r = dict(d)
            del r[key]
            return r

        clear_filters(ss_id, filters, service)

        requests = []
        for sheetId, filter in filters.items():
            # By removing the starting and ending indices from the 'range' property,
            # we ensure the basicFilter will apply to the entire sheet bounds. If one knows the
            # desired values for startColumnIndex, startRowIndex, endRowIndex, endColumnIndex,
            # then they can be used to create a range-specific basic filter.
            # The 'range' property is a `GridRange`:
            if 'filterSpecs' not in filter:
                filter['filterSpecs'] = [{
                    'filterCriteria': {
                        'hiddenValues': []
                    }
                }]
            requests.append({'setBasicFilter': {'filter': filter}})
        if not requests:
            return
        params = {'spreadsheetId': ss_id,
                  'body': {'requests': requests}}
        print("Params")
        print(params)
        service.spreadsheets().batchUpdate(**params).execute()
    except Exception as e:
        PrintException()
        raise e


def create_filter_structure(ranges, values, sheet_id):
    try:
        new_filter = {
            'range': ranges
        }
        startColumnIndex = ranges['startColumnIndex']
        endColumnIndex = ranges['endColumnIndex']
        new_filter['filterSpecs'] = []
        for index in range(startColumnIndex, endColumnIndex):
            new_filter['filterSpecs'].append({
                'columnIndex': index,
                'filterCriteria': {
                    'hiddenValues': values
                }
            })
        new_filter_with_sheet_id = {
            sheet_id: new_filter
        }
        return new_filter_with_sheet_id
    except Exception as e:
        PrintException()
        raise e

if module == "unfilterData":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")
    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    try:
        service = discovery.build('sheets', 'v4', credentials=creds)
        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()
        
        if sheet == None or sheet == "":
                    sheet_id = 0
        else:
            for element in data["sheets"]:
                if element["properties"]["title"] == sheet:
                    sheet_id = element["properties"]["sheetId"]
        
        requests = []
        requests.append({'clearBasicFilter': {'sheetId': sheet_id}})
        
        params = {'spreadsheetId': ss_id,
                  'body': {'requests': requests}}
        
        service.spreadsheets().batchUpdate(**params).execute()      
        
    except Exception as e:
        PrintException()
        raise e

if module == "filterData":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")
    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    col = GetParams("col").lower()
    valor_filtro = GetParams("valor_filtro")
    try:
        col_index = get_column_index(col)
        print(col_index)
        service = discovery.build('sheets', 'v4', credentials=creds)
        data = service.spreadsheets().get(spreadsheetId=ss_id).execute()
        
        if sheet == None or sheet == "":
            sheet_id = 0
        else:
            for element in data["sheets"]:
                if element["properties"]["title"] == sheet:
                    sheet_id = element["properties"]["sheetId"]
                    
        print(sheet_id)
        
        range_ = sheet+"!A:"+col
        req = service.spreadsheets().values().get(spreadsheetId=ss_id, range=range_).execute()
        
        # It checks where the table that is going to be filtered starts and ends 
        first_row = 0
        values = req["values"]
        print(values)
        for cell in values:
            if cell == []:
                first_row += 1
            else:
                break
        last_row = len(req['values'])
        print(last_row)
        
        ranges = {
            "sheetId": sheet_id,
            'startRowIndex': first_row,
            'endRowIndex': last_row,
            'startColumnIndex': col_index,
            'endColumnIndex': col_index + 1,
        }
        
        hidden_values = []
        for row in values:
            # It appends a blank space to the list so the row is recognized as one in the following "for"
            if row == []:
                row.append("")
            for cell in row:
                if valor_filtro != cell:
                    hidden_values.append(cell)
        
        filters = create_filter_structure(ranges, hidden_values, sheet_id)
        apply_filters(ss_id, filters, service)
    except Exception as e:
        PrintException()
        raise e

if module == "filterCells":
    if not creds:
        raise Exception(
            "No hay credenciales ni token válidos, por favor configure sus credenciales")
    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    res = GetParams("res")
    range = GetParams("range_")
    try:
        service = discovery.build('sheets', 'v4', credentials=creds)
        
        data_ = service.spreadsheets().get(spreadsheetId=ss_id).execute()
        
        for element in data_["sheets"]:
            if sheet == None or sheet == "":
                    sheet = data_["sheets"][0]["properties"]["title"]
            if element["properties"]["title"] == sheet:
                sheet_id = element["properties"]["sheetId"]
                filter_start = element["basicFilter"]["range"]["startRowIndex"]
                
        data = service.spreadsheets().get(spreadsheetId=ss_id, fields="sheets(data(rowMetadata(hiddenByFilter)),properties/sheetId)").execute()

        #column_filter = get_existing_basic_filters(ss_id, service)
        list_hidden_rows = []
        for column in data['sheets']:
            if column['properties']['sheetId'] == sheet_id:
                for index, item in enumerate(column['data'][0]['rowMetadata']):
                    if bool(item):
                        list_hidden_rows.append(index)
       
        # It makes sure that always start from the first row of the filter, so the row index vs hidden rows can be done
        range_first_row = range[1]
        if range_first_row != filter_start:
            tmp = list(range)
            tmp[1] = filter_start + 1
            print(tmp)
            range = "".join(str(x) for x in tmp)
            print(range)
            
        range_ = sheet + "!" + range
        request = service.spreadsheets().values().get(spreadsheetId=ss_id, range=range_)
        response = request.execute()
        value = response["values"]
        
        final_cells = []
        for row_index, item in enumerate(value):
            row_index = (row_index + filter_start)
            if row_index not in list_hidden_rows:
                final_cells.append(item)
        SetVar(res, final_cells)
    except Exception as e:
        PrintException()
        raise e
