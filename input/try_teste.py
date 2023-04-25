while True:
    nome_usuario=input('Qual é o seu nome? ')
    if all(c.isalpha() for c in nome_usuario):
     print(nome_usuario, ('seja bem vindo!'))
     break
    else:
        print('Você não digitou um nome valido, digite apenas letras!')
        