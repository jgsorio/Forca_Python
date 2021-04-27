import random


# Inicio do game, pedindo o nome do usuário
nome = input('Digite seu nome: ')
print(f'Bem vindo {nome}')
print('____________________')


def esconder_palavra(word, typed_letters):
    word_accept = ''
    for letter in word:
        if letter in typed_letters:
            word_accept += letter
        else:
            word_accept += '_'

    if verify_if_won(word, word_accept):
        print('Parabéns Você Ganhou!!!')
        print(f'A palavra escondida é {word_accept}')
        exit()
    else:
        return word_accept


def verify_if_won(word, word_typed):
    return word == word_typed


def draw_doll(tentativas):
    if tentativas == 9:
        print('-----------')
        print('     0     ')
    if tentativas == 8:
        print('-----------')
        print('     0/    ')
    if tentativas == 7:
        print('-----------')
        print('   \\0/    ')
    if tentativas == 6:
        print('-----------')
        print('   \\0/    ')
        print('    |      ')
    if tentativas == 5:
        print('----------')
        print('   \\0/   ')
        print('    |     ')
        print('   /      ')
    if tentativas == 4:
        print('----------')
        print('   \\0/   ')
        print('    |     ')
        print('   / \\   ')
    if tentativas == 3:
        print('----------')
        print('   \\0|/  ')
        print('    |     ')
        print('   / \\   ')
    if tentativas == 2:
        print('----------')
        print('   \\0_|/ ')
        print('    |     ')
        print('   / \\   ')
    if tentativas == 1:
        print('Essa é a sua última chance, está quase sufocando')
        print('----------')
        print('   \\0_|/ ')
        print('    |     ')
        print('   / \\   ')
    if tentativas == 0:
        print('Que pena, você perdeu!!!')
        print('----------')
        print('    0_|   ')
        print('  /  \\   ')
        print('    |     ')
        print('   / \\   ')
        pergunta = input('Gostaria de jogar novamente? Digite s ou n')
        if pergunta.lower() == 's':
            game()
        else:
            print('Obrigado por jogar!')
            exit()


def game():
    # Tentativas
    tentativas = 10
    print(f'Tente advinhar a palavra em menos de {tentativas} tentativas')
    # Sorteia uma palavra
    palavra = random.choice(['casamento', 'cerimonia', 'padre', 'igreja',
                             'convidados', 'comida', 'banda', 'danca', 'musica'])
    print('A palavra é: ', esconder_palavra(palavra, []))
    letras_digitadas = []
    while tentativas > 0:
        letra_digitada = input('Digite uma letra: ')
        # Verifica se a letra digitada está contida na palavra sorteada
        if letra_digitada in palavra:
            letras_digitadas.append(letra_digitada)
            print(esconder_palavra(palavra, letras_digitadas))

        else:
            tentativas -= 1
            print(f'Restam {tentativas} tentativas')
            draw_doll(tentativas)


game()
