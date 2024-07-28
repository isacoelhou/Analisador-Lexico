import re

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

def getVar(var):
    padrao = re.compile(r'^[a-zA-Z0-9]+$') #Padrão suportado pela declaração de variaveis, apenas números e letras
    if padrao.match(var):
        return True
    else:
        return False

def getNum(num):
    padrao = re.compile(r'^[0-9]+$') #Verifica se só tem números na variavel
    if padrao.match(num):
        return True
    else:
        return False

def getFloat(num):
    padrao = re.compile(r'^[0-9.]+$') #Verifica se só tem números e ponto final na variavel
    if padrao.match(num):
        if num.count('.') <= 1: #Não pode haver mais de um . na variavel
            return True
    else:
        return False

def getOpAritmetico(op):
    if op.lenght() > 1:
        return -1
    else: 
        if op in operadores_aritmeticos:
            posicao = operadores_aritmeticos.index(op)        
            return posicao
        else:
            return -1

def adicionar_par(linha, posicao, tipo):
    tokens.append((linha, posicao, tipo))

token = input("Enter a token: ")
tokens = []
linha = 0

match token[0]:

    case _ if token[0].isalpha():
        if(getVar(token)):
            adicionar_par(linha, None, 'Variável')

    case _ if token[0].isdigit():
        if token.__contains__('.'):
            if(getFloat(token)):
                adicionar_par(linha, None, 'Float')
        else:
            if(getNum(token)):
                adicionar_par(linha, None, 'Inteiro')

    case '_':
        pos = getPalavraReservada(token)
        if(pos != -1):
            adicionar_par(linha, pos, 'Palavra Reservada')

    case '+' | '-' | '*' | '/':
        pos = getOpAritmetico(token)
        if(pos != -1):
            adicionar_par(linha, pos, 'Operador Aritmético')

    case '&' | '|' :
        if token.lenght() == 1:
            if token == '&':
                pos = 0
            else:
                pos = 1
            adicionar_par(linha, pos, 'Operador Lógico')

    case ' ' | '    ':
        print('espaços')
    
    case '(':
        print('abre parenteses')

    case ')':
        print('fecha parenteses')

    case '{':
        print('abre chaves')

    case '}':
        print('fecha chaves')

    case '[':
        print('abre colchete')

    case ']':
        print('fecha colchete')

    case ';':
        print('ponto e virgula')

    case ',':
        print('virgula')
    
    case ':':
        if token[1] == ':' and token.lengh() == 2:
            adicionar_par(linha, 0, 'Operador Relacional')
        else:
            print('ERRO: Não é um token')

    case '>':
        if token.lenght() == 1:
            adicionar_par(linha, 1, 'Operador Relacional')
    
    case '<':
        if token.lenght() == 1:
            adicionar_par(linha, 2, 'Operador Relacional')
        
print(tokens)


arquivo = 'listatokens.txt'
