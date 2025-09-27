# Sintaxe basica em Python

# o Hashtag (#) se usado ira criar um  comentário, mensagem transparente que é ignorada pelo codigo.
# o Hashtag (#) pode ser tanto no inicio da linha ou no final dela.

# Variaveis em Python
# As Variaveis em Python são dinamicas, ou seja, não é necessário declarar o tipo de dado que a variavel ira armazenar.
# Ao inves de declarar uma variavel como int, float, str, etc, você simplesmente atribui um valor a ela.
# Nome da variavel deve começar com uma letra ou um underline (_), e pode conter letras, numeros e underscores.
# Exemplo:

nome = "João"           # Variavel do tipo string   (letra/texto)
idade = 25              # Variavel do tipo inteiro  (numero sem casa decimal)
altura = 1.83           # Variavel do tipo float    (numero com casa decimal)
estudante = True        # Variavel do tipo booleano (True ou False: verdadeiro ou falso)
_nome_Amigo = "Andre"   # Variavel com underline no inicio
idade2 = 30             # Variavel com numero no final

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
# Você pode separar diferentes itens no print() com uma vírgula (,) e o python irá adicionar um espaço entre eles automaticamente.
# Voce pode usar o \n no print() que ele ira pular uma linha apos ou durante a mensagem. dependendo de onde for colocado.
# Exemplo: 

print("Bom dia, Mundo!")          # Mostra a mensagem "Bom dia, Mundo!" no console
print("Nome:", nome)              # Mostra a mensagem "Nome: João"
print(a + b)                      # Mostra o resultado da soma (15)
print("Bom" "dia")                # Mostra a mensagem "Bomdia" (sem espaço entre as palavras)
print("Bom", "dia")               # Mostra a mensagem "Bom dia" (com espaço entre as palavras)
print("idade:", idade, "anos\n")  # Mostra a mensagem "idade: 25 anos"

#Entrada de Dados
# A função input() é usada para receber dados do usuário.
# O input() sempre retorna uma string, então se você precisar de outro tipo de dado, é necessário converter. passando um tipo de variavel antes do input() Ex: Float(), int() 
# Exemplo:

Usuario = input("Digite seu nome: ")              # Mostra na Tela "Digite seu nome: " e espera o usuario digitar algo
Idade_Usuario = int(input("Digite sua idade: "))  # Mostra na Tela "Digite sua idade: " e como usamos int() ele espera o usuario digitar um numero inteiro

print("Olá", Usuario, "voce tem", Idade_Usuario, "anos\n") # Mostra a mensagem "Olá [Nome do Usuario] voce tem [Idade do Usuario] anos" 

# Operadores de Comparação
# Os operadores de comparação são usados para comparar dois valores.
# Eles Sâo > (maior que),  < (menor que),  >= (maior ou igual a),  <= (menor ou igual a),  == (exatamente igual a),  != (diferente de).
# Eles retornam um valor booleano (True ou False) com base na comparação.
# Exemplo:

p = 10
o = 5
print(p == o)       # 10 não é igual a 5 (False) falso
print(p != o)       # 10 e 5 são diferentes (True) verdadeiro
print(p > o, "\n")  # 10 é maior que 5 (True) verdadeiro

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
    
# Operadores lógicos
# Os operadores lógicos são usados para ter mais de uma condição em uma estrutura condicional.
# Os principais operadores lógicos são: and (e), or (ou), not (não)
# Voce pode usar quantos operadores logicos quiser em uma unica estrutura condicional.
# Exemplo:

paulo = 17
caio  = 24
chovendo = True

if paulo >= 18 and caio >= 18:
    print("Os dois são maiores de idade")         # Se paulo e caio tiverem 18 ou mais anos    
else:
    print("Pelo menos um deles é menor de idade") # Se pelo menos algum deles tiver menos de 18 anos


if paulo or caio >= 18:
    print("Algum deles é maior de idade")         # Pelo menos um deles tem que ser maior de idade
else:
    print("Nenhum deles é maior de idade")        # Nenhum deles é maior de idade


if not chovendo:
    print("Não esta chovendo")                    # Se não estiver chovendo: chovendo = False     
else:
    print("ta chovendo")                          # Se estiver chovendo: chovendo = True


if (paulo and caio >= 18) and not chovendo:
    print("Os dois são maiores de idade e não esta chovendo\n") # Se os 2 tiverem 18 ou mais anos e não estiver chovendo
else:
    print("Algum deles é menor de idade ou esta chovendo\n")    # Se algum deles tiver menos de 18 anos ou estiver chovendo

# Estrutura de Repetição
# É uma Estrutura que pode repetir uma parte do codigo uma determinada quantidade definida ou enquanto uma condição for verdadeira.
# As principais estruturas de repetição em Python são: for e while.    
# O for é usado para percorrer sobre uma sequência (como uma lista, string,) ou uma determinada quantidade de números.  ////////////(ver depois tupla, dicionário, conjunto e string)
# O while é usado para repetir um bloco de código enquanto uma condição for verdadeira.
# Exemplo:

for i in range(5):    # Repete o bloco de código 5 vezes (de 0 a 4)
    print(i)          # Mostra os números de 0 a 4 


carta = 6

while carta >= 0:                                                       # Enquanto a carta for maior ou igual a 0
    print("Voce descartou uma carta e agora tem:", carta, " cartas")    # Mostra uma mensagem com a quantidade de cartas
    carta -= 1                                                          # Diminui 1 carta a cada repetição


senha = "1234"                             
tentativa = ""

while tentativa != senha:                           # Enquanto a tentativa for diferente da senha
    tentativa = input("\nDigite a senha:")          # Digita a senha
    if tentativa != senha:                          # Se errar a senha
        print("Senha incorreta, tente novamente.")  # Mostra a mensagem que a senha esta incorreta

print("Senha correta!")                     # Mostra a mensagem quando a senha estiver correta
