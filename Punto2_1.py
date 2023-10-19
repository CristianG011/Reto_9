def p(*args):
    for num in args:
        x = num ** 2
        return x
if __name__ == "__main__":
    a = int(input("Ingrese numero a: "))
    x = p(a)
    print(f"El cuadrado del número {a} es {x}")