palavras_reservadas = [
    '_for', '_begin', '_end', '_receba', '_seliga', '_if', '_else', 
    '_int', '_float', '_bool', '_while', '_true', '_false', '_pot'
]

def getPalavraReservada(palavra):
    if palavra in palavras_reservadas:
        posicao = palavras_reservadas.index(palavra)        
        return posicao
    else:
        return -1

def getVar(var):
    return

def getOpAritmetico(op):
    return

def getOpRelacional(op):
    return

def getOpLogico(op):
    return

def getNum(num):
    return

def getFloat(num):
    return

def adicionar_par(linha, posicao, tipo):
    tokens.append((linha, posicao, tipo))

token = input("Enter a token: ")
tokens = []
linha = 0

match token[0]:

    case _ if token[0].isalpha():
        getVar(token)

    case _ if token[0].isdigit():

        if token.__contains__('.'):
            getFloat(token)
        else:
            getNum(token)

    case '_':
        pos = getPalavraReservada(token)
        if(pos != -1):
            adicionar_par(linha, pos, 'Palavra Reservada')

    case '+' | '-' | '*' | '/':
        getOpAritmetico(token)

    case '&' | '|' :
        getOpLogico(token)

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
    
    case '>' | '<':
        getOpRelacional(token)
    
    case ':':
        if token[1] == ':':
            getOpRelacional(token)
        else:
            print('ERRO: Não é um token')
        
print(tokens)
