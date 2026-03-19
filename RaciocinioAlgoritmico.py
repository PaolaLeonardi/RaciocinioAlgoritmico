
#No Exercício 01, o programa pede para o usuário informar o ano de nascimento.
#Esse valor é digitado pelo usuário e armazenado em uma variável.
#Como o input sempre recebe o valor como texto, é necessário usar int() para converter para número inteiro. 
#Depois disso, o programa subtrai o ano de nascimento do ano atual (2026) para calcular a idade.

print ('Exercício 01') # serve para mostrar algo na tela, no caso: o n° do exercício.

nascimento = input ('Qual sua data de nascimento?') # o input pede para o usuário digitar algo, esse algo vai se tornar a variável
print () # apenas para pular uma linha
ano_atual= 2026 # Define que a variável ano_atual seja igual a 2026
idade= int (ano_atual) - int (nascimento)

# int converte os valores para números inteiros, o nascimento era frase mas deve ser um número agora.
# idade = ano_atual menos nascimento.

# VARIÁVEL = Pode assumir qualquer valor
# CONSTANTE = Não muda

#No Exercício 02, é definido o valor de um carro (100 reais). 
#Em seguida, o programa pergunta quantos carros o usuário deseja comprar.
#O valor digitado é convertido para número e multiplicado pelo preço do carro, calculando assim o valor total da compra. 
#O resultado é exibido na tela usando um print com f-string, que permite colocar variáveis dentro do texto.

print ('Exercício 02')

carro= float (100.00)
# Real -> Float

quantidade = input ('Quantos carros gostaria de comprar?')
valor_total = (int (quantidade) * int (carro))
print (f" O valor dos carros fica: {valor_total} reais")
# o F antes das aspas deixa colocar variáveis dentro do texto

#No Exercício 03, o usuário informa uma temperatura em Celsius. 
#O programa utiliza a fórmula de conversão para Fahrenheit (C × 9/5 + 32) 
#para transformar a temperatura e mostrar o resultado na tela.

print ('Exercício 03')

celcius = input ('Diga uma temperatura em Celsius')
print ()

Fahrenheit= int (celcius) * 9/5 + 32
print ( f" temperatura em Fahrenheit: {int(Fahrenheit)}")

# Usar o {int()} faz com que o valor final fique sem o .0

#No Exercício 04, o programa pede quatro notas ao usuário. 
#Depois, ele soma todas as notas e divide por quatro para calcular a média final.

print ('Exercício 04')

Nota1= input ("Qual sua primeira nota?")
Nota2= input ("Qual sua segunda nota?")
Nota3= input ("Qual sua terceira nota?")
Nota4= input ("Qual sua quarta nota?")

Soma= (int (Nota1) + int (Nota2) + int (Nota3) + int (Nota4))
print (f" Sua nota final é {int (Soma) / 4 }")

#No Exercício 05, o programa pede o ano de nascimento novamente,
#calcula a idade usando o ano atual e depois multiplica a idade por 12 
#para descobrir a idade em meses.

print ('Exercício 05')

Ano_Atual= 2026

nascimento = int (input ("Qual o ano do seu nascimento?"))

Idade = Ano_Atual - nascimento
idade_meses= Idade * 12

print (f"Sua idade em meses seria: {idade_meses}")
