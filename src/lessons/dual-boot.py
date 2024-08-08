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

# Tema: Computadores com dual boot, UEFI, GRUB Refind e etc
# O professor deve explicar de forma bem simples e descontraída sobre o dual boot, UEFI, GRUB, Refind e etc.
# O professor deve explicar a diferença entre UEFI e BIOS.
# O professor deve explicar a diferença entre UEFI e MBR.
# O professor deve explicar a diferença entre UEFI e GPT.
# O professor deve explicar a diferença entre UEFI e Legacy.
# O professor deve explicar o que é um gerenciador de boot.
# O professor deve explicar a diferença entre GRUB e Refind.
# O professor deve explicar a diferença entre dual boot e multi boot.
# O preofessor deve explicar como o Windows e o Linux podem ser instalados no mesmo computador.
# O professor deve explicar como o dual boot pode ser feito em um computador.
# O professor deve explicar como o GRUB funciona.
# O professor deve explicar como o Refind funciona.
# O professor deve explicar como o UEFI funciona.
# O professor deve explicar como o BIOS funciona.
# O professor deve explicar como o MBR funciona.
# O professor deve explicar como o GPT funciona.
# O professor deve explicar como o Legacy funciona.
# O professor deve explicar como o Windows lida com o dual boot.

t("Olá, Doença! Hoje vamos falar sobre dual boot. Alias, como funciona o boot de um computador...")
t("Você sabe o que é boot?")
s(f"Não, {c.Teacher()}. Que desgraça é essa?")
t("Calma, Doença! Boot é o processo de inicialização do computador.")
s("Ah... é tipo um despertar?")
t("Exatamente! Quando você liga o computador, ele faz o boot.")
t("O boot é o processo de inicialização do sistema operacional.")
t("O sistema operacional é o software que controla o hardware do computador.")
t("O sistema operacional é o que você vê na tela do computador.")
t("O sistema operacional é o que você usa para executar programas.")
t("O sistema operacional é o que você usa para acessar a internet.")
t("O sistema operacional é o que você usa para jogar.")
t("O sistema operacional é o que você usa para trabalhar.")
t("O sistema operacional é o que você usa para estudar.")
t("O sistema operacional é o que você usa para se divertir.")
t("O sistema operacional é o que você usa para tudo!")
q("Tudo mesmo? Como assim?")
t("Sim, Doença! O sistema operacional é o que você usa para tudo!")
q("E como funciona esse negócio de boot?")
t("Quando você liga o computador, ele faz o boot.")
t("Quando um computador liga, ele tem alguns processos que são executados, antes de carregar qualquer coisa, existe um cara chamado POST, que verifica se o hardware está funcionando corretamente.")
t("Depois disso, o computador procura um sistema operacional para carregar.")
t("E é aí que entra o boot. Existem várias formas de fazer isso.")
t("Uma delas é o BIOS, que é um sistema antigo de boot. Também é conhecido por Legacy.")
t("O BIOS é um sistema de boot antigo, que busca em uma partição do disco rígido o sistema operacional.")
t("Outra forma é o UEFI, que é um sistema de boot mais moderno.")
t("O UEFI é um sistema de boot mais moderno, que busca em uma partição do disco rígido o sistema operacional. É bem mais versátil que o BIOS.")
t("O UEFI é mais rápido que o BIOS e tem mais recursos além de ser mais seguro.")
t("O UEFI é o sistema de boot mais usado atualmente.")
s("Caraca... e como eu faço para escolher qual sistema operacional eu quero usar?")
t("Bom, Doença! Aqui que a coisa fica ainda mais complexa, mas vou tentar simplificar...")
t("Quando você tem dois sistemas operacionais no mesmo computador, isso é chamado de dual boot.")
t("Dual boot é quando você tem dois sistemas operacionais no mesmo computador.")
t("Por exemplo, você pode ter o Windows e o Linux no mesmo computador.")
t("Quando você liga o computador, você pode escolher qual sistema operacional você quer usar.")
t("Isso é feito através de um gerenciador de boot.")
t("O gerenciador de boot é um programa que permite escolher qual sistema operacional você quer usar.")
s("Esse que é o tal do GRUB?")
t("Sim, Doença! O GRUB é um gerenciador de boot muito usado no Linux.")
t("O GRUB é um programa que permite escolher qual sistema operacional você quer usar.")
q("E o Refind? O que é isso?")
t("O Refind é outro gerenciador de boot, muito usado em computadores Apple.")
t("O Refind é um programa que permite escolher qual sistema operacional você quer usar.")
t("O Refind é mais moderno que o GRUB e tem mais recursos.")
t("O Refind é um gerenciador de boot muito bonito e fácil de usar.")
q("Eu tinha um dual boot no meu computador, com windows e linux, mas eu não sabia que era dual boot. Meu windows foi atualizado e sumiu o linux. Como eu faço para recuperar?")
t("Bom, Doença! Quando você atualiza o Windows, ele pode apagar o GRUB.")
t("O GRUB é o gerenciador de boot do Linux.")
t("Quando você atualiza o Windows, ele pode apagar o GRUB e você perde o dual boot.")
t("Para recuperar o dual boot, você precisa reinstalar o GRUB.")
t("Você pode fazer isso usando um live CD do Linux ou a partir da imagem de instalação do Linux em um pendrive.")
t("Depois de reinstalar o GRUB, você terá o dual boot de volta.")
q("Mas eu não consigo pelo Windows resolver isso?")
t("Não, Doença! O Windows não consegue recuperar o GRUB.")
t("Você precisa usar o Linux para reinstalar o GRUB.")
q("E o Windows não saberia ser esse meu gerenciador de boot?")
t("Não, Doença! O Windows não sabe ser gerenciador de boot.")
t("O Windows só sabe carregar o Windows.")
t("Para carregar o Linux, você precisa do GRUB.")
s("Mas que porcaria esse gerenciador do Windows, hein?")
t("É, Doença! O Windows é assim mesmo.")
t("O Windows é um sistema operacional fechado.")
q("Mas eu ouço um monte de coisas sobre esses caras, o Refind, o GRUB, o UEFI... eu preciso saber disso tudo?")
t("Não, Doença! Você não precisa saber de tudo isso.")
t("Mas é bom saber o básico.")
q("Consigo instalar o Refind no meu computador com Linux?")
t("Sim, Doença! Você pode instalar o Refind no seu computador com Linux.")
s("Uau! E como eu faço isso?")
t("Você pode instalar o Refind usando o gerenciador de pacotes do Linux.")
t("O Refind é um programa que você pode instalar no Linux.")
t("Depois de instalar o Refind, você pode usá-lo como gerenciador de boot.")
q("E o que é esse tal de MBR?")
t("O MBR é um sistema de particionamento de disco.")
t("O MBR é um sistema antigo de particionamento de disco.")
t("O MBR é um sistema de particionamento de disco que é usado com o BIOS.")
t("O MBR é um sistema de particionamento de disco que é usado com o Legacy.")
t("O Windows usa o MBR para particionar o disco. É antigo mas ainda é muito usado e tem grande compatibilidade.")
q("E o GPT? O que é isso?")
t("O GPT é um sistema de particionamento de disco. Não confunda com o ChatGPT.")
t("O GPT é um sistema moderno de particionamento de disco.")
t("O GPT é um sistema de particionamento de disco que é usado com o UEFI.")
t("O GPT é um sistema de particionamento de disco que é usado com o Refind.")
t("O GPT é um sistema de particionamento de disco que é mais moderno que o MBR.")
q("Quantas siglas... o que cada uma delas signifinca?")
t("MBR significa Master Boot Record.")
t("GPT significa GUID Partition Table.")
t("UEFI significa Unified Extensible Firmware Interface.")
t("BIOS significa Basic Input/Output System.")
t("GRUB significa GRand Unified Bootloader.")
t("Refind significa REally Find.")
t("POST significa Power-On Self-Test.")
t("Cansou? Quer mais?")
s(f"Não, {c.Teacher()}! Chega por hoje.")


