# String de exemplo
linha_conteudo = "O_token_b;_da_linha_3_não_faz_parte_da_linguagem,_verifique_a_digitacao"

# Lista de palavras para comparar
lista_palavras = ["token", "linha", "parte", "linguagem"]

# Inicializar uma string vazia para armazenar os caracteres
string_atual = ""

# Inicializar uma lista para armazenar palavras extraídas
palavras_extraidas = []

# Iterar sobre cada caractere da string original
for caractere in linha_conteudo:
    # Verificar se o caractere é um delimitador (não alfanumérico e não underscore)
    if caractere.isalnum() or caractere == '_':
        # Adicionar o caractere à string atual se for alfanumérico ou underscore
        string_atual += caractere
    else:
        # Se encontrar um delimitador, verificar se a string atual está na lista de palavras
        if string_atual in lista_palavras:
            palavras_extraidas.append(string_atual)
        # Resetar a string atual
        string_atual = ""

# Verificar a última palavra após o loop
if string_atual in lista_palavras:
    palavras_extraidas.append(string_atual)

# Imprimir as palavras extraídas que estão na lista de palavras
print(palavras_extraidas)
