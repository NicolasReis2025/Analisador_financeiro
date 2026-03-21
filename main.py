import csv

def exportar_csv(dicionario, total_gasto, nome_arquivo):

    # Função para exportar arquivos do dicionário para formato csv

    try:
        with open(nome_arquivo, mode="w", newline='', encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(['Categoria', 'Valor (R$)', 'Impacto (%)'])
            for categoria, valor in dicionario.items():
                porcentagem = (valor * 100) / total_gasto
                escritor.writerow([categoria.title(), f"{valor:.2f}", f"{porcentagem:.1f}%"])
            
            escritor.writerow([])
            escritor.writerow(['TOTAL GERAL', f"{total_gasto:.2f}", '100%'])
        print(f"\n✅ Relatório salvo com sucesso como: {nome_arquivo}")
    
    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")


def mostrar_despesas(dicionario, total_gasto):

    # Função para mostrar o nome e os gastos das despesas
 
    print("\n==== Exibição do relatório ====")
    for keys, values in dicionario.items():
        porcentagem = (values * 100) / total_gasto
        print(f"{keys.title()} | custo: R${values} | impacto: {porcentagem:.1f}%")

def verificar_saude_financeira(gastos, limite):

    # Função para verificar se os gastos ultrapassam a renda mensal

    if gastos > limite:
        print("O total de despesas ultrapassou o limite da sua renda mensal!")
        print("Encerrando o programa...")
        return True 
    else:
        return False 

def excluir_despesa(dicionario, nome_despesa):

    # Função para excluir despesa

    if nome_despesa in dicionario:
        del dicionario[nome_despesa]
        print(f"\n'{nome_despesa}' excluida com sucesso")
    else:
        print(f"\n'{nome_despesa}' não está cadastrada no sistema ")


print("\n====== ANALISADOR DE FINANÇAS ======= \n")
despesas = {}

renda_mensal = float(input("Insira sua renda mensal: "))
tot = 0.0

while True:
    print(
        "\n[1] Adicionar despesa" 
        "\n[2] Deletar despesa" 
        "\n[3] Sair e mostrar relatório"
    )
    try:
        while True:
            opcao = int(input("Digite uma opção: "))
            if opcao not in [1, 2, 3]:
                print("❌Opção inválida. Tente novamente!")
            else:
                break
        
        if opcao == 3:
            while True:
                if despesas:
                    try:
                        resp = str(input("Deseja exportar o relatório para CSV? (S - sim / N = não)  ")).lower().strip()
                        
                        if resp in ['s', 'sim']:
                            nome_arquivo = str(input("Digite o nome para criar o arquivo: "))
                            if not nome_arquivo.endswith(".csv"):
                                nome_arquivo += ".csv"
                            exportar_csv(despesas, tot, nome_arquivo)
                            break
                        
                        elif resp in ['n', 'não', 'nao']:
                            break
                        
                        else:
                            print("❌ Opção inválida. Digite S ou N.")
                    
                    except Exception:
                        print("❌ERRO: A opção precisa ser uma letra entre 's' ou 'n'. Tente novamente!")
                break  
            break

        else:
            if opcao == 1:
                nome_despesa = str(input("Digite o nome da despesa: ")).title()
                custo = float(input(f"Custo da despesa: "))
                if custo > 0:
                    tot += custo
                    despesas[nome_despesa] = round(custo, 2)
                else:
                    print("O custo da despesa precisa ser um numero válido e positivo. Tente novamente!")

                if verificar_saude_financeira(tot, renda_mensal):
                    break
            
            if opcao == 2:
                nome_despesa = str(input("Digite o nome da despesa para excluir: ")).title()
                excluir_despesa(despesas, nome_despesa)

         
    except ValueError:
        print("❌ERRO: A opção precisa ser um numero entre (1 ~ 2). Tente novamente!")


if despesas:
    total = sum(despesas.values())
    maior_despesa = max(despesas.items(), key=lambda x: x[1])
    menor_despesa = min(despesas.items(), key=lambda x: x[1])
    media_categoria = total / len(despesas)

    mostrar_despesas(despesas, total)

    if total <= renda_mensal:
        print("\n📊 RESUMO ESTATÍSTICO: ")
        print(f"Total da despesa mensal:\tR${total:.2f}")
        print(f"Maior despesa:\t{maior_despesa[0].title()} | R${maior_despesa[1]:.2f}")
        print(f"Menor despesa:\t{menor_despesa[0].title()} | R${menor_despesa[1]:.2f}")
        print(f"Média de custo por categoria:\tR${media_categoria:.2f}")

    valor_economizado = renda_mensal - total
    if valor_economizado > 0:
        print("\n📈 DICA DE INVESTIMENTOS: ")
        montante = valor_economizado * (((1 + 0.008)**12 - 1) / 0.008)
        print(f"O valor economizado no mês foi de R${valor_economizado:.2f}")
        print(f"Esse valor aplicado em um investimento de 0.8% a.m, em 1 ano retornaria um total de R${montante:.2f} tendo um lucro líquido de R${montante - (valor_economizado * 12):.2f}")

else:
    print("\nNenhum dado foi inserido no sistema!")

