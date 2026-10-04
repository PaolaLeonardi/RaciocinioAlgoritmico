#Peça um número e verifique:
#se está entre 10 e 50 (inclusive);
#se é menor que 10;
#se é maior que 50.

numero = int(input("Diga um número"))

if numero >= 50:
  print ("Maior que 50")
elif numero <= 10:
  print ("Menor que 10")
elif numero >= 10 and numero <=50:
  print("Está entre 10 e 50!")
else:
  print("Número inválido")

#Peça um ano e verifique se ele é bissexto. Um ano é bissexto se:
#for divisível por 4 e não for divisível por 100 ou for divisível por 400.

ano = (int(input("Diga um ano")))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print ("Ano Bissexto!")
else:
    print ("Não é um ano bissexto!")

#Peça usuário e senha.
#Só permita acesso se usuário for "admin" e a senha for "1234".
#Caso contrário, bloqueie.
#Se o usuário for "convidado" e não digitar senha, exiba “Acesso restrito”.

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print ("Usuário logado!")
elif usuario == "convidado":
    print("Acesso restrito")
else:
    print("Usuário ou senha incorreta")

#verifique a posição do ponto em relação a um quadrado
#cujos vértices vão de (0,0) até (10, 10).
#Se o ponto estiver estritamente dentro da região, mostre “Dentro do quadrado”.
#Se estiver exatamente em uma das bordas, mostre “Na fronteira”.
#Caso contrário, mostre “Fora do quadrado”.

x = (int(input("Cordenada x: ")))
y = (int(input("Cordenada y: ")))

if x == 10 or x == 0 or y == 0 or y == 10:
    print("Na fronteira")
elif x <= 9 or y <= 9 or x >= 0 or y >=0:
    print("Dentro do quadrado")
else:
    print("Fora do quadrado")

#Peça os três lados de uma figura. Primeiro, verifique se esses valores podem
#formar um triângulo.
#⚠Lembre-se: a soma de dois lados deve ser sempre maior que o terceiro.
#Se for possível formar um triângulo, classifique-o:
#Equilátero: todos os lados têm o mesmo tamanho.
#Isósceles: dois lados têm o mesmo tamanho.
#Escaleno: todos os lados são diferentes.
#Além disso, verifique se o triângulo é retângulo:
#⚠️Um triângulo é retângulo quando o quadrado do maior lado
#é igual à soma dos quadrados dos outros dois lados.
#Caso os valores não formem um triângulo, informe isso ao usuário.

a= (int (input ("Lado 1: ")))
b= (int (input ("Lado 2: ")))
c= (int (input ("Lado 3: ")))

if a + b > c and a + c > b and b + c > a:
    print ("Triângulo!")

    if a == b and b == c:
        print("Equilátero")
    elif a == b or a == c or b == c:
        print("Isósceles")
    else:
        print("Escaleno")

    if pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2) or pow(b, 2) + pow(c, 2) == pow(a, 2):
        print ("Triângulo Retângulo")
    else:
        print("não é um Triângulo Retângulo")
else:
    print ("não é um Triângulo")
