def getPalavraReservada(palavra):
    return

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

token = input("Enter a token: ")

match token[0]:

    case _ if token[0].isalpha():
        getVar(token)

    case _ if token[0].isdigit():

        if token.__contains__('.'):
            getFloat(token)
        else:
            getNum(token)

    case '_':
        getPalavraReservada(token)

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
        

    

     
    # case 