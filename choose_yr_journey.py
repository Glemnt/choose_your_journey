nome = input('Qual o seu nome exporador? ')
print(f'Olá {nome}, bem vindo a esta aventura!')

input('Precione Enter para começar ')

resposta = input(
    'Aparentemente você está perdido em uma estrada de terra e está completamente sozinho, depois de andar por um tempo a estrada chaga ao fim,\nvocê então olha para os lados e percebe que so lhe resta ir para esquerda ou para direita \nEntão você escolhe ir para a direita ou para a esquerda: ')
    
if resposta == 'esquerda':
    resposta = input('Você chegou até um rio, você pode atravessar nadando ou então andar em volta.\nEscreva nadar para entrar no rio e atravessar nadando ou escreva andar para dar a volta no rio andando. ').lower()                            
    
    if resposta == 'nadar':
        print('Você então entra no rio e começa a atravessa-lo nadando, porém um jacaré aparece e te come vivo. ')
    elif resposta == 'andar':
        print('Você anda por quilômetros e não encontra nada, fica então com muita sede e morre desidratado. ')
    else:
        print('Resposta inválida. Você perdeu.')
    
elif resposta == 'direita':
    resposta = input('Você chegou a uma ponte, ela parece bem instável, você quer atravessa-la ou passar pelas enormes pedras pontiagudas em baixo (atravessar/pedras)? ')

    if resposta == 'pedras':
        print('Você então começa a desbravar um caminho por baixo da ponte, porém oque você não imaginaria é que essas pedras estão todas instáveis, você então cai e é soterrado pelas pedras. ')
    elif resposta == 'atravessar':
        print('Você então começa a atravessar, a ponte parece que pode bambear e cair a qualquer momento porém você ainda sim continua e consegue chegar do outro lado.\nVocê então avista um estranho, deseja falar com ele? (sim/não) ')

        if resposta == 'sim':
            print('Você conversa com o estranho e ele fala que é um morador local da região podendo te ajudar a arrumar mantimentos e dinheiro, para que assim possa voltar para casa. ')
        elif resposta == 'não':
            print('Você então ignora o estranho, porém ele se sente ofendido e então mata você com uma facada. ')
        else:
            print('Resposta inválida. Você perdeu.')

    else:
        print('Resposta inválida. Você perdeu.')

else:
    print('Resposta inválida. Você perdeu.')

print('Obrigado pela aventura', nome)
