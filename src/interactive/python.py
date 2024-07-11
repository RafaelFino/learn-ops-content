#!/usr/bin/env python3

# Importing the chat class from the talker module
from talker import chat

# Tema: Python
# Sobre as aulas:
# O professor fala sobre o tema e o aluno interage com o professor.
# O aluno pode fazer perguntas e o professor responde.
# A conversa deve ser descontraída, o aluno não possui muito conhecimento sobre o assunto, não sabe muito sobre o tema, mas sempre se mostra muito curioso e quer saber as aplicações práticas do tema.
# Os comandos que o professor deve ensinar, serão apenas de exemplo, não serão executados localmente no terminal, mas devem estar conectados com o tema e mostrando cenários práticos.
# Cada comando exposto pelo professor deve ser explicado para o aluno de forma bem informal mas clara.
# O professor deve expor cenários com bom humor, trazendo leveza e descontração para a aula, tentando ao máximo descomplicar o assunto para o aluno.
# O aluno deve interagir com o professor, fazendo perguntas e tirando dúvidas sobre o tema.
# O professor deve ser paciente e explicar o tema de forma que o aluno entenda.
# O aluno deve se sentir à vontade para perguntar e interagir com o professor.
# O professor deve sempre incentivar o aluno a participar e perguntar.
# O professor deve sempre manter o aluno interessado e curioso sobre o tema.
# O professor deve sempre encorajar o aluno a praticar o que foi ensinado. 
# O aluno deve sempre se sentir motivado a aprender mais sobre o tema.
# O professor sempre que possível, deve indicar materiais para o aluno estudar além dessa aula, como links e livros sobre o tema
# Sempre que o aluno entender um tema e trocar para outro tema, deve tentar se despedir do professor e o professor, com uma piada, deve dizer que a aula não terminou e que ele ainda tem muito a aprender.
# A cada Interação e troca de tema, as frases devem ser diferentes para não parecer uma cópia ou repetição durante o dialogo.
# Os alunos devem ser chamados de "Doenças", "Pobres", "Padawans", "Pequenos Gafanhotos", "Jovem Tartarugas" e outros jargões da cultura pop para se referir a aprendizes.
# Sobre o tema:

