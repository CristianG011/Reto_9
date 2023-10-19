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