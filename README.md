# compilador
TRABALHO 01 DE COMPILADORES - ANÁLISE LÉXICA
ALUNOS: ISADORA COELHO E LEONARDO  CALSAVARA
NOME ESCOLHIDO: LI(C2)

TIPOS DE DADOS SUPORTADOS:
INT;
FLOAT;
BOOL.

OPERADORES SUPORTADOS:
ARITMÉTICOS BÁSICOS (‘+’, ‘-’, ‘/’, ‘*’, ‘[‘, ‘]’, ‘(‘, ‘)’)
POTENCIAÇÃO _POT(VARIÁVEL, POTÊNCIA); 
OBS: só vale para números inteiros.
OPERAÇÕES LÓGICAS:
 OR: ‘|’;
AND: ‘&’;
NOT-> ‘!’.
OPERAÇÕES RELACIONAIS:
IGUAL: ‘::’;
MENOR QUE:  ‘<’;
MAIOR QUE:  ‘>’;
DIFERENTE: ‘!=’;
MAIOR OU IGUAL ‘>=’;
MENOR OU IGUAL: ‘<=’.

FORMAÇÃO DOS IDENTIFICADORES
Declaração de variável: Não poderá começar com número ou o caractere de underline “_”.
tipo nome; ou
tipo nome = atribuição;
Para funções e palavras reservadas há necessidade de colocar um “_” antes de cada uma, sem a necessidade de espaço.

COMANDOS DE ENTRADA E SAÍDA:
ENTRADA: _receba() -> _receba(Nomevariavel);
SAÍDA: _seliga(); -> _seliga(“Alguma coisa”, Nomevariavel);

PALAVRAS-RESERVADAS:
_begin;
_end;
_receba;
_seliga;
_if;
_else;
_int;
_float;
_bool;
_while;
_true;
_false;
_pot.

ESTRUTURAS SUPORTADAS PELA LINGUAGEM:
_if( condição ){
comandos…
}
_else{
comandos…
}

while(condição ){
comandos…
}

for(int variavel; condição; incrementa){
	comandos;
}
