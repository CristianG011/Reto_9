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