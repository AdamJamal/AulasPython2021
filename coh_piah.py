import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input('Digite o texto ' + str(i) + ' (aperte enter para sair): ')
    while texto:
        textos.append(texto)
        i = i + 1
        texto = input('Digite o texto ' + str(i) + ' (aperte enter para sair): ')
    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -=1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

def compara_assinatura(as_a, as_b):
    Sab = 0
    for i in range(0,6):
        Sab = Sab + (abs(as_a[i] - as_b[i])) / 6
    return (Sab)
    

def calcula_assinatura(texto):
    vetor_sentencas = separa_sentencas(texto)
    n_sentencas = len(vetor_sentencas)
    soma_caracteres_sentenca = 0
    for i in range(0,n_sentencas):
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(vetor_sentencas[i])

    # Tamanho médio da sentença:
    sal = soma_caracteres_sentenca / n_sentencas

    vetor_frases = []
    n_frases = 0
    soma_caracteres_frase = 0
    vetor_palavras = []
    n_palavras = 0
    soma_caracteres_palavra = 0
    for i in range(0,n_sentencas):
        vetor_frases.append(separa_frases(vetor_sentencas[i]))
        n_frases = n_frases + len(vetor_frases[i])
        frases = vetor_frases[i]
        for j in range(0,len(frases)):
            soma_caracteres_frase = soma_caracteres_frase + len(frases[j])
            frase_separada = frases[j]
            palavras = separa_palavras(frase_separada)
            for k in range(0,len(palavras)):
                soma_caracteres_palavra = soma_caracteres_palavra + len(palavras[k])
                vetor_palavras.append(palavras[k])
                                        
    # Complexidade de sentença:
    sac = n_frases / n_sentencas

    # Tamanho médio de frase:
    pal = soma_caracteres_frase / n_frases

    # Tamanho médio de palavra:
    wal = soma_caracteres_palavra / len(vetor_palavras)

    # Relação Type-Token:
    ttr = n_palavras_diferentes(vetor_palavras) / len(vetor_palavras)

    # Razão Hapax Legomana:
    hlr = n_palavras_unicas(vetor_palavras) / len(vetor_palavras)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    Sab = []
    for i in range(0,len(textos)):
        ass_texto = calcula_assinatura(textos[i])
        Sab.append(compara_assinatura(ass_cp, ass_texto))
    j = 0
    while min(Sab) != Sab[j] and j <= len(Sab):
        j = j + 1
    return(j + 1)           

ass_cp = le_assinatura()
textos = le_textos()
texto_infectado = avalia_textos(textos, ass_cp)
print()
print('O autor do texto', texto_infectado, 'está com COH-PIAH')