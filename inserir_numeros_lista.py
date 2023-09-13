print("\n\033[1;31m{:=^60} \033[m \n".format(" Insira valores em uma lista "))

valores = []

while True:
    num = int(input("Digite um número: "))
    while num in valores:
        num = int(input("Valor inválido. Digite outro: "))
    valores.append(num)
    continuar = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Opção inválida. Deseja continuar [S/N]? ")).strip().upper()[0]
    if continuar == "N":
        break

print(f"\nVocê digitou {len(valores)} números. Os números digitados foram: {sorted(valores)}")
