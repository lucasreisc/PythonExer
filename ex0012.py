valor = float(input('Digite o valor do produto para saber o desconto: '))

desconto = (5 / 100) * valor
valorFinal =  valor - desconto

print( 'O produto custava {} após a aplicação do desconto passou a custar {}'.format(valor, valorFinal))
