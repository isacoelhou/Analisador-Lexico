palavras_reservadas = [
    '_for', '_begin', '_end', '_receba', '_seliga', '_if', '_else', 
    '_int', '_float', '_bool', '_while', '_true', '_false', '_pot'
]

operadores_aritmeticos = ['+', '-', '*', '/']

operadores_logicos = ['&', '|', '!']

def getPalavraReservada(palavra):
    if palavra in palavras_reservadas:    
        return palavra
    else:
        return -1

def getFloat(num):
    if num.count('.') <= 1: #Aqui precisa arrumar
        return True
    else:
        return False

def getOpAritmetico(op):
    if len(op) > 1:
        return -1
    else: 
        if op in operadores_aritmeticos:
            return op
        else:
            return -1

def adicionar_par(linha, tipo):
    k.append((linha, tipo))
    
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
            adicionar_par(linha, a)
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

            if(getFloat(aux)):
                adicionar_par(linha, 'num')
            else:
                print('O token', aux, 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')

        else:
            adicionar_par(linha, 'num')
        i = j

    elif tokens[i] == ' ':

        #adicionar_par(linha, 'Espaço')
        i += 1

    elif tokens[i] == '	':
        i += 1

    elif tokens[i].isalpha():

        j = i + 1
        aux = tokens[i]

        while j < len(tokens) and tokens[j].isalnum():

            aux += tokens[j]
            j += 1

        adicionar_par(linha, 'id')     
        i = j  

    elif tokens[i] == '\n':

        #adicionar_par(linha, 'Fim de linha')
        linha += 1
        i += 1

    elif tokens[i] in ['+', '-', '*', '/']:
        pos = getOpAritmetico(tokens[i])
        if(pos != -1):
            adicionar_par(linha, pos)
        else:
            print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i += 1

    elif tokens[i] == ':':
        if tokens[i+1] == ':':
            adicionar_par(linha, '::')
            i += 2
        else:                        
            print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')

    elif tokens[i] == '>':
        if tokens[i+1] == '=':
            adicionar_par(linha,'>=' )
            i+=2
        else:  
            adicionar_par(linha,'>' )
            i += 1

    elif tokens[i] == '<':
        if tokens[i+1] == '=':
            adicionar_par(linha,'<=')
            i+=2
        else:  
            adicionar_par(linha,'<')
            i += 1

    elif tokens[i] == '=':
        adicionar_par(linha, '=')
        i+= 1
    
    elif tokens[i] == '!':
        if  [i+1] == '=':
            adicionar_par(linha, '!=')
            i+=2
        else:  
            adicionar_par(linha, '!')
            i += 1
    
    elif tokens[i] == '(':
        adicionar_par(linha, '(')
        i += 1

    elif tokens[i] == ')':
        adicionar_par(linha, ')')
        i += 1

    elif tokens[i] == '{':
        adicionar_par(linha, '{')
        i += 1

    elif tokens[i] == '}':
        adicionar_par(linha, '}')
        i += 1

    elif tokens[i] == ';':
        adicionar_par(linha, ';')
        i += 1

    elif tokens[i] == ',':
        adicionar_par(linha,',')
        i += 1

    elif tokens[i] == '“':
        adicionar_par(linha,'“')
        j = i+1

        while i < len(tokens) and tokens[i] != '"':
            i+=1
        adicionar_par(linha, 'str')
        #aqui precisa arrumar, se ele não encontrar uma aspas ele precisa para o programa ou demarcar erro e adicionar um fecha aspas   
        if i < len(tokens):
            adicionar_par(linha, '"')
            i+=1
        else:
            print("Erro léxico, necessita de um fechas aspas na linha", linha, "Anter de continuar ajuste o erro...")
            break
    
        if tokens[i] == '&':
           adicionar_par(linha,'&')
        elif tokens[i] == '|':
            pos = 1
        adicionar_par(linha, '|')
                       
    else:
        print('O token', tokens[i], 'da linha', linha, 'não faz parte da linguagem, verifique a digitação')
        i += 1


with open('tokens_saida.txt', 'w') as saida:
    for t in k:
        linha, pos = t
        saida.write(f"{pos}\n")