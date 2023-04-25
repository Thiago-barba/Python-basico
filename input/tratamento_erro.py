try:
 idade=int(input('Digite sua idade: '))
except:
 print('Você não digitou um número inteiro ')
else:
 print('Você tem', idade, 'anos')
finally:
 print('Fim!!!')