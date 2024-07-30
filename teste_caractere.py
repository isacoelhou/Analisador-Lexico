palavras_reservadas = [
    '_for', '_begin', '_end', '_receba', '_seliga', '_if', '_else', 
    '_int', '_float', '_bool', '_while', '_true', '_false', '_pot'
]

operadores_aritmeticos = ['+', '-', '*', '/']

operadores_relacionais = ['::', '>', '<']

operadores_logicos = ['&', '|']

def getPalavraReservada(palavra):
    if palavra in palavras_reservadas:
        posicao = palavras_reservadas.index(palavra)        
        return posicao
    else:
        return -1

def getFloat(num):
    if num.count('.') <= 1: #Não pode haver mais de um . na variavel
        return True
    else:
        return False

def getOpAritmetico(op):
    if len(op) > 1:
        return -1
    else: 
        if op in operadores_aritmeticos:
            posicao = operadores_aritmeticos.index(op)        
            return posicao
        else:
            return -1

def adicionar_par(linha, posicao, tipo):
    k.append((linha, posicao, tipo))
    
def ler_caracteres(arquivo):
    tokens = ''
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            while True:
                char = f.read(1)
                if not char:
                    break
                tokens += char
        return tokens

    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")

tokens = ler_caracteres('tokens.txt')

k = []
i = 0
linha = 1

while i < len(tokens):

    if tokens[i] == '_':

        j = i + 1
        aux = tokens[i]

        while j < len(tokens) and tokens[j].isalpha():
            aux += tokens[j]
            j += 1
        
        a = getPalavraReservada (aux)
        if (a != -1):
            adicionar_par(linha, a, 'Palavra reservada')
        else:
            print('O token', aux, 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i = j

    elif tokens[i].isdigit():

        j = i + 1
        aux = tokens[i]

        while j < len(tokens) and (tokens[j].isdigit() or tokens[j] == '.'):
            aux += tokens[j]
            j += 1
        
        if(aux.__contains__('.')):

            if(getFloat()):
                adicionar_par(linha, None, 'Float')
            else:
                print('O token', aux, 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')

        else:
            adicionar_par(linha, None, 'Inteiro')
        i = j

    elif tokens[i] == ' ':

        adicionar_par(linha, None, 'Espaço')
        i += 1

    elif tokens[i].isalpha():

        j = i + 1
        aux = tokens[i]

        while j < len(tokens) and tokens[j].isalnum():

            aux += tokens[j]
            j += 1

        adicionar_par(linha, None, 'Variável')     
        i = j  

    elif tokens[i] == '\n':

        adicionar_par(linha, None, 'Fim de linha')
        linha += 1
        i += 1

    elif tokens[i] in ['+', '-', '*', '/']:
        pos = getOpAritmetico(tokens[i])
        if(pos != -1):
            adicionar_par(linha, pos, 'Operador Aritmético')
        else:
            print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i += 1

    elif tokens[i] == '(':
        adicionar_par(linha, None, 'abre parenteses')
        i += 1

    elif tokens[i] == ')':
        adicionar_par(linha, None, 'fecha parenteses')
        i += 1

    elif tokens[i] == '{':
        adicionar_par(linha, None, 'abre chaves')
        i += 1

    elif tokens[i] == '}':
        adicionar_par(linha, None, 'fecha chaves')
        i += 1

    elif tokens[i] == '[':
        adicionar_par(linha, None, 'abre colchete')
        i += 1

    elif tokens[i] == ']':
        adicionar_par(linha, None, 'fecha colchetes')
        i += 1

    elif tokens[i] == ';':
        adicionar_par(linha, None, 'ponto e virgula')
        i += 1

    elif tokens[i] == ',':
        adicionar_par(linha, None, 'virgula')
        i += 1

    elif tokens[i] in ['&', '|'] :
        if tokens[i] == '&':
            pos = 0
        else:
            pos = 1
        adicionar_par(linha, pos, 'Operador Lógico')
                       
    else:
        print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i += 1
print(k)
print('\nVetores:\n\nPalavras reservadas:', palavras_reservadas, '\n')
print('Operadores aritméticos: ', operadores_aritmeticos, '\n')
print('Operadores logicos: ',operadores_logicos, '\n')
print('Operadores relacionais: ',operadores_relacionais, '\n')

with open('tokens_saida.txt', 'w') as saida:
    for t in k:
        linha, pos, tipo = t
        saida.write(f"Linha: {linha}, Posição em seu respectivo vetor: {pos}, Tipo: {tipo}\n")