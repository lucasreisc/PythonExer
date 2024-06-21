import math

oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comrimento do cateto adjacente: '))

x = oposto**2 + adjacente**2
hipo = math.sqrt(x)

print('A hipotonesua vai medir {:.2f}'.format(hipo))
