# -*- coding: utf-8 -*-
import os
import random
from time import sleep

print("""# E aí? td bem?
#
# A primeira coisa que você vai ver em um programa python normalmente são os "import", mas que raio é isso?
# Os "imports" são os comando que você passa para o interpretador olhar fora do seu arquivo de programa e trazer recursos que estão em outros lugares para serem usados aqui
#
# Eles seguem os seguintes modelos:
#   import MODULO
#   from ARQUIVO import MODULO|CLASSE
#   from ARQUIVO import * (nesse caso, importa tudo daquele arquivo, prático não?)
#   from .ARQUIVO import *|MODULO|CLASS (use o .ARQUIVO quando o arquivo estiver no mesmo diretório do seu arquivo)
#
# Aperte algo aí no teclado que continuamos...
""")
input()

print("""
# Quando começamos uma linha com o 'def' que dizer q estamos definindo algo que vai se comportar como um contexto, ou seja, uma função
# A estrutura básica dessa parte fica assim:

    def NomeDaFuncao():
        (código da função)

# Lembre-se que o contexto do Python é definido por sua identação, portanto, tudo oq estiver "dentro" do escopo desse dev, será sua função
#
# Uma função pode (ou não) receber parametros, algo assim:

    def Soma(numero1, numero2):
        print(numero1 + numero2)

# Vamos tentar? Aperta aí qualquer coisa que vamos tentar somar 5 e 3?
    RESPOSTA:""", end='')

# define a função soma, como dissemos


def Soma(numero1, numero2):
    print(numero1 + numero2)


# chama a função Soma passando os valores
Soma(5, 3)
input()

print("""
# Agora vamos criar uma outra função mais interessante e que vamos usar várias vezes mais para frente? uma que limpa a tela para não deixarmos tanta 'sujeira' pelo caminho?
# Uma função que faz isso ficaria assim:

def ClearScreen():
    # Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # windows
        _ = os.system('cls')

# Aqui a coisa é simples, nós estamos usando um recurso do SO para executar um comando, para windows chamamos o 'cls' (Clear Screen) e em sistemas posix (Linux, macOS, etc) esse comando é o 'clear'
# A partir do momento em que definimos essa função em nosso código, podemos chamar sua execução da mesma forma que fizemos com o 'Soma', colocando uma linha invocando essa ação:

ClearScreen()

# Vamos ver como se comporta? Aperta qualquer coisa aí...""")


def ClearScreen():
    # Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # windows
        _ = os.system('cls')


input()
ClearScreen()

print(
    """# Eureka! limpou a tela aí? aperta qualquer coisa que vamos continuar... e daqui para frente, limpando a tela a cada passo...""")
input()
ClearScreen()

print("""
# Tem outra coisa que precisamos explicar aqui, o '#' no começo de cada linha quer dizer q é uma linha de comentário e o interpretador irá ignorar, ok?
# isso pode te ajudar a entender oq estamos fazendo aqui
#
# Agora vamos deixar isso mais bonito e destacar algumas coisas que estamos escrevendo?
# Vamos criar uma classe com os comandos de cores do python para poder formatar de uma maneira interessante o que queremos escrever
# Para isso, vamos usar alguns recursos legais de cores e formatação no terminal, olha esse hello world azul (aperta aí algo):

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(color.BOLD + color.BLUE + 'Hello World !' + color.END)

# Aperte o ENTER aí para vermos!!
""")


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


input()

print(color.BOLD + color.BLUE + 'Hello World !' + color.END)

print("""# Está ficando legal né? mas ainda podemos deixar isso aqui melhor... vamos continuar? (ENTER!)""")
input()

