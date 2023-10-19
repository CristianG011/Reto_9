# Reto_9
# Punto 1
1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
Primero
```python
#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
if __name__ == "__main__":
  c = int(input("Ingrese número de contagiados actuales :"))
  d = int(input("Ingrese número de días trasncurridos :"))
  avance = lambda c, d: c * 2 ** (d-1)
  contagiados = avance(c, d)
  if d < 0:
    print(f"Por favor ponga valores positivos")
  else:
    print(f"La cantiad de personas contagiadas al día {d} son {contagiados} personas ")
```
Segundo
```
if __name__ == "__main__":
    c = float(input("Ingrese el dinero a deudar :"))
    i = float(input("Ingrese el interes sin % :"))
    n = float(input("Ingrese la cantidad de años :"))
    interes = lambda c, n, i: (c * ((1+i)**n-1)) + c
    deuda = interes(c, n, i)
    
    print(f"su deuda total es {deuda}.")
```
Tercero
```
if __name__ == "__main__":
    p = float(input("Ingrese la cantidad de panes :"))
    m = float(input("Ingrese la cantidad de leche :"))
    h = float(input("Ingrese la cantidad de huevos :"))
    b = float(input("¿Cuánto dinero les vas a dar a Manuel:"))
    precio = lambda p, m , h ,b: p * 300 + m * 3300 + h * 350
    vueltas = b - precio(p, m, h, b)
    if vueltas < 0:
        vueltas = vueltas * -1
        print(f"No le alcanzó a Manuel, ahora debe {vueltas} pesos")
    else:
        print(f"Las vueltas de Manuel son {vueltas} pesos")
```
# Punto 2
2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
Primero
```
def p(*args):
    for num in args:
        x = num ** 2
        return x
if __name__ == "__main__":
    a = int(input("Ingrese numero a: "))
    x = p(a)
    print(f"El cuadrado del número {a} es {x}")
```
Segundo
```
def precio(*args):
    c = (p * 300) + (m * 3300) + (h * 350)
    vueltas = b - c
    return vueltas
if __name__ == "__main__":
    p = float(input("Ingrese la cantidad de panes :"))
    m = float(input("Ingrese la cantidad de leche :"))
    h = float(input("Ingrese la cantidad de huevos :"))
    b = float(input("¿Cuánto dinero les vas a dar a Manuel:"))
    vueltas = precio(p, m, h)
    if vueltas < 0:
            vueltas = vueltas * -1
            print(f"No le alcanzó a Manuel, ahora debe {vueltas} pesos")
    else:
        print(f"Las vueltas de Manuel son {vueltas} pesos")
    
```
Tercero
```
def p(x : int , y : float):
    if y == 0:
        return 1
    else:
        potencia = x * p(x, y - 1)
        return potencia
if __name__ == "__main__":
  x = int(input("Ingrese la potencia : "))
  y = float(input("Ingrese la base : "))
  p = p(x, y)
  print(f"La pontencia de {x} a {y} es igual a {p}.")
```
# Punto 3
Escriba una función recursiva para calcular la operación de la potencia.
```
def covid(*args):
    cov = c * 2 ** (d-1)
    return cov
if __name__ == "__main__":
  c = int(input("Ingrese número de contagiados actuales :"))
  d = int(input("Ingrese número de días trasncurridos :"))
  cov = covid(c, d)
if d < 0:
    print(f"Por favor ponga valores positivos")
else:
    print(f"La cantiad de personas contagiadas al día {d} son {cov} personas ")  
```
# Punto 4
#Punto 5
![](https://i.ibb.co/F7R56GJ/SAIODAS123.jpg)
#Punto 6
![](https://i.ibb.co/MM0NmgR/Captura2.jpg)

