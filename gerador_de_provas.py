import random
prova = ''
tema1=('Tema1Questão1','Tema1Questão2','Tema1Questão3','Tema1Questão4','Tema1Questão5')
tema2=('Tema2Questão1','Tema2Questão2','Tema2Questão3','Tema2Questão4','Tema2Questão5')
tema3=('Tema3Questão1','Tema3Questão2','Tema3Questão3','Tema3Questão4','Tema3Questão5')
tema4=('Tema4Questão1','Tema4Questão2','Tema4Questão3','Tema4Questão4','Tema4Questão5')
tema5=('Tema5Questão1','Tema5Questão2','Tema5Questão3','Tema5Questão4','Tema5Questão5')
temas = (tema1,tema2,tema3,tema4,tema5)

print(f'Bem vindo(a)! você possuí {len(tema1+tema2+tema3+tema4+tema5)}  questões no seu banco de dados!')
quantidade = int(input('Escolha a quantidade total de questões que você deseja colocar na sua prova: '))
while quantidade > len(tema1+tema2+tema3+tema4+tema5):
    print(f'Seu banco de dados possuí no máximo  {len(tema1+tema2+tema3+tema4+tema5)} questões, por favor, selecione um valor entre 1 e {len(tema1+tema2+tema3+tema4+tema5)} ')
    quantidade = int(input('Escolha a quantidade total de questões que você deseja colocar na sua prova: '))
for c in range(0,quantidade):
    questaoselecionada = random.choice(temas[random.randint(0,4)])
    while questaoselecionada in prova:
        questaoselecionada = random.choice(temas[random.randint(0, 4)])

    prova += f'Questão {c+1}) ' + questaoselecionada + '\n'

print(prova)
