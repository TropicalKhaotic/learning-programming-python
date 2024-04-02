#Selecionando qual calculadora o usuario precisa
print("Trapezio,Quadrado")
calculadora = input("Qual calculadora voce deseja: ")
calculadora = calculadora.lower()
#Calculadora Trapezio
if calculadora == "trapezio":
    maior = float(input("Qual o valor da base maior: "))
    menor = float(input("Qual o valor da base menor: "))
    altura = float(input("Qual o valor da altura do trapezio: "))
    Resultado = (maior+menor/2)*altura #Calculo para a area do trapezio
    print("A area do Trapezio é:",Resultado)
#Calculadora Quadrado
elif calculadora == "quadrado":
    lado = float(input("Qual o valor de um dos lados do quadrado:"))
    Resultado = (lado*lado) #Calculo para a area do quadrado
    print("A area do quadrado é:",Resultado)
