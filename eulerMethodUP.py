"""
--- MÉTODO DE EULER PARA RESOLVER EDO's INGRESADAS POR TECLADO --- 

Este archivo es para resolver EDO's ingresadas por teclado por el usuario.
Implemento las mismas librerías, funciones y la misma forma de trabajar 
que en el archivo "eulerMethod.py". La mayoría de explicaciones están en 
ese archivo.
"""
from eulerMethod import eulerMethod, generarTabla, graficarSol, calcularErrores
import sympy as sp

# Ingresar la EDO por teclado
print("Introducir la EDO sin espacios y con los operadores aritméticos de Python")
edo_str = input("Introduce una EDO de la forma dy/dx = f(x,y) = ").strip()

x, y = sp.symbols("x y")

try:
    edo = sp.sympify(edo_str)
    ed = sp.Eq(sp.diff(y, x), edo)
except sp.SympifyError:
    print("Error: La entrada no es una expresión válida.")
    exit()

# Convertir la ecuación en una función
funcion = sp.lambdify((x, y), edo)

# Ingresar la condición inicial y(x0) = y0
print("Ingresa la condición inicial de la forma y(x0) = y0")
x0 = float(input("x0 = "))
y0 = float(input("y0 = "))

# Ingresar el paso h y la x final
print("Ingresa el paso h y la x donde quieres evaluar por Euler")
h = float(input("h = "))
xFinal = float(input("xFinal = "))
iteraciones = (xFinal-x0)/h

# Resuelvo
data = eulerMethod(funcion, x0, y0, iteraciones, h)
generarTabla(data, ejercicio="")

# Resuelvo la EDO exacta con sympy
solucion_general = sp.dsolve(ed)
condicion_inicial = {y.subs(x, x0): y0}
solucion_particular = sp.dsolve(ed, ics=condicion_inicial)
print(solucion_particular)

#graficarSol(0,data,x0,xFinal)
#calcularErrores(data,)