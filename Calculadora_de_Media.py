# Exercício 05 

resposta = input ("Digite S para começar: \n>") # o \n > serve pra deixar mais claro onde o usuário digita

if resposta == "S":

    soma = 0
    contador = 0

    while True:
        numero = int (input ("Digite um número para fazer a média (-1 para parar): \n > "))

        if numero == -1:
            break

        soma += numero
        contador += 1

    if contador > 0:
        media = soma / contador
        print ("Média:", media)
    else:
        print ("Nenhum número válido foi digitado")

else:
    print ("Programa não iniciado")