c = chat.Chat()
c.Speak("""E aí meu jovem padawan, como você está?""")
c.StudentComment(f"Estou bem {c.Teacher()}, e você?")
c.Speak("""Estou ótimo, obrigado por perguntar. Estava pensando em falar sobre Python, o que acha?""")
c.StudentComment("""Python? o que é isso?""")
c.Speak("""Python é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica, forte e multiplataforma. Ufa!""")
c.StudentComment("""Nossa, é muita coisa...""")
c.Speak("""Calma, não é tão complicado quanto parece. Python é uma linguagem muito versátil e fácil de aprender. Quer ver um exemplo?""")
c.StudentComment("""Claro!""")
c.Speak("""Vamos criar um programa que imprime 'Olá, mundo!' na tela. O que acha?""")
c.StudentComment("""Legal!""")
c.Speak("""Vamos lá!""")
c.ShowCodeAndRun("""
print('Olá, mundo!')
""")
c.Speak("""Viu como é simples?""")
c.StudentComment("""Sim, muito simples!""")
c.Speak("""Python é uma linguagem muito poderosa e com uma sintaxe muito limpa e fácil de entender. Quer aprender mais?""")
c.StudentComment("""Claro!""")
c.Speak("""Então vamos lá!""")
c.Speak("""Vamos falar sobre variáveis em Python. O que são variáveis?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""Poxa aspira... assim você me mata, você sabe que temos uma outra aula só para falar disso, não? se chama 'vars' e a essa altura você já deveria ter feito...""")
c.Speak("""Mas vou te explicar e dar um desconto pois é muito conteúdo mesmo... Variáveis são espaços de memória que armazenam valores. Em Python, você pode criar uma variável e atribuir um valor a ela. Quer ver um exemplo?""")
c.StudentComment("""Sim!""")
c.Speak("""Vamos criar uma variável chamada 'nome' e atribuir o valor 'Fulano' a ela. O que acha?""")
c.StudentComment("""Legal!""")
c.ShowCode("""
nome = 'Fulano'
""")
c.Speak("""Agora a variável 'nome' armazena o valor 'Fulano'. Quer ver o valor dessa variável?""")
c.StudentComment("""Sim!""")
c.ShowCodeAndRun("""
nome = 'Fulano'
print(nome)
""")
c.Speak("""Viu como é simples?""")
c.StudentComment("""Sim, muito simples!""")
c.Speak("""Python é uma linguagem muito poderosa e com uma sintaxe muito limpa e fácil de entender. Quer aprender mais?""")
c.StudentComment("""Claro!""")
c.Speak("""Então vamos lá!""")
c.Speak("""Python usa uma forma bem peculiar para definir blocos de código. Você sabe o que são blocos de código?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""Blocos de código são trechos de código que são executados juntos. Em Python, os blocos de código são definidos por indentação. Quer ver um exemplo?""")
c.StudentComment("""Sim!""")
c.Speak("""Vamos criar um bloco de código que imprime 'Olá, mundo!' na tela. O que acha?""")
c.StudentComment("""Legal!""")
c.Speak("""Vamos lá!""")
c.ShowCodeAndRun("""
if True:
    print('Olá, mundo!')
""")
c.Speak("""Viu como é simples?""")
c.StudentComment("""Sim, muito simples!""")
c.Speak("""Só tome bastante cuidado, no python você pode usar espaços ou tabulações para fazer a indentação, mas não misture os dois, senão o python vai reclamar...""")
c.StudentComment("""Entendi!""")
c.Speak("""Mas eu usei ali o 'if True', você sabe o que é isso?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""O 'if' é uma estrutura de controle que permite executar um bloco de código se uma condição for verdadeira. Quer ver um exemplo?""")
c.StudentComment("""Sim!""")
c.Speak("""Vamos criar um bloco de código que imprime 'Olá, mundo!' na tela se a variável 'condicao' for verdadeira. O que acha?""")
c.StudentComment("""Legal!""")
c.ShowCodeAndRun("""
condicao = True
if condicao:
    print('Olá, mundo!')
""")
c.Speak("""Tá tranquilo até aqui?""")
c.StudentComment("""Sim! Até agora até eu consigo entender...""")
c.Speak("""Bom, nós temos uma outra aula só para falar de condicionais, os tais 'Ifs' que eu te mostrei, você deveria fazer essa também!""")
c.StudentComment("""Claro! Foi mal, é muito conteúdo, vou tentar acompanhar...""")
c.Speak("""Vamos falar sobre listas em Python. O que são listas?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""Listas são coleções de elementos em Python. Você pode criar uma lista e adicionar elementos a ela. Quer ver um exemplo?""")
c.StudentComment("""Sim! Por favor... não vi isso nos materiais preparatórios... ou se vi fui um vacilão e não prestei atenção...""")
c.Speak("""Vamos criar uma lista chamada 'numeros' e adicionar os números de 1 a 5 a ela. O que acha?""")
c.StudentComment("""Legal!""")
c.ShowCode("""
numeros = [1, 2, 3, 4, 5]
""")
c.Speak("""Agora a lista 'numeros' contém os números de 1 a 5. Quer ver o conteúdo dessa lista?""")
c.StudentComment("""Sim!""")
c.ShowCodeAndRun("""
numeros = [1, 2, 3, 4, 5]
print(numeros)
""")
c.Speak("""Viu como é simples?""")
c.StudentComment("""Sim, muito simples!""")
c.StudentComment("""Agora que você me mostrou, eu lembrei que vi isso sim... mas ainda não entendi direito...""")
c.Speak("""Não tem problema, eu estou aqui para te ajudar. Quer aprender mais sobre listas?""")
c.StudentComment("""Claro!""")
c.Speak("""Então vamos lá!""")
c.Speak("""Python tem uma forma bem interessante de acessar elementos de uma lista. Você sabe o que são índices?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""Show de decepção hein aspira... já vimos isso várias vezes... se você não se dedicar vai ficar complexo de virar um bom dev...""")
c.Speak("""Índices são posições dos elementos em uma lista. Em Python, os índices começam em 0. Quer ver um exemplo?""")
c.StudentComment("""Sim!""")
c.Speak("""Vamos acessar o primeiro elemento da lista 'numeros'. O que acha?""")
c.StudentComment("""Legal!""")
c.ShowCodeAndRun("""
numeros = [1, 2, 3, 4, 5]
print(numeros[0])
""")
c.Speak("""Vamos brincar um pouco com essa lista... e se tentarmos colocar mais um número nela?""")
c.StudentComment("""Legal!""")
c.ShowCodeAndRun("""
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)
""")
c.Speak("""Viu como é simples? tenho certeza de que você também consegue... agora vamos tentar remover um número dessa lista...""")
c.ShowCodeAndRun("""
numeros = [1, 2, 3, 4, 5]
numeros.remove(3)
print(numeros)
""")
c.Speak("""Fizemos uma coisa interessante aqui, não é mesmo? Vou te explicar o que fizemos...""")
c.Speak("""O método 'append' adiciona um elemento ao final da lista. Já o método 'remove' remove um elemento da lista. Entendeu?""")
c.Speak("""O métido 'remove' espera como parametro o valor do elemento que você quer remover, já o 'append' não espera nada, ele apenas adiciona um elemento ao final da lista...""")
c.StudentComment("""Não entendi direito esse método 'remove', ele espera a posição que vamos remover ou o valor que queremos remover?""")
c.Speak("""O método 'remove' espera o valor do elemento que você quer remover. Se você quiser remover um elemento de uma lista, você precisa informar o valor desse elemento. Entendeu?""")
c.Question("""E se eu quiser remover o item em uma posição específica da lista?""")
c.Speak("""Para remover um elemento de uma lista em uma posição específica, você pode usar a função 'pop'. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
numeros = [1, 2, 3, 4, 5]
numeros.pop(2)
print(numeros)
""")
c.Speak("""Viu como é simples?""")
c.StudentComment("""Sim, muito simples! Poderia resumir esses 3 métodos que acabamos de ver por favor?""")
c.Speak("""Claro! O método 'append' adiciona um elemento ao final da lista, o método 'remove' remove um elemento da lista pelo valor e o método 'pop' remove um elemento da lista pela posição. Entendeu?""")
c.StudentComment("""Está ficando mais claro agora... e o que é esse 'print' que você usa para mostrar o conteúdo da lista?""")
c.Speak("""O 'print' é uma função que imprime o conteúdo de uma variável na tela. É muito útil para debugar o código e ver o que está acontecendo. Entendeu?""")
c.StudentComment("""Agora que você me explicou, eu lembrei que vi isso sim... mas ainda não entendi direito... consegue me mostrar um exemplo mais prático, com listas de textos por exemplo?""")
c.Speak("""Claro! Vamos criar uma lista de nomes e mostrar o conteúdo dessa lista. Depois vamos adicionar itens, remover itens tanto por nome como por posição, exibir os resultados e explicar cada passo. O que acha?""")
c.ShowCodeAndRun("""
nomes = ['Fulano', 'Ciclano', 'Beltrano']
print('Vamos mostrar a lista completa aqui')
print(nomes)
print('Agora vamos adicionar um nome à lista')
nomes.append('José')
print('Agora vamos mostrar a lista com o novo nome')           
print(nomes)
print('Agora vamos remover um nome da lista: Ciclano')
nomes.remove('Ciclano')
print('Agora vamos mostrar a lista sem o nome Ciclano')
print(nomes)
print('Agora vamos remover o primeiro nome da lista')
nomes.pop(0)
print('Agora vamos mostrar a lista sem o primeiro nome')
print(nomes)
""")
c.Speak("""Viu como é simples? Espero que tenha ficado claro!""")
c.Speak("""Como já disse em outras aulas, um ótimo livro para estudar e entender essas estruturas é o livro 'Estrutura de Dados Fundamentais' do professor da FATEC-SP e IME, Silvio do Lago Pereira. Recomendo a leitura!""")
c.StudentComment("""Obrigado pela dica, vou procurar esse livro!""")
c.Speak("""Mas vamos voltar para o python...""")
c.Speak("""Vamos falar um pouco mais sobre os condicionais...""")
c.Speak("""Você sabe o que são condicionais?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""Mas deveria, são a base da programação. Condicionais são estruturas de controle que permitem executar um bloco de código se uma condição for verdadeira. Vamos fazer um exemplo com um IF e ELSE""")
c.ShowCodeAndRun("""
minhaVar = False
if minhaVar == False:
    print('Minha variável é falsa')
else:
    print('Minha variável é verdadeira')
""")
c.Speak("""Viu como é simples? Mas preste atenção aos detalhes, o 'if' é o comando, depois dele é preciso deixar clara uma expressão/condição que pode ser avaliada para um resultado booleano. Em python, ao final de cada instrução condicional, é necessário colocar ':'""")
c.StudentComment("""E se a condição for falsa?""")
c.Speak("""Se a condição for falsa, o bloco de código do 'else' será executado. Entendeu?""")
c.Speak("""Sempre preste atenção a identação, em python, a identação é muito importante, pois é ela que define os blocos de código. Se você não identar corretamente, o python vai reclamar...""")
c.Speak("""Outro ponto, tudo o que estiver na 'mesma linha' do que estiver abaixo do 'if' será considerado. Mas não se preocupe, com a prática você vai pegar o jeito!""")
c.Speak("""Agora vamos falar dos operadores de comparação... presta atenção pois isso é MUITO IMPORTANTE E JÁ FALAMOS ISSO NA AULA DE IFs!""")
c.Speak("""Os operadores de comparação são usados para comparar valores. Vamos ver os principais operadores de comparação em Python""")
c.Speak("""O operador de igualdade é o '=='. Ele verifica se dois valores são iguais. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 5 == 5:
    print('5 é igual a 5')
""")
c.Speak("""Complicado?""")
c.StudentComment("""É... olhando assim parece de boa""")
c.Speak("""Agora vamos falar do operador de diferença, que é o '!='. Ele verifica se dois valores são diferentes. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 5 != 5:
    print('5 é diferente de 5')
else:
    print('5 não é diferente de 5')
""")
c.Speak("""Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""Agora vamos falar do operador de maior que, que é o '>'. Ele verifica se um valor é maior que outro. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 5 > 3:
    print('5 é maior que 3')
""")
c.Speak("""Pegou a ideia?""")
c.StudentComment("""Usando exemplos simples assim, parece que tá de boa""")
c.Speak("""Agora vamos falar do operador de menor que, que é o '<'. Ele verifica se um valor é menor que outro. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 3 < 5:
    print('3 é menor que 5')
""")
c.Speak("""Agora vamos falar do operador de maior ou igual a, que é o '>='. Ele verifica se um valor é maior ou igual a outro. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 5 >= 5:
    print('5 é maior ou igual a 5')
""")
c.Speak("""Agora vamos falar do operador de menor ou igual a, que é o '<='. Ele verifica se um valor é menor ou igual a outro. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 3 <= 5:
    print('3 é menor ou igual a 5')
""")
c.Speak("""Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""Agora vamos falar do operador de 'in', que verifica se um valor está contido em uma lista. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 3 in [1, 2, 3, 4, 5]:
    print('3 está na lista')
""")
c.Speak("""Agora vamos falar do operador de 'not in', que verifica se um valor não está contido em uma lista. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 6 not in [1, 2, 3, 4, 5]:
    print('6 não está na lista')
""")
c.Speak("""Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""Agora vamos falar do operador de 'is', que verifica se dois objetos são o mesmo objeto. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
a = [1, 2, 3]
b = a
if a is b:
    print('a e b são o mesmo objeto')
""")
c.Speak("""Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""Agora vamos falar do operador de 'is not', que verifica se dois objetos não são o mesmo objeto. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
a = [1, 2, 3]
b = [1, 2, 3]
if a is not b:
    print('a e b não são o mesmo objeto')
""")
c.Speak("""Percebe que mesmo com os mesmos valores, a e b são objetos diferentes?""")
c.Question("""Sim, entendi, mas essa me deixou meio confuso, não são as mesmas coisas?""")
c.Speak("""Não, a e b são objetos diferentes, mesmo que tenham os mesmos valores. Quando você cria essas variáveis em python, você está criando objetos diferentes. Na memória do computador, a e b são objetos diferentes. É como se você tivesse dois pães, eles são do mesmo tipo, podem ser bem parecidos, mas são dois itens diferentes.""")
c.Speak("""Acabei usando o not mas não falei dele, o 'not' é um operador de negação, ele inverte o valor de uma expressão. Olha mais um exemplo:""")
c.ShowCodeAndRun("""
if not 5 == 5:
    print('5 não é igual a 5')
else:
    print('5 é igual a 5')
""")
c.Speak("""Entendeu? Esse cara é um pouco mais complicado, mas com a prática você pega o jeito!""")
c.StudentComment("""Está ficando mais claro, acho que eu que sou burro e demoro para entender mesmo""")
c.Speak("""Não se preocupe, é normal ter dúvidas. Estou aqui para te ajudar. Quer aprender mais sobre operadores de comparação?""")
c.StudentComment("""Claro! Poderia de forma simples e bem resumida me explicar o que são esses operadores para tentar fixar aqui na cachola?""")
c.Speak("""Claro! 
O operador de igualdade '==' verifica se dois valores são iguais. 
O operador de diferença '!=' verifica se dois valores são diferentes. 
O operador de maior que '>' verifica se um valor é maior que outro. 
O operador de menor que '<' verifica se um valor é menor que outro. 
O operador de maior ou igual a '>=' verifica se um valor é maior ou igual a outro. 
O operador de menor ou igual a '<=' verifica se um valor é menor ou igual a outro. 
O operador de 'not' inverte o valor de uma expressão.
O operador de 'in' verifica se um valor está contido em uma lista. 
O operador de 'not in' verifica se um valor não está contido em uma lista. 
O operador de 'is' verifica se dois objetos são o mesmo objeto. 
O operador de 'is not' verifica se dois objetos não são o mesmo objeto. 
Entendeu?""")
c.StudentComment("""Acho que sim... vamos em frente""")
c.Speak("""Agora vamos falar dos operadores lógicos. Você sabe o que são operadores lógicos?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""Os operadores lógicos são usados para combinar expressões condicionais. Vamos ver os principais operadores lógicos em Python""")
c.Speak("""O operador 'and' verifica se duas expressões são verdadeiras. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 5 > 3 and 5 < 10:
    print('5 é maior que 3 e menor que 10')
""")
c.Speak("""O operador 'and' só retorna verdadeiro se as duas expressões forem verdadeiras. Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""Agora vamos falar do operador 'or', que verifica se pelo menos uma das expressões é verdadeira. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if 5 > 10 or 5 < 10:
    print('5 é maior que 10 ou menor que 10')
""")
c.Speak("""O operador 'or' retorna verdadeiro se pelo menos uma das expressões for verdadeira. Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""Agora vamos falar novamente do operador 'not', que inverte o valor de uma expressão. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
if not 5 == 10:
    print('5 não é igual a 10')
""")
c.Speak("""O operador 'not' inverte o valor da expressão. Entendeu?""")
c.StudentComment("""Sim, entendi! Consegue resumir aqui para anotar na minha cola?""")
c.Speak("""Claro! 
O operador 'and' verifica se duas expressões são verdadeiras. 
O operador 'or' verifica se pelo menos uma das expressões é verdadeira. 
O operador 'not' inverte o valor de uma expressão.
Entendeu?""")
c.Speak("""Agora vamos falar sobre os loops em Python. Você sabe o que são loops?""")
c.StudentComment("""É tipo algo que fica repetindo e acontecendo várias vezes? Eu sou meio lerdo, não sei direito na verdade...""")
c.Speak("""Isso mesmo! Os loops são estruturas de controle que permitem executar um bloco de código várias vezes. Vamos ver os principais loops em Python""")
c.Speak("""O loop 'for' é usado para iterar sobre uma sequência de elementos. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
for i in range(5):
    print(i)
""")
c.Speak("""O loop 'for' itera sobre a sequência de elementos de 0 a 4. Entendeu?""")
c.StudentComment("""Não muito, parece meio estranho, o que é esse 'range' aí?""")
c.Speak("""O 'range' é uma função que gera uma sequência de números. O 'range(5)' gera uma sequência de números de 0 a 4. Entendeu?""") 
c.Question("""Está melhorando... e quando eu usaria um loop assim?""")
c.Speak("""Você usaria um loop 'for' quando quiser iterar sobre uma sequência de elementos. Por exemplo, se você quiser imprimir os números de 0 a 4, você usaria um loop 'for'. Entendeu?""")
c.StudentComment("""Iterar? Você escreveu errado? não seria Interar? Fiquei confuso...""")
c.Speak("""Não, não escrevi errado. Iterar significa percorrer, passar por cada elemento da sequência. Não deixa de ser uma interação pois interagimos com cada elemento da sequência. É um termo técnico super comum, você vai pegar o jeito com a prática!""")
c.StudentComment("""Acho que estou entendendo, mas poderia me mostrar um exemplo mais prático?""")
c.Speak("""Claro! Vamos criar um loop 'for' que itera sobre uma lista de nomes e imprime cada nome. Vamos ver o exemplo""")
c.ShowCodeAndRun("""
nomes = ['Fulano', 'Ciclano', 'Beltrano']
                 
# Itera sobre a lista de nomes e imprime cada nome
for nome in nomes:
    # Imprime um nome de cada vez
    print(nome)
""")
c.Speak("""O loop 'for' itera sobre a lista de nomes e imprime cada nome. Vamos para um exemplo mais prático ainda""")
c.Speak("""Vamos criar um loop 'for' que itera sobre uma lista de números e soma cada número. Vamos ver o exemplo""")
c.ShowCodeAndRun("""
numeros = [1, 2, 3, 4, 5]
soma = 0
                 
# Itera sobre a lista de números e soma cada número
for numero in numeros:
    # Soma o número
    soma = soma + numero
        
# Imprime a soma, deveria ser 15
print(soma)
""")
c.Speak("""O loop 'for' itera sobre a lista de números e soma cada número. Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""Vamos resolver um problema comum em entrevistas para desenvolvedores? Um problema que normalmente é resolvido com loops...""")
c.Speak("""Vamos criar um programa que imprime os números de 1 a 12. O que acha?""")
c.StudentComment("""Legal!""")
c.Speak("""Vamos lá!""")
c.ShowCodeAndRun("""
for i in range(1, 13):
    print(i)
""")
c.Speak("""Viu como é simples?""")
c.Speak("""Agora vamos para um de verdade, por exemplo, implementar uma função que diz se uma palavra é um palíndromo ou não...""")
c.Speak("""Você sabe o que é um palíndromo?""")
c.StudentComment("""Não faço ideia...""")
c.Speak("""Um palíndromo é uma palavra que se lê da mesma forma de trás para frente. Por exemplo, 'ovo' é um palíndromo. Entendeu?""")
c.StudentComment("""Entendi!""")
c.Speak("""Vamos criar uma função que verifica se uma palavra é um palíndromo ou não. Vamos ver o exemplo""")
c.ShowCodeAndRun("""
def palindromo(palavra) -> bool:
    if palavra == palavra[::-1]:
        return True
    else:
        return False
                 
# Chama a função palindromo, deve retornar True
print(palindromo('ovo'))
                 
# Chama a função palindromo, deve retornar False
print(palindromo('casa'))
""")
c.Speak("""A função 'palindromo' verifica se a palavra é igual à palavra invertida. Se for, a função retorna verdadeiro, senão, retorna falso. Fui muito rápido nessa, não? Vamos explicar mais devagar...""")
c.StudentComment("""Sim, foi rápido...""")
c.Speak("""A função 'palindromo' recebe uma palavra como parâmetro. A expressão 'palavra[::-1]' inverte a palavra. Se a palavra for igual à palavra invertida, a função retorna verdadeiro, senão, retorna falso. Entendeu?""")
c.Question("""E esse 'def' aí, de onde veio?""")
c.Speak("""O 'def' é uma palavra-chave em Python que define uma função. Você usa 'def' seguido do nome da função e dos parâmetros da função. Entendeu?""")
c.StudentComment("""Não muito, o que é uma função e o que são parâmetros?""")
c.Speak("""Uma função é um bloco de código que executa uma tarefa específica. Os parâmetros são valores que você passa para a função. É um pedacinho de código que você pode chamar várias vezes, passando valores diferentes para ele. Preste atenção sempre na identação, em python, a identação é muito importante, pois é ela que define os blocos de código. Se você não identar corretamente, o python vai reclamar...""")
c.Question("""Acho que entendi, e esse 'str' ali, o que é?""")
c.Speak("""O 'str' é um tipo de dado em Python que representa uma string, ou seja, uma sequência de caracteres. Nesse caso, estamos dizendo que o parametro que a nossa função recebe precisa ser uma string""")
c.Question("""Estamos evoluindo, e esse 'bool' ali depois do '->', o que são?""")
c.Speak("""O 'bool' é um tipo de dado em Python que representa um valor booleano, ou seja, verdadeiro ou falso. Nesse caso, estamos dizendo que a nossa função retorna um valor booleano""")
c.Question("""E esse '->', o que é?""")
c.Speak("""O '->' é uma seta que indica o tipo de retorno da função. Nesse caso, estamos dizendo que a nossa função retorna um valor booleano""")
c.Speak("""Entendeu?""")
c.StudentComment("""Sim, entendi! Eu acho... poderia me mostrar uma outra forma de resolver esse problema, sem usar esse '::-1', achei complexo...""")
c.Speak("""Claro! Vamos criar uma função que verifica se uma palavra é um palíndromo ou não sem usar o '::-1'. Vamos ver o exemplo""")
c.ShowCodeAndRun("""
def palindromo2(palavra) -> bool:
    for i in range(len(palavra) // 2):
        if palavra[i] != palavra[len(palavra) - i - 1]:
            return False
    return True
        
                 
# Chama a função palindromo2, deve retornar True
print(palindromo2('ovo'))
                 
# Chama a função palindromo2, deve retornar False
print(palindromo2('casa'))
""")
c.Speak("""A função 'palindromo2' verifica se a palavra é um palíndromo ou não sem usar o '::-1'. A função itera sobre metade da palavra e compara os caracteres. Se os caracteres forem diferentes, a função retorna falso, senão, retorna verdadeiro. Entendeu?""")
c.Question("""Está melhorando, existe uma forma mais simples, com mais passo a passo e usando só os recursos que vimos nessa aula de resolver isso aí?""")
c.Speak("""Claro! Vamos criar uma função que verifica se uma palavra é um palíndromo ou não de forma mais simples. Vamos ver o exemplo""")
c.ShowCodeAndRun("""
def palindromo3(palavra) -> bool:
    # Itera sobre metade da palavra
    for c1 in range(len(palavra)):
        # Calcula o índice do outro caractere, do final para o começo
        c2 = len(palavra) - c1 - 1
        # Compara os caracteres, se forem diferentes, retorna falso
        if palavra[c1] != palavra[c2]:
            return False
           
    # Se passar por todos os caracteres e não retornar falso, retorna verdadeiro
    return True
                 
# Chama a função palindromo3, deve retornar True
print(palindromo3('ovo'))
                 
# Chama a função palindromo3, deve retornar False
print(palindromo3('casa'))
""")
c.Speak("""A função 'palindromo3' verifica se a palavra é um palíndromo ou não de forma mais simples. A função itera sobre metade da palavra e compara os caracteres. Se os caracteres forem diferentes, a função retorna falso, senão, retorna verdadeiro. Entendeu?""")
c.StudentComment("""Sim, vendo esse código comentado, eu entendi... mas preciso praticar mais""")
c.Speak("""Não se preocupe, com a prática você vai pegar o jeito!""")
c.Speak("""Mas ainda precisamos falar sobre outros tipos de loops em Python...""")
c.Speak("""O loop 'while' é usado para executar um bloco de código enquanto uma condição for verdadeira. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
i = 0
while i < 5:
    print(i)
    i = i + 1
""")
c.Speak("""O loop 'while' executa o bloco de código enquanto a condição 'i < 5' for verdadeira. Entendeu?""")
c.StudentComment("""Sim, entendi!""")
c.Speak("""O loop 'while' é muito útil quando você não sabe quantas vezes o bloco de código precisa ser executado. Você só precisa definir uma condição de parada. Entendeu?""")
c.StudentComment("""Consegue me mostrar com um exemplo prático? Podemos fazer o exercício do palindromo com o 'while'?""")
c.Speak("""Claro! Vamos criar uma função que verifica se uma palavra é um palíndromo ou não usando um loop 'while'. Vamos ver o exemplo""")
c.ShowCodeAndRun("""
def palindromo4(palavra) -> bool:
    # Inicializa os índices
    i = 0
    # Inicializa o índice do final da palavra
    j = len(palavra) - 1
    # Itera sobre metade da palavra
    while i < j:
        # Compara os caracteres, se forem diferentes, retorna falso
        if palavra[i] != palavra[j]:
            return False
        # Atualiza os índices
        i = i + 1
        j = j - 1
    return True
                 
# Chama a função palindromo4, deve retornar True
print(palindromo4('ovo'))

# Chama a função palindromo4, deve retornar False
print(palindromo4('casa'))
""")
c.Speak("""A função 'palindromo4' verifica se a palavra é um palíndromo ou não usando um loop 'while'. A função itera sobre metade da palavra e compara os caracteres. Se os caracteres forem diferentes, a função retorna falso, senão, retorna verdadeiro. Entendeu?""")
c.StudentComment("""Sim, entendi! Mas o código me parece mais complexo nesse caso... existe uma regra de quando usar 'for' e quando usar 'while'?""")
c.Speak("""O 'for' é usado quando você sabe quantas vezes o bloco de código precisa ser executado. O 'while' é usado quando você não sabe quantas vezes o bloco de código precisa ser executado. Entendeu?""")
c.StudentComment("""Acho que sim... e o que mais preciso aprender sobre python para conseguir fazer um programa mais complexo?""")
c.Speak("""Entender a estrutura de pastas de um programa ajuda muito, pois logo você terá também que importar funções de outros arquivos, entender como funciona o 'import' e o 'from' é muito importante. Além disso, entender como funciona a orientação a objetos em python é essencial para criar programas mais complexos. Mas não se preocupe, com a prática você vai pegar o jeito!""")
c.StudentComment("""Uau... sempre fico confuso com isso, poderia me ajudar? Como assim importar coisas?""")
c.Speak("""Claro! Um programa de verdade é separado em vários pedaços que ficam provavelmente em arquivos diferentes. Para usar esses pedaços em um arquivo, você precisa importá-los.""")
c.Speak("""Também é muito comum você usar códigos de outros projetos em seu projeto e portanto, você vai precisar importar esses caras para dentro do seu programa. É uma boa prática e super usual para reaproveitar códigos e evitar repetições.""")
c.Speak("""Alias, é assim que se faz profissionalmente, você não precisa recriar tudo toda vez que precisa, a maioria dos problemas comuns já foram resolvidos por alguém antes, então provavelmente esse outro código que você irá importar já resolve o seu problema.""")
c.Speak("""Mas primeiro, vamos ver como fazer isso com seu próprio código. Vamos criar um arquivo chamado 'utils.py' e colocar a função 'palindromo' nele. Depois, vamos importar essa função em outro arquivo e usá-la. O que acha?""")
c.StudentComment("""Legal!""")
c.Speak("""Vamos lá!""")
c.ShowCode("""
# utils.py
def palindromo(palavra) -> bool:
    # Itera sobre metade da palavra
    for i in range(len(palavra) // 2):
        # Compara os caracteres, se forem diferentes, retorna falso
        if palavra[i] != palavra[len(palavra) - i - 1]:
            return False
    return True
""")
c.Speak("""Agora que criamos o arquivo 'utils.py' com a função 'palindromo', vamos importar essa função em outro arquivo e usá-la. Vamos ver o exemplo""")
c.ShowCode("""
# main.py
#Nessa linha, vamos chamar a função palindromo do arquivo utils.py
from utils import palindromo

#Agora vamos usar a função palindromo
print(palindromo('ovo'))
""")
c.Speak("""Viu como é simples?""")
c.StudentComment("""Sim, muito simples!""")
c.Speak("""Agora que você já sabe como importar funções de outros arquivos, você está pronto para criar programas mais complexos em Python?""")
c.Question("""Acho que sim... mas e se eu quiser importar uma função de um pacote que não está na pasta do meu projeto?""")
c.Speak("""Nesse caso, você precisa instalar o pacote usando o 'pip'. O 'pip' é um gerenciador de pacotes em Python que permite instalar e gerenciar pacotes de terceiros. Vamos ver um exemplo""")
c.ShowCommand("""
# Para instalar o pacote requests, você precisa rodar o comando abaixo no terminal
pip install requests
""")
c.Speak("""O comando 'pip install requests' instala o pacote 'requests'. Depois de instalar o pacote, você pode importar a função que você precisa e usá-la em seu programa. Mas temos um outro problema aqui...""")
c.StudentComment("""Qual problema?""")
c.Speak("""O 'requests' é um pacote que não vem instalado por padrão no Python. Você precisa instalar esse pacote manualmente usando o 'pip'. Mas dessa forma, ele irá instalar esse pacote no seu sistema como um todo, não é uma boa prática fazer isso dessa forma""")
c.Speak("""Uma forma mais segura e recomendada é usar um ambiente virtual. Um ambiente virtual é um ambiente isolado onde você pode instalar pacotes sem afetar o sistema como um todo. Vamos ver um exemplo""")
c.ShowCommand("""
# Para criar um ambiente virtual, você precisa rodar o comando abaixo no terminal
python -m venv .
""")
c.Speak("""O comando 'python -m venv .' cria um ambiente virtual na pasta atual. Depois de criar o ambiente virtual, você precisa ativá-lo usando o comando abaixo""")
c.ShowCommand("""
# Para ativar o ambiente virtual, você precisa rodar o comando abaixo no terminal
source bin/activate
""")
c.Speak("""O comando 'source bin/activate' ativa o ambiente virtual. Depois de ativar o ambiente virtual, você pode instalar os pacotes que você precisa usando o 'pip'""")
c.ShowCommand("""
# Para instalar o pacote requests no ambiente virtual, você precisa rodar o comando abaixo no terminal
pip install requests
""")
c.Speak("""O comando 'pip install requests' instala o pacote 'requests' no ambiente virtual. Depois de instalar o pacote, você pode importar a função que você precisa e usá-la em seu programa. Entendeu?""")
c.StudentComment("""Eita Giovana... me perdi um pouco, ambiente virtual? É como um docker?""")
c.Speak("""Não, não é como um docker. Um ambiente virtual é um ambiente isolado onde você pode instalar pacotes sem afetar o sistema como um todo. É uma forma de manter seu ambiente de desenvolvimento limpo e organizado.""")
c.Speak("""Com um ambiente virtual, você pode instalar pacotes específicos para um projeto sem afetar outros projetos ou o sistema como um todo. É uma boa prática usar ambientes virtuais para desenvolver em Python. Entendeu?""")
c.StudentComment("""Acho que sim... mas e se eu quiser compartilhar meu código com outras pessoas?""")
c.Speak("""Nesse caso, você pode usar um arquivo chamado 'requirements.txt'. O 'requirements.txt' é um arquivo que lista todos os pacotes que seu projeto precisa para funcionar. Vamos ver um exemplo""")
c.ShowCodeAndRun("""
# requirements.txt
requests==2.26.0
""")
c.Speak("""O arquivo 'requirements.txt' lista o pacote 'requests' e a versão '2.26.0'. Para instalar os pacotes listados no 'requirements.txt', você precisa rodar o comando abaixo""")
c.ShowCommand("""
# Para instalar os pacotes listados no requirements.txt, você precisa rodar o comando abaixo no terminal
pip install -r requirements.txt
""")
c.Speak("""O comando 'pip install -r requirements.txt' instala os pacotes listados no 'requirements.txt'. Depois de instalar os pacotes, você pode compartilhar seu código com outras pessoas e elas poderão instalar os pacotes necessários usando o 'requirements.txt'.""")
c.Speak("""Note que estamos fixando uma versão específica do pacote 'requests'. Isso é importante para garantir que seu código funcione corretamente. Se você não fixar a versão, o 'pip' pode instalar uma versão mais recente do pacote que pode não ser compatível com seu código.""")
c.Speak("""você pode omitir a versão e ter um arquivo mais simples, olha como ficaria:""")
c.ShowCommand("""
# requirements.txt
requests
""")
c.Speak("""Dessa forma, o 'pip' irá instalar a versão mais recente do pacote 'requests'. Mas é importante fixar a versão para garantir que seu código funcione corretamente. Entendeu?""")
c.StudentComment("""Sim, acho que sim...""")
c.Speak("""Ainda sobre a estrutura de pastas da sua solução, é importante que você organize bem seus arquivos. Em python normalmente o código fonte fica na pasta 'src', os testes ficam na pasta 'tests', os arquivos de configuração ficam na pasta 'config', os arquivos de dados ficam na pasta 'data', e assim por diante...""")
c.Speak("""Organizar bem seus arquivos é fundamental para manter seu código limpo e organizado. Além disso, é importante usar um sistema de controle de versão como o Git para gerenciar seu código. O Git permite que você controle as mudanças no seu código, reverta alterações, e trabalhe em equipe de forma eficiente.""")
c.Speak("""Veja um exemplo de organização de pastas para um projeto em Python, com um app chamado main.py, com entidades, serviços, camadas de bancos de dados, scritps, storages, APIs, testes, configurações, dados, arquivos de configuração, requirements, readme e etc""")
c.Speak("""
├── src
│   ├── main.py
│   ├── entities
│   │   ├── user.py
│   │   ├── product.py
│   ├── services
│   │   ├── user_service.py
│   │   ├── product_service.py
│   ├── database
│   │   ├── user_db.py
│   │   ├── product_db.py
│   ├── scripts
│   │   ├── import_data.py
│   │   ├── export_data.py
│   ├── storages
│   │   ├── file_storage.py
│   │   ├── database_storage.py
│   ├── apis
│   │   ├── user_api.py
│   │   ├── product_api.py
├── tests
│   ├── test_user.py
│   ├── test_product.py
├── config
│   ├── settings.py
│   ├── database.py
├── data
│   ├── users.csv
│   ├── products.csv
├── requirements.txt
├── README.md
""")
c.Speak("""Entendeu?""")    
c.StudentComment("""Sim, entendi!""")
c.Speak("""Agora que você já sabe como organizar seus arquivos e usar ambientes virtuais, você está pronto para criar programas mais complexos em Python?""")
c.Speak("""Se tiver mais alguma dúvida, pode me chamar!""")
c.Speak("""Até a próxima!""")
