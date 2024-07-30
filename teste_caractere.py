# linha_conteudo = "a b"

# lista_palavras = ["_token", "linha", "parte", "linguagem", " "]

# string_atual = ""

# palavras_extraidas = []

# for caractere in linha_conteudo:
#     if caractere.isalnum() or caractere == '_':
#         string_atual += caractere
#     else:
#         if string_atual in lista_palavras:
#             palavras_extraidas.append(string_atual)
#         string_atual = ""

# # Verificar a última palavra após o loop
# if string_atual in lista_palavras:
#     palavras_extraidas.append(string_atual)

# # Imprimir as palavras extraídas que estão na lista de palavras
# print(palavras_extraidas)

# vetor = lista
# for i in range listadecaracteres:
    
#     if vetor[i] == "_":
#         j = 1
#         while vetor[j] == letras
#             string += veotr[j]
#             j++
#             i = j-1
#         getToken()
def ler_caracteres(arquivo):
    tokens = ''
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            while True:
                char = f.read(1)
                if not char:
                    break
                #print(char, end='')
                tokens += char
        return tokens

    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")

# Exemplo de uso:
tokens = ler_caracteres('tokens.txt')


i = 0
while i < len(tokens):
    if tokens[i] == '_':
        j = i + 1
        aux = tokens[i]
        while j < len(tokens) and tokens[j].isalpha():
            aux += tokens[j]
            j += 1
        print(f"Encontrado token: {aux}")
        i = j
    elif tokens[i].isdigit():
        j = i + 1
        aux = tokens[i]
        while j < len(tokens) and (tokens[j].isdigit() or tokens[j] == '.'):
            aux += tokens[j]
            j += 1
        print(f"Encontrado número: {aux}")
        i = j
    elif tokens[i] == ' ':
        print('espaço')
        i += 1
    elif tokens[i].isalpha():
        j = i + 1
        aux = tokens[i]
        while j < len(tokens) and tokens[j].isalpha():
            aux += tokens[j]
            j += 1
        print(f"Encontrado token: {aux}")      
        i=j  
    else:
        i += 1

