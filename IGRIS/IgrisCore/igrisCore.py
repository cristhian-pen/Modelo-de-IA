import os
from IgrisLearn import getAnswer, searchQuestionDB

#variavel de controle do loop de interação do igris
keyword = True

#loop de interação do igris
while keyword == True:

    os.system('cls')
    print('Bem Vindo ao Igris meu assistente Pessoal!')
    print('Digite 1 para sair do console \n \n')
    new_question = str(input('Digite uma pergunta para o Igris: '))
    print('Resposta \n \n')
    answer = searchQuestionDB(new_question)

    if not answer:
        print('Não encontrei sua resposta aqui no banco, vou buscar na internet e aprender...')
    else:
        trueAnswers = getAnswer(new_question)
        print(trueAnswers)
        input('\n \n \n Pressione uma tecla para perguntar novamente...')

