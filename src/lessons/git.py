#!/usr/bin/env python3

# Importing the chat class from the talker module
from talker import chat

# Especificação da aula de git:
# O professor fala sobre o Git e o aluno
# interage com o professor.
# O aluno pode fazer perguntas e o professor responde.
# A conversa deve ser descontraída, o aluno não possui muito conhecimento sobre o assunto, não sabe nem o que é um gerenciador de versões.
# O professor deve explicar o que é o Git e como ele funciona.
# O professor deve contar a história do Git e como ele foi criado.
# O professor deve explicar o que é um repositório e como ele funciona.
# O professor deve explicar o que é um commit e como ele funciona.
# O professor deve explicar o que é um branch e como ele funciona.
# O professor deve explicar o que é um merge e como ele funciona.
# O professor deve explicar o que é um pull request e como ele funciona.
# O professor deve explicar o que é um fork e como ele funciona.
# O professor deve explicar o que é um clone e como ele funciona.
# O professor deve explicar o que é um push e como ele funciona.
# O professor deve ajudar o aluno a criar uma conta no github.com
# O professor deve ajudar o aluno a criar um repositório no github.com
# Os comandos que o professor deve ensinar, serão apenas de exemplo, não serão executados localmente no terminal.
# Cada comando exposto pelo professor deve ser explicado para o aluno de forma bem informal mas clara.
# Os comandos não precisam ser sincronizados com o repositorio remoto, apenas localmente.
# Ao final da aula, não devem ficar arquivos criados localmente, todos os exemplos de comandos devem ser teóricos

