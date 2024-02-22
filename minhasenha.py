minhaSenha = int(input("Digite sua senha: "))

senhalida = 1
encontreiMinhaSenha = False

while senhalida != 0 and not encontreiMinhaSenha:
    senhalida = int(input("Digite a próxima senha: "))
    if senhalida == minhaSenha:
        encontreiMinhaSenha = True

if encontreiMinhaSenha:
    print("UHuhuuU, achei minha senha!")        
else:
    print("Minha senha não está lá.")    