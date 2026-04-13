# Contadores
qtde_excelente = 0
qtde_ruim = 0

for i in range(1, 51):
    print("\nEntrevistado número:", i)
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    opiniao = int(input("Qual a sua opinião sobre nós? (Sendo: 1=EXCELENTE, 2=BOM, 3=RUIM): "))

    # Estrutura de decisão
    if opiniao == 1:
        qtde_excelente += 1
    elif opiniao == 3:
        qtde_ruim += 1

# Resultado final
print("\nRESULTADO DA PESQUISA")
print("Quantidade de avaliações EXCELENTES:", qtde_excelente, "🤩")
print("Quantidade de avaliações RUINS:", qtde_ruim, "🙁")