import csv

def exportar_csv(dicionario, total_gasto, nome_arquivo="relatorio_despesas.csv"):
    # exportar dados para formato de arquivo csv

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
    #Imprime o resumo das despesas e estatísticas financeiras.
    
    print("\n==== Exibição do relatório ====")
    for keys, values in dicionario.items():
        porcentagem = (values * 100 ) / total_gasto
        print(f"{keys.title()} | custo: R${values} | impacto: {porcentagem:.1f}%")

def verificar_saude_financeira(gastos, limite):
    # Verifica se as despesas estão acima da renda mensal

    if gastos > limite:
        print("⚠️O total de despesas ultrapassou o limite!")


print("💰Analisador de finanças \n")
despesas = {}

renda_mensal = float(input("Insira sua renda mensal: "))
tot = 0.0

while True:
    print(
        "\n[1] Adicionar despesa" 
        "\n[2] Sair e mostrar relatório"
    )
    try:
        while True:
            opcao = int(input("Digite uma opção: "))
            if opcao not in [1, 2]:
                print("❌Opção inválida. Tente novamente!")
            else:
                break

        if opcao == 2:
            while True:
                if despesas:
                    try:
                        resp = str(input("Deseja exportar o relatório para CSV? (S - sim / N = não)  ")).lower().strip()
                        
                        if resp in ['s', 'sim']:
                            exportar_csv(despesas, tot)
                            break
                        
                        elif resp in ['n', 'não', 'nao']:
                            break
                        
                        else:
                            print("❌ Opção inválida. Digite S ou N.")
                    
                    except Exception:
                        print("❌ERRO: A opção precisa ser uma letra entre 's' ou 'n'. Tente novamente!")
            break

        else:
            nome_despesa = str(input("Digite o nome da despesa: ")).title()
            custo = float(input(f"Custo da despesa: "))

            tot += custo
            if not verificar_saude_financeira(tot, renda_mensal):
                despesas[nome_despesa] = round(custo, 2)
                
    except ValueError:
        print("❌ERRO: A opção precisa ser um numero entre (1 ~ 2). Tente novamente!")



if despesas:
    total = sum([dados for dados in despesas.values()])
    maior_despesa= max(despesas.items(), key = lambda x:x[1])
    menor_despesa = min(despesas.items(), key = lambda x:x[1])
    media_categoria = total / len(despesas)

    mostrar_despesas(despesas, total)
    print("\n📊 RESUMO ESTATÍSTICO: ")
    print(f"Total da despesa mensal:\tR${total:.2f}")
    print(f"Maior despesa:\t{maior_despesa[0].title()} | R${maior_despesa[1]:.2f}")
    print(f"Menor despesa:\t{menor_despesa[0].title()} | R${menor_despesa[1]:.2f}")
    print(f"Média de custo por categoria:\tR${media_categoria:.2f}")

    valor_economizado = renda_mensal - total
    if valor_economizado > 0:
        print("\n📈 DICA DE INVESTIMENTOS: ")
        montante = valor_economizado * (((1 + 0.008)**12 - 1) / 0.008)
        print(f"O valor economizado no mês foi de R${valor_economizado}")
        print(f"Esse valor aplicado em um investimento de 0.8% a.m, em 1 ano retornaria um total de R${montante:.2f} tendo um lucro liquido de R${montante - (valor_economizado * 12):.2f}")

