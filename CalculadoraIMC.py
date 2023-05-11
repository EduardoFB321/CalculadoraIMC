#Desenvolva uma calculadora de IMC, o programa deve pedir o peso e a altura ao usuario. calcular o IMC e retronar para o usuario o IMC
# e a categoria em que se encontra 


def calculadora_IMC(peso,altura):
    calculo_altura = altura * altura
    calculo_IMC = peso / calculo_altura
    if calculo_IMC < 18.5:
        print("abaixo do peso")
    elif calculo_IMC < 24.9:
        print("peso normal")
    elif calculo_IMC < 29.9:
        print("sobrepeso")
    elif calculo_IMC <30:
        print("Obesidade")
    return calculo_IMC

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
print(calculadora_IMC(peso,altura))
