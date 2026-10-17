# Simulador de Aprovação de Crédito Corporativo - ArkeTech

# 1. Solicitar os dados de entrada ao utilizador
renda_mensal = float(input("Introduza a renda mensal da empresa parceira: "))
valor_emprestimo = float(input("Introduza o valor do empréstimo solicitado: "))

# 2. Aplicação das três regras lógicas (if, elif, else)
if valor_emprestimo <= renda_mensal * 3:
    status = "APROVADO"
elif valor_emprestimo <= renda_mensal * 5:
    status = "EM ANÁLISE"
else:
    status = "RECUSADO"

# 3. Exibição do status final alinhado
print("\n" + "=" * 40)
print(f"{'STATUS DO CRÉDITO:':<25} {status:>12}")
print("=" * 40)