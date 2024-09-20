# CYK

Implementación del Algoritmo CYK
Este proyecto implementa el algoritmo de Cocke-Younger-Kasami (CYK) para el análisis de gramáticas libres de contexto. El algoritmo determina si una cadena dada puede ser generada por una gramática libre de contexto en Forma Normal de Chomsky.
Comenzando
Prerrequisitos

Python 3.x

Descarga del Proyecto
Para descargar este proyecto, sigue estos pasos:

Abre una terminal o línea de comandos.
Navega al directorio donde quieres clonar el proyecto.
Ejecuta el siguiente comando:
```bash
git clone https://github.com/MalianR/Ejercicio-en-clase.git
```

Cambia al directorio del proyecto:
```bash
Copycd Ejercicio-en-clase
```
Modificación de Rutas de Archivos
Antes de ejecutar el script, necesitas modificar las rutas de los archivos en el archivo CYK.py para que coincidan con la estructura de directorios de tu máquina local.

Abre el archivo CYK.py en un editor de texto.
Localiza las siguientes líneas (alrededor de las líneas 73-74):
```bash
pythonCopyarchivo_gramatica = r'C:\Users\jrinc\Desktop\Leng de prog y trans\gramatica.txt'
archivo_cadena = r'C:\Users\jrinc\Desktop\Leng de prog y trans\cadenas.txt'
```

Cambia estas rutas a las ubicaciones correctas de tus archivos gramatica.txt y cadenas.txt. Por ejemplo:
```bash
pythonCopyarchivo_gramatica = 'ruta/a/tu/gramatica.txt'
archivo_cadena = 'ruta/a/tu/cadenas.txt'
```
Asegúrate de usar barras inclinadas (/) o barras invertidas escapadas (\\) en las rutas.

Ejecución del Script
Después de modificar las rutas de los archivos, puedes ejecutar el script:

Abre una terminal o línea de comandos.
Navega al directorio del proyecto.
Ejecuta el siguiente comando:
```bash
python CYK.py
```

El script leerá la gramática desde gramatica.txt y las cadenas de entrada desde cadenas.txt, y luego mostrará si cada cadena es aceptada por la gramática o no.
Descripción de los Archivos

CYK.py: El script principal de Python que implementa el algoritmo CYK.
gramatica.txt: Contiene la gramática libre de contexto en Forma Normal de Chomsky.
cadenas.txt: Contiene las cadenas de entrada que se comprobarán contra la gramática.
