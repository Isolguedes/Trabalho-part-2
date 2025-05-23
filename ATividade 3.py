def main():

    saldo = float(input("DIGITE O SALDO DISPONIVEL NA SUA CONTA: "))
    print(f"SALDO DISPONIVEL EM REAIS: R$ {saldo} ")
    while True:
          saque = float(input("DIGITE O VALOR DESEJADO PARA O SAQUE"))
          if saque > saldo:
                print("Valor de saque maior que o saldo disponivel, tente novamente...")
          else














if __name__=="__main__":
        main()