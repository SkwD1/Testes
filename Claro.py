import random

def plano1(reais, reaismin, reaismb, reaissms):
    reais = 0
    if (min > 50 or mb > 1024 or sms > 50):
        reaismin = (min - 50) * 0.70

        reaismb = (mb - 1024) * 0.09

        reaissms = (sms - 50) * 0.04

        reais = reaismin + reaismb + reaissms + 50
        print(reais)

    else:
        reaismin = 0
        reaismin = 0
        reaissms = 0

        print("Você vai pagar o valor padrão em R$: 50")


def plano2(reais, reaismin, reaismb, reaissms):
    reais = 0
    if (min > 100 or mb > 2048 or sms > 100):
        reaismin = (min - 100) * 0.70

        reaismb = (mb - 2048) * 0.09

        reaissms = (sms - 100) * 0.04

        reais = reaismin + reaismb + reaissms + 80
        print(reais)

    else:
        reaismin = 0
        reaismin = 0
        reaissms = 0

        print("Você vai pagar o valor padrão em R$: 80")

def plano3(reais, reaismin, reaismb, reaissms):
    reais = 0
    if (min > 200 or mb > 4096 or sms > 200):
        reaismin = (min - 200) * 0.70

        reaismb = (mb - 4096) * 0.09

        reaissms = (sms - 200) * 0.04

        reais = reaismin + reaismb + reaissms + 120
        print(reais)

    else:
        reaismin = 0
        reaismin = 0
        reaissms = 0

        print("Você vai o valor padrão em R$: 120")


if __name__ == '__main__':
    min = 0
    mb = 0
    sms = 0
    reais = 0
    reaismin = 0
    reaismb = 0
    reaissms = 0
    print("OLÁ, BEM VINDO A CLARO - Nos  fornecemos 3 planos diferentes, descritos abaixo:\n"
          "PLANO 1 - R$50, 50 minutos, 1GB (1024 MB), 50 SMS\n"
          "PLANO 2 - R$80, 100 minutos, 2GB (2048 MB), 100 SMS\n"
          "PLANO 3 - R$120, 200 minutos, 4GB (4096 MB), 200 SMS\n")
    print("Além disso, podem ser cobradas taxas adicionais quando ocorre o consumo acima do previsto.\n"
          "Cada minuto a mais custa R$0,70. Cada MB a mais custa R$0,09. Cada SMS a mais custa R$0,04.\n")
    plano = int(input("Escolha seu plano "))

    min = int(input("Quantos minutos você usou? "))
    mb = int(input("Quantos megas você usou? "))
    sms = int(input("Quantos sms você usou? "))
    if(plano == 1):
        plano1(reais, reaismin, reaismb, reaissms)

    elif(plano == 2):
        plano2(reais, reaismin, reaismb, reaissms)

    elif(plano == 3):
        plano3(reais, reaismin, reaismb, reaissms)

