#Notas dos jogadores distribuidas pelo torcedor
print('Dê a nota para cada jogador do Corinthians de 0 a 10, partida Liverpool vs Corinthians pela libertadores de america')
try:
 nome_goleiro=float(input('Cassio: '))
 lateral_direito=float(input('Fagner: '))
 zagueiro_direito=float(input('Bruno Mendes: '))
 zagueiro_central=float(input('Gil: '))
 lateral_esquerdo=float(input('Fabio Santos: '))
 volante_central=float(input('Fausto Vera: '))
 Volante_joga=float(input('Giuliano: '))
 meio_de_campo=float(input('Renato Augusto: '))
 ponta_direita=float(input('Adson: '))
 pont_esquerda=float(input('Roger Guedes: '))
 centro_avante=float(input('Yuri Albero: '))
 tecnico=float(input('Fernando Lazaro: '))
 media_final=round((nome_goleiro+zagueiro_direito+zagueiro_central+lateral_direito+lateral_esquerdo+volante_central+Volante_joga+meio_de_campo+ponta_direita+pont_esquerda+centro_avante+tecnico)/12,2)
 print('Nota do time do corinthians: ', media_final)
except:
 print('Você não digitou um número valido')
finally:
 print('Obrigado!')