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
import pickle
import json
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Google-SpreadSheets' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery



"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

global creds

if module == "GoogleSuite":
    cred = None
    credential_path = GetParams("credentials_path")
    print(credential_path)
    if not os.path.exists(credential_path):
        raise Exception("El archivo de credenciales no existe en la ruta especificada")

    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/drive'
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
if module == "CreateSpreadSheet":

    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

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
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

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
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet_name = GetParams('sheetName')
    service = discovery.build('sheets', 'v4', credentials=creds)

    sheets = service.spreadsheets().get(spreadsheetId=ss_id).execute()["sheets"]

    for sheet in sheets:
        if sheet["properties"]["title"] == sheet_name:
            sheet_id =  sheet["properties"]["sheetId"]

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
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    range_ = GetParams('range')
    text = GetParams('text')

    try:
        print(text,"*****")
        if not text.startswith("["):
            text = text.replace('"', '\\\"')
            text = "[[ \"{}\" ]]".format(text)
            print(text, "-----")
        values = json.loads(text)
        print(values)

        service = discovery.build('sheets', 'v4', credentials=creds)

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
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    range_ = GetParams('range')
    result = GetParams('result')

    try:
        service = discovery.build('sheets', 'v4', credentials=creds)

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
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
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
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    try:
        ss_id = GetParams('ss_id')
        sheet_name = GetParams('sheetName')
        result = GetParams('result')

        range_ = sheet_name + "!A1:ZZZ999999"

        service = discovery.build('sheets', 'v4', credentials=creds)
        request = service.spreadsheets().values().get(spreadsheetId=ss_id, range=range_ )
        response = request.execute()

        length = len(response["values"])
        if result:
            SetVar(result, length)

    except Exception as e:
        PrintException()
        raise e
if module == "DeleteColumn":
    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    col = GetParams('column').lower()

    try:
        service = discovery.build('sheets', 'v4', credentials=creds)

        range_ = sheet + "!A1:ZZZ999999"
        abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
        request = service.spreadsheets().values().get(spreadsheetId=ss_id, range=range_)
        print(request)
        text = request.execute()['values']

        around_abc = len(col) - 1
        col_index = around_abc*len(abc) + abc.index(col)
        print(col_index)
        for row in text:
            row.append("")
            if len(row)>= col_index:
                row.pop(col_index)

        body = {
            "values": text
        }
        print(body)

        request = service.spreadsheets().values().update(spreadsheetId=ss_id, range=range_,
                                                         valueInputOption="USER_ENTERED",
                                                         body=body)
        response = request.execute()

    except Exception as e:
        PrintException()
        raise e
if module == "DeleteRow":
    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    ss_id = GetParams('ss_id')
    sheet = GetParams("sheetName")
    row = GetParams('row')

    try:

        row = int(row)
        service = discovery.build('sheets', 'v4', credentials=creds)

        range_ = sheet + "!A1:ZZZ999999"

        request = service.spreadsheets().values().get(spreadsheetId=ss_id, range=range_)
        print(request)
        text = request.execute()['values']

        if len(text) >= row:
            for i in range(len(text)):
                try:
                    difference = len(text[i]) - len(text[i + 1])
                    if difference > 0:
                        for j in range(difference):
                            text[i + 1].append("")
                except:
                    pass
            length = len(text[int(row) - 1])
            after = text[int(row):]
            text[int(row) - 1:] = after
            text.append([""]*length)
        print(text)

        body = {
            "values": text
        }

        request = service.spreadsheets().values().update(spreadsheetId=ss_id, range=range_,
                                                         valueInputOption="USER_ENTERED",
                                                         body=body)
        response = request.execute()

    except Exception as e:
        PrintException()
        raise e
