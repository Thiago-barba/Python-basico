#Criando um sistema de notas, vai pegar as médias, vai fazer os calculos e printar na tela
primeira_Nota=float(input('Digite a nota da primeira avaliacao'))
segunda_Nota=float(input('Digite a nota da segunda avaliacao'))
terceira_Nota=float(input('Digite a nota da terceira avaliação'))
quarta_Nota=float(input('Digite a nota da quarta avaliaçã'))
media_Final=round((primeira_Nota+segunda_Nota+terceira_Nota+quarta_Nota)/4,2)
print('Sua média é:', media_Final)