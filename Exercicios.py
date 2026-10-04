#2. Peça um número e verifique:
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
