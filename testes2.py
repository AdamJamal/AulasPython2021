import re
import math


def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def calcula_tamanho_medio_palavra(palavras):
    total_palavras = len(palavras)
    somatorio = 0
    for i in range(len(palavras)):
        somatorio = somatorio + len(palavras[i])
    return somatorio / total_palavras


def calcula_relacao_type_token(palavras):
    total_palavras = len(palavras)
    num_palavras_diferentes = n_palavras_diferentes(palavras)
    return num_palavras_diferentes / total_palavras


def calcula_razao_hapax_legomana(palavras):
    total_palavras = len(palavras)
    num_palavras_diferentes = n_palavras_unicas(palavras)
    return num_palavras_diferentes / total_palavras


def total_caracteres_delimitadores_fora_sentences(palavras):
    caracteres = ['.', '!', '?']
    total_caracteres = 0;
    print("total_caracteres_delimitadores_fora_sentences:", palavras)
    for i in range(len(palavras)):
        #if palavras[i].find('.') >= 0 or palavras[i].find("!") >= 0 or palavras[i].find("?") >= 0:
        if palavras[i].find('.') >= 0 or palavras[i].find("!") >= 0 or palavras[i].find("?") >= 0:
            total_caracteres = total_caracteres + 1
    print("total_caracteres: ", total_caracteres)
    return total_caracteres


def calcula_tamanho_medio_sentencas(sentencas, palavras):
    total_sentencas = len(sentencas)
    #print("total_sentencas: ", total_sentencas)
    #print("palavras: ", palavras)
    #return total_caracteres_delimitadores_fora_sentences(palavras) / total_sentencas
    return len(palavras) / total_sentencas


def calcula_complexidade_sentencas(sentencas, frases):
    total_sentencas = len(sentencas)
    total_frases = len(frases)
    return total_frases / total_sentencas


def total_caracteres_delimitadores_fora_frases(palavras):
    total_caracteres = 0;
    for i in range(len(palavras)):
        for j in range(len(palavras[i])):
            if palavras[i].find(',') >= 0 or palavras[i].find(":") >= 0 or palavras[i].find(";") >= 0:
                total_caracteres = total_caracteres + 1
    return total_caracteres


def calcula_tamanho_medio_frases(frases, palavras):
    total_frases = len(frases)
    return total_caracteres_delimitadores_fora_frases(palavras) / total_frases


def compara_assinatura(as_a, as_b):
    sum = 0
    for i in range(6):
        #a = as_a[i]
        #b = as_b[i]
        #sum = sum + math.fabs(a - b)
        sum = sum + math.fabs(as_a[i] - as_b[i])

    return sum / 6


def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    for i in range(len(sentencas)):
        temp_frases = separa_frases(sentencas[i])
        for j in range(len(temp_frases)):
            frases.append(temp_frases[j])

    for i in range(len(frases)):
        temp_palavras = separa_palavras(frases[i])
        for j in range(len(temp_palavras)):
            palavras.append(temp_palavras[j])

    # Tamanho médio de palavra - wal
    wal = calcula_tamanho_medio_palavra(palavras)
    #print("calculated Tamanho médio de palavra: ", wal)
    # Relação Type-Token - ttr
    ttr = calcula_relacao_type_token(palavras)
    #print("calculated Relação Type-Token: ", ttr)
    # Razão Hapax Legomana - hlr
    hlr = calcula_razao_hapax_legomana(palavras)
    #print(" calculated Razão Hapax Legomana - hlr: ", hlr)
    # Tamanho médio de sentença - sal
    sal = calcula_tamanho_medio_sentencas(sentencas, palavras)
    #print("sentencas: ", sentencas)
    print("calculated Tamanho médio de sentença: ", sal)
    # Complexidade de sentença -  sac
    sac = calcula_complexidade_sentencas(sentencas, frases)
    #print("calculated Complexidade de sentença: ", sac)
    # Tamanho médio de frases - pal
    pal = calcula_tamanho_medio_frases(frases, palavras)
    #print("calculated Tamanho médio de frases: ", pal)

    return [wal, ttr, hlr, sal, sac, pal]


def reconhece_autor_infectado(array):
    min = array[0]
    i = 1
    pos = 0
    while i < len(array):
        if array[i] < min:
            min = array[i]
            pos = i
        i = i + 1
    return pos


def avalia_textos(textos, ass_cp):
    array_grau_similiaridades_textos = []
    for i in range(len(textos)):
        ass_text = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(ass_cp, ass_text)
        array_grau_similiaridades_textos.append(grau_similaridade)
        print("calculate grau similariadade", array_grau_similiaridades_textos)

    return reconhece_autor_infectado(array_grau_similiaridades_textos)


def loadTexts():
    texts = []
    temp = "Navegadores antigos tinham uma frase gloriosa:\"Navegar é preciso; viver não é preciso\". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
    texts.append(temp)
    temp = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
    texts.append(temp)
    temp = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
    texts.append(temp)
    return texts


def loadAssinaturas():
    return [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]


def main():
    texts = loadTexts()
    print("load texts...")
    ass_cp = loadAssinaturas()
    print("load assinaturas...")
    print("O autor do texto", avalia_textos(texts, ass_cp), "está infectado com COH-PIAH")