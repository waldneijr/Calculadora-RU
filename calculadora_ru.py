# Armazena os dois últimos números do RU em variáveis
n1 = 5
n2 = 6
# Cria uma variável para fazer o loop com while funcionar
selecionar = '0'

# Cria a classe "Calculadora"
class Calculadora:
    # Cria um menu com o loop para o usuário selecionar a operação matemática a ser feita com os números do RU
    while selecionar != '7':
        selecionar = input("Por favor, digite o número da operação matemática que você deseja realizar entre os números 5 e 6: \n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n5. Exponenciação\n6. Módulo\n7. Sair da calculadora\n")
        # Se o usuário digitar "1", os números do RU são somados e o resultado é mostrado na tela
        if selecionar == '1':
            soma = n1 + n2
            print(f'O resultado da soma dos números é {soma}')
        # Se o usuário digitar "2", os números do RU são subtraídos e o resultado é mostrado na tela
        elif selecionar == '2':
            subtracao = n1 - n2
            print(f'O resultado da subtração dos números é {subtracao}')
        # Se o usuário digitar "3", os números do RU são multiplicados e o resultado é mostrado na tela
        elif selecionar == '3':
            multiplicacao = n1 * n2
            print(f'O resultado da multiplicação dos números é {multiplicacao}')
        # Se o usuário digitar "4", o penúltimo número do RU é dividido pelo último e o resultado é mostrado na tela
        elif selecionar == '4':
            divisao = n1 / n2
            print(f'O resultado divisão dos números é {divisao:.2f}')
        # Se o usuário digitar "5", o penúltimo número do RU é elevado ao último e o resultado é mostrado na tela
        elif selecionar == '5':
            exponenciacao = n1 ** n2
            print(f'O resultado do primeiro número elevado ao segundo é {exponenciacao}')
        # Se o usuário digitar "6", o penúltimo número do RU é dividido pelo último e o resto da divisão é mostrado na tela
        elif selecionar == '6':
            modulo = n1 % n2
            print(f'O resto da divisão entre os operandos é {modulo}')
        # Se o usuário digitar "7", o programa encerra
        elif selecionar == '7':
            print('Encerrando a calculadora...')
        # Se o usuário digitar algo que não entra em nenhuma das condições, o loop se repete
        else:
            print('Opção inválida, tente novamente')

# É chamada a classe "Calculadora"
Calculadora()