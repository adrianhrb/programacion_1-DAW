# LISTAS, TUPLAS, DICCIONARIOS...

Apuntes sobre el tema 3 de Python.  

## ***LISTAS:***  

- Las listas permiten almacenar objetos en un orden y permitiendo la mutabilidad (modificarlas y que mantengan el mismo lugar en memoria)  

### *Creación de listas:*
- Para crear una lista en Python utilizaremos los corchetes. 'fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]'  

### *Conversión:*
- Si quisieramos convertir un tipo de dato en una lista usaríamos la función list(), por ejemplo: list('Python')  

- Otra forma de crear una lista es hacerla mediante rangos, de forma que podemos transformar un rango de números en una lista: list(range(10))  

### *Operando con listas:*  
- Si queremos obtener un elemento de una lista usaremos el índice, lugar en el que está lo que queramos. shopping[0] o shopping[2]. Si indicamos un índice que no está en la lista nos dara error.  

- Para trocear una lista seleccionaremos el rango (con índices) de lo que queramos: shopping[2:5] o shopping[-1:-4:-1]  

- Para invertir una lista, podemos hacerlo de dos formas:
    - shopping[::-1], es como indicar que vamos del principio al final dando saltos de -1 en -1 (es decir, saltos de 1 al contrario)  
    - list(reversed(shopping)), una posibilidad pero que no es óptima porque generamos un nuevo espacio en memoria  
    - shopping.reverse(), la mejor opción  

- Para añadir al final de la lista usamos: shopping.append('Atún')  

- Para añadir en cualquier posición de una lista: shopping.insert(1, 'Jamón'), indicando en primer lugar la posición de índice y en segundo lo que queremos insertar  

- Para repetir elementos, ocurre igual que con las cadenas de texto: shopping * 3

- Para combinar dos listas poodemos usar varias formas:
    - Si queremos mantener la lista original, usaremos el operador + o += : shopping + fruitshop  
    - Si queremos modificar la lista original usamos shopping.extend(fruitshop)
    - Si usamos el .append Python nos meterá una lista dentro de otra lista  

- Para modificar, usaremos los índices y lo que queramos poner, aplicable a rangos y a posiciones concretas: shopping[0] = 'Hola' o shopping [1:4] = ['Adiós', 'Hola']  

- Para borrar elementos podemos hacerlo mediante:
    - Por su índice con la función del() ---> del(shopping[3])  
    - Por su valor con la función remove() ---> shopping.remove('Atún')  
    - Además, Python ofrece una función para borra y mostrar o recuperar el elemento ---> shopping.pop(2)  
    - Por su rango mediante ---> shopping[1:4] = []  
    - Borrar la lista por completo usando la función .clear o asignandole el valor de lista vacía '[]'  
    