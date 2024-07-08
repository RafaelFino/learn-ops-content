from talker import chat

chat = chat.Chat("Fino", "Aluno")

chat.Speak("""E aí cara, como vc está?
Falamos tanto sobre codar, sobre o tal do python, java script, linguagens de todos os tipos
mas as vezes esquecemos que precisamos começar pelo começo...""")
chat.StudentComment("""Como assim? do que vc está falando?""")
chat.Speak("""Quando falamos em lógica, o modelo booleano sempre é o mais simples que vem a mente...
mas vc sabe oq é esse tal modelo booleano?""")
chat.StudentComment("""Claro que não... nunca vi mais gordo...""")
chat.Speak("""O modelo booleano é o modelo que trata a lógica baseada em apenas dois possíveis caminhos:
O VERDADEIRO.........
e o FALSO
E quando falamos de computadores, isso ajuda bastante a entender como as coisas funcionam...
Sabe quando falam que é tudo baseado em 0 e 1? então, é uma representação matemática desse modelo lógico aí...
o 0 é considerado falso e o 1 é o verdadeiro, legal né?""")
chat.StudentComment("""Caramba! jura q é isso aí? simples assim?""")
chat.Speak("""Bom, no conceito é só isso mesmo... tudo é baseado em algo q pode ser verdadeiro ou não...
mas já parou para pensar como podemos usar isso nos nossos códigos?
Então, é aqui que entra o comando mais importante de qualquer tipo de código: o tal do IF
Que na prática, siginifica um comando de teste de uma condição...
a tradução de IF é SE
Ou seja, SE (ISSO AQUI FOR VERDADE) Faça alguma coisa
E o comando IF tem um irmão bem importante... o ELSE!!
O Else é o SENÃO.... ou seja:
SE (ISSO AQUI FOR VERDADE) faça isso SENÃO faça aquilo...""")
chat.Question("""Uau! bem legal isso... mas como q isso aí fica no código?""")
chat.Speak("""Cada linguagem lida com isso de uma forma, mas o conceito é sempre o mesmo...
Vamos ver isso no python? """)
chat.StudentComment("""Claro!!!""")
chat.Speak("""primeiro vamos criar uma veriável chamada minhaVar e colocar o um valor de FALSE dentro dela?""")

chat.ShowCode("""
minhaVar = False
print(minhaVar)
""", False, True)

chat.Speak("""No python, os valores de verdadeiro e falso são constantes na linguagem, isso acontece em praticamente todas as linguagens
no python o verdadeiro corresponde a constante chamada True (com o 'T' maiúsculo) e o falso responde por False (com o 'F' maiúsculo)
Bom, agora que você já sabe o básico da lógica booleana, vamos para o lendário IF
Vamos testar a nossa variável aqui para ver oq tem dentro dela?""")

chat.ShowCode("""

minhaVar = False

if minhaVar == False:
    print('Minha variável é Falsa')

""", False, True)

chat.Speak("""Viu que legal? agora só vai tentar imprimir a mensagem se o valor da variável for falso, vamos melhorar isso aí?""")

chat.ShowCode("""

minhaVar = False

if minhaVar == False:
    print('Minha variável é Falsa')

# agora vamos mudar o valor da variável e tentar de novo
minhaVar = True

if minhaVar == False:
    print('Minha variável é Falsa mesmo? acho que não... rs...')

# a segunda mensagem não foi exibida, pois mudamos a condição do IF

""", True, True)

chat.Speak("""A segunda mensagem não foi exibida... vamos tentar o ELSE agora?""")

chat.ShowCode("""

minhaVar = False

if minhaVar == False:
    print('primeiro IF: Minha variável é falsa - DEVE APARECER ESSE!')
else:
    print('primeiro IF, mas no ELSE: Minha variável é verdadeira')

# agora de novo, vamos mudar o valor da variável
minhaVar = True

if minhaVar == False:
    print('segundo IF: Minha variável é falsa')
else:
    print('segundo IF, mas no ELSE: Minha variável é verdadeira - DEVE APARECER ESSE!')

""", True, True)

chat.Question(
    """Isso tá começando a ficar bom, mas como exatamente isso aí fica no python? explica no detalhe... """)
