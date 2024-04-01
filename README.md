# Método de Euler para resolver EDO's en Python 🐍

Trabajo realizado para Análisis Matemático II - UTN FRSR.

### Profesores:
- Daniela Armijo
- Alejandro Javier Gonzalez

### Datos del alumno:
- Nombre y apellido: Valentino Araya.
- Legajo: 9938 
- Ingeniería en Sistemas de la información.
- Segundo año - 2024

## Explicación de cada archivo:
### eulerMethod.py
En este archivo resuelvo los problemas "hardcodeando" los datos y las ecuaciones diferenciales.

Utilizo las librerías math y numpy para números y cálculos matemáticos, la librería matplotlib es para graficar las soluciones, y la librería tkinter es para la creación de la tabla con los datos del método de Euler.

Utilicé ayuda de IA para guiarme y poder implementar estas funciones, la IA me guió pero tuve que adaptar bastante el código para poder implementar las funciones correctamente.

Las funciones "generarTabla()" y "graficarSol()" son funciones cuyo código interno puede ser ignorado ya que no se pide en el trabajo, pero considero que con ellas es más cómodo ver las soluciones.

Ambos ejercicios de este archivo fueron verificados manualmente en lápiz y papel, también con ayuda de algunos softwares y las respuestas que dá el programa son bastante acertadas. 

Recomendación: Antes de ejecutar el código leer bien los comentarios de los archivos, las funciones están comentadas para que no se superpongan, los comentarios indican cuáles deben descomentarse.

¡IMPORTANTE! -> COMENTAR LAS FUNCIONES (generarTabla, graficarSol, calcularErrores) DE AMBOS EJERCICIOS ANTES DE EJECUTAR EL ARCHIVO "eulerMethodUP.py".

### eulerMethodUP.py
En este archivo permito al usuario ingresar la EDO mediante teclado, por eso añado al nombre las siglas UP (User Prompt).

Gracias a la librería sympy es posible ingresar la EDO como un string y luego convertirla a una ecuación operable.

El usuario puede ingresar la EDO, la condición inicial, el paso, y el punto donde quiere evaluar la solución aproximadamente. No pude hacer que sympy encuentre una solución a la EDO ingresada, me tiraba un error al intentar resolverla, por lo que no pude implementar el cálculo de errores ni la gráfica de ambas soluciones (aproximada y exacta), investigué bastante pero no encontré nada que me resuelva el error, de igual manera voy a seguir probando.

En este archivo no hay funciones desactivadas (comentadas) por lo que se puede ejecutar directamente.

No estoy seguro de si el código puede aproximarnos a las soluciones de todas las EDO's, fueron probadas las dos EDO's del trabajo práctico y algunas más, y los resultados fueron correctos. La implementación de que el usuario pudiera ingresar la EDO resultó bastante desafiante.

## Para clonar el repositorio y utilizar el código:

1. Abra un terminar y diríjase a el directorio donde quiera clonar.

2. Ejecute el siguiente comando:

```
git clone https://github.com/valentinoaraya/Euler-method 
```
### Gracias por su atención ❤️🧉👨🏻‍💻
