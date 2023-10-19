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