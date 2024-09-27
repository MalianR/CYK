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

**Complejidad del Algoritmo CYK - O(n³)**

**Paso 1: Estructura de la tabla**
El algoritmo utiliza una tabla de tamaño n x n (donde n es la longitud de la cadena de entrada) para almacenar los posibles símbolos no terminales que pueden derivar una subcadena de la cadena de entrada.

Para una cadena de longitud n, la tabla tiene n filas y n columnas.
Cada celda de la tabla table[i][j] almacena un conjunto de no terminales que pueden derivar la subcadena que va desde la posición i hasta j de la cadena de entrada.
**Paso 2: Llenado de la tabla - Primer ciclo**
El llenado de la tabla ocurre en dos fases principales:

Producciones unitarias (de longitud 1):
Para cada símbolo de la cadena, se verifican las reglas de la gramática que pueden generar ese símbolo.
Esto requiere verificar todas las producciones de la gramática para cada símbolo de la cadena, lo que toma un tiempo O(n) para recorrer la cadena y O(r) para verificar las producciones, donde r es el número de reglas en la gramática.
Dado que r es constante para una gramática fija, la primera fase tiene complejidad O(n).

**Paso 3: Llenado de la tabla - Segundo ciclo**
Producciones binarias (de longitud mayor a 1):
Para cada subcadena de la cadena de entrada (con longitud mayor que 1), el algoritmo intenta encontrar producciones binarias que dividan la subcadena en dos partes.
Se itera sobre todas las posibles longitudes de subcadenas, desde 2 hasta n. Para una subcadena de longitud k, se consideran todas las posibles particiones (puntos medios) que dividen la subcadena en dos partes.
**Paso 4: Análisis de la complejidad cúbica**
El algoritmo tiene tres ciclos principales que contribuyen a la complejidad:

Longitud de la subcadena (de 2 a n):

El primer ciclo recorre todas las posibles longitudes de las subcadenas desde 2 hasta n. Esto se realiza en O(n).
Posición inicial de la subcadena:

Para cada longitud de subcadena, se consideran todas las posibles posiciones de inicio en la cadena, lo cual toma O(n) iteraciones.
Punto medio de la subcadena:

Para cada subcadena, el algoritmo intenta dividirla en dos partes, considerando todos los puntos medios posibles. Esto también requiere O(n) iteraciones.
Cada ciclo anidado depende linealmente de n, lo que resulta en una complejidad de O(n) x O(n) x O(n) = O(n³).

**Paso 5: Ejemplo de recorrido de la tabla**
Para una cadena de longitud n = 4, el llenado de la tabla se realizaría como sigue:

Para subcadenas de longitud 2, se consideran todas las divisiones posibles de subcadenas de longitud 2, 3, 4, etc.
El número de subcadenas que deben ser procesadas es proporcional a n².
Para cada subcadena, el algoritmo debe intentar todas las combinaciones posibles de dos subcadenas más pequeñas, lo que introduce otro factor n, resultando en O(n³).
