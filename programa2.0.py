#menu de texto no python
import random
import math
print('='*30)
nome = input('Qual seu nome?\n').title().strip().split()
ind = int(input('Qual sua idade?'))
def print_menu():
    print('-'*10,'olá {} em que posso te ajudar?'.format(nome[0]),'-'*10)
    print('1 - Calulos matematicos?')
    print('2 - Jogar um jogo?')
    print('3 - Opção 3 do Menu')
    print('4 - Opção 4 do Menu')
    print('5 - fechar o programa. ')
    print('-')
loop=True
Opção = 0

while loop:
    print_menu()
    Opção = int(input("Digite uma opção: "))

    if Opção == 1:#matemetica
        def print_ajuda():
            print('1 - media')
            print("2 - media especifica")
            print("3 - soma, subitração, mutiplicação, divisião. Entre dos numeros.")
            print('4 - Sair')


        aju = True
        opçãomat = 0

        while aju:
            print_ajuda()
            opçãomat = int(input("escolha uma opção: "))
            if opçãomat == 1:#Media
                conti = ''
                nu = 0
                cont = 0
                while conti != 'sim' and conti != 's':
                    nu += int(input("Digite um numero para a media dos numeros: "))
                    conti = str(input("só?")).lower()
                    cont += 1
                print('A media dos numeros é {:.2f}'.format(nu / cont))
            elif opçãomat == 2:#media especifica
                conti = ''
                nu = 0
                cont = int(input("A media vai ser entre quantos?"))
                while conti != 'sim' and conti != 's':
                    nu += int(input("Digite um numero para a media dos numeros: "))
                    conti = str(input("só?")).lower()
                print('='*40)
                print('A media dos numeros é {:.2f}'.format(nu / cont))
                print('='*40)

            elif opçãomat == 3:#opecacoes basicas
                print('-' * 40)
                n = int(input('Digito 1: '))
                n2 = int(input('Digito 2: '))
                s = n + n2
                subi = n - n2
                mut = n * n2
                div = n / n2
                print('A soma de {}+{} é: {}'.format(n, n2, s))
                print('A subitração de {}-{} é: {}'.format(n, n2, subi))
                print('A multiplicação de {}x{} é: {}'.format(n, n2, mut))
                print('A divisão de {}/{} é: {:.3f}'.format(n, n2, div))
                print('-' * 40)

            elif opçãomat == 4:#sair
                aju = False

            else:
                print('nada')

    elif Opção == 2:#jogo
        print('=' * 30)
        con1 = 0
        con0 = 0
        if ind > 18:
            t1 = str(input(('Olá {}, você quer jogar um jogo?\n'.format(nome[0])))).lower()
            if t1 == 'sim' or t1 == 's':
                con1 = 0
                con0 = 0
                n = random.randint(0, 4)
                print('-' * 40)
                print('Vou escolher um numero de 1 a 4\nVocê tem que adivinhar qual foi esse numero.')
                print('-' * 40)
                con = ''
                while con != 'sim' and con != 's':
                    con = str(input('você entendeu? ')).lower()
                num = int(input('Qual o numero que to pensando? '))
                if num == n:
                    con1 += 1
                    print('voce acertou, parabens {}'.format(nome[0]))
                else:
                    con0 += 1
                    print('voce errou')
            else:
                print('Não queria mesmo,kkkk')
        else:
            print('você não pode jogar, vovê é menor de idade!')

        if con0 == 1 or con1 == 1:
            print('ok')
            nov = str(input('Quer jogar novamente?')).lower()
            while 'sim' and 's' in nov:
                n2 = random.randint(0, 4)
                print('-' * 40)
                t2 = int(input('Eai {}, Qual numero estou pensando agora?'.format(nome[0])))
                if t2 == n2:
                    print('Você acertou, {}'.format(nome[0]))
                    con1 += 1
                else:
                    print('Você errou')
                    con0 += 1
                nov = str(input('eai, jogar novamente?')).lower()

        print()
        print('=' * 30)
        print('{}, Obrigado por jogar o jogo do Marlon Coelho!\nAté a proxima ;)'.format(nome[0]))
        print('=' * 40)
        print('Estastiticas:\nVocê acertou {} vezes e você errou {} vezes'.format(con1, con0))
        print('=' * 40)

    elif Opção == 3:
        print('A opcçao 3 do menu foi selencionada')
    elif Opção == 4:
        print('A opcçao 4 do menu foi selencionada')
    elif Opção == 5:
        print('Até a proxima')
        loop=False
    else:
       Opção=int(input("seleção de opção errada"))
