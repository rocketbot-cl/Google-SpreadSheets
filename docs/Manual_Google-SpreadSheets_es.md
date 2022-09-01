



# Google SpreadSheet
  
Módulo para manejar Google SpreadSheet desde Rocketbot  
  
![banner](imgs/Banner_Google-SpreadSheets.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  

## Como usar este modulo

Antes de usar este modulo, es necesario registrar tu aplicación en el portal de Google Cloud. Registration

1. Ingresar con una cuenta de google al siguiente link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Completar el formulario y luego presionar Crear
3. Dentro del Menu de Navegación (Izquierdo), ingresar en API y Servicios
4. En la sección superior, ingresar a "+ HABILITAR API Y SERVICIOS"
5. Buscar "Google Sheets API", seleccionar y por ultimo habilitar
6. Nuevamente dirigirse a Menu de Navegación (Izquierdo) > API y Servicios > Credenciales
7. Presionas Crear Credenciales > ID de cliente de OAuth, seleccionar como Tipo de Aplicación: App de Escritorio, colocar un nombre y crear.
8. Descargar el achivo JSON de credenciales.
9. Por ultimo dirigirse a Menu de Navegación (Izquierdo) > Pantalla de Consentimiento y agregar usuario dentro de la seccion "Usuarios de prueba"


## Descripción de los comandos

### Configurar credenciales G-Suite
  
Obtiene los permisos para manejar Google SpreadSheet con Rocketbot
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta||C:/ruta/a/credenciales.json|

### Crear Hoja de Cálculo
  
Crea una nueva hoja de cálculo en Google SpreadSheet
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la hoja de cálculo||Nombre|
|Variable donde se guardará el ID||Variable|

### Crear Hoja
  
Crear una nueva hoja en la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Nombre|

### Borrar Hoja
  
Elimina una hoja de la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja a borrar||Nombre de la hoja|

### Escribir en celdas
  
Escribe en una celda o rango de celdas en la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Celda a escribir ||A1|
|Texto ||[["data","data"],["data","data"]]|

### Leer celdas
  
Lee una celda o rango de celdas desde la Hoja de Cálculo seleccionada, ejemplo A1 o A1:B5
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Celda o rango de celdas ||A1|
|Resultado||Variable|

### Obtener hojas
  
Obtener lista de hojas con su ID de la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Resultado||Variable|

### Contar filas
  
Cuenta las filas de la hoja seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Resultado||Variable|

### Agregar columna
  
Agregar columnas a la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Columna||A|
|Cantidad||Cantidad|
|Mantener formato|||

### Agregar fila
  
Agregar filas a la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Fila||5|
|Cantidad||Cantidad|
|Mantener formato|||

### Eliminar columna
  
Elimina una columna de una Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Columna||A|
|Dejar en blanco|||

### Eliminar fila
  
Elimina una fila de una Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Fila||5-7|
|Dejar en blanco|||

### Filtrar datos
  
Filtrar datos en la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|
|Columna||Columna|
|Valor||Valor a filtrar|

### Desfiltrar datos
  
Desfiltrar datos en la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja|

### Obtener celdas filtradas
  
Obtiene las celdas filtradas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja:|
|Rango||A1:B2|
|Resultado||Variable|