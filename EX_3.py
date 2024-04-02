#Calculadora para determinar o volume de um cilindro
import math

print("Calculadora de volume de um cilindro")
operação = (input("Deseja calcular o volume de um cilindro (Y/N):"))
operação = operação.lower()
if operação == "y":
   raio = float(input("Qual o valor do raio:"))
   altura = float(input("Qual o valor da altura:"))
   resultado = (math.pi*(raio*raio))*altura
   resultado = round(resultado,2)
   print("O valor do volume é:",resultado)

elif operação == "n":
   print("Acontece")
else:
   print("Blz ent")
