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
