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
# Os alunos devem ser chamados de "Doenças", "Pobres", "Padawans", "Pequenos Gafanhotos", "Jovem Tartarugas" e outros jargões da cultura pop para se referir a aprendizes.

def t(m):
    c.Speak(m)

def s(m):
    c.StudentComment(m)

def q(m):
    c.Question(m)

# Tema: Raspberry Pi
# O professor deve explicar o que é o Raspberry Pi, como ele funciona e como ele pode ser utilizado.
# O professor deve explicar o que é um SBC (Single Board Computer) e como ele se diferencia de um computador convencional.
# O professor deve explicar as diferenças entre os modelos de Raspberry Pi e quais diferenças entre cada um deles.
# O professor deve mostrar algumas alternativas ao Raspberry Pi, como o Arduino e quais problemas diferentes eles resolvem.
# O professor pode falar sobre outros SBC, como o Banana Pi, Orange Pi, BeagleBone, Odroid, Asus Tinker Board, entre outros.
# O professor deve explicar como instalar o Raspberry Pi OS no Raspberry Pi.
# O professor deve explicar como instalar o Raspberry Pi.
# O professor deve explicar como acessar o Raspberry Pi remotamente.
# O professor deve explicar como executar comandos no Raspberry Pi.
# O professor deve explicar como acessar arquivos do Raspberry Pi.

