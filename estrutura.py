#1 - Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if (media == 10):
  mensagem = 'Aprovado com Distinção!' 
elif(media >= 7):
  mensagem = 'Aprovado com média', media
else:
  mensagem = 'Reprovado com média' , media

print(mensagem)

#2- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Informe um valor entre 0 e 10: '))

while ( nota != True ):
  if (nota > 10 or nota < 0):
    nota = int(input('Informe um valor válido! '))
  
  print(f'A nota foi {nota}')
  break

#um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

temperaturaC = float(input('Informe a temperatura em Fahrenheit! '))

temperaturaF = (temperaturaC * 1.8)+32

print(temperaturaF)


#4- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Informe o ano: '))
if (ano % 4 == 0):
  print(f'{ano} é bissexto.')
else:
  print(f'{ano} não é bissexto.')


#5 - Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

#6 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range (1,6):
  idade = int(input('Informe a idade: '))
  altura = float(input('Informe a altura: '))
  idades.append(idade)
  alturas.append(altura)

print([i],'Pessoa')