chat.Speak("""a estrutura não é complicada, olha:
if condição:
    <oq precisa acontecer>
else:
    <oq precisa acontecer>
é importante ter alguns cuidados com relação a linguagem
o 'if' é o comando, depois dele é preciso deixar clara uma expressão/condição que pode ser avaliada para um resultado booleano (hein?)
Isso quer dizer que a condição deve ser algo que é verdadeiro ou faço
Para isso, podemos usar uma variável já com esse valor (como usamos aqui nesse exemplo)
""")
chat.StudentComment("""Mas eu sempre preciso colocar uma variável ali?""")
chat.Speak(
    """Não, você pode recorrer a uma coisa linda que são os OPERADORES DE COMPARAÇÃO!! """)
chat.StudentComment("""Hein?""")
chat.Speak("""Toda vez que vc precisar comparar coisas (qualquer coisa) vc precisa saber qual a relação entre duas variáveis ou expressões, você pode usar esses caras
Fica calmo, o nome é mais assustador do que a realidade""")
chat.StudentComment("""Ufa!""")
chat.Speak("""o mais simples e comum dos operadores é o de igualdade... para esse usamos o comando ==
ou seja: 5 == 5? isso é uma expressão que pergunta se o número 5 é igual ao número 5... sabe o resultado?""")
chat.StudentComment("""Ué? 5 é igual a 5... então é verdadeiro, certo?""")
chat.Speak("""Isso, simples assim, parece simples mas esse tipo de mecanismo resolve quase tudo na vida do programador
pense que no lugar do número 5, vamos colocar variáveis ali...
e comparar o valor delas para tomar alguma ação em nosso código""")
chat.Question("""Está començando a fazer sentido! e se for diferente?""")
chat.Speak("""Usamos um outro simbolo, o != para comparar coisas, perguntando se são diferentes
algo como 5 != 5, consegue imaginar qual é o resultado dessa expressão? Estou perguntando se 5 é diferente de 5""")
chat.StudentComment("""Eita...""")
chat.Speak("""Bom, 5 não é diferente de 5, logo o resultado dessa expressão é FALSO!! importante ter essa noção
Vamos ver como isso ficaria no código?""")

chat.ShowCode("""

minhaVar = 5

if minhaVar == 5:
    print('primeiro IF: EITA! é 5 o valor DEVE APARECER ESSE!')
else:
    print('primeiro IF, Não, o valor não é 5')

# agora vamos comparar para ver se não é 5 o valor
if minhaVar != 5:
    print('segundo IF: Deveria entrar aqui se o valor não for 5')
else:
    print('segundo IF, mas no ELSE: O valor é 5 e estamos testando se é diferente de 5, logo a expressão é falsa - DEVE APARECER ESSE!')

""", True, True)


chat.Speak("""Da mesma forma que usamos simbolos para comparar a igualdade ou não de valores
podemos comparar também se são maiores ou menores usando os outros operadores:
 var1 > var2 
Para comparar se a varável 1 (var1) é maior do que a variável 2 (var2)
Da mesma forma, podemos verificar usando a lógica inversa:
 var1 < var2
Nesse caso, nós consideramos se um valor é maior ou menor que o outro...""")
chat.Question("""Mas e se forem iguais?""", False)
chat.Speak(
    """Para considerar a igualdade na comparação, usamos o simbolo >= ou <= """)
chat.StudentComment("""Agora tudo está fazendo mais sentido""")
chat.Speak("""No fim do dia, temos os seguintes operadores de comparação:
==      testa igualdade (True para iguais, False para diferentes)
!=      testa igualdade também, mas com a lógica inversa: (True para diferentes, False para iguais)
>       teste para saber se uma variável é MAIOR do que a outra, ou seja, se a primeira variável for maior, o resultado será TRUE, se forem iguais ou o inverso disso, o resultado será FALSE
<       testa para saber se uma variável é MENOR do que a outra, ou seja, se a primeira variável for menor, o resultado será FALSE, se forem iguais ou o inverso disso, o resultado será TRUE
>=      teste para saber se uma variável é MAIOR do que a outra, ou seja, se a primeira variável for maior ou IGUAIS, o resultado será TRUE, senão o resultado será FALSE
<=      testa para saber se uma variável é MENOR do que a outra, ou seja, se a primeira variável for menor ou IGUAIS, o resultado será FALSE, senão o resultado será TRUE
Tá facil?
""")
