import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Examen Analisis')
    root.iconbitmap('logo.ico')
    root.resizable(0,0)

    frame = tk.Frame(root)
    frame.pack()
    frame.config(width= 580, height= 420, bg = '#46b2cf')

    Titulo = tk.Label(frame, text= 'Examen II Parcial')
    Titulo.config(font= ('Arial', 16, 'bold'), bg = '#46b2cf')
    Titulo.grid(row=0, column=2, padx=10, pady=10)

    # Mostrar listas

    # Llenar el arreglo A y B de acuerdo como se muestra en la figura.
    array_a = [100, 200, 300, 400, 500, 600, 700, 800, 1200, 3000]
    array_b= [500, 430, 450, 360, 2000, 50, 100, 250, 100, 500]

    lista = tk.Label(frame, text= 'Campos')
    lista.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    lista.grid(row= 2, column= 0, padx= 10, pady= 10)

    lista = tk.Label(frame, text= 'Resultados')
    lista.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    lista.grid(row= 2, column= 1, padx= 10, pady= 10)

    lista = tk.Label(frame, text= 'Campos')
    lista.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    lista.grid(row= 2, column= 3, padx= 10, pady= 10)

    lista = tk.Label(frame, text= 'Resultados')
    lista.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    lista.grid(row= 2, column= 4, padx= 10, pady= 10)

    arrayA = tk.Label(frame, text= 'Lista A:')
    arrayA.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    arrayA.grid(row= 3, column= 0, padx= 10, pady= 10)

    arrayAL = tk.Label(frame, text= array_a)
    arrayAL.config(font= ('Arial', 12), width= 36, anchor= 'w')
    arrayAL.grid(row= 3, column= 1, padx= 10, pady= 10)

    arrayB = tk.Label(frame, text= 'Lista B:')
    arrayB.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    arrayB.grid(row= 4, column= 0, padx= 10, pady= 10)

    arrayBL = tk.Label(frame, text= array_b)
    arrayBL.config(font= ('Arial', 12), width= 36, anchor= 'w')
    arrayBL.grid(row= 4, column= 1, padx= 10, pady= 10)

    arrayC = tk.Label(frame, text= 'Lista sumada:')
    arrayC.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    arrayC.grid(row= 5, column= 0, padx= 10, pady= 10)

    # Crear un arreglo que contenga la suma de cada uno de los valores de los arreglos A y B.
    array_c = [a + b for a, b in zip(array_a, array_b)]

    arrayCL = tk.Label(frame, text= array_c)
    arrayCL.config(font= ('Arial', 12), width= 36, anchor= 'w')
    arrayCL.grid(row= 5, column= 1, padx= 10, pady= 10)

    # Valor mayor

    # Del arreglo resultante de la suma de ambos arreglos A y B, mostrar el valor mayor.
    max_value = max(array_c) 

    max_valu = tk.Label(frame, text= 'Valor mayor:')
    max_valu.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    max_valu.grid(row= 6, column= 0, padx= 10, pady= 10)

    max_valul = tk.Label(frame, text= f'El valor maximo es: {max_value}')
    max_valul.config(font= ('Arial', 12), width= 36, anchor= 'w')
    max_valul.grid(row= 6, column= 1, padx= 10, pady= 10)

    # Valor menor

    # Del arreglo resultante de la suma de ambos arreglos A y B, mostrar el valor menor.
    min_value = min(array_c)

    max_valu = tk.Label(frame, text= 'Valor menor:')
    max_valu.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    max_valu.grid(row= 7, column= 0, padx= 10, pady= 10)

    max_valul = tk.Label(frame, text= f'El valor minimo es: {min_value}')
    max_valul.config(font= ('Arial', 12), width=36, anchor= 'w')
    max_valul.grid(row= 7, column= 1, padx= 10, pady= 10)

    # Del arreglo resultante de la suma de ambos arreglos A y B, mostrar encontrar mediante interpolación el valor de 650.
    def interp_value(array_c, search_value):
        low = 0
        high = len(array_c) - 1

        while low <= high and search_value >= array_c[low] and search_value <= array_c[high]:
            if low == high:
                if array_c[low] == search_value:
                    return low
                return -1

            pos = low + round(((high - low) / (array_c[high] - array_c[low])) * (search_value - array_c[low]))

            if array_c[pos] == search_value:
                return pos

            if array_c[pos] < search_value:
                low = pos + 1
            else:
                high = pos - 1

        return -1

    search_value = 650
    array_c.sort() 
    index = interp_value(array_c, search_value)

    sortB = tk.Label(frame, text= 'Interpolación:')
    sortB.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    sortB.grid(row= 3, column= 3, padx= 10, pady= 10)

    if index != -1:
        sortindex = tk.Label(frame, text= f'La posicion donde se encuentra 650 es: {index}')
        sortindex.config(font= ('Arial', 12), width=36, anchor= 'w')
        sortindex.grid(row= 3, column= 4, padx= 10, pady= 10)
    else:
        sortBR = tk.Label(frame, text= 'El valor 650 no se encontro')
        sortBR.config(font= ('Arial', 12), bg = '#46b2cf')
        sortBR.grid(row= 3, column= 4, padx= 10, pady= 10)

    # Del arreglo resultante de la suma de ambos arreglos A y B, mostrar el valor SUMA.
    suma_c = sum(array_c)

    sumal = tk.Label(frame, text= 'Valor SUMA:')
    sumal.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    sumal.grid(row= 4, column= 3, padx= 10, pady= 10)

    sumaR = tk.Label(frame, text= f'El valor SUMA es: {suma_c}')
    sumaR.config(font= ('Arial', 12), width=36, anchor= 'w')
    sumaR.grid(row= 4, column= 4, padx= 10, pady= 10)

    # Mediante búsqueda binaria encuentre el elemento 790

    sumal = tk.Label(frame, text= 'Binario 790:')
    sumal.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    sumal.grid(row= 5, column= 3, padx= 10, pady= 10)

    def binary_search(array_c, search_value):
        start = 0
        end = len(array_c) - 1
        while start <= end:
            middle = (start + end) // 2
            if array_c[middle] < search_value:
                start = middle + 1
            elif array_c[middle] > search_value:
                end = middle - 1
            else:
                return middle
        return None
    
    search_value = 790
    index2 = binary_search(array_c, search_value)

    if index2 is not None:

        binari = tk.Label(frame, text= f'Índice del valor 790 en el arreglo_c: {index2}')
        binari.config(font= ('Arial', 12), width=36, anchor= 'w')
        binari.grid(row= 5, column= 4, padx= 10, pady= 10)
    else:

        binarin = tk.Label(frame, text= 'El valor 790 no se encuentra en el arreglo_c')
        binarin.config(font= ('Arial', 12), width=36, anchor= 'w')
        binarin.grid(row= 5, column= 4, padx= 10, pady= 10)


    """
    Dado el siguiente arreglo ordenado de enteros: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], busca el 
    índice del elemento 23 utilizando el algoritmo de búsqueda binaria. Describe los pasos que 
    seguirías y en qué iteraciones se dividiría el arreglo hasta encontrar el elemento.
    """

    bina23 = tk.Label(frame, text= 'Binario 23:')
    bina23.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    bina23.grid(row= 6, column= 3, padx= 10, pady= 10)

    def binary_search(array, search_value):
        low = 0
        high = len(array) - 1
        mid = 0

        while low <= high:
            
            mid = (high + low) // 2

            # Bucando el elemento en medio
            if array[mid] < search_value:
                low = mid + 1

            elif array[mid] > search_value:
                high = mid - 1

            else:
                return mid

        # Si no encontramos el elemento
        return -1

    array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    search_value = 23
    result = binary_search(array, search_value)

    if result != -1:

        binar23 = tk.Label(frame, text= f'El elemento está en el índice: {result}')
        binar23.config(font= ('Arial', 12), width=36, anchor= 'w')
        binar23.grid(row= 6, column= 4, padx= 10, pady= 10)
    else:
        binar23 = tk.Label(frame, text= 'El elemento no se encuentra en el arreglo')
        binar23.config(font= ('Arial', 12), width=36, anchor= 'w')
        binar23.grid(row= 6, column= 4, padx= 10, pady= 10)

    """
    Escribe una función recursiva llamada suma_recursiva que tome como entrada un número 
    entero positivo n y calcule la suma de todos los números enteros positivos desde 1 hasta n. Por 
    ejemplo, si n es 5, la función debe devolver 15 (1 + 2 + 3 + 4 + 5).
    """
    def suma_recursiva(n):
        if n == 1:
            return 1
        else:
            return n + suma_recursiva(n-1)

    def click():
        valor = val.get()
        nun = int(valor)
        recu = tk.Label(frame, text= f'La suma de todos los elementos es: {suma_recursiva(nun)}')
        recu.config(font= ('Arial', 12), width=36, anchor= 'w')
        recu.grid(row= 8, column= 1, padx= 10, pady= 10)
    
    resul = tk.Label(frame, text= 'Ingresar valor:')
    resul.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    resul.grid(row= 9, column= 0, padx= 10, pady= 10)
    
    cal = tk.Button(frame, text= 'Calcular', command= click)
    cal.grid(row= 9, column= 2, padx= 10, pady= 10)
    val = tk.Entry(frame)
    val.config(font= ('Arial', 12), width= 36)
    val.grid(row= 9, column= 1, padx= 10, pady= 10)

    recul = tk.Label(frame, text= 'Suma Recursiva:')
    recul.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    recul.grid(row= 8, column= 0, padx= 10, pady= 10)

    """
    Escribe una función recursiva llamada mult_recursiva que tome como entrada un número 
    entero positivo n y calcule la multiplicacion de todos los números enteros positivos 
    desde 1 hasta n. Por ejemplo, si n es 5, la función debe devolver 15 (1 * 2 * 3 * 4 * 5)
    """
    def mult_recursiva(n):

        if n == 1:
            return 1
        else: 
            return n * mult_recursiva(n-1)

    def click():
        valor2 = val.get()
        nun2 = int(valor2)
        recu2 = tk.Label(frame, text= f'La mult de todos los elementos es: {mult_recursiva(nun2)}')
        recu2.config(font= ('Arial', 12), width=36, anchor= 'w')
        recu2.grid(row= 7, column= 4, padx= 10, pady= 10)
    
    resul2 = tk.Label(frame, text= 'Ingresar valor:')
    resul2.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    resul2.grid(row= 8, column= 3, padx= 10, pady= 10) # 15
    
    cal2 = tk.Button(frame, text= 'Calcular', command= click)
    cal2.grid(row= 9, column= 4, padx= 10, pady= 10)
    val2 = tk.Entry(frame)
    val2.config(font= ('Arial', 12), width= 36)
    val2.grid(row= 8, column= 4, padx= 10, pady= 10)

    recul = tk.Label(frame, text= 'Mult Recursiva:')
    recul.config(font= ('Arial', 12, 'bold'), bg = '#46b2cf')
    recul.grid(row= 7, column= 3, padx= 10, pady= 10)


    root.mainloop()

if __name__ == '__main__':
    main()
