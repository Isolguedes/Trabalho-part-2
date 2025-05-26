def main():
    pessoas = []
 
    while True:
        nome = input("Digite o seu nome: ").strip()
        while True:
            idadeinput = input("Digite a sua idade: ").strip()
            if idadeinput.isdigit(): 
                idade = int(idadeinput)
                break
            else:
             print("IDADE INVÁLIDA, DIGITE APENAS NUMÉROS INTEIROS!")

        pessoas.append([nome, idade])

        cont = input("VOCÊ DESEJA CONTINUAR? (S/N): ").strip().upper()
        while cont not in ['S', 'N']:
            cont = input("OPÇÃO INVÁLIDA, DIGITE APENAS 'S' OU 'N': ")
        if cont == 'N':
         break

    total = len(pessoas)
    soma = sum(p[1] for p in pessoas)
    media = soma / total if total > 0 else 0
    mvelho = max(pessoas, key=lambda p: p[1])

    print("\nRESULTADOS FINAIS:")
    print(f"Total de pessoas cadastradas: {total}")
    print(f"Média de idades cadastradas: {media}")
    print(f"A pessoa mais velha é: {mvelho}")



if __name__=="__main__":
   main()