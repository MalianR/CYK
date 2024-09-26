# CYK

**Realizado por**

- Andrés Sebastian Urrego Amaya

- Sebastián Cortés Briceño

- Mariana Ruge Vargas

- Julian Esteban Rincón Rodríguez


## Implementación del Algoritmo CYK

Este proyecto implementa el algoritmo de Cocke-Younger-Kasami (CYK) para el análisis de gramáticas libres de contexto. El algoritmo determina si una cadena dada puede ser generada por una gramática libre de contexto en Forma Normal de Chomsky.


**Requisitos**

- Python 3.x

En caso de no tenerlo, ejecuta en tu terminal

```bash
sudo apt install python
python --version
```


**Clonación en local**
Para descargar este proyecto, sigue estos pasos:

1. Abre una terminal o línea de comandos.
2. Navega al directorio donde quieres clonar el proyecto.
```bash
cd 'CYK'
```

3. Ejecuta el siguiente comando:
```bash
git clone https://github.com/MalianR/CYK.git
```

Cambia al directorio del proyecto:
```bash
cd CYK
```
Al clonar, deberías ver los siguientes archivos
- **CYK.py**: El script principal de Python que implementa el algoritmo CYK.
- **gramatica.txt**: Contiene la gramática libre de contexto en Forma Normal de Chomsky.
- **cadenas.txt:** Contiene las cadenas de entrada que se comprobarán contra la gramática.

**Modificación de Rutas de Archivos**

Antes de ejecutar el script, necesitas modificar las rutas de los archivos en el archivo CYK.py para que coincidan con la estructura de directorios de tu máquina local.

1. Abre el archivo CYK.py en un editor de texto.
Localiza las siguientes líneas (alrededor de las líneas 73-74):
```bash
archivo_gramatica = r'C:\Users\jrinc\Desktop\Leng de prog y trans\gramatica.txt'
archivo_cadena = r'C:\Users\jrinc\Desktop\Leng de prog y trans\cadenas.txt'
```

2. Cambia estas rutas a las ubicaciones correctas de tus archivos gramatica.txt y cadenas.txt. Por ejemplo:
```bash
archivo_gramatica = 'ruta/a/tu/gramatica.txt'
archivo_cadena = 'ruta/a/tu/cadenas.txt'
```
Asegúrate de usar barras inclinadas (/) o barras invertidas escapadas (\\) en las rutas.

**Ejecución del Script**
Después de modificar las rutas de los archivos, puedes ejecutar el script:

3. Abre una terminal o línea de comandos.
Navega al directorio del proyecto.
```bash
cd CYK
```
Ejecuta el siguiente comando:
```bash
python CYK.py
```

El script leerá la gramática desde gramatica.txt y las cadenas de entrada desde cadenas.txt, y luego mostrará si cada cadena es aceptada por la gramática o no.
