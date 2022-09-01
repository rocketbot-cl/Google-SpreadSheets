



# Google SpreadSheet
  
Módulo para manejar Google SpreadSheet desde Rocketbot  

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  

## Como usar este modulo

Antes de usar este modulo, es necesario registrar tu aplicación en el portal de Google Cloud. 

1. Ingresar con una cuenta de google al siguiente link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Completar el formulario y luego presionar Crear
3. Dentro del Menu de Navegación (Izquierdo), ingresar en API y Servicios
4. En la sección superior, ingresar a "+ HABILITAR API Y SERVICIOS"
5. Buscar "Google Sheets API", seleccionar y por ultimo habilitar
6. Nuevamente dirigirse a Menu de Navegación (Izquierdo) > API y Servicios > Credenciales
7. Presionas Crear Credenciales > ID de cliente de OAuth, seleccionar como Tipo de Aplicación: App de Escritorio, colocar un nombre y crear.
8. Descargar el achivo JSON de credenciales.
9. Por ultimo dirigirse a Menu de Navegación (Izquierdo) > Pantalla de Consentimiento y agregar usuario dentro de la seccion "Usuarios de prueba".

Nota: Cuando se realice la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio desde otra cuenta, debe eliminar
ese archivo Realice el mismo procedimiento para el caso en que caduquen las credenciales.

## Overview

1. Configurar credenciales G-Suite  
Obtiene los permisos para manejar Google SpreadSheet con Rocketbot

2. Crear Hoja de Cálculo  
Crea una nueva hoja de cálculo en Google SpreadSheet

3. Crear Hoja  
Crear una nueva hoja en la Hoja de Cálculo seleccionada

4. Borrar Hoja  
Elimina una hoja de la Hoja de Cálculo seleccionada

5. Escribir en celdas  
Escribe en una celda o rango de celdas en la Hoja de Cálculo seleccionada

6. Leer celdas  
Lee una celda o rango de celdas desde la Hoja de Cálculo seleccionada, ejemplo A1 o A1:B5

7. Obtener hojas  
Obtener lista de hojas con su ID de la Hoja de Cálculo seleccionada

8. Contar filas  
Cuenta las filas de la hoja seleccionada

9. Agregar columna  
Agregar columnas a la Hoja de Cálculo seleccionada

10. Agregar fila  
Agregar filas a la Hoja de Cálculo seleccionada

11. Eliminar columna  
Elimina una columna de una Hoja de Cálculo seleccionada

12. Eliminar fila  
Elimina una fila de una Hoja de Cálculo seleccionada

13. Filtrar datos  
Filtrar datos en la Hoja de Cálculo seleccionada

14. Desfiltrar datos  
Desfiltrar datos en la Hoja de Cálculo seleccionada

15. Obtener celdas filtradas  
Obtiene las celdas filtradas  




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