c = chat.Chat()
c.Speak("""E aí cara, como vc está? Vamos falar um pouco sobre Git?""")
c.StudentComment("""Claro! Mas oque é Git?""")
c.Speak("""Sabe o código fonte que você faz? é uma ferramenta que te ajuda a guardar ele, e a controlar as mudanças que você faz nele.""")  
c.Speak("""O Git é um sistema de controle de versão, que te ajuda a guardar o histórico de alterações do seu código.""")
c.Speak("""Ele foi criado por Linus Torvalds, o mesmo cara que criou o Linux, e é uma ferramenta muito poderosa.""")
c.Speak("""O Git é um sistema distribuído, ou seja, você pode ter uma cópia do seu código em vários lugares.""")
c.Speak("""O Git é muito usado em projetos de software, mas também pode ser usado para guardar qualquer tipo de arquivo.""")
c.Speak("""Uma das melhores ferramentas gratuitas para guardar seu código é o GitHub, que é um site que te ajuda a guardar seu código.""")
c.Speak("""O GitHub é uma rede social de programadores, onde você pode compartilhar seu código com outras pessoas.""")
c.Speak("""O GitHub é muito usado em projetos de software livre, e é uma ferramenta muito poderosa.""")
c.StudentComment("""Legal! Mas como eu faço para usar o Git?""")
c.Speak("""Para usar o Git, você precisa instalar ele no seu computador.""")
c.Speak("""Você pode baixar o Git no site oficial dele, e instalar ele no seu computador.""")
c.Speak("""Depois de instalar o Git, você pode usar ele no seu terminal.""")
c.StudentComment("""Mas oque é um terminal?""")
c.Speak("""O terminal é uma ferramenta que te ajuda a interagir com o seu computador.""")
c.Speak("""Você pode usar o terminal para executar comandos no seu computador.""")
c.Speak("""O terminal é muito poderoso, e é a melhor forma de usar o Git.""")
c.Speak("""Você pode usar o terminal para executar comandos do Git, e controlar o seu código. É como adultos resolvem esses problemas.""")
c.StudentComment("""Entendi! Mas como eu faço para criar um repositório no GitHub?""")
c.Speak("""Para criar um repositório no GitHub, você precisa criar uma conta no site.""")
c.Speak("""Depois de criar uma conta no GitHub, você pode criar um repositório novo.""")
c.Speak("""Um repositório é um lugar onde você guarda o seu código.""")
c.StudentComment("""Eu preciso pagar por isso?""")
c.Speak("""Não, o GitHub é gratuito para projetos de código aberto. Você só precisa pagar se quiser guardar código privado.""")
c.Speak("""Mas você pode usar o Git sem o GitHub, e guardar o seu código no seu computador.""")
c.StudentComment("""Posso usar meu email particular para isso?""")
c.Speak("""Sim, você pode usar o seu email particular para criar uma conta no GitHub.""")
c.Speak("""Está fazendo sentido? Pq eu já disse várias vezes que é uma solução gratuita para projetos de código aberto, mas se vc quiser guardar código privado, vc precisa pagar... ficou claro?""")
c.StudentComment("""Sim, ficou claro!""")
c.Speak("""Então, vamos criar uma conta no GitHub e um repositório novo.""")
c.StudentComment("""Vamos lá!""")
c.Speak("""Para criar uma conta no GitHub, você precisa acessar o site github.com e clicar em Sign Up.""")
c.Speak("""Depois de criar uma conta no GitHub, você pode criar um repositório novo clicando em New Repository.""")
c.Speak("""Depois de criar um repositório novo, você pode clonar ele no seu computador usando o comando git clone.""")
c.Speak("""O comando git clone faz uma cópia do seu repositório no seu computador.""")
c.ShowCommand("""git clone github.com/usuario/repositorio""")
c.Speak("""Depois de clonar o repositório, você pode fazer alterações no seu código e guardar essas alterações usando o comando git commit.""")
c.Speak("""Se você olhar no seu diretório, vai ver que uma pasta com o nome do seu repositório foi criada.""")
c.Speak("""Dentro dessa pasta, você vai ver todos os arquivos do seu repositório.""")
c.Speak("""Como não colocamos nenhum arquivo ali, deve estar vazia... na verdade não estará vazia, você vai ver um arquivo oculto chamado .git""")  
c.Speak("""Esse arquivo é o que o Git usa para guardar o histórico de alterações do seu código.""")
c.StudentComment("""Entendi! Mas como eu faço para adicionar arquivos ao meu repositório?""")
c.Speak("""Para adicionar arquivos ao seu repositório, você precisa usar o comando git add.""")
c.Speak("""O comando git add adiciona arquivos ao seu repositório.""")
c.StudentComment("""Mas eu não criei nenhum arquivo ainda... como podemos seguir?""")
c.Speak("""Vamos criar um arquivo novo no seu repositório.""")
c.ShowCommand("""touch README.md""")
c.Speak("""Depois de criar um arquivo novo no seu repositório, você pode adicionar ele ao seu repositório usando o comando git add.""") 
c.ShowCommand("""git add README.md""")
c.Speak("""Depois de adicionar o arquivo ao seu repositório, você pode guardar as alterações usando o comando git commit.""")
c.Speak("""O comando git commit guarda as alterações no seu repositório.""")
c.ShowCommand("""git commit -m \"Adicionando arquivo README.md\"""")
c.Speak("""Depois de guardar as alterações no seu repositório, você pode enviar as alterações para o GitHub usando o comando git push.""")
c.Speak("""O comando git push envia as alterações para o GitHub.""")
c.ShowCommand("""git push""")
c.StudentComment("""Entendi! Mas e se eu quiser fazer alterações no meu código?""")
c.Speak("""Se você quiser fazer alterações no seu código, você pode criar um branch novo.""")
c.Speak("""Um branch é uma cópia do seu código onde você pode fazer alterações sem afetar o código principal.""")
c.StudentComment("""Não entendi direito, o que é uma branch? Quais problemas ela resolve?""")
c.Speak("""Uma branch é uma cópia do seu código onde você pode fazer alterações sem afetar o código principal.""")
c.Speak("""Por exemplo, se você quiser adicionar uma nova funcionalidade ao seu código, você pode criar um branch novo.""")
c.Speak("""Depois de adicionar a nova funcionalidade ao seu código, você pode enviar as alterações para o GitHub usando o comando git push.""")
c.Speak("""Vamos treinar, você pode criar um branch novo no seu repositório?""")
c.StudentComment("""Vamos lá!""")
c.Speak("""Para criar um branch novo no seu repositório, você precisa usar o comando git branch.""")
c.ShowCommand("""git branch novo-branch""")
c.Speak("""Depois de criar um branch novo no seu repositório, você pode mudar para ele usando o comando git checkout.""")
c.ShowCommand("""git checkout novo-branch""")
c.Speak("""Depois de mudar para o branch novo, você pode fazer alterações no seu código.""")
c.Speak("""Depois de fazer alterações no seu código, você pode guardar as alterações usando o comando git commit.""")
c.Speak("""Depois de guardar as alterações no seu branch novo, você pode enviar as alterações para o GitHub usando o comando git push.""")
c.ShowCommand("""git push""")
c.Speak("""Depois de enviar as alterações para o GitHub, você pode fazer um pull request.""")
c.StudentComment("""Oque é um pull request?""")
c.Speak("""Ótima pergunta meu pequeno gafanhoto, vamos lá!""")
c.Speak("""Um pull request é uma solicitação para adicionar as suas alterações ao código principal.""")
c.Speak("""Por exemplo, se você fez uma alteração no seu código e quer que ela seja adicionada ao código principal, você pode fazer um pull request.""")
c.Speak("""Depois de fazer um pull request, alguém que é responsável pelo código principal pode revisar as suas alterações e decidir se elas devem ser adicionadas.""")
c.Speak("""Se as suas alterações forem aceitas, elas são adicionadas ao código principal.""")
c.StudentComment("""Entendi! Mas e se eu quiser adicionar as alterações de outra pessoa ao meu código?""")
c.Speak("""Se você quiser adicionar as alterações de outra pessoa ao seu código, você pode fazer um merge.""")
c.StudentComment("""Oque é um merge? Cada doideira que aparece aqui...""")
c.Speak("""Um merge é uma operação que combina duas branches em uma.""")
c.Speak("""Por exemplo, se você fez uma alteração no seu código e outra pessoa fez uma alteração no código dela, você pode fazer um merge.""")
c.Speak("""Depois de fazer um merge, as alterações da outra pessoa são adicionadas ao seu código.""")
c.Speak("""Merge, em uma explicação simples, é o nome que usamos para a ação de misturar o código de duas branches.""")
c.StudentComment("""Entendi! Mas e se eu quiser fazer alterações no código de outra pessoa?""")
c.Speak("""Se você quiser fazer alterações no código de outra pessoa, você pode fazer um fork.""")
c.StudentComment("""Oque é um fork? Garfo? que nome estranho...""")
c.Speak("""Um fork é uma cópia do código de outra pessoa.""")
c.Speak("""Por exemplo, se você quer fazer alterações no código de outra pessoa, você pode fazer um fork.""")
c.Speak("""Depois de fazer um fork, você pode fazer alterações no código da outra pessoa.""")
c.Speak("""Depois de fazer as alterações, você pode fazer um pull request para a pessoa que é responsável pelo código.""")
c.Speak("""Se as suas alterações forem aceitas, elas são adicionadas ao código principal.""")
c.StudentComment("""Entendi! Mas e se eu quiser fazer um clone do código de outra pessoa?""")
c.Speak("""Gosto assim, bem curioso... vamos lá!""")
c.Speak("""Se você quiser fazer um clone do código de outra pessoa, você pode usar o comando git clone.""")
c.Speak("""O comando git clone faz uma cópia do código de outra pessoa no seu computador.""")
c.ShowCommand("""git clone github.com/usuario/repositorio""")
c.Speak("""Depois de fazer um clone do código de outra pessoa, você pode fazer alterações no código.""")
c.Speak("""Depois de fazer as alterações, você pode enviar as alterações para o GitHub usando o comando git push.""")
c.ShowCommand("""git push""")
c.Speak("""Depois de enviar as alterações para o GitHub, você pode fazer um pull request para a pessoa que é responsável pelo código.""")
c.Speak("""Se as suas alterações forem aceitas, elas são adicionadas ao código principal.""")
c.StudentComment("""Isso aqui é um mundo novo... como esse tipo de coisa era feita antes do Git?""")
c.Speak("""Antes do Git, as pessoas usavam outras ferramentas para controlar o código.""")
c.Speak("""Por exemplo, algumas pessoas usavam o Subversion, que é um sistema de controle de versão centralizado.""")
c.Speak("""O Subversion é uma ferramenta muito poderosa, mas tem algumas limitações.""")
c.Speak("""Uma das limitações do Subversion é que ele é centralizado, ou seja, você precisa de uma conexão com a internet para usar ele.""")
c.Speak("""O Git resolve esse problema sendo um sistema de controle de versão distribuído.""")
c.Speak("""Além disso, o Git é muito mais rápido que o Subversion, e tem mais recursos.""")
c.Speak("""Além do Subversion, as pessoas usavam outras ferramentas para controlar o código, como o CVS e o Mercurial.""")
c.Speak("""O Git é a ferramenta mais usada atualmente, e é a melhor opção para controlar o código.""")
c.StudentComment("""Entendi! Mas e se eu quiser aprender mais sobre o Git?""")
c.Speak("""Se você quiser aprender mais sobre o Git, você pode acessar o site oficial dele.""")
c.Speak("""O site oficial do Git tem muita documentação, tutoriais e exemplos.""")
c.Speak("""Além disso, você pode acessar o GitHub e ver os repositórios de outras pessoas.""")
c.Speak("""O GitHub é uma ótima fonte de informação, e você pode aprender muito vendo o código de outras pessoas.""")
c.Speak("""Além disso, você pode acessar o Stack Overflow e fazer perguntas sobre o Git.""")
c.Speak("""O Stack Overflow é uma comunidade de programadores onde você pode fazer perguntas e obter respostas.""")

              
             
