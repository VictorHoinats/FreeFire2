# Iniciando Variáveis
Prox_Cliente = 1
Contador_Clientes = 0
Lista_Clientes = [1]
Lista_Espera = [1]

# Mostra o Menu de Opções na tela

while True:
    
    print("\nMenu de Opções:")
    print("A - Atender próximo cliente")
    print("B - Ver número de clientes na Lista de espera")
    print("C - Ver número total de clientes atendidos")
    
    # Escolha A, B ou C para qual opção você vai querer
    
    opcao = input("Escolha uma opção (A, B, C): ").upper()
    
    if opcao == 'A':
        
        if Lista_Espera:
            proximo_cliente = Lista_Espera.pop(0)
            print(f"Atendendo o cliente {proximo_cliente}")
            Contador_Clientes += 1
        else:
            print("Não tem clientes para serem atendidos")
    
    elif opcao == 'B':
        
        print(f"Número de clientes na Lista de Espera: {len(Lista_Espera)}")
    
    elif opcao == 'C':
        
        print(f"Número total de clientes atendidos: {Contador_Clientes}")
    
    else:
        print("Opção inválida. Por favor, escolha A, B ou C.")
        
    # Pergunta se você quer continuar o código
    
    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar != 'S':
        break

print("Fim do programa")