print("""
# Bom, temos alguns pontos legais até aqui, agora os comandos vão aparecer em negrito e a parte em que falo com vc, será dentro de um comentário, ok? Vamos seguir?
# Mas isso aqui está muito feio, meio chato, um monte de texto branco no terminal, vamos deixar melhor, bonitão e parecendo um chat?
# vou criar umas funções aqui para brincar com o o formato do que vamos exibir, primeiro vamos definir algumas respostas e textos para exibir:

nextStepMessages = [
    'Ok, entendi...',
    'Certo, vamos ver esse negócio',
    'Hummm... interessante!',
    'Vamos falar sobre isso...',
    'Bom ponto! Vamos falar disso aí...',
    'Não é complexo, vamos olhar de perto...',
    'Vamos ver isso aí...',
    'Olha... vc tem razão, um passo de cada vez, vamos explicar essa parte...',
    'Estamos indo bem, vamos chegar lá...'
]

pressEnterMessages = [
    'Para continuar, aperta o ENTER aí...',
    'ENTER e vamos em frente...',
    'Será que hoje vai chover? Aperta o ENTER aí para seguir...',
    'Aperta o ENTER aí vai...',
    'Manda um ENTER pra continuarmos...',
    'Só estou esperando vc apertar o ENTER para seguirmos...',
    'No seu tempo campeão... aperta o ENTER aí quando vc quiser...',
    'E aí? td bem com vc? quando estiver de boa, aperta o ENTER aí que continuamos... ',
    'Tá divertido? quando quiser, aperta o ENTER que vamos em frente...'
]
""")
input()

print("""# Agora vamos criar as funções, essa primeira é a que vou usar quando eu for falar com vcs:
def Speak(msg):
    for line in msg.splitlines():
        print(color.END + color.PURPLE + color.BOLD + "# [Fino] " +
              color.END + color.GREEN + line + color.END)
        # Espera um pouquinho para cada linha poder ser lida...
        sleep(len(line)/100)
""")
input()

print("""# Essa é para quando fizer sentido você perguntar algo que eu preciso explicar:
def Question(msg):
    print(color.END + color.DARKCYAN + color.BOLD +
          "\n# [Aluno] " + color.END + color.YELLOW + msg + color.END)
    # tempo para entender oq está acontecendo
    sleep(2)
    NextStep()
""")
input()

print("""# Essa aqui exibe um trecho de código e ainda executa se precisar... legal né?
def ShowCode(code, wait=True, run=True):
    print(color.END + color.BOLD + "\n[Python code] - START" + color.END)
    print(color.END + color.BOLD + color.BLUE +
          "{}".format(code) + color.END)
    print(color.END + color.BOLD +
          "[Python code] - END\n" + color.END)
    if run:
        exec(code)
    if wait:
        AskEnter()
""")
input()

print("""# Essa é simples, só exibe na tela de forma formatada o resultado de alguma coisa:
def PrintResult(msg):
    print(color.END + color.CYAN + "RESULTADO: {}".format(msg) + color.END)
""")
input()

print("""# Essa é simples também, mas tem um efeito interessante, pegamos aleatóriamente (usado o random.randint) uma das frases que criamos antes e esperamos o usário (vc) apertar o ENTER
def AskEnter():
    print(color.END + color.PURPLE + color.BOLD + "# [Fino] " +
          color.END + color.BOLD + pressEnterMessages[random.randint(0, len(pressEnterMessages)-1)] + color.END)
    input()
""")
input()

print("""# Aqui pegamos uma das frases que criamos e esperamos o ENTER, é só uma função para facilitar a vida... espero que isso esteja fazendo sentido para você:
def NextStep():
    Speak(nextStepMessages[random.randint(0, len(nextStepMessages)-1)])
    AskEnter()
""")

nextStepMessages = [
    """Ok, entendi...""",
    """Certo, vamos ver esse negócio""",
    """Hummm... interessante!""",
    """Vamos falar sobre isso...""",
    """Bom ponto! Vamos falar disso aí...""",
    """Não é complexo, vamos olhar de perto...""",
    """Vamos ver isso aí...""",
    """Olha... vc tem razão, um passo de cada vez, vamos explicar essa parte...""",
    """Estamos indo bem, vamos chegar lá..."""
]

pressEnterMessages = [
    """Para continuar, aperta o ENTER aí...""",
    """ENTER e vamos em frente...""",
    """Será que hoje vai chover? Aperta o ENTER aí para seguir...""",
    """Aperta o ENTER aí vai...""",
    """Manda um ENTER pra continuarmos...""",
    """Só estou esperando vc apertar o ENTER para seguirmos...""",
    """No seu tempo campeão... aperta o ENTER aí quando vc quiser...""",
    """E aí? td bem com vc? quando estiver de boa, aperta o ENTER aí que continuamos... """,
    """Tá divertido? quando quiser, aperta o ENTER que vamos em frente..."""
]


