condicao = True
while condicao == True:
    try:
        nome = input('Qual o nome do arquivo? ')
        arquivo = open('../../Pictures/' + str(nome) + '.txt', 'x')
        texto = input('O que você quer escrever? ')
        arquivo.write(texto)
        arquivo.close()
        condicao = False
        break
    except IOError:
        print('Este arquivo já existe, Deseja sobrescrever o arquivo? ')
        resposta = input('(S)im ou (N)ão? ')
        if resposta == 'N':
            arquivo = open('../../Pictures/' + str(nome) + '.txt', 'a')
            texto = input('O que você quer escrever? ')
            arquivo.write('\n' + texto)
            arquivo.close()
            condicao = False
            break
        else:
            arquivo = open('../../Pictures/' + str(nome) + '.txt', 'w')
            texto = input('O que você quer escrever? ')
            arquivo.write('\n' + texto)
            arquivo.close()
            condicao = False
            break