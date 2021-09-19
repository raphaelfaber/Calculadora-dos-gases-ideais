import time
print('x'*60)
print('Seja bem vindo(a) a calculadora da lei dos gases ideais!')
print('x'*60)
p=0
v=0
n=0
r=0.082
t=0
while True:
	var = str(input("""O que você deseja calcular?
	Digite:
	[P] para calcular a pressão
	[V] para volume
	[n] para número de mols
	[T] para temperatura
	 """)).lower().strip()
	time.sleep(0.25)
	if var in ('pvnt'):
		if var == 'p':
			v = float(input('Digite o volume (em L):   '))
			n = float(input('Digite o número de mols (n):   '))
			t = float(input('Digite a temperatura(T) em kelvin:  '))
			p = (n*r*t)/v
			print('A pressão nas condições inseridas é {} ATM'.format(p))
		if var == 'v':
			p = float(input('Digite a pressão (em ATM):  '))
			n = float(input('Digite o número de mols (n):  '))
			t = float(input('Digite a temperatura(T) em kelvin:  '))
			v = (n*r*t)/p
			print('O volume nas condições inseridaes é {} L'.format(v))
		if var == 'n':
			p = float(input('Digite a pressão (em ATM):  '))
			v = float(input('Digite o volume (em L):  '))
			t = float(input('Digite a temperatura(T) em kelvin:  '))
			n=(p*v)/(r*t)
			print('A quantidade de mols nessas condições é de {} mol(s)'.format(n))
		if var == 't': 
			p = float(input('Digite a pressão (em ATM):  '))
			v = float(input('Digite o volume (em L):  '))
			n = float(input('Digite o número de mols (n):  '))
			t=(p*v)/(n*r)
			print('A temperatura nessas condições é de {} K'.format(t))
		loop = str(input(('Deseja calcular outro parâmetro?[Y/N]'))).lower().strip()
		while loop not in ('ysn'):
			loop = str(input(('Deseja calcular outro parâmetro?[Y/N]'))).lower().strip()
		if loop == 'n':
					print('Obrigado por usar a calculadora dos gases ideais!')
					break
          
          
