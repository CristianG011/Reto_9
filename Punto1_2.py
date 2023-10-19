if __name__ == "__main__":
    c = float(input("Ingrese el dinero a deudar :"))
    i = float(input("Ingrese el interes sin % :"))
    n = float(input("Ingrese la cantidad de años :"))
    interes = lambda c, n, i: (c * ((1+i)**n-1)) + c
    deuda = interes(c, n, i)
    

    print(f"su deuda total es {deuda}.")