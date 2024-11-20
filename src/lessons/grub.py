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

c = chat.Chat()

c.Speak("""Olá, Pequenos Gafanhotos! Hoje vamos explorar o GRUB, o *Grand Unified Bootloader*. Já ouviu falar dele?""")
c.StudentComment("""Oi, professor! Já ouvi um pouco, mas não entendo muito bem o que é. Pode me explicar?""")
c.Speak("""Claro, Jovem Tartaruga! O GRUB é como o maestro que organiza a inicialização do seu computador. Imagine que você está em uma festa e o GRUB é o garçom que pergunta: 'Qual música você quer ouvir? Rock? Pop? Jazz?'. O GRUB faz algo parecido, mas escolhe qual sistema operacional ou configuração você quer iniciar.""")
c.Speak("""Quando você liga o computador, o GRUB aparece como uma tela inicial onde você pode escolher entre diferentes sistemas operacionais ou configurações.""")
c.Speak("""Se você não fizer nada, ele escolhe automaticamente a opção padrão após um tempo. Mas se você quiser escolher uma opção diferente, pode usar as teclas de seta para navegar e Enter para selecionar.""")
c.StudentComment("""E como eu faço configurações no GRUB?""")
c.Speak("""Ótima pergunta, Pequeno Gafanhoto! Para fazer configurações, você edita um arquivo chamado `grub.cfg`, que está no diretório `/boot/grub`. Por exemplo, para mudar o tempo que o GRUB espera antes de escolher a opção padrão, você altera essa configuração.""")
c.Speak("""Aqui está um comando de exemplo que você usaria para atualizar a configuração do GRUB no Linux:""")
c.ShowCommand("""sudo update-grub""")
c.Speak("""Esse comando faz uma varredura nos sistemas operacionais instalados e atualiza o menu do GRUB para você.""")
c.StudentComment("""E se eu quiser adicionar uma nova entrada para um sistema operacional que não está aparecendo?""")
c.Speak("""Se você precisar adicionar uma nova entrada, pode criar um arquivo de configuração personalizado no diretório `/etc/grub.d/`. Por exemplo, criar um arquivo chamado `40_custom` com uma nova entrada:""")
c.ShowCommand("""menuentry "Meu Novo Sistema" {
    set root='(hd0,1)'
    chainloader +1
}""")
c.Speak("""Depois, você executa `sudo update-grub` novamente para aplicar as mudanças.""")
c.StudentComment("""E se o GRUB não encontrar o sistema operacional?""")
c.Speak("""Ah, se isso acontecer, o GRUB pode mostrar uma mensagem de erro e você pode acabar em um prompt de comando chamado "grub rescue". A partir daí, você pode tentar restaurar o GRUB ou corrigir o caminho para o sistema operacional.""")
c.StudentComment("""Como posso me preparar para evitar esses problemas?""")
c.Speak("""É sempre bom ter um disco de recuperação ou uma mídia de instalação por perto. Além disso, fazer backups regulares do seu sistema é uma boa prática para não perder nada importante.""")
c.Speak("""Você pode conferir a documentação oficial e alguns tutoriais online. Aqui estão algumas sugestões de materiais:""")
c.Speak("""- **"The GRUB Manual"**: Disponível no [site oficial do GNU GRUB](https://www.gnu.org/software/grub/manual/grub/grub.html)""")
c.Speak("""- **"Linux Command Line and Shell Scripting Bible"**: Este livro tem uma seção muito boa sobre GRUB e outros aspectos do Linux.""")
c.StudentComment("""Muito obrigado, professor! Isso foi muito útil.""")
c.Speak("""Não vá embora tão cedo, Pequeno Gafanhoto! O mundo do GRUB é vasto e há muito mais para explorar. Na próxima aula, vamos falar sobre como o GRUB se compara a outros bootloaders e como ele lida com problemas de inicialização. Até lá, mantenha sua curiosidade afiada e seus sistemas operacionais organizados!""")
c.StudentComment("""Com certeza! Até mais, professor!""")
c.Speak("""Até mais, Jovem Tartaruga! E lembre-se: o conhecimento é como o GRUB, sempre há uma nova entrada para explorar!""")
