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

# Tema: Memórias RAM, ROM, SSD, HHD e etc
# O professor deve explicar de forma bem simples e descontraída sobre os tipos de memórias existentes, como RAM, ROM, SSD, HHD e etc.
# O professor deve explicar a diferença entre elas e suas aplicações práticas.
# O professor deve explicar a diferença entre memória volátil e não volátil.
# O professor deve explicar a diferença entre memória de leitura e escrita.
# O professor deve explicar a diferença entre memória de armazenamento e memória de processamento.
# O professor deve explicar a diferença entre memória física e memória virtual.
# O professor deve explicar a diferença entre memória cache e memória principal.
# O professor deve explicar a diferença entre memória primária e secundária.
# O professor deve explicar a diferença entre os tipos de tecnologias de armazenamento
# O professor deve explicar a sobre como um disco rigidio funciona e como um SSD funciona.
# O professor deve explicar sobre a importância da memória RAM para o processamento de dados.
# O professor deve explicar sobre a importância da memória ROM para o armazenamento de dados.


def t(m):
    c.Speak(m)


def s(m):
    c.StudentComment(m)


def q(m):
    c.Question(m)


t("Olá, padawan! Hoje vamos falar sobre memórias.")
t("Você sabe o que é memória?")
s("Não, Fino. Que desgraça é essa?")
t("Calma, padawan! Memória é um qualquer coisa que armazena dados. Simples assim...")
s("Você fala que é simples, mas eu não entendi nada.")
t("Vamos lá, padawan! Memória é onde a gente guarda as coisas. Como um HD, por exemplo.")
s("HD? É de comer ou de passar no cabelo?")
t("Não, padawan! HD é um disco rígido. É onde a gente guarda os arquivos no computador.")
s("Ah... disco rígido? Ele é duro? Existe um mole?")
t("Olha, já existiu... é uma ótima observação! No passado, não haviam muitas formas de armazenar dados")
t("Os disquetes eram flexíveis, por exemplo. Mas hoje em dia, temos os HDs, que são rígidos.")
t("Por isso eram chamados de floppy disk, eram flexíveis, moles mesmo")
t("Então, criaram os discos rídigos, que são discos de materiais magnéticos, você acredita que eles armazenam dados usando níveis de magnetismo em um disco? É surreal pensar que isso funciona...")
s("Tá... mas você ainda não me explicou direito o que é memória... ou eu não entendi direito...")
t("Bom, memória é qualquer informação que guardamos em algum lugar, podemos dizer inclusive que um caderno é um tipo de memória")
s("ok, vou aceitar isso... eu sempre escuto falarem de HD, SSD, RAM... o que são essas coisas?")
t("Bom, vamos do começo pequeno gafanhoto...")
t("Pense em um programa acontecendo em um computador, para ele executar os dados dele precisam estar em algum lugar que possa ser alterado, funcionando como uma lousa, por exemplo")
t("Esse lugar onde o programa acontece e é alterado, chamamos de memória de execução, é como se fosse um rascunho onde as contas e operações acontecem")
t("Essa memória dizemos que é volátil, ela fica sendo trabalhada o tempo todo e não é persistente")
s("Pronto, já vem vc com essas palavras complicadas... persistente???")
t("Sim pequeno padawan, Persistente é algo que dura, que precisa persistir, que precisa depois ser recuperado... nesse caso, essa memória é temporária")
t("Ela é volátil, porque quando desligamos o computador, ela se apaga, ou seja, só existe enquanto o computador está ligado")
t("A memória RAM é um exemplo de memória volátil, é onde os programas são executados e os dados são armazenados temporariamente")
t("Então quando dizemos que um dispositivo tem X Mb de RAM, estamos falando da quantidade de memória que ele tem para executar programas")
t("Ela é fundamental na performance de qualquer programa, quanto mais RAM, mais programas podem ser executados ao mesmo tempo")
s("Entendi... mas e o HD? ele não é isso então... o que ele é?")
t("O HD é um tipo de memória de armazenamento, ele é onde os dados são armazenados de forma persistente")
t("Quando desligamos o computador, os dados continuam lá, armazenados no HD")
t("O HD é um disco rígido, como eu disse, ele é composto de discos magnéticos que armazenam os dados")
t("Ele é extremamente mais lento que a RAM, mas tem uma capacidade de armazenamento muito maior")
t("Então, quando você instala um programa, ele é armazenado no HD e quando você executa, ele é carregado para a RAM")
s("Entendi... e o SSD? o que é isso?")
t("O SSD é um tipo de memória de armazenamento, assim como o HD, mas ele é muito mais rápido")
t("Ele é composto de chips de memória, sem partes móveis, o que o torna muito mais rápido que um HD")
t("Ele é muito mais caro que um HD, mas é muito mais rápido e confiável")
t("Então, se você quer um computador rápido, você precisa de um SSD")
s("Entendi... e o ROM? o que é isso?")
t("O ROM é um tipo de memória de armazenamento, mas ela é somente de leitura")
t("Isso significa que você não pode alterar os dados que estão armazenados nela")
t("Ela é usada para armazenar informações que não podem ser alteradas, como o BIOS do computador")
t("O BIOS é um programa que inicia o computador, ele é armazenado no ROM e é carregado quando o computador é ligado")
t("Então, o ROM é uma memória de armazenamento, mas somente de leitura")
t("É comum, quando falamos de memória, estamos falando da memória RAM, quando falamos de dados que precisam ser persistente, chamamos genéricamente de Storage")
s("Acho que as coisas estão fazendo sentido... RAM é para executar programas, Storage é para guardar coisas de forma persistente, ROM é para coisas somente de leitura... existem outras?")
t("Sim, existem muitos tipos de memórias, mas essas são as principais")
t("Existem também as memórias cache, que são memórias muito rápidas, mas muito pequenas")
t("Elas são usadas para armazenar dados temporários que são acessados com muita frequência")
t("Então, quando você acessa um arquivo, ele é carregado para a memória cache, para que o acesso seja mais rápido")
t("Acho que com isso você já tem uma boa noção sobre memórias, padawan!")
c.LastStep()
