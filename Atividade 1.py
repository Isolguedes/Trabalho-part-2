
def main():
    numeros = []
    for numero in range(2, 101):
        primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break
        if primo:
            numeros.append(numero)
    print("Numeros primos entre 1 e 100: ")
    for i in range(0, len(numeros), 5):
        linha = numeros[i:i+5]
        print("  ".join(f"{n:2}" for n in linha))
    print(f"Total de numeros primos encontrados: {len(numeros)}")


if __name__=="__main__":
   main()







