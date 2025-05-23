def main():
    saldo = float(input("DIGITE O SALDO DISPONIVEL NA SUA CONTA: "))
    print(f"SALDO DISPONIVEL EM REAIS: R$ {saldo} ")
    while True:
          saque = float(input("DIGITE O VALOR DESEJADO PARA O SAQUE: "))
          if saque > saldo:
            print("Valor de saque maior que o saldo disponivel, tente novamente...") 
          else:
           break
          
    notas = [100, 50, 20, 10, 5, 2]
    resultado = []
    restante = saque
    for nota in notas:
      qtd = restante //nota
      if qtd > 0:
          resultado.append([nota, qtd])
          restante -= nota * qtd
          print("\nNOTAS DISPONIVEIS PARA SAQUE:")
          for item in resultado:
              print(f"{item[1]} nota(s) de R$ {item[0]}")

if __name__=="__main__":
  main()
         