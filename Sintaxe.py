# Sintaxe basica em Python

# o Hashtag (#) se usado ira criar um  comentário, mensagem transparente que é ignorada pelo codigo.
# o Hashtag (#) pode ser tanto no inicio da linha ou no final dela.

# Variaveis em Python
# As Variaveis em Python são dinamicas, ou seja, não é necessário declarar o tipo de dado que a variavel ira armazenar.
# Ao inves de declarar uma variavel como int, float, str, etc, você simplesmente atribui um valor a ela.
# Nome da variavel deve começar com uma letra ou um underline (_), e pode conter letras, numeros e underscores.
# Exemplo:

nome = "João"  # Variavel do tipo string
idade = 25     # Variavel do tipo inteiro
altura = 1.83  # Variavel do tipo float
estudante = True  # Variavel do tipo booleano
_nome_Amigo = "Andre" # Variavel com underline no inicio
idade2 = 30 # Variavel com numero no final

# Operações Matematicas
a = 10
b = 5
soma            = a + b  #resultado 15
subtracao       = a - b  #resultado 5
multiplicacao   = a * b  #resultado 50
divisao         = a / b  #resultado 2.0
divisao_inteira = a // b #resultado 2
modulo          = a % b  #resultado 0
exponenciacao   = a ** b #resultado 100000

# Operadores de Atribuição
# Os operadores de atribuição são usados para modificar o valor de uma variável de forma abreviada.
# Eles combinam uma operação matemática com a atribuição.
# Exemplo:
x = 10   # Atribuição simples
x += 5   # x = x + 5 (x agora é 15)
x -= 3   # x = x - 3 (x agora é 12)
x *= 2   # x = x * 2 (x agora é 24)
x /= 4   # x = x / 4 (x agora é 6.0)

# Função de Impressão
# A função print() é usada para exibir mensagens e dados na tela.
# No print() aspas duplas ou simples (") (') são usadas para definir strings (textos).
# Você pode usar o print() para exibir variaveis, textos ou uma combinação de ambos.
# Você pode separar diferentes itens no print() com uma vírgula (,)
# Exemplo: 

print("Bom dia, Mundo!")        # Mostra a mensagem "Bom dia, Mundo!" no console
print("Nome:", nome)            # Mostra a mensagem "Nome: João"
print(a + b)                    # Mostra o resultado da soma (15)
print("Bom" "dia")              # Mostra a mensagem "Bomdia" (sem espaço entre as palavras)
print("Bom", "dia")             # Mostra a mensagem "Bom dia" (com espaço entre as palavras)
print("idade:", idade, "anos")  # Mostra a mensagem "idade: 25 anos"

#Entrada de Dados
# A função input() é usada para receber dados do usuário.
# O input() sempre retorna uma string, então se você precisar de outro tipo de dado, é necessário converter. passando um tipo de variavel antes do input() Ex: Float(), int() 
# Exemplo:

Usuario = input("Digite seu nome: ")                     # Mostra na Tela "Digite seu nome: " e espera o usuario digitar algo
Idade_Usuario = int(input("Digite sua idade: "))         # Mostra na Tela "Digite sua idade: " e como usamos int() ele espera o usuario digitar um numero inteiro

print("Olá", Usuario, "voce tem", Idade_Usuario, "anos") # Mostra a mensagem "Olá [Nome do Usuario] voce tem [Idade do Usuario] anos" 

# Operadores de Comparação
# Os operadores de comparação são usados para comparar dois valores.
# Eles Sâo > (maior que),  < (menor que),  >= (maior ou igual a),  <= (menor ou igual a),  == (exatamente igual a),  != (diferente de).
# Eles retornam um valor booleano (True ou False) com base na comparação.
# Exemplo:

p = 10
o = 5
print(p == o)  # 10 não é igual a 5 (False) falso
print(p != o)  # 10 e 5 são diferentes (True) verdadeiro
print (p > o)  # 10 é maior que 5 (True) verdadeiro

# Operador Condicional
# São usadas para criar decisões no código com base em condições estabelecidas.
# As principais estruturas condicionais são: if, elif e else.
# O if é usado para verificar uma condição. Se a condição for verdadeira (True), o código dentro do if será executado.
# O elif (else if) funciona como o if ele é pra verificar uma nova condição caso o if ou a condição anterior seja falsa, mas é opcional e apenas deve ser usado após um if inicial e pode colocar quantos forem necessários.
# O else é usado caso nenhuma das condições anteriores sejam verdadeira, ele tambem é opcional e deve ser usado apenas no Final da estrutura condicional.
# Exemplo:

idade3 = 19

if idade3 < 18:
    print("Menor de idade")  # Se a idade for menor que 18, mostra "Menor de idade"
elif idade3 == 18:
    print("Tem 18 anos")     # Se a idade for exatamente 18, mostra "Tem 18 anos"
else:
    print("Maior de idade")  # Se a idade for maior que 18, mostra "Maior de idade"
    
# Estrutura de Repetição
# É uma parte do codigo que ira se repetir enquanto uma condição for verdadeira.
# As principais estruturas de repetição em Python são: for e while.    