print ("Exercício 01") #------------

temperatura = float (input ('Temperatura':))
if temperatura > 25:
    print ('Está um tempo quente!')

print("Exercício 02") #-------------

numero = int (input("Número"))
print (numero % 2 )

if numero % 2 == 0:
    print ('É par')

 print("Exercício 03") #------------

temp = float (input('Diga sua temperatura'))
if temp <= 23:
    print ("Está frio")

print("Exercício 04") #-------------

number = float (input("Diga um número"))
if number % 2 == 0:
    print ("Seu número é par!")
else:
    print ("Seu número é impar!")

print("Exercício 05") #-------------

graus = float (input("Diga uma temperatura"))
if graus > 25:
    print ("A temperatura está quente")
elif graus >= 18 and temperatura <= 25:
    print ("A temperatura está amena")
else:
    print ("Está frio!")

print("Exercício 06") #-------------

anos = int (input("Diga sua idade para o filme"))
ingresso = (input("Tem o ingresso para o filme? (S/N) "))

if ingresso == "Sim":
    ingresso = True  #True e False Faz mudar de string para booleano

elif ingresso == "Não":
    ingresso = False

if anos >= 18:
    if ingresso:
        print ("Bom filme!")
    else:
        print ("não tem ingresso")
else:
    print ("menor de idade")