def Speak(msg):
    for line in msg.splitlines():
        print(color.END + color.PURPLE + color.BOLD + "# [Fino] " +
              color.END + color.GREEN + line + color.END)
        # Espera um pouquinho para cada linha poder ser lida...
        sleep(len(line)/100)


def Question(msg):
    print(color.END + color.DARKCYAN + color.BOLD +
          "\n# [Aluno] " + color.END + color.YELLOW + msg + color.END)
    # tempo para entender oq está acontecendo
    sleep(2)
    NextStep()


def ShowCode(code, wait=True, run=True):
    print(color.END + color.BOLD + "\n[Python code] - START" + color.END)
    print(color.END + color.BOLD + color.BLUE +
          "{}".format(code) + color.END)
    if run:
        print(color.END + color.BOLD +
              "[Python code] - EXEC:\n" + color.END)
        exec(code)
    if wait:
        AskEnter()

    print(color.END + color.BOLD +
          "[Python code] - END\n" + color.END)


def PrintResult(msg):
    print(color.END + color.CYAN + "RESULTADO: {}".format(msg) + color.END)


def AskEnter():
    print(color.END + color.PURPLE + color.BOLD + "# [Fino] " +
          color.END + color.BOLD + pressEnterMessages[random.randint(0, len(pressEnterMessages)-1)] + color.END)
    input()


def NextStep():
    Speak(nextStepMessages[random.randint(0, len(nextStepMessages)-1)])
    AskEnter()


print("""# Agora, as coisas vão ficar mais bonitas, vamos usar essas funções que criamos para formatar as mensagens e fazer isso parecer uma conversa mesmo, olha:""")
NextStep()
ClearScreen()

Speak("""Esse sou eu falando com vc, veja como os códigos vão aparecer a partir daqui:""")
ShowCode("""
def Multiplica(numero1, numero2):
    print(numero1 * numero2)

Multiplica(2, 3)
""", False)

Speak("""Ficou melhor? Eu acho que sim... vamos seguir?""")
NextStep()
ClearScreen()

Speak("""Falamos de muitas coisas, agora vamos falar sobre variáveis
No python, o código não é compilado, isso quer dizer que o interpretador vai entender o seu código em 'tempo de execução'.... mas que raios isso quer dizer?
Isso quer dizer que o código é interpretado enquanto ele é executado, a quente... legal né? bom, existem, como em tudo, vantagens e desvantagens nisso
Vamos falar de uma dessas características: a não tipagem de variáveis...
(Ah! abri espaço para quando vcs fizerem perguntas e pretendo responder... elas vão aparecer de outra cor ;) ) """)
Question("""Pow Fino, jura cara q vc nem falou oq são variáveis direito e já quer que faça sentido essa tal de tipagem? que treco é esse?""")
Speak("""Sim, eu sei q é um termo estranho, mas logo tudo fará sentido...
Quando criamos uma variável em um programa, oq isso quer dizer?
Quer dizer q estamos falando para o computador reservar um pedaço de memória para guardarmos alguma coisa... simples assim!
Em linguagens compiladas (lembram oq é isso? podemos depois falar sobre isso) o compilador entende um tipo de variável descrito no código
E aloca esse espaço para usarmos de acordo com o tipo escolhido... isso quer dizer que um campo inteiro de 32bits irá ocupar, olha só q coisa, 32 bits de memória! incrível não?
Só que no python, para o bem ou para o mal, ele vai entendendo o seu código enquanto ele acontece...
Então não existe essa 'pré alocação' de recursos, eles são alocados de acordo com a necessidade
Isso traz uma caracterisca interessante, uma variável não precisa ter um tipo na hora em que é criada, 
O interpretador do python simplesmente no momento em que você coloca um valor dentro da variável
O python entende q esse tipo de dado que foi colocado lá dentro, será o tipo da variável
Isso quer dizer que a variável será mesmo tipo do tipo do dado que estiver dentro dela...
Lembrem do Homem Aranha: 'Grandes poderes trazem grandes bugs em produção...' ops, não, pera.... era algo quase assim....""")
Question("""Tá Fino, ok... acho q isso está fazendo mais sentido, mas como fica no código?""")

Speak("""Vamos criar uma variável chama MinhaVar e colocar um número nela e ver como ela será exibida...""")
ShowCode("""
MinhaVar = 7
PrintResult(MinhaVar)
""", False)

Speak("""Boa! o número 7 ficou guardado lá dentro... vamos começar a bagunça! E se eu colocar um outro tipo de dados lá dentro? vamos rodar esse código aqui:""")
ShowCode("""
MinhaVar = 7
PrintResult(MinhaVar)

MinhaVar = 'minha string felizona'
PrintResult(MinhaVar)
""", False)

Speak("""Notou que agora o conteúdo da 'MinhaVar' é um texto? em outras linguagens com 'tipagem forte' isso não seria possível... legal né?""")
AskEnter()
ClearScreen()

# Vetores
Speak("""Vamos falar de estruturas mais legais? já pensou em como organizar variaveis em coleções?
Existem basicamente duas formas de organizar variaveis:
    Arrays ou Vetores (uma coleção sequêncial de coisas)
    Dicionários (hashmap, maps ou o tal do chave/valor)""")
Question("""Tá, legal, mas qual a diferença entre esses dois aí?""")
Speak("""O primeiro, mais simples e comum, o vetor é só uma lista de objetos e vc precisa saber a posição deles nessa lista para chegar em um item...
Usamos o simbolo de '[]' para representar um vetor e podemos colocar valores dentro desse vetor, usando o conceito do Python, podem ser de qualquer tipo
Para incluir valores no vetor, usamos uma função chamada 'append'""")
ShowCode("""
meuVetor = []

for i in range(10):
    meuVetor.append(i)
PrintResult(meuVetor)
""", False)
Speak("""Temos nosso primeiro vetor!
Para acessar os valores dentro do vetor, temos que apontar para eles usando a ordem deles lá dentro (também chamamos esse cara de índice/index do vetor)""")
ShowCode("""
meuVetor = []

for i in range(10):
    meuVetor.append(i)

# Vamos imprimir o valor da posicao 7?
PrintResult(meuVetor[7])
""", False)
Speak("""Reparou que a posição 7 é o valor 7? Calma q isso é menos obvio do que parece rs...
quando colocamos os valores lá dentro, usamos um loop (o tal do for) e uma função chamada range (essa é nativa do Python)
Essa função começou do 0 e 'contou' 10 vezes...
""")
Question("""Sempre então devemos considerar o 0?""")
Speak("""Na grande maioria das linguagens toda vez que falaramos de indices, o 0 (ZERO) é a primeira posição...
para mostrar isso, deixa eu te apresentar uma outra função padrão do python muito legal, o 'len'
o 'len' é usado para nos dizer quantos elementos estão em uma estrutura de coleções, olha:""")


ShowCode("""
meuVetor = []

for i in range(10):
    meuVetor.append(i)


PrintResult(len(meuVetor))
""", False)
AskEnter()

# Dicionarios
Question("""Bem legal, mas e o outro? Dicionário né? que negócio é esse? """)
Speak("""Bom, o dicionário tem um comportamento diferente, ele também é uma estrutura para guardamos uma coleção de coisas
Mas nesse caso não usamos a ordem para achar os itens que estão guardados ali
No caso do dicionário, também podemos guardar variáveis de qualquer tipo dele, mas diferente do vetor, onde a posição dele é o que ordena as coisas, aqui cada item desses possui um nome
Ou chave, como costumamos chamar...
Ou seja: Cada item tem um ID único ali dentro e com essa chave vc só pode ter um item... ficou complicado? 
Para criar um mapa, usamos o seguinte simbolo {} vamos ver:""")
ShowCode("""
meuMap = {}
meuMap["chave1"] = "valor1"
meuMap["chave2"] = "valor2"
meuMap["chave3"] = "valor3"
PrintResult(meuMap)
""", False)

Speak(""" Percebe como os valores dentro dessa estrutura ficam organizados de uma meneira diferente? a ordem aqui não faz diferença, o que importa é a chave
Para acessar os dados dentro de um map é muito mais eficiente você conhecer a chave correspondente a esse valor:""")
ShowCode("""
meuMap = {}
meuMap["chave1"] = "valor1"
meuMap["chave2"] = "valor2"
meuMap["chave3"] = "valor3"

PrintResult(meuMap["chave2"])
""", False)

# Loops!
Speak("""
Estou aqui falando e falando e nem paramos para ver alguns outros conceitos básicos...
Usei várias vezes comandos do python e você nem falou nada?
""")
