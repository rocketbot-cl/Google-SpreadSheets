# Google SpreadSheet
  
Módulo para utilizar Google SpreadSheets  
  
![banner](imgs/Banner_Google-SpreadSheets.png)
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
9. Por ultimo dirigirse a Menu de Navegación (Izquierdo) > Pantalla de Consentimiento y agregar usuario dentro de la seccion "Usuarios de prueba"

Nota: Cuando se realice la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio desde otra cuenta, debe eliminar
ese archivo Realice el mismo procedimiento para el caso en que caduquen las credenciales.


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

### Actualizar propiedades de Hoja
  
Actualiza las propiedades de una hoja de la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja a actualizar||Nombre de la hoja|
|Nuevo Nombre (Opcional)||Nuevo|
|Ocultar hoja||False|

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
|Nombre de la hoja||Hoja1|
|Celda a escribir ||A1|
|Texto ||[["data","data"],["data","data"]]|

### Formatear celdas
  
Cambiar formato de una celda o rango de celdas en la hoja de cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Celdas a formatear ||A1:C1|
|Combinar celdas|||
|Separar celdas|||
|Ajustar tamaño de columnas|||

### Leer celdas
  
Lee una celda o rango de celdas desde la Hoja de Cálculo seleccionada, ejemplo A1 o A1:B5
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Celda o rango de celdas ||A1|
|Resultado||Variable|

### Copiar/cortar y pegar
  
Copie o corte y pegue una celda o rango de celdas en la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja origen||Hoja1|
|Celdas origen ||A1:C1|
|Nombre de la hoja destino||Hoja2|
|Celdas destino ||A2:C2|
|Tipo de pegado||---- Select type ----|
|Transponer|||
|Cortar|||

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
|Nombre de la hoja||Hoja1|
|Resultado||Variable|

### Agregar columna
  
Agregar columnas a la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Columna||A|
|Cantidad||Cantidad|
|Mantener formato|||

### Agregar fila
  
Agregar filas a la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Fila||5|
|Cantidad||Cantidad|
|Mantener formato|||

### Eliminar columna
  
Elimina una columna de una Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Columna/as||A:C|
|Dejar en blanco|||

### Eliminar fila
  
Elimina una fila de una Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Fila||5:7|
|Dejar en blanco|||

### Filtrar datos
  
Filtrar datos en la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Columna||Columna|
|Valor||Valor a filtrar|

### Desfiltrar datos
  
Desfiltrar datos en la Hoja de Cálculo seleccionada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|

### Obtener celdas filtradas
  
Obtiene las celdas filtradas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Rango||A1:B2|
|Obtener datos con número de fila|||
|Resultado||Variable|

### Duplicar hoja
  
Duplica la hoja seleccionada al mismo o a otro libro
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Spreadsheet ID||Spreadsheet ID|
|Resultado||Variable|

### Texto a columnas
  
Divide una columna de texto en varias columnas, en función de un delimitador en cada celda.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Spreadsheet ID||Spreadsheet ID|
|Nombre de la hoja||Hoja1|
|Separador||---- Select separator ----|
|Resultado||Variable|
