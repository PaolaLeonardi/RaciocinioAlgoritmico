#contador = 0
#while contador <= 10:
# if contador % 2 != 0:
#print(f“{contador} é ímpar.”)
# else:
#print(f“{contador} é par.”)

# contador = contador +

#Faça um programa que percorra os números de 1 até 100 e mostre apenas aqueles que
#são múltiplos de 3 e, ao mesmo tempo, não são múltiplos de 5. Ao final, mostre também
#quantos números atenderam a essa condição.

i = 1
quantidade= 0

while i <=100:
    if  i %3 == 0 and i %5 !=0:
        print(i)
        quantidade += 1
    i += 1
print ("Quantidade:", quantidade)