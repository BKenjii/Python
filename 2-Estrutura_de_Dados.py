# Estrutura de Dados em Python

# Estrutura de Dados são formas de organizar, armazenar e manipular dados de maneira eficiente.
# As principais estruturas de dados em Python são: listas, tupla e sets, dicionários e conjuntos.
# Listas são usadas para armazenar uma coleção ordenada e mutável de itens.(mutavel = pode ser alterada, adicionar ou remover itens) 
# Elas são definidas por colchetes [] e os itens são separados por vírgulas.
# Exemplo:

lista_frutas = ["maçã", "banana", "laranja"]  # lista com 3 frutas
print(lista_frutas)                           # Mostra a lista completa
print(lista_frutas[0])                        # Mostra o primeiro item da lista (maçã)  esquerda pra direita   //ordem começa pelo 0
print(lista_frutas[1])                        # Mostra o segundo  item da lista (banana)
print(lista_frutas[2])                        # Mostra o terceiro item da lista (laranja)
print(lista_frutas[-1])                       # Mostra o primeiro item da lista (laranja) da direita pra esquerda  //ordem negativa começa pelo -1
print(len(lista_frutas))                      # Mostra a quantidade de itens na lista (3)                          
#explicar sort depois

lista_frutas.append("pera")                   # O Append adiciona o item "pera" no final da lista ai fica ["maçã", "banana", "laranja", "pera"]
lista_frutas.remove("banana")                 # Remove o item "banana" da lista ficando                   ["maçã", "laranja", "pera"]
lista_frutas[1] = "abacaxi"                   # Altera o segundo item da lista para "abacaxi"             ["maçã", "abacaxi", "pera"]
lista_frutas.insert(1, "uva")                 # Adiciona a "uva" na segunda posição da lista ficando      ["maçã", "uva", "abacaxi", "pera"]
print(lista_frutas)                           # Mostra a lista
print("\n")

# Tuplas são iguais as listas, mas são imutáveis (não podem ser alteradas, adicionar ou remover itens).
# Elas são definidas por parênteses () e os itens são separados por vírgulas.
# Em tuplas Alterar, Append, Remove e Insert não funcionam
# Exemplo:

tupla_cores = ("vermelho", "verde", "azul")  # tupla com 3 cores
print(tupla_cores)                           # Mostra a tupla completa
print("\n")

# tupla_cores[1] = "amarelo"                 # Isso vai dar erro, pois tuplas são imutáveis

# Conjuntos (sets) é parecido com a Lista, armazena uma coleçao de itens e é mutavel(pode alterar) porém não permite itens duplicados e não mantém a ordem dos itens.
# Eles são definidos por chaves {} e os itens tambem são separados por vírgulas.
# Exemplo:

num = {1, 2, 3, 3, 4}                 # Conjunto com 3 números, o "3" duplicado não é considerado
print(num)                            # Mostra o conjunto, a ordem pode variar mas não vai repetir o "3"

letra = {"A", "B", "C", "A"}          # Conjunto com 3 letras, o "A" duplicado não é considerado
print(letra)                          # Mostra o conjunto, a ordem pode variar (A, B, C) ou (C, A, B) ou (B, C, A) etc mas não vai repetir o "A"

letra.add("D")                        # Adiciona o item "D" ao conjunto
letra.remove("B")                     # Remove o item "B" do conjunto mas se o item não existir vai dar erro
letra.discard("X")                    # Remove o item "X" do conjunto mas se o item não existir não vai dar erro

print("B" in letra)                   # Verifica se o item "A" está no conjunto, retorna True ou False

for l in letra:                     # Percorre cada item do conjunto
    print(l)                        # Imprimi cada item em linhas diferentes

print("\n")


# Dicionário(dict) é uma Coleção de itens que associa Chaves a Dados
# Exemplo:

aluno = {                 # Pode ser escrito assim tambem aluno = {"nome": "João", "idade": 19, "cidade": "sarandi"}
    "nome": "João",
    "idade": 19,
    "cidade": "sarandi" 
}

print(aluno)                # Mostra {'nome': 'João', 'idade': 19, 'cidade': 'sarandi'}
print(aluno["nome"])        # Mostra só "João"
print(aluno["idade"])       # Mostra só "19"

aluno["curso"] = "ADS"      # Adiciona uma nova chave e um dado a ela {'nome': 'João', 'idade': 19, 'cidade': 'sarandi', 'curso': 'ADS'}
aluno["idade"] = 21         # Altera a idade para 21
del aluno["nome"]           # Deleta a chave "nome" e seu dado "João"
print("\n")

for chave in aluno:         # Mostra somente as chaves (idade, cidade, curso)
    print(chave)

print("\n")

for info in aluno.values(): # Mostra somente os Dados das chaves(21, sarandi, ADS)
    print(info)

print("\n")

for chave, info in aluno.items(): # Mostra a chave e Dado
    print(chave, ":", info)

turma = {
    "aluno1": {"nomes": "Edu", "idade": 17},
    "aluno2": {"nomes": "Ana", "idade": 19} 
}

print(turma["aluno1"]["nomes"])