salario = float(input('Digite o valor do seu salário para saber seu aumento'))
if salario <= 1250:
   print('O seu salario que era {}, você passa a ganhar {}'.format(salario, salario +(salario*0.15)))
else:
   print('O seu salario que era {}, você passa a ganhar {}'.format(salario, salario +(salario*0.10)))
