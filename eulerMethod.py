# Ecuación Diferencial Ordinaria
def f(x,y):
    return 0.2*x*y

# Condición Inicial -> y(1) = 1
x0 = 1
y0 = 1

# Paso h y x final -> y(1.5)
h = 0.05
xFinal = 1.5
iteraciones = (xFinal-x0)/h

# Método de Euler
def eulerMethod():
    x0 = 1
    y0 = 1
    for i in range(int(iteraciones)):
        x1 = x0 + h
        y1 = y0 + (h*f(x0,y0))
        print(f"y({'{:.2f}'.format(x1)}) = {y1}")
        x0 = x1
        y0 = y1
        
eulerMethod()