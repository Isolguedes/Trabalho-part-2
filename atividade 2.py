def main():
    quant = int(input("Digite a quantidade de produtos que você deseja comprar: "))
    lista = [ ]
    for i in range (quant):
        produtos = input(f"Digite o nome do produto desejado {i+1}: ")
        lista.append([produtos])

        lista.sort(key=lambda x: x[0].lower())

    print("\nLISTA DE COMPRAS COMPLETA:")
    for sublista in lista:
        print(sublista[0])
    print(f"\nQUANTIDADE DE ITENS DA LISTA: {len(lista)}")


if __name__=="__main__":
   main()