#notas_jogadores
goleiro=float(input('Digite a nota do goleiro'))
if goleiro==8:
    print('Você está na média')
elif goleiro<7:
    print('Você precisa treinar muito')
elif goleiro<4:
    print('Você vai para reserva')
else:
  print('Não disponível')