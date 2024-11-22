#solicitar a pontuação e presença do usuário

pontuaçao = float(input("Digite a pontuação final:"))
presença = float(input("Digite a porcentagem de presença:"))

#definindo as condições

if pontuaçao >=  80 and presença >= 90:
    categoria =  "Excelente"
elif pontuaçao >=  50 and pontuaçao <= 79:
    if presença >= 75:
        categoria = "Bom"
    else:
        categoria = "Regular"
else:
    categoria = "Ruim"

    #exibir resultado
print(f"Sua categoria é:{categoria}")