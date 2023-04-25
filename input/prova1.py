#Qual o time paulista do mês
while True:
   nome=(input('Qual é o seu nome? '))
   print('Olá,' , nome, 'seja bem vindo!!')
   time=input('Qual é o seu time paulista favorito? ')
   print('Será', nome, 'que o', time, 'virá em algum mês?! Boa Sorte!')
   mes=input('Qual é o seu mês favorito: ')
   if all(c.isalpha() for c in mes):
      print('Realmente o mês de', mes, 'foi uma boa escolha, agora iremos trazer uma breve descrição desse time do mês de', mes, 'e um breve resumo desse time.')
   if mes=='Janeiro':
      print('São paulo, é um time fundado na cidade de são paulo, atualmente é dirigido pelo técnino Rogério Ceni, seu uniforme principal é Branco, com duas listas, sendo Vermelho e Preto na horizontal')
   elif mes=='Fevereiro':
      print(' Santos, é um time da baixada santista, tendo como maior ídolo o Rei Pelé, atualmente é dirigido pelo técnino Aldair, seu uniforme principal é branco, faz um tempo que está sem ganhar um título')
   elif mes=='Março':
      print(' São bento é um time com novas perspectiva no cenário paulista, no ano 2023, o time chegou na semi final paulista')
   elif mes=='Abril':
      print(' Santo André é um time do ABC paulista, onde no começo dos anos 2000 teve suas maiores conquistas')
   elif mes=='Maio':
      print(' São caetano é um time que fez muito sucesso nos anos 2000, onde já fez final de libertadores, sendo derrotado pelo Olimpia do Paraguay')
   elif mes=='Junho':
      print(' Red Bull Bragantino, antes conhecido como Bragança Paulista, onde teve o aporte da empresa Red Bull, tornando-se um time mais forte no cenário paulista e Brasileiro')
   elif mes=='Julho':
      print(' Ituano é um time da cidade de Itú, o uniforme é preto e vermelho')
   elif mes=='Agosto':
      print(nome, 'o Corinthians é o maior time paulista, tendo a segunda maior torcida do Brasil, atualmente o treinador é o Lazaro, seus títulos de maiores representatividade é a libertadores e o mundial de 2012')
   elif mes=='Setembro':
      print('Palmeiras', nome, ' essa não foi uma boa escolha, mas fazer o que?, atualmente o Palemiras é um dos times mais vencedores do Brasil, o Palmeiras é o atual campeão paulista.')
   elif mes=='Outubro':
      print(nome, ' ' 'o time para você esse mes de ', mes, ' é a Ferroviária, o time não performou muito bem no campeonato paulista de 2023')
   elif mes=='Novembro':
      print(nome, ' Cara você fez uma boa escolha, o time esse mês é o Água Santa, o time foi finalista no paulista 2023, porém foi derrotado pelo Palmeiras por 4x0.')
   elif mes=='Dezembro':
      print(nome,'; Não acredito, o Botafogo de ribeirão preto foi selecionado no mês de', mes,', você sabia que o jogador Socrates é um dos ídolos do time de ribeirão?! Então', nome, ' você teve muita sorte.')
      break
   else:
      print(nome, 'você não digitou o mês correto', nome, ' acho que você torce para o Vasco, hahahahaha')