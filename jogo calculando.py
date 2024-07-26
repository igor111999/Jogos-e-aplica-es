ligar = input("on ou off")
while ligar == "off":
    break


if ligar == "on":
    print("digite um numero no campo abaixo")
    numero = input()
    if numero.isnumeric()== True or numero.isdigit()== False:
        pass
    elif numero.isalpha()== False:
        while numero.isalpha() == False:
            numero = input('digite um numero')
    else:
        while numero != " ":
            numero = input('digite um numero')
    print(numero+2)

    sinal= input("digite um sinal")