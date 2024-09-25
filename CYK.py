def leer_gramatica_y_cadena(archivo_gramatica, archivo_cadena):
    # Leer la gramática desde el archivo
    gramatica = []
    # Abrir el archivo que contiene la gramática en modo lectura
    with open(archivo_gramatica, 'r') as file:
        # Leer cada línea del archivo
        for linea in file:
            # Eliminar espacios en blanco al principio y al final de la línea
            linea = linea.strip()
            # Si la línea no está vacía
            if linea:
                # Dividir la línea en partes usando '->' como delimitador
                partes = linea.split('->')
                # La parte izquierda (LHS) de la producción
                lhs = partes[0].strip()
                # La parte derecha (RHS) de la producción
                rhs = partes[1].strip()
                # Agregar la producción a la lista de gramática
                gramatica.append((lhs, rhs))

    # Leer la cadena desde el archivo
    cadenas = []
    # Abrir el archivo que contiene las cadenas en modo lectura
    with open(archivo_cadena, 'r') as file:
        # Leer cada línea del archivo
        for linea in file:
            # Eliminar espacios en blanco al principio y al final de la línea
            cadena = linea.strip()
            # Si la línea no está vacía
            if cadena:
                # Agregar la cadena a la lista de cadenas
                cadenas.append(cadena)

    # Devolver la gramática y las cadenas leídas
    return gramatica, cadenas


def cyk_algorithm(grammar, string):
    # Obtener la longitud de la cadena
    n = len(string)
    # Obtener el número de producciones en la gramática
    r = len(grammar)
    
    # Crear una tabla de tamaño n x n (inicialmente vacía)
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    # Llenar la tabla para las producciones unitarias (de longitud 1)
    for i in range(n):
        for lhs, rhs in grammar:
            # Si la producción es igual al símbolo en la posición i de la cadena
            if rhs == string[i]:
                # Agregar el símbolo no terminal LHS a la tabla en la posición correspondiente
                table[i][i].add(lhs)
    
    # Llenar la tabla para las producciones no unitarias (de longitud > 1)
    for length in range(2, n + 1):  # Longitud de la subcadena
        for start in range(n - length + 1):  # Posición de inicio de la subcadena
            end = start + length - 1  # Posición de fin de la subcadena
            for mid in range(start, end):  # Posición de división de la subcadena
                for lhs, rhs in grammar:
                    # Si la producción tiene longitud 2 y ambas partes están en las posiciones correspondientes
                    if len(rhs) == 2 and rhs[0] in table[start][mid] and rhs[1] in table[mid + 1][end]:
                        # Agregar el símbolo no terminal LHS a la tabla en la posición correspondiente
                        table[start][end].add(lhs)
    
    # Verificar si el símbolo inicial 'S' está en la tabla para la cadena completa
    return 'S' in table[0][n - 1]


# Función principal para leer archivos y ejecutar el algoritmo CYK
def main():
    # Rutas a los archivos de gramática y cadenas
    #Importante: Al clonar este repositorio se debe cambiar 
    archivo_gramatica = r'C:\Users\jrinc\Desktop\Leng de prog y trans\gramatica.txt'
    archivo_cadena = r'C:\Users\jrinc\Desktop\Leng de prog y trans\cadenas.txt'

    # Leer la gramática y las cadenas desde los archivos
    gramatica, cadenas = leer_gramatica_y_cadena(archivo_gramatica, archivo_cadena)

    # Para cada cadena en la lista de cadenas
    for i, cadena in enumerate(cadenas, 1):
        # Ejecutar el algoritmo CYK para la cadena actual
        resultado = cyk_algorithm(gramatica, cadena)
        # Imprimir si la cadena es aceptada o no
        if resultado:
            print(f"Línea {i}: '{cadena}' Es aceptada.")
        else:
            print(f"Línea {i}: '{cadena}' NO es aceptada.")


if __name__ == '__main__':
    # Ejecutar la función principal si el script se ejecuta directamente
    main()
