linha_conteudo = "a b"

lista_palavras = ["_token", "linha", "parte", "linguagem", " "]

string_atual = ""

palavras_extraidas = []

for caractere in linha_conteudo:
    if caractere.isalnum() or caractere == '_':
        string_atual += caractere
    else:
        if string_atual in lista_palavras:
            palavras_extraidas.append(string_atual)
        string_atual = ""

# Verificar a última palavra após o loop
if string_atual in lista_palavras:
    palavras_extraidas.append(string_atual)

# Imprimir as palavras extraídas que estão na lista de palavras
print(palavras_extraidas)

vetor = lista
for i in range listadecaracteres:
    
    if vetor[i] == "_":
        j = 1
        while vetor[j] == letras
            string += veotr[j]
            j++
            i = j-1
        getToken()
