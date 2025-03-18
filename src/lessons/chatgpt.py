#!/usr/bin/env python3

# Importing the chat class from the talker module
from talker import chat
c = chat.Chat()

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
# Os alunos devem ser chamados de "padawans", "Pobres", "Padawans", "Pequenos Gafanhotos", "Jovem Tartarugas" e outros jargões da cultura pop para se referir a aprendizes.


def t(m):
    c.Speak(m)


def s(m):
    c.StudentComment(m)


def q(m):
    c.Question(m)


# Tema: uso do chatGPT para ajudar a estudar
# Sobre o tema:
# O professor deve explicar de forma bem simples e descontraída sobre o uso do chatGPT para ajudar a estudar.
# O professor deve explicar como o chatGPT pode ser usado para tirar dúvidas sobre um tema.
# O professor deve explicar como o chatGPT pode ser usado para gerar textos sobre um tema.
# O professor deve explicar como o chatGPT usa as informações que são passadas para ele.
# O professor deve explicar como o chatGPT não garante a privacidade das informações passadas para ele.

t("Olá, padawan! Hoje vamos falar sobre o chatGPT.")
t("Você sabe o que é chatGPT?")
s("Não, Fino. Que parada é essa aí?")
t("ChatGPT é um modelo de linguagem que pode ser usado para gerar texto.")
s("Ah, é tipo um professor?")
t("É, padawan! Ele pode ser usado para gerar textos sobre um tema.")
s("E como ele faz isso?")
t("Ele usa as informações que são passadas para ele.")
s("Mas ele é confiável?")
t("Ele não garante a privacidade das informações passadas para ele. Então, é bom ter cuidado com o que você passa para ele.")
t("E aí, padawan? Entendeu?")
s("Entendi, Fino! Obrigado!")
t("De nada, padawan! Estou aqui para ajudar!")
q("Como assim? já acabou?")
t("Não, padawan! A aula não terminou! Ainda temos muito o que aprender!")
t("Vamos continuar?")
s("Vamos!")
q("Mas como diabos esse tal chat sabe das coisas?")
t("Ele usa as informações que são passadas para ele.")
s("Que informações? se eu perguntar algo aleatório, onde ele vai buscar a resposta?")
t("Ele usa as informações que são passadas para ele.")
s("PORRA, Fino! Eu entendi isso! Mas de onde ele tira as informações?")
t("Da internet, padawan! Alguém já passou um monte de informações pra ele e ele indexou tudo.")
s("Indexar? Que porra é essa?")
t("Ele organizou as informações de forma que ele consiga acessar rapidamente.")
s("Entendi! Guardou tudo em um banco de dados?")
t("Mais ou menos, padawan! Ele guardou tudo em um modelo de linguagem.")
s("E como ele sabe o que eu quero saber?")
t("Essa é a beleza da coisa, nem é exatamente ter as respostas, mas saber o que você quer saber.")
s("Entendi! Ele é tipo um adivinho?")
t("É, padawan! Ele é tipo um adivinho! Mas não é garantido que ele vai acertar sempre. Não é um Oraculo. Ele vai tentar responder da melhor forma possível.")
q("E o que é esse tal de LLM que todo mundo tem falado?")
t("LLM é um modelo de linguagem que é treinado em um grande volume de dados.")
s("E o que é um modelo de linguagem?")
t("Um modelo de linguagem é um modelo que é treinado para gerar texto. Existem vários tipos de modelos de linguagem.")
s("E o que é um modelo?")
t("Um modelo é uma representação matemática de um sistema.")
s("E o que é um sistema?")
t("Um sistema é um conjunto de elementos interconectados.")
s("E o que é um elemento?")
t("Um elemento é uma parte de um sistema.")
s("E o que é uma parte?")
t("Uma parte é uma fração de um todo.")
s("E o que é um todo?")
t("Um todo é um conjunto de partes.")
s("E o que é um conjunto?")
t("Um conjunto é um agrupamento de elementos.")
s("E o que é um agrupamento?")
t("Um agrupamento é um conjunto de elementos.")
t("Você jura que quer ir nessa linha? Não estou achando muito produtivo...")
s("É... ficou meio merda essse papo, mas vamos voltar... Já que ele tem todas as informações da internet, como que ele organiza isso tudo?")
t("Ele usa um modelo de linguagem.")
s(f"{c.Teacher()} tá de sacanagem né? já falamos disso... pode ser mais didático e explicar melhor por favor?")
t("Ok pequeno gafanhoto, vou parar de brincar com você... Ele usa um modelo de linguagem para organizar as informações. Mas vamos detalhar melhor")
t("Um modelo de linguagem é como se fosse uma grande estrutura de dados relacionando palavras e frases gerando uma grande estrutura de grafos")
t("Essa estrutura de grafos é usada para prever a próxima palavra em uma frase. Você sabe o que é um grafo?")
s(f"Não, {c.Teacher()}. Que parada é essa?")
t("Um grafo é uma estrutura de dados que representa um conjunto de objetos e as relações entre eles.")
s("E como ele usa isso para organizar as informações?")
t("Ele usa essa estrutura para prever a próxima palavra em uma frase. Como se fosse uma grande teia de ideias, conceitos correlacionados.")
t("É um modelo muito legal e complexo, mas que pode ser usado de forma muito simples. É um modelo que se parece com como o nosso cérebro funciona.")
s("Uau! Que interessante! E como ele sabe o que eu quero saber?")
t("Ele usa as informações que são passadas para ele e procura as relações entre elas. Dessa forma ele tenta prever o que você quer saber.")
s("E se eu perguntar algo aleatório?")
t("Ele vai tentar responder da melhor forma possível. Mas não é garantido que ele vai acertar sempre. Alias, ele pode errar muito! dizemos que quando isso acontece que o modelo gerou uma alucinação.")
s("Que ótimo nome para isso! Alucinação! hahahahah")
t("É, padawan! É engraçado, mas é sério! Ele pode gerar respostas que não fazem sentido.")
s("E quais são as tecnologias atuais, que fazem esse tipo de coisa? poderia me contar um pouco da história disso?")
t("Bom, vamos do começo pequeno gafanhoto...")
t("O chatGPT é um modelo de linguagem que foi desenvolvido pela OpenAI.")
t("Ele é baseado em um modelo chamado GPT-3.")
t("O GPT-3 é um modelo de linguagem que foi treinado em um grande volume de dados da internet.")
t("Ele é um dos modelos de linguagem mais avançados atualmente.")
t("Ele é capaz de gerar texto de forma muito natural.")
t("Ele é capaz de responder perguntas e gerar textos sobre um tema.")
t("Ele é capaz de gerar textos em vários idiomas.")
t("Ele é capaz de gerar textos sobre qualquer tema.")
t("Ele é capaz de gerar textos de forma muito rápida.")
t("Ele é capaz de gerar textos de forma muito precisa e com uma acertividade muito alta.")
q("E existem outros como ele?")
t("Sim, padawan! Existem outros modelos de linguagem como o BERT, o GPT-2, o T5, o RoBERTa, o XLNet, o BART, o MarianMT, o T5 e etc.")
s("E qual é o melhor?")
t("Isso depende do que você quer fazer, padawan! Cada modelo tem suas vantagens e desvantagens.")
s("Me fale um pouco sobre eles então, o que cada um faz de bom, de diferente e comparar com o chatGPT")
t("Bom, vamos do começo pequeno gafanhoto...")
t("O BERT é um modelo de linguagem que foi desenvolvido pela Google.")
t("Ele é baseado em um modelo chamado Transformer.")
t("Ele é um dos modelos de linguagem mais avançados atualmente.")
t("Ele é capaz de gerar texto de forma muito natural.")
t("Ele é capaz de responder perguntas e gerar textos sobre um tema.")
t("Ele é capaz de gerar textos em vários idiomas.")
s("E como ele se compara com o ChatGPT?")
t("O BERT é um modelo de linguagem que é mais focado em responder perguntas.")
t("Ele é capaz de responder perguntas de forma muito precisa.")
t("Ele é capaz de responder perguntas sobre um tema específico.")
t("Ele em comparado com o ChatGPT é mais focado em responder perguntas.")
q("E o GPT-2?")
t("O GPT-2 é um modelo de linguagem que foi desenvolvido pela OpenAI.")
t("Ele é baseado em um modelo chamado Transformer.")
t("Ele é um dos modelos de linguagem mais avançados atualmente.")
t("Ele é capaz de gerar texto de forma muito natural.")
q("E os outros?")
t("O T5 é um modelo de linguagem que foi desenvolvido pela Google.")
t("Ele é baseado em um modelo chamado Transformer, assim como o BERT.")
q("E exitem outros tipos de IA?")
t("Sim, padawan! Existem vários tipos de IA como a IA fraca, a IA forte, a IA estreita, a IA geral, a IA simbólica, a IA sub-simbólica, a IA baseada em regras, a IA baseada em aprendizado de máquina, a IA baseada em redes neurais, a IA baseada em lógica, a IA baseada em agentes, a IA baseada em sistemas especialistas, a IA baseada em sistemas de recomendação, a IA baseada em sistemas de busca, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, a IA baseada em sistemas de classificação, a IA baseada em sistemas de agrupamento, a IA baseada em sistemas de regressão, ou seja, muitas!")
t("Vamos fazer uma tabelinha para mostrar isso:")
t("IA fraca: É uma IA que é capaz de realizar tarefas específicas.")
t("IA forte: É uma IA que é capaz de realizar tarefas gerais.")
t("IA estreita: É uma IA que é capaz de realizar tarefas específicas.")
t("IA geral: É uma IA que é capaz de realizar tarefas gerais.")
t("IA simbólica: É uma IA que é baseada em símbolos.")
t("IA sub-simbólica: É uma IA que é baseada em sub-símbolos.")
t("IA baseada em regras: É uma IA que é baseada em regras.")
t("IA baseada em aprendizado de máquina: É uma IA que é baseada em aprendizado de máquina.")
t("IA baseada em redes neurais: É uma IA que é baseada em redes neurais.")
t("IA baseada em lógica: É uma IA que é baseada em lógica.")
t("IA baseada em agentes: É uma IA que é baseada em agentes.")
t("IA baseada em sistemas especialistas: É uma IA que é baseada em sistemas especialistas.")
t("IA baseada em sistemas de recomendação: É uma IA que é baseada em sistemas de recomendação.")
t("IA baseada em sistemas de busca: É uma IA que é baseada em sistemas de busca.")
t("IA baseada em sistemas de classificação: É uma IA que é baseada em sistemas de classificação.")
t("IA baseada em sistemas de agrupamento: É uma IA que é baseada em sistemas de agrupamento.")
t("IA baseada em sistemas de regressão: É uma IA que é baseada em sistemas de regressão.")
q("Nossa, muita coisa! Elas podem lidar com diferentes tipos de dados, como imagens ou sons?")
t("Sim, padawan! Existem modelos de IA que são capazes de lidar com diferentes tipos de dados como imagens ou sons.")
s("E como eles fazem isso?")
t("Eles usam algoritmos que são capazes de processar esses tipos de dados.")
s("E como esses algoritmos funcionam?")
t("Esses algoritmos funcionam de forma muito parecida com o nosso cérebro.")
q("E para me ajudar a gerar códigos, existe alguma dessas?")
t("Sim, padawan! Existem modelos de IA que são capazes de gerar códigos.")
s("E como eles fazem isso? Quais podem me ajudar a cofificar melhor?")
t("Bom, vamos do começo pequeno gafanhoto...")
t("Existem modelos de IA que são capazes de gerar códigos.")
t("Eles usam algoritmos que são capazes de processar códigos.")
t("Eles são capazes de gerar códigos de forma muito rápida e eficiente.")
t("Eles são capazes de gerar códigos de forma muito precisa e com uma acertividade muito alta.")
s("E quais são os melhores?")
t("Isso depende do que você quer fazer, padawan! Cada modelo tem suas vantagens e desvantagens.")
s("Me fale um pouco sobre eles então, o que cada um faz de bom, de diferente e comparar com o chatGPT")
t("Eu uso muito o Copilot, padawan! Ele é um modelo de IA que é capaz de gerar códigos.")
t("Ele é baseado em um modelo chamado Codex. Ajuda demais na produtividade, você pode integrar ele com o VSCode e ele vai te ajudar a escrever códigos.")
s("E o que é o Codex?")
t("O Codex é um modelo de IA que é capaz de gerar códigos, assim como o ChatGPT gerar textos e uma experiência de conversa, o Codex gera códigos de programação.")
s("E como ele faz isso?")
t("Ele usa as informações que são passadas para ele e procura as relações entre elas. Dessa forma ele tenta prever o que você quer saber.")
t("Em geral, ele aprendeu usando muitos códigos open source para aprender a gerar códigos.")
t("Acho que foi muita informação, padawan! Entendeu?")
s("Entendi, Fino! Obrigado!")
t("De nada, padawan! Estou aqui para ajudar!")
c.LastStep()