t("Olá, pequeno Doença! Hoje vamos falar sobre o Raspberry Pi. Você sabe o que é o Raspberry Pi?")
s(f"Sei não {c.Teacher()}, é um bolo?")
t("Hahaha, não, não é um bolo. O Raspberry Pi é um computador do tamanho de um cartão de crédito.")
s("Sério? Um computador tão pequeno?")
t("Sim, é um computador muito pequeno, mas muito poderoso. Ele é um SBC, um Single Board Computer.")
s("E o que é um SBC?")
t("Um SBC é um computador que possui todos os componentes de um computador convencional em uma única placa.")
s("Entendi. E para que serve um Raspberry Pi?")
t("O Raspberry Pi pode ser utilizado para diversos fins, como servidores, media centers, automação residencial, entre outros.")
s("Legal! E como eu faço para usar um Raspberry Pi?")
t("Você pode comprar um Raspberry Pi e instalar o Raspberry Pi OS nele. É uma distribuição de Linux feita especialmente para o Raspberry Pi.")
q("Um Linux completo? Então ele é um computador completo? Como o meu Desktop?")
t("Sim, ele é um computador completo, mas em um tamanho muito menor. Você pode acessá-lo remotamente e executar comandos nele.")
s("E eu posso acessar os arquivos dele?")
t("Sim, você pode acessar os arquivos do Raspberry Pi e transferir arquivos entre o Raspberry Pi e o seu computador.")
s("Legal! Vou comprar um Raspberry Pi para mim! Que tipos de aplicação eu posso fazer com ele?")
t("Você pode fazer muitas coisas com o Raspberry Pi, como servidores, media centers, automação residencial, entre outros.")
s("Muito legal! É como se fosse um Arduino, mas mais poderoso, né?")
t("Isso mesmo! O Arduino é mais voltado para projetos de eletrônica, enquanto o Raspberry Pi é um computador completo.")
s("Entendi! Eu consigo rodar um Linux no Arduino?")
t("Não, o Arduino não é um computador completo, ele é mais voltado para projetos de eletrônica.")
s("Entendi! E consigo rodar uma interface gráfica decente no Raspberry Pi?")
t("Sim, você pode rodar uma interface gráfica no Raspberry Pi, como o LXDE, XFCE, entre outros.")
s("Legal! E quais são os modelos de Raspberry Pi disponíveis?")
t("Existem vários modelos de Raspberry Pi, como o Raspberry Pi Zero, Raspberry Pi 3, Raspberry Pi 4, Raspberry Pi 5, entre outros.")
s("E qual é o melhor modelo para começar?")
t("Para começar, eu recomendo o Raspberry Pi 4, pois é um modelo recente e poderoso por um preço adequado, mas existem outros modelos mais simples e baratos.")
q("Existem outros SBC?")
t("Sim, existem outros SBC, como o Arduino, Banana Pi, Orange Pi, BeagleBone, Odroid, Asus Tinker Board, entre outros.")
q("E qual a diferença entre eles? quais são os mais poderosos? E os mais baratos?")
t("Cada SBC tem suas características, alguns são mais poderosos, outros são mais baratos. O Raspberry Pi é um dos mais populares e versáteis.")
s("E quais são essas características?")
t("As características de um SBC incluem processador, memória, portas de entrada e saída, entre outros.")
s("E como eu escolho o melhor SBC para o meu projeto?")
t("Você deve escolher o SBC de acordo com as necessidades do seu projeto, como processamento, memória, portas de entrada e saída, entre outros.")
s("Entendi! Obrigado pela aula, professor! Acho que vou comprar um Raspberry Pi para mim!")
t("Hahaha, a aula ainda não acabou, pequeno Doença! Ainda temos muito mais para aprender sobre o Raspberry Pi!")
s("Hahaha, ok! Vamos continuar então!")
s("Eu vi que eles usam um tal de ARM, o que é isso?")
t("O ARM é uma arquitetura de processadores utilizada em dispositivos móveis e sistemas embarcados.")
s("E o que isso tem a ver com o Raspberry Pi?")
t("O Raspberry Pi utiliza processadores ARM, que são eficientes e econômicos em termos de energia.")
q("E um ARM é diferente do meu computador?")
t("Sim, os processadores ARM são diferentes dos processadores x86 utilizados em computadores convencionais.")
s("E qual a diferença entre eles?")
t("Os processadores ARM são mais eficientes em termos de energia e são utilizados em dispositivos móveis e sistemas embarcados.")
s("Isso está ficando complicado... Mas eu estou gostando de aprender sobre esses ARM e X86... poderia me contar a história deles por favor?")
t("Claro, pequeno Doença! Os processadores ARM foram criados pela empresa britânica Acorn Computers na década de 1980.")
t("Os processadores x86 foram criados pela empresa americana Intel na década de 1970.")
s("Eles são inimigos?")
t("Não, eles são concorrentes no mercado de processadores, cada um com suas características e aplicações. Caramba, 40 anos atrás? E o que aconteceu até hoje? onde estão os ARM e os X86?")
t("Os processadores ARM são amplamente utilizados em dispositivos móveis, como smartphones e tablets.")
t("Os processadores x86 são utilizados em computadores convencionais, como desktops e laptops.")
s("Entendi! E qual é o melhor?")
t("Não existe um melhor, cada um tem suas características e aplicações. Os processadores ARM são mais eficientes em termos de energia, enquanto os processadores x86 são mais poderosos.")
s("E eu posso escolher entre eles?")
t("Sim, você pode escolher entre processadores ARM e x86 de acordo com as suas necessidades e preferências.")
t("Os novos computadores da Apple, por exemplo, utilizam processadores ARM, enquanto a maioria dos computadores convencionais utilizam processadores x86.")
s("E os aplicativos entre eles, são compativeis?")
t("Alguns aplicativos são compatíveis com ambos os processadores, enquanto outros são específicos para um ou outro.")
q("Mas os mesmos binários rodam nos dois tipos de processadores? achei que era só instalar e rodar...")
t("Alguns aplicativos são compilados para rodar em processadores ARM, enquanto outros são compilados para rodar em processadores x86.")
t("Mas cada um deles tem suas vantagens e desvantagens, e cabe a você escolher o que melhor se adapta às suas necessidades. Quanto aos aplicativos, eles precisam ser compilados para o processador específico.")
s("Então para algo rodar em um ARM, ele precisa ser compilado para ARM e o mesmo para X86?")
t("Isso mesmo! Os aplicativos precisam ser compilados para o processador específico para rodar corretamente.")
t("A Apple, por exemplo, está migrando seus aplicativos para a arquitetura ARM, para aproveitar as vantagens dos processadores ARM em seus novos computadores.")
t("Tem sido uma longa jornada para migrar a maior parte dos aplicativos para a nova arquitetura, mas a empresa está otimista com os resultados.")
t("E o raspberry usa ARM, então os aplicativos que rodam nele precisam ser compilados para ARM. No futuro, a tendência é que mais aplicativos sejam compilados para ARM, devido às vantagens dessa arquitetura.")
t("O Raspberry Pi é um ótimo exemplo de como a arquitetura ARM pode ser utilizada em sistemas embarcados e projetos DIY. Ele em muitos aspectos, se assemelha a um computador convencional, mas seu hardware se parece muito com o de um celular.")
s("Entendi! Obrigado pela aula, professor! Acho que vou comprar um Raspberry Pi para mim!")
t("Hahaha, a aula ainda não acabou, pequeno Doença! Ainda temos muito mais para aprender sobre o Raspberry Pi!")
s("Hahaha, ok! Vamos continuar então!")
q("É verdade que podemos rodar um video game em um raspberry, com emuladores de consoles antigos?")
t("Sim, é possível rodar emuladores de consoles antigos no Raspberry Pi e jogar jogos clássicos.")
s("E como eu faço isso?")
t("Você pode instalar emuladores de consoles antigos no Raspberry Pi e baixar as ROMs dos jogos para jogar.")
s("E é legal fazer isso?")
t("Sim, é uma forma divertida de relembrar os jogos clássicos e experimentar consoles antigos.")
s("E é fácil de fazer?")
t("Sim, é relativamente fácil de instalar os emuladores e configurar os controles para jogar. Existem algumas distribuições linux que resolvem esse problema para você.")
q("E você conhece alguma dessas? poderia me ajudar?")
t("Claro, pequeno Doença! Você pode usar a distribuição RetroPie, que é uma distribuição linux voltada para emulação de consoles antigos.")
t("A RetroPie possui uma interface amigável e suporte para diversos emuladores e controles.")
s("E existem outras?")
t("Sim, existem outras distribuições linux voltadas para emulação de consoles antigos, como o Lakka, o Recalbox e o Batocera.")
s("E qual é a melhor?")
t("Cada uma tem suas características e vantagens, cabe a você escolher a que melhor se adapta às suas necessidades.")
t("Eu gosto muito da Recalbox, é bem estável e fácil de configurar. Mas a RetroPie é a mais popular e tem uma comunidade bem ativa.")
s("E eu consigo jogar jogos de qual console?")
t("Você pode jogar jogos de diversos consoles antigos, como o NES, SNES, Mega Drive, entre outros.")
s("E eu consigo jogar jogos de qual época?")
t("Você pode jogar jogos clássicos de diversas épocas, desde os anos 80 até os anos 2000.")
s("E eu consigo jogar jogos de qual gênero?")
t("Você pode jogar jogos de diversos gêneros, como plataforma, ação, aventura, entre outros.")
s("E eu consigo jogar com qual controle?")
t("Você pode jogar com diversos tipos de controles, como controles USB, controles bluetooth, entre outros.")
s("E eu consigo jogar com qual resolução?")
t("Você pode jogar com diversas resoluções, desde as resoluções originais dos consoles até resoluções mais altas.")
s("E eu consigo jogar com qual qualidade?")
t("Você pode jogar com diversas qualidades gráficas, desde as qualidades originais dos consoles até qualidades mais altas.")
s("E eu consigo jogar com qual desempenho?")
t("Você pode jogar com diversos desempenhos, desde os desempenhos originais dos consoles até desempenhos mais altos.")
s("Caramba! Parece incrível!!! Vou comprar um Raspberry Pi e instalar a Recalbox para jogar!")
t("Se você quiser Aspira, eu te passo a minha imagem pronta, que foi baseada no RecalBox, ela se chama finoPI e tem muitos jogos já configurados. Além do driver de vídeo, bibliotecas de jogos e tudo mais.")
s("Sério? Você tem uma imagem pronta?")
t("Sim, eu tenho a imagem pronta do finoPI, com muitos jogos clássicos já configurados e prontos para jogar. Eu fiz para o meu filho em 2016, é uma imagem bem madura e estável.")
s(f"Nossa, que legal! Eu quero sim! Obrigado {c.Teacher()}!")
