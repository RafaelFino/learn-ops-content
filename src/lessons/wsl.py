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

# Tema: WSL - Windows Subsystem for Linux
# O professor deve explicar o que é o WSL, como ele funciona e como ele pode ser utilizado.
# O professor deve explicar como instalar o WSL no Windows.
# O professor deve explicar como instalar distribuições Linux no WSL.
# O professor deve explicar como executar comandos Linux no WSL.
# O professor deve explicar como acessar arquivos do Windows no WSL.
# O professor deve explicar como acessar arquivos do WSL no Windows.
# O professor deve explicar como acessar a interface gráfica de aplicações Linux no Windows.
# O professor deve explicar como acessar a interface gráfica de aplicações Windows no WSL.
# O professor deve explicar como compartilhar portas entre o WSL e o Windows.
# O professor deve explicar como compartilhar arquivos entre o WSL e o Windows.
# O professor deve explicar como compartilhar a área de transferência entre o WSL e o Windows.
# O professor deve explicar como compartilhar impressoras entre o WSL e o Windows.
# O professor deve explicar como compartilhar dispositivos USB entre o WSL e o Windows.
# O professor deve explicar ows conceitos de containers e como eles podem ser utilizados no WSL.
# O professor deve explicar como instalar o Docker no WSL.
# O professor deve falar sobre os problemas mais comuns ao utilizar o WSL e como resolvê-los.
# O professor deve explicar como é um melhor caminho usar um linux nativo no lugar de WSL.

t("Olá, pequno padawan! Hoje vamos falar sobre o WSL - Windows Subsystem for Linux. Você sabe o que é o isso?")
s(f"Sei não {c.Teacher()}, é de comer ou de passar no cabelo?")
t("Hahaha, não, não é nada disso. O WSL é um recurso do Windows que permite executar comandos Linux no Windows.")
s("Ah, entendi. Rodar um linux dentro do Windows? Tipo uma VM?")
t("Isso mesmo, mas o WSL é mais leve que uma VM e permite executar comandos Linux diretamente no terminal do Windows.")
s("Legal! É o docker?")
t("Não, não é o Docker. O Docker é uma ferramenta de containers, que também pode ser utilizada no WSL.")
s("Entendi. E como eu faço para instalar o WSL?")
t("Para instalar o WSL, você precisa habilitar o recurso nas configurações do Windows.")
s("E depois?")
t("Depois de habilitar o WSL, você precisa instalar uma distribuição Linux disponível na Microsoft Store.")
s("E como eu faço isso?")
t("Você pode instalar a distribuição Linux diretamente pela Microsoft Store ou utilizando o PowerShell.")
s("Você recomenda alguma dessas para começar? Se lembre que eu sou meio lerdo e não sei nada sobre isso...")
t("Eu recomendo a distribuição Ubuntu, pois é uma das mais populares e fáceis de usar.")
s("Ok, vou instalar o Ubuntu. E depois?")
t("Depois de instalar o Ubuntu, você pode acessar o terminal do WSL e executar comandos Linux normalmente.")
s("E como eu acesso arquivos do Windows no WSL?")
t("Você pode acessar os arquivos do Windows no WSL através do diretório /mnt.")
s("E como eu acesso arquivos do WSL no Windows?")
t("Você pode acessar os arquivos do WSL no Windows através do diretório %LOCALAPPDATA%\\Packages.")
s("E como eu acesso a interface gráfica de aplicações Linux no Windows?")
t("Você pode acessar a interface gráfica de aplicações Linux no Windows utilizando um servidor X.")
t("Mas eu realmente recomendo usar o WSL 2, que é mais rápido e possui melhor suporte para a interface gráfica. Porém usar interfaces gráficas dessa forma talvez não seja a melhor opção.")
s("Lembrei do filme inception, um linux dentro de um windows dentro de um linux. Acho que vou ficar só nas aplicações de terminal mesmo.")
t("Hahaha, é quase isso! Mas é bom saber que você pode acessar a interface gráfica se precisar. Mas como sempre falamos, o terminal é o melhor amigo do desenvolvedor.")
q("Eu usei aqui o meu google e vi que tem dois, o WSL e o WSL2, qual a diferença?")
t("O WSL 2 é uma versão mais recente e melhorada do WSL, que possui um kernel Linux completo e melhor desempenho.")
s("Entendi, então é melhor usar o WSL 2?")
t("Sim, eu recomendo usar o WSL 2, pois ele possui melhor desempenho e suporte para mais recursos.")
s("E como eu faço para instalar o Docker no WSL?")
t("Para instalar o Docker no WSL, você precisa seguir as instruções de instalação do Docker para Linux.")
s("E quais são os problemas mais comuns ao utilizar o WSL?")
t("Alguns problemas comuns ao utilizar o WSL são relacionados à integração entre o Windows e o Linux, como compartilhamento de arquivos e portas.")
s("E como eu posso resolver esses problemas?")
t("Você pode resolver esses problemas configurando corretamente as permissões de arquivos e portas no WSL e no Windows. Mas a melhor forma mesmo é usando um linux como adultos fazem, instala na sua máquina e larga esse Windows") 
s("Entendi, obrigado pelas dicas! Vou tentar instalar o WSL e ver como funciona.")
t("Ótimo! Se tiver alguma dúvida, é só me chamar. Boa sorte com o WSL!")
