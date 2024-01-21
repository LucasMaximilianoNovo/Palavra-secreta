palavra_secreta = 'cachorro'
acertos = ''
tentativa = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    tentativa += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        acertos += letra_digitada

    palavra_formada = ''  
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in acertos:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        print('Parabéns você acertou!!')
        print('A palavra era', palavra_secreta)
        print('Você acertou em:', tentativa)
        
        acertos = ''
        tentativa = 0      
