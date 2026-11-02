
from colorama import Fore, Style, init

init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para definir a cor
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

# Exibição do menu
print("===== CONTROLE DE NÍVEIS DE ÁGUA =====")

print("\nEscolha o nível do reservatório:")
for i in range(len(niveis)):
    print(f"{i + 1} - {niveis[i]}")

# Entrada do usuário
escolha = int(input("\nDigite o nível desejado (1 a 5): "))

# Verificação e exibição
if escolha >= 1 and escolha <= 5:
    cor = definir_cor(escolha)

    print("\n===== SITUAÇÃO DO RESERVATÓRIO =====")
    print(cor + f"Nível {escolha} - {niveis[escolha - 1]}" + Style.RESET_ALL)
else:
    print(Fore.RED + "Nível inválido! Escolha um número de 1 a 5.")

print("\nMonitoramento finalizado.")

