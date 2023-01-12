nome = input('Qual o seu nome exporador? ')
print(f'Olá {nome}, bem vindo a esta aventura!')

input('Precione Enter para começar ')

resposta = input(
    'Aparentemente você está perdido em uma estrada de terra e está completamente sozinho, depois de andar por um tempo a estrada chaga ao fim,\nvocê então olha para os lados e percebe que so lhe resta ir para esquerda ou para direita \nEntão você escolhe ir para a direita ou para a esquerda: ')
    
if resposta == 'esquerda':
    resposta = input('')                                    # *to do*
elif resposta == 'direita':
    print('')
else:
    print('Resposta inválida. Você perdeu.')
