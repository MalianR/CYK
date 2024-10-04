import time
import matplotlib.pyplot as plt

def leer_gramatica_y_cadena(archivo_gramatica, archivo_cadena):
    gramatica_unitaria = []
    gramatica_binaria = []
    
    with open(archivo_gramatica, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if linea:
                partes = linea.split('->')
                lhs = partes[0].strip()
                rhs = partes[1].strip()
                
                if len(rhs) == 1:
                    gramatica_unitaria.append((lhs, rhs))
                elif len(rhs) == 2:
                    gramatica_binaria.append((lhs, rhs))

    cadenas = []
    with open(archivo_cadena, 'r') as file:
        for linea in file:
            cadena = linea.strip()
            if cadena:
                cadenas.append(cadena)

    return gramatica_unitaria, gramatica_binaria, cadenas


def cyk_algorithm(gramatica_unitaria, gramatica_binaria, string):
    n = len(string)
    table = [[set() for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for lhs, rhs in gramatica_unitaria:
            if rhs == string[i]:
                table[i][i].add(lhs)

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            for mid in range(start, end):
                for lhs, rhs in gramatica_binaria:
                    if rhs[0] in table[start][mid] and rhs[1] in table[mid + 1][end]:
                        table[start][end].add(lhs)

    return 'S' in table[0][n - 1]


def main():
    archivo_gramatica = r'C:\Users\jrinc\Desktop\Leng de prog y trans\CYK\gramatica.txt'
    archivo_cadena = r'C:\Users\jrinc\Desktop\Leng de prog y trans\CYK\cadenas.txt'

    gramatica_unitaria, gramatica_binaria, cadenas = leer_gramatica_y_cadena(archivo_gramatica, archivo_cadena)

    longitudes = []
    tiempos = []

    for i, cadena in enumerate(cadenas, 1):
        longitud = len(cadena)
        longitudes.append(longitud)

        inicio = time.time()
        cyk_algorithm(gramatica_unitaria, gramatica_binaria, cadena)
        fin = time.time()
        
        tiempo = fin - inicio
        tiempos.append(tiempo)
        print(f"Línea {i}: Longitud de la cadena = {longitud}, Tiempo de ejecución = {tiempo:.6f} segundos")
    
    # Graficar longitud de cadena vs tiempo de ejecución solo con puntos
    plt.plot(longitudes, tiempos, 'o', label='Tiempo de ejecución')
    plt.xlabel('Longitud de la cadena (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Complejidad temporal del algoritmo CYK: O(n^3)')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
