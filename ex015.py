dias = float(input('Quantos dias voce ficou com o carro? '))
km = float(input('Qual a quantidade de km percorrida? '))

diasValor = dias * 60
kmValor = km * 0.15

totalAluguel = diasValor + kmValor

print('O valor total do seu aluguel é R$ {}'.format(totalAluguel))
