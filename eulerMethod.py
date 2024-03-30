"""
--- MÉTODO DE EULER PARA RESOLVER LOS PROBLEMAS DADOS EN EL TRABAJO --- 

Este archivo es para resolver los problemas "hardcodeados" del trabajo práctico,
en el archivo "eulerMethodUP.py" (Euler Method User Prompt) podremos ingresar la EDO,
el paso, la condición inicial, etc.

En este archivo genero una tabla con la librería tkinter para poder ver de mejor manera
los resultados y los valores que van tomando X e Y, también con la librería matplotlib
genero un gráfico de la solución exacta (calculada manualmente y luego escrita en código)
y un gráfico de la aproximación utilizando el método de Euler. El código escrito para poder
ejecutar estas dos acciones puede ser ignorado (funciones "generarTabla" y "graficarSol"), 
ya que es algo extra que agregué y no lo pide el trabajo. Me ayudé con ChatGPT para poder
implementar estas funciones y las adapté a mi código.

"""

# Importo funciones matemáticas
from math import ceil # -> Redondea para arriba
import numpy as np

# Importo Matplotlib para graficar
import matplotlib.pyplot as plt

# Importo tkinter para poder generar tablas
import tkinter as tk
from tkinter import ttk
        
# Generar Tabla (Opcional, lo adapté para ver mejor los resultados)
def generarTabla(matriz, ejercicio):
    
    # Crear Ventana
    root = tk.Tk()
    root.title(f"Ejercicio {ejercicio}")
    
    # Tamaño ventana
    root.geometry("600x400")
    
    # Estilos de la tabla
    style = ttk.Style()
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    style.map("Treeview", background=[("selected", "#347083")])
    
    # Definir encabezados
    tree = ttk.Treeview(root, columns=("Iteración", "X", "Y"), show="headings")
    tree.heading("Iteración", text="Iteración")
    tree.heading("X", text="X")
    tree.heading("Y", text="Y")
    tree.column("Iteración", width=100)
    tree.column("X", width=100)
    tree.column("Y", width=100)
    
    # Estilos
    tree.configure(displaycolumns="Iteración X Y", selectmode="browse")
    style.configure("Treeview.Heading", font=('Calibri', 10, 'bold'), foreground="blue")
    style.configure("Treeview", font=('Calibri', 10), rowheight=20)
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) # Remover el borde y el espacio adicional

    # Insertar datos en la tabla
    for fila in matriz:
        tree.insert("", tk.END, values=(fila[0],fila[1],fila[2]))

    # Posicionar el widget
    tree.pack(expand=True, fill="both")
    
    # Ejecutar
    root.mainloop()

# Graficar Solución exacta y Aproximación numérica con el método de Euler
def graficarSol(funcion, matrizDatos):

    # Definir los valores de x
    x = np.linspace(1, 1.5, 400)

    # Calcular los valores de y
    y = funcion(x)

    # Aproximación Numérica (con Euler)
    valoresX = []
    valoresY = []
    for fila in matrizDatos:
        valoresX.append(float(fila[1]))
        valoresY.append(fila[2])
    
    x_aproximaciones = np.array(valoresX)
    y_aproximaciones = np.array(valoresY)
    
    # Crear la gráfica
    plt.plot(x, y, label='Solución Analítica')
    plt.plot(x_aproximaciones, y_aproximaciones, color='red', linestyle="dashed", label='Aproximación Numérica')
    
    # Configurar títulos y etiquetas
    plt.title('Comparativa de Gráficas')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()  # Mostrar leyenda con etiquetas de los conjuntos de datos

    # Mostrar la gráfica
    plt.grid(True)
    plt.show()

# Método de Euler
def eulerMethod(ed, x0, y0, cantIteraciones, h):
    matrizDatos = [[" ",x0,y0]]
    for i in range(ceil(cantIteraciones)):
        x1 = x0 + h
        y1 = y0 + (h*ed(x0,y0))
        matrizDatos.append([i+1,"{:.3f}".format(x1),y1])
        x0 = x1
        y0 = y1
    return matrizDatos

# --- EJERCICIO 1 ---

# Ecuación Diferencial Ordinaria
def f(x,y):
    return 0.2*x*y

# Condición Inicial -> y(1) = 1
x0_ej1 = 1
y0_ej1 = 1

# Paso h, x final -> y(1.5)
h1 = 0.1
xFinal1 = 1.5
iteraciones1 = (xFinal1-x0_ej1)/h1

# Llamo al método de Euler y me devuelve una matriz con todos los datos
data = eulerMethod(ed=f, x0=x0_ej1, y0=y0_ej1, cantIteraciones=iteraciones1, h=h1)

# Generación de tabla
generarTabla(data, ejercicio="1")

# Solución Particular del problema (Calculada en hoja)
def y(x):
    return (np.e**(0.1*(x**2)))*(1/(np.e**0.1))

# Comparativa de gráficas
graficarSol(y,data)

# --- EJERCICIO 2 ---