from pathlib import Path
import re  
from caminho import caminho

with caminho.open("r", encoding="utf-8") as arquivo:
	linha_1 = arquivo.readline().strip() #lê a primeira linha do arquivo
	if "INICIO" in linha_1: #se a primeira linha conter INICIO executa o restante

		while True:
			linha = arquivo.readline().strip() #as linhas que vão ser lidas 1 por 1 até o while terminar
			escreva = re.search(r"escreva\((.*?)\)", linha) #para pegar oq vai ser escrito pelo comando escreva
			leia = re.search(r"leia\((.*?)\)", linha)#para pegar os argumentos do comando leia, por exemplo "leia(escreva seu nome:)"
			var_func = re.match(r"(\w+)\s*=\s*leia\((.*?)\)", linha) #para pegar o nome das variáveis que tem leia() atribuído e verificar se o comando tem argumentos

			#verifica as variaveis no txt e cria elas no globals
			if "=" in linha and not var_func:
				nome, valor = linha.split("=", 1)
				nome = nome.strip()
				valor = valor.strip()

				try: #converte os valores numéricos
					valor = eval(valor)
				except:
					pass

				globals()[nome] = valor #salva a variável com seu valor e nome iguais aos passados no .txt

			#se encontrar um comando leia() atribuído a uma variável
			elif var_func:
				nome_var = var_func.group(1) #nome da variável
				args = var_func.group(2).strip('"') #pega os argumentos do comando leia()

				globals()[nome_var] = input(f"{args}") #aqui, replica oq foi passado no .txt, ou seja, um input atribuído a uma variável (var = leia()) com argumentos (se houver)

			#se encontrar um comando escreva
			if escreva:
				conteudo = escreva.group(1).strip()#pega oque vai ser escrito
				if conteudo in globals(): #verifica se o conteúdo dentro de escreva não é uma variável criada anteriormente
					print(globals()[conteudo]) #se for, escreve o conteúdo da variável
				else:
					print(conteudo) #se não for, escreve oq foi inserido pelo usuário

			#se encontrar um comando leia que não está atribuído a uma variável
			if leia and not var_func:
				conteudo_l = leia.group(1).strip() #aqui pega os argumentos do comando leia()
				globals()[conteudo_l] = input(f"{conteudo_l}") #aqui passa os argumentos de leia() para o input()

			if "FIM" in linha: #se encontra a palavra FIM no arquivo, encerra a execução do while
				break
	else:
		print("Erro, definição de INICIO não encontrada")