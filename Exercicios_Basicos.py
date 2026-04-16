print ("Exercício 01")

nome = str (input ("Qual seu nome? \n> "))
cpf = int (input ("Qual seu CPF? \n> "))
telefone = str (input ("Qual seu número de telefone? \n> "))
ano= str (input ("Qual seu ano de nascimento? \n> "))
print (f"Seu nome é {nome}, seu cpf é {cpf}, seu telefone é {telefone} e seu ano de nascimento é {ano}!")
# -----------------------------------------------------------------------
print ("Exercício 02")

print ('Bem vindo á loja! são 100 reais cada carro!')
carro = 100
quantidade = int (input ("Quantos carros gostaria de comprar? \n> "))
print (f"Então você gostaria de pedir {quantidade} de carros por {carro} reais, ao total sua compra será de {quantidade * carro} reais")

# -----------------------------------------------------------------------
print ("Exercício 03")

celcius = int (input ("Diga uma temperatura em Celsius: \n> "))
f = (celcius * 9/5) + 32
print (f"A temperatura de {celcius} em fahrenheit é de {f}!")
# -----------------------------------------------------------------------
print ("Exercício 03")

print ("Vamos calcular a média de suas quatro notas!")
um = int (input ("Qual a sua primeira nota? \n> "))
dois = int (input ("Qual a sua segunda nota? \n> "))
tres = int (input ("Qual a sua terceira nota? \n> "))
quatro = int (input ("Qual a sua quarta nota? \n> "))
print (f"Sua média foi de {(um+dois+tres+quatro) / 4}")
