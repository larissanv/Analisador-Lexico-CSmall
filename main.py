#Importacao de classe Token
import token as Token

def dicionario():
		dic_tokens = {
		'main': 'MAIN',
		'int': 'INT', 
		'float': 'FLOAT', 
		'if':'IF',
		'else': 'ELSE',
		'while': 'WHILE',
		'for': 'FOR',
		'read': 'READ',
		'print': 'PRINT',
		'(': 'LBRACKET',
		')': 'RBRACKET',
		'{': 'LBRACE',
		'}': 'RBRACE',
		',': 'COMMA',
		';': 'PCOMMA',
		'=': 'ATTR',
		'<': 'LT',
		'<=': 'LE',
		'>': 'GT',
		'>=': 'GE',
		'==': 'EQ',
		'!=': 'NE',
		'||': 'OR',
		'&&': 'AND',
		'+': 'PLUS',
		'-': 'MINUS',
		'*': 'MULT',
		'/': 'DIV'
	}
		return dic_tokens


def main():

	print "Analisador Lexico CSmall"

	#variavel que define o estado em que se encontra o automato  
	estado = 1
	#variavel que marca em qual linha se encontra a leitura do arquivo
	linha = 0
	#lista que armazenara os tokens
	lista_tokens = list()
	#dicionario com os tokens
	dic = dicionario()

	#arquivo que contem o codigo fonte a ser analisado
	arq = open('codigo-fonte.txt', 'r')
	caracteres = list(arq.read())

	for c in caracteres:
		# print c
		# print 'linha:' , linha

		#se o caractere lido for quebra de linha, aumenta o contador de linhas
		if c == '\n':
			linha += 1
		
		if estado == 1:
			if c in dic:
				novotoken = Token.Token(c,dic[c],linha)
				lista_tokens.append(novotoken)
		# elif estado == 2:
	
	# print "lista->", lista_tokens[10].lexema , '\n'


if __name__ == "__main__":
	main()