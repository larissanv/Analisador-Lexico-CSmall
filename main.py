#Importacao de classe Token
import token as Token
#biblioteca para expressao regular
import regex

class Main():

	def __init__(self):
		self.dic_tokens = {'main': 'MAIN', 'int': 'INT', 'float': 'FLOAT', 'if':'IF','else': 'ELSE','while': 'WHILE','for': 'FOR','read': 'READ','print': 'PRINT','(': 'LBRACKET',')': 'RBRACKET','{': 'LBRACE','}': 'RBRACE',',': 'COMMA',';': 'PCOMMA','=': 'ATTR','<': 'LT','<=': 'LE','>': 'GT','>=': 'GE','==': 'EQ','!=': 'NE','||': 'OR',	'&&': 'AND','+': 'PLUS','-': 'MINUS','*': 'MULT','/': 'DIV'}
		self.operadores = ['+','-','*','/','=','<','>','!','&','|']
		self.separadores = [' ', '\n', '\t', '(', ')','{','}',',',';','\r']
		
	def run(self):

		print "Analisador Lexico CSmall"

		line = ""

		# print regex.search("main", line)
		# print regex.match("main", line)
		# resultado = regex.match('[A-Za-z]([A-Za-z]|[0-9])*', line)
		# resultado = regex.match('main', line)

		# print resultado

		flag = 0
		#variavel que define o estado em que se encontra o automato  
		estado = 1
		#variavel que marca em qual linha se encontra a leitura do arquivo
		linha = 0
		#lista que armazenara os tokens
		lista_tokens = list()
		#dicionario com os tokens

		#Buffer de leitura 
		buffer = ""
		#arquivo que contem o codigo fonte a ser analisado
		arq = open('codigo-fonte.txt', 'r')
		codigofonte = list(arq.read())

		for c in codigofonte:
			# print c
			# print 'linha:' , linha

			#se o caractere lido for quebra de linha, aumenta o contador de linhas
			if c == '\n':
				linha += 1
			
			if estado == 1:
				if c in self.separadores or c in self.operadores:
					flag = 1
					if c in self.dic_tokens:
						print c
						novotoken = Token.Token( self.dic_tokens[c],c,linha)
						lista_tokens.append(novotoken)
				else:
					if flag == 1:
						print buffer
						buffer = ""
						flag = 0
					buffer = buffer + c
					# print "buffer: " + buffer
					if buffer in self.dic_tokens:
						novotoken = Token.Token( self.dic_tokens[buffer],buffer,linha)
						lista_tokens.append(novotoken)
				# if c in self.dic_tokens:
				# 	# print c
				# 	novotoken = Token.Token( self.dic_tokens[c],c,linha)
				# 	lista_tokens.append(novotoken)
		
		for i in lista_tokens:
			print str(i)
				# ' | '.join(str(notoken) for novotoken in self.lista_tokens)		
				# repr(a) for a in lista_tokens

def inicio():
		main = Main()
		main.run()

if __name__ == "__main__":
	inicio()