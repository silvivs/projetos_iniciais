def menu():
    op = input('1 - calcular cota de pagamento\n2 - sair\n')
    return op

while True:

    op = menu()

    if op == '1':
        divida = float(input('Informe o valor a ser dividido: '))
        qtde_pag = int(input('Informe a quantidade de contribuintes: '))
        pagantes = []
        salarios = []
        taxas = []
        cotas = []

        while qtde_pag != 0:
            pagantes.append(input('Informe o nome dos contribuintes: '))
            qtde_pag -= 1

        for nome in pagantes:
            salarios.append(float(input('Informe o salário de {}: '.format(nome))))

        sum_sal = sum(salarios)

        for salario in salarios:
            taxas.append((salario * 100) / sum_sal)

        for taxa in taxas:
            cotas.append((taxa * divida) / 100)
        
        for i in range(len(pagantes)):
            print('{} deve pagar R${:.2f}'.format(pagantes[i], cotas[i]))

    elif op == '2':
        break

    else:
        print('Opção inválida!!')