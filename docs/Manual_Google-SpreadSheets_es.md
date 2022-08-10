



# Google SpreadSheet
  
Módulo para manejar Google SpreadSheet desde Rocketbot  
  
<!-- ![banner]() -->

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  



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
  
Crear una nueva hoja en la Hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Nombre|

### Borrar Hoja
  
Elimina una hoja de la Hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja a borrar||Nombre de la hoja|

### Escribir en celdas
  
Escribe en una celda o rango de celdas desde una hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Ingrese la celda a escribir ||A1|
|Ingrese texto ||[["data","data"],["data","data"]]|

### Leer celdas
  
Lee celdas o rango de celdas desde una hoja de cálculo seleccionada, ejemplo A1 o A1:B5
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Ingrese celda o rango de celdas ||A1|
|Resultado||Variable|

### Obtener hojas
  
Obtener lista de hojas con su id desde una hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Resultado||Variable|

### Contar filas
  
Cuenta las filas de una hoja seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Resultado||Variable|

### Agregar columna
  
Agrega una columna desde una hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Columna||A|
|Cantidad||Cantidad|
|Mantener formato|||

### Agregar fila
  
Agregar una fila desde una hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Fila||5|
|Cantidad||Cantidad|
|Mantener formato|||

### Eliminar columna
  
Elimina una columna desde una hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Columna||A|
|Dejar en blanco|||

### Eliminar fila
  
Elimina una fila desde una hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Fila||5-7|
|Dejar en blanco|||

### Filtrar datos
  
Filtra datos en una hoja de cáclulo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|
|Ingrese la columna||Columna|
|Ingrese el valor||Valor a filtrar|

### Desfiltrar datos
  
Desfiltra datos en una hoja de cáclulo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja|

### Obtener celdas filtrdas
  
Obtiene las celdas filtradas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ingrese Spreadsheet ID||Spreadsheet ID|
|Ingrese nombre de la hoja||Hoja:|
|Rango||A1:B2|
|Resultado||Variable|
