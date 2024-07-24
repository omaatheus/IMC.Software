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
    float(peso)
    float(altura)

    imc = float(f'{peso / (altura**2):.2f}')

    if(imc < 18.5):
        r = 'Baixo peso'
    elif(imc < 24.9):
        r = 'Eutrofia'
    elif(imc < 29.9):
        r = 'Sobrepeso'
    elif(imc < 34.9):
        r = 'Obesidade Grau I'
    elif(imc < 39.9):
        r = 'Obesidade Grau II'
    else:
        r = 'Obesidade Grau III'

    print(imc)
    print(r)

calcularImc(75, 1.84)