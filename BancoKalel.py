print('=' * 30)
print('{:^30}'.format('Banco Kalel'))
print('=' * 30)

menu = ''''
[d] Depositar
[s] Sacar
[e] Extrato
[f] Sair
=> '''

saldo = (0)
limite = (1000)
extrato = ('')
numero_saques = (0)
LIMITE_SAQUES = (3)

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('informe o valor do deposito: R$ '))
        if valor > 0:
            saldo = saldo + valor
            extrato += f'Deposito R$ {valor:.2f}\n'
            print('=' * 30) 
            print(f'voce realizou um deposito de R$ {valor:.2f}')
            
        else:
            print('Operação falhou tente novamente')    
            print('=' * 30)
        
    elif opcao == 's':
        valor = float(input('informe o valor de saque: R$ '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
                
        if excedeu_saldo:
            print('Operação falhou você não tem saldo')
        elif excedeu_limite:
            print('operação falhou, o valor excede seu limite de saque diario')
        elif excedeu_saque:
            print('Operação falhou, consulte seu saldo')
        elif valor > 0:
            saldo -= valor
            extrato += f'saque R$ {valor:.2f}\n'
            numero_saques += 1
            
        else:
            print('Operação falhou! o valor informado é invalido.')
    
    elif opcao == "e":
        print('=' * 12, 'EXTRATO', '=' * 12)
        print('Não foram realidadas movimentaçoes.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=' * 30)
            
    if opcao == 'f':
        print('='*30)
        print('Obrigado por usar nossos serviços! Volte sempre')
        print('='*30)
        break