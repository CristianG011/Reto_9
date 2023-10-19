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