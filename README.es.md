



# Google SpreadSheet
  
Este módulo le permite leer, escribir y actualizar hojas de cálculo de Google. Puede agregar, eliminar, duplicar o incluso ocultar hojas; filtrar datos; agregar o eliminar filas y columnas; modificar el formato de las celdas, copiarlas/cortarlas y pegarlas; y más.  

  
*Read this in other languages: [English](Manual_Google SpreadSheet.md), [Português](Manual_Google SpreadSheet.pr.md), [Español](Manual_Google SpreadSheet.es.md)*  


## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

Antes de usar este módulo, debe registrar su aplicación en Google Cloud Portal.

1. Inicie sesión con una cuenta de Google y acceda al siguiente enlace: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete el formulario para crear un nuevo proyecto y luego presione "Crear".
3. Dentro del menú de navegación (izquierda), acceda a API y servicios.
4. Ve a la sección superior y presiona "+ HABILITAR API Y SERVICIOS".
5. Busque 
"Google Sheets API", selecciónelo y luego presione "HABILITAR".
6. Vuelva al menú de navegación, vaya a API y servicios y luego acceda a Credenciales.
7. Pulse Crear credenciales y seleccione ID de cliente de OAuth. Luego seleccione Tipo de aplicación: Aplicación de escritorio, asígnele un nombre y presione Crear.
8. Descargue el archivo JSON de credenciales.
9. Finalmente, vuelve al Menú de Navegación, ve a la Pantalla de Consentimiento y agrega tu usuario en la sección "Usuarios de prueba" 
(aunque sea el mismo que está creando la aplicación).

Nota: Cuando se realiza la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio con otra cuenta, debe asignar un nombre a cada sesión. Si las credenciales caducan, debe eliminar el archivo .pickle y crear y descargar un archivo de credenciales nwe (JSON).


## Overview


1. Configurar credenciales G-Suite  
Obtiene los permisos para manejar Google SpreadSheet con Rocketbot

2. Crear Hoja de Cálculo  
Crea una nueva hoja de cálculo en Google SpreadSheet

3. Crear Hoja  
Crear una nueva hoja en la Hoja de Cálculo seleccionada

4. Actualizar propiedades de Hoja  
Actualiza las propiedades de una hoja de la Hoja de Cálculo seleccionada

5. Borrar Hoja  
Elimina una hoja de la Hoja de Cálculo seleccionada

6. Escribir en celdas  
Escribe en una celda o rango de celdas en la Hoja de Cálculo seleccionada

7. Formatear celdas  
Cambiar formato de una celda o rango de celdas en la hoja de cálculo seleccionada

8. Leer celdas  
Lee una celda o rango de celdas desde la Hoja de Cálculo seleccionada, ejemplo A1 o A1:B5

9. Copiar/cortar y pegar  
Copie o corte y pegue una celda o rango de celdas en la Hoja de Cálculo seleccionada

10. Obtener hojas  
Obtener lista de hojas con su ID de la Hoja de Cálculo seleccionada

11. Contar filas y/o columnas  
Cuenta las filas y/o columnas utilizadas de la hoja seleccionada

12. Agregar columna  
Agregar columnas a la Hoja de Cálculo seleccionada

13. Agregar fila  
Agregar filas a la Hoja de Cálculo seleccionada

14. Eliminar columna  
Elimina una columna de una Hoja de Cálculo seleccionada

15. Eliminar fila  
Elimina una fila de una Hoja de Cálculo seleccionada

16. Filtrar datos  
Filtrar datos en la Hoja de Cálculo seleccionada

17. Desfiltrar datos  
Desfiltrar datos en la Hoja de Cálculo seleccionada

18. Obtener celdas filtradas  
Obtiene las celdas filtradas

19. Duplicar hoja  
Duplica la hoja seleccionada al mismo o a otro libro

20. Texto a columnas  
Divide una columna de texto en varias columnas, en función de un delimitador en cada celda.  




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