# Uma produtora de software está criando diversos sistemas para nutricionistas. 
#Ela precisa de um códigos que possa ser reutilizados entre os diversos programas que devolvam os seguinte resultados: 

#  - O índice  de massa corpórea (IMC) de um paciente 
#  - A classificação de um paciente de acordo com o IMC 

# Considere

# Considere o seguinte : 
# IMC <18,5kg/m2 - baixo peso.
# IMC >18,5 até 24,9kg/m2 - eutrofia (peso adequado)
# IMC ≥25 até 29,9kg/m2 - sobrepeso.
# IMC >30,0kg/m2 até 34,9kg/m2 - obesidade grau 1.
# IMC >35kg/m2 até 39,9kg/m2 - obesidade grau 2.
# IMC > 40kg/m2 - obesidade extrema.



def calcularImc(peso, altura):
    p = float(peso)
    a = float(altura)

    imc = float(p / (a**2))
    total = round(imc, 2)
    return total

def classificarImc(i):
    if(i < 18.5):
        r = 'Baixo peso'
    elif(i < 24.9):
        r = 'Eutrofia'
    elif(i < 29.9):
        r = 'Sobrepeso'
    elif(i < 34.9):
        r = 'Obesidade Grau I'
    elif(i < 39.9):
        r = 'Obesidade Grau II'
    else:
        r = 'Obesidade Grau III'
    return r


p = input('Informe o Peso: ')
a = input('Informe a altura: ')

calc = calcularImc(p, a)

print(f' O Calculo de IMC é: {calc}\n A Classificação de IMC é: {classificarImc(calc)}')
