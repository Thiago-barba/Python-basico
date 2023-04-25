#Validação peso do usuário
usuario=float(input('Digite o seu peso para saber em qual nível você se encontra'))
if usuario>110:
    print('Você está obeso')
elif usuario>=109:
    print('Você está na zona de risco')
elif usuario>=95:
    print('Você está um pouco sedentário')
elif usuario>=85:
    print('Você está em forma')
elif usuario>=50:
    print('Você precisa ganhar mais peso')
else:
 print('Você não se enquadra nos critérios, procure um médico')