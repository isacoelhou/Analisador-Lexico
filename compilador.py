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

tokens = []
linha = 0

with open('tokens.txt', 'r') as f:
    for linha_num, linha_conteudo in enumerate(f, start=1):
        lidos = linha_conteudo.split()
        print(lidos)
        for token in lidos:

            match token[0]:

                case _ if token[0].isalpha():
                    if(getVar(token)):
                        adicionar_par(linha_num, None, 'Variável')
                    else: 
                        print('O token', token, 'da linha', linha_num, 'não faz parte da linguagem, verifique a digitação')

                case _ if token[0].isdigit():
                    if token.__contains__('.'):
                        if(getFloat(token)):
                            adicionar_par(linha_num, None, 'Float')
                        else: 
                            print('O token', token, 'da linha', linha_num, 'não faz parte da linguagem, verifique a digitação')
                    else:
                        if(getNum(token)):
                            adicionar_par(linha_num, None, 'Inteiro')

                case '_':
                    pos = getPalavraReservada(token)
                    if(pos != -1):
                        adicionar_par(linha_num, pos, 'Palavra Reservada')
                    else:
                        print('O token', token, 'da linha', linha_num, 'não faz parte da linguagem, verifique a digitação')

                case '+' | '-' | '*' | '/':
                    pos = getOpAritmetico(token)
                    if(pos != -1):
                        adicionar_par(linha_num, pos, 'Operador Aritmético')
                    else:
                        print('O token', token, 'da linha', linha_num, 'não faz parte da linguagem, verifique a digitação')    

                case '&' | '|' :
                    if token.lenght() == 1:
                        if token == '&':
                            pos = 0
                        else:
                            pos = 1
                        adicionar_par(linha_num, pos, 'Operador Lógico')

                case ' ' | '    ':
                    adicionar_par(linha_num, None, 'Espaços')
                
                case '(':
                    adicionar_par(linha_num, None, 'abre parenteses')

                case ')':
                    adicionar_par(linha_num, None, 'fecha parenteses')

                case '{':
                    adicionar_par(linha_num, None, 'abre chaves')

                case '}':
                    adicionar_par(linha_num, None, 'fecha chaves')

                case '[':
                    adicionar_par(linha_num, None, 'abre colchete')

                case ']':
                    adicionar_par(linha_num, None, 'fecha colchetes')

                case ';':
                    adicionar_par(linha_num, None, 'ponto e virgula')

                case ',':
                    adicionar_par(linha_num, None, 'virgula')
                
                case ':':
                    if token[1] == ':' and token.lengh() == 2:
                        adicionar_par(linha_num, 0, 'Operador Relacional')
                    else:                        
                        print('O token', token, 'da linha', linha_num, 'não faz parte da linguagem, verifique a digitação')

                case '>':
                    if token.lenght() == 1:
                        adicionar_par(linha_num, 1, 'Operador Relacional')
                    else:  
                        print('O token', token, 'da linha', linha_num, 'não faz parte da linguagem, verifique a digitação')
                
                case '<':
                    if token.lenght() == 1:
                        adicionar_par(linha_num, 2, 'Operador Relacional')
                    else:  
                        print('O token', token, 'da linha', linha_num, 'não faz parte da linguagem, verifique a digitação')
        
print('\nVetores:\n\nPalavras reservadas:', palavras_reservadas, '\n')
print('Operadores aritméticos: ', operadores_aritmeticos, '\n')
print('Operadores logicos: ',operadores_logicos, '\n')
print('Operadores relacionais: ',operadores_relacionais, '\n')

with open('tokens_saida.txt', 'w') as saida:
    for t in tokens:
        linha, pos, tipo = t
        saida.write(f"Linha: {linha}, Posição em seu respectivo vetor: {pos}, Tipo: {tipo}\n")