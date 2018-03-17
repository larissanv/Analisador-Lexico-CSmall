#Importacao de classe Token
import token as Token
#biblioteca para expressao regular
import regex

class Main():

	def __init__(self):
		self.dic_tokens = {'id': 'ID', 'main': 'MAIN', 'int': 'INT', 'float': 'FLOAT', 'if':'IF','else': 'ELSE','while': 'WHILE','for': 'FOR','read': 'READ','print': 'PRINT','(': 'LBRACKET',')': 'RBRACKET','{': 'LBRACE','}': 'RBRACE',',': 'COMMA',';': 'PCOMMA','=': 'ATTR','<': 'LT','<=': 'LE','>': 'GT','>=': 'GE','==': 'EQ','!=': 'NE','||': 'OR',	'&&': 'AND','+': 'PLUS','-': 'MINUS','*': 'MULT','/': 'DIV', 'num_integer': 'INTEGER_CONST', 'num_float': 'FLOAT_CONST'}
		self.operadores = ['+','-','*','/','=','<','>','!','&','|']
		self.separadores = [' ', '\n', '\t', '(', ')','{','}',',',';','\r']
		
	def num_inteiro(self, token):
		result = regex.match("^-?\\d*(\\d+)?$", token)
		if result == None:
			return False
		else:
			 return True

	def num_float(self, token):
		result = regex.match("([0-9]+[.])+[0-9]+", token)
		if result == None:
			return False
		else:
			 return True
	
	def identificador(self, token):
		result = regex.match('[A-Za-z]([A-Za-z]|[0-9])*', token)
		if result == None:
			return False
		else:
			 return True

	def run(self):

		print "Analisador Lexico CSmall"

		flag = 0
		#variavel que define o estado em que se encontra o automato  
		estado = 1
		#variavel que marca em qual linha se encontra a leitura do arquivo
		linha = 0
		#lista que armazenara os tokens
		lista_tokens = list()
		#Buffer de leitura 
		buffer = ""
		#arquivo que contem o codigo fonte a ser analisado
		arq = open('codigo-fonte.txt', 'r')
		codigofonte = list(arq.read())

		for c in codigofonte:
			
			#se o caractere lido for quebra de linha, aumenta o contador de linhas
			if c == '\n':
				linha += 1
			
			# if estado == 1:
			if c in self.separadores or c in self.operadores:
				flag = 1
				if c in self.dic_tokens:
					# print c
					novotoken = Token.Token(self.dic_tokens[c],c,linha)
					lista_tokens.append(novotoken)
				
			else:
				if flag == 1:
					if buffer in self.dic_tokens:
						novotoken = Token.Token(self.dic_tokens[buffer],buffer,linha)
						lista_tokens.append(novotoken)
					else:
						if self.num_inteiro(buffer):
							novotoken = Token.Token(self.dic_tokens['num_integer'],buffer,linha)
						elif self.num_float(buffer):
							novotoken = Token.Token(self.dic_tokens['num_float'],buffer,linha)
						elif self.identificador(buffer):
							novotoken = Token.Token(self.dic_tokens['id'],buffer,linha)

						lista_tokens.append(novotoken)

					# print buffer
					buffer = ""
					flag = 0
				# else:
				# 	if buffer in self.dic_tokens:
				# 		novotoken = Token.Token( self.dic_tokens[buffer],buffer,linha)
				# 		lista_tokens.append(novotoken)
				# 		buffer = ""

				buffer = buffer + c
		
		for i in lista_tokens:
			print str(i)
	

def inicio():
		main = Main()
		main.run()

if __name__ == "__main__":
	inicio()