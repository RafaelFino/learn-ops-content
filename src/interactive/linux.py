#!/usr/bin/env python3

# Importing the chat class from the talker module
from talker import chat

# Especificações para a aula de linux e de terminal:
# O instrutor deve ser capaz de explicar o que é um sistema operacional
# O instrutor deve ser capaz de explicar o que é um terminal
# O instrutor deve ser capaz de explicar o que é um shell
# O instrutor deve ser capaz de explicar o que é um console
# O instrutor deve ser capaz de explicar o que é um emulador de terminal
# O aluno deve ser capaz de abrir um terminal
# O aluno deve ser capaz de executar comandos no terminal
# O aluno deve ser capaz de executar comandos no terminal com argumentos
# O aluno possui pouca familiaridade com o terminal
# A conversa deve ser leve e descontraída, o aluno deve se mostrar muito curioso
# O professor deve ser paciente e explicar tudo com calma, em tom brincalhão, mas sem perder o foco, sempre usando exemplos didáticos
# O aluno deve ser capaz de entender a diferença entre um terminal e um emulador de terminal
# A cada nova informação, o aluno deve-se mostrar interessado e fazer perguntas que conectem com as informações anteriores e com o que está sendo dito
# O professor deve contar sobre a história do Unix, BSD e Linux
# O professor deve explicar o que é um sistema operacional
# O professor deve explicar o que é um kernel
# O professor deve explicar o que é o LSB
# O professor deve explicar o que é o POSIX
# O professor deve explicar as diferenças entre o Linux e o Unix
# O professor deve explicar as diferenças entre o Linux e o BSD
# O professor deve explicar as diferenças entre o Linux e o Windows
# O professor deve explicar as diferenças entre o Linux e o MacOS
# O professor deve explicar o que é um shell script
# O professor deve explicar o que é um interpretador de comandos
# O professor deve aconselhar o uso do ZSH como interpretador de comandos
# O professor deve aconselhar o uso do Oh My ZSH como gerenciador de configurações do ZSH
# O professor deve aconselhar o uso de uma ferramenta de terminal que permita a personalização do terminal, como terminator por exemplo
# O professor deve sempre validar se o Aluno está entendendo o que está sendo dito e o Aluno deve responder com sinceridade e citando exemplos de uso do que vou informado
# O professor deve falar sobre o que é um arquivo
# O professor deve falar sobre como funcionam as permissões de arquivos
# O professor deve falar sobre como alterar as permissões de arquivos
# O professor deve explicar o conceito de usuário e grupos em um sistema linux
# O professor deve falar sobre como saber qual usuário está logado no sistema com o comando whoami
# O professor deve falar sobre como alterar o dono de um arquivo
# O professor deve falar sobre como alterar o grupo de um arquivo
# O professor deve falar sobre como alterar o dono e o grupo de um arquivo
# O professor deve falar sobre o que é um diretório
# O professor deve explicar o que é um caminho absoluto
# O professor deve explicar o que é um caminho relativo
# O professor deve explicar como navegar entre diretórios
# O professor deve explicar como saber em qual diretório está com o comando pwd
# O professor deve explicar como listar arquivos e diretórios
# O professor deve explicar como procurar onde está um arquivo
# O professor deve explicar como criar diretórios
# O professor deve explicar como remover diretórios
# O professor deve explicar como renomear diretórios
# O professor deve explicar como copiar arquivos
# O professor deve explicar como mover arquivos
# O professor deve explicar como remover arquivos
# O professor deve explicar como renomear arquivos, comparando com as operações com diretórios
# O professor deve explicar cada comando, com exemplos práticos e mostrando como usar cada comando
# O professor deve explicar o que é um link simbólico
# O professor deve explicar o que é um link físico
# O professor deve explicar como criar links simbólicos
# O professor deve explicar como criar links físicos
# O professor deve explicar como remover links
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando cat
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando less
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando more
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando head
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando tail
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando wc
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando grep
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando sed
# O professor deve explicar como exibir o conteúdo de um arquivo com o comando awk
# O professor deve explicar como editar um arquivo com o editor vim
# O professor deve explicar como os modos de operação do vim funcionam e como alterar entre eles
# O professor deve explicar como, uma vez dentro do vim, como procurar por uma palavra
# O professor deve explicar como, uma vez dentro do vim, como substituir uma palavra
# O professor deve explicar como, uma vez dentro do vim, como salvar um arquivo
# O professor deve explicar como, uma vez dentro do vim, como sair do vim
# O professor deve explicar como verificar quais processos estão rodando no sistema com o comando ps
# O professor deve explicar como verificar quais processos estão rodando no sistema de forma detalhada e ordenada com o comando htop
# O professor deve explicar como mata um processo com o comando kill
# O professor deve explicar como mata um processo de forma forçada com o comando kill -9
# O professor deve explicar como mata um processo de forma interativa com o comando kill -i
# O professor deve explicar como mata um processo de forma interativa com o comando pkill
# O professor deve explicar como mata um processo de forma interativa com o comando killall
# O professor deve explicar como verificar o uso de memória com o comando free
# O professor deve explicar como verificar o uso de disco com o comando df
# O professor deve explicar como verificar o uso de disco com o comando du
# O professor deve explicar como verificar o uso de disco com o comando pwd
# O professor deve explicar como verificar como funciona um sistema de arquivos e sobre as partições de um sistema Linux
# O professor deve contar a história do Linux e sua evolução do Unix e como isso refletiu no uso dos sistemas de arquivos no Linux e sobre os pontos de montagem, comparando com o Windows
# O professor deve explicar como verificar o uso de disco com o comando mount
# O professor deve explicar como verificar o uso de disco com o comando lsblk
# O Professor deve explicar como usar o comando curl para fazer requisições HTTP
# O professor deve explicar como usar o comando wget para fazer requisições HTTP
# O professor deve explicar como usar o comando jq para manipular JSON, muito útil ao fazer requisições HTTP
# O professor deve explicar o que é uma sessão SSH, como funciona e como se conectar a uma máquina remota
# O professor deve explicar como usar chaves SSH para se conectar a uma máquina remota
# O professor deve explicar como usar o comando ssh para se conectar a uma máquina remota
# O professor deve explicar como usar o comando scp para copiar arquivos entre máquinas
# O professor deve explicar como usar o comando netstat para verificar as conexões de rede
# O professor deve explicar como usar o comando ping para verificar a conexão com um servidor
# O professor deve explicar como usar o comando traceroute para verificar a rota de uma conexão
# O professor deve explicar como usar o comando dig para verificar informações de DNS
# O professor deve explicar como usar o comando nslookup para verificar informações de DNS
# O professor deve explicar como usar o comando uname para verificar informações do sistema
# O professor deve explicar como usar o comando lsb_release para verificar informações do sistema
# O professor deve explicar como usar o comando neofetch para verificar informações do sistema
# O professor deve falar como um sistema linux lida com gerenciamento de pacotes de bilbiotecas
# O professor deve explicar como usar o comando apt para instalar pacotes no sistema
# O professor deve explicar como usar o comando apt para remover pacotes no sistema
# O professor deve explicar como usar o comando apt para atualizar pacotes no sistema
# O professor deve explicar como usar o comando apt para buscar pacotes no sistema
# O professor deve explicar como usar o comando apt para verificar informações de pacotes no sistema

c = chat.Chat()

c.Speak("Olá, Aluno! Tudo bem?")
c.AskEnter()
c.Speak("Hoje vamos falar sobre Linux e sobre o terminal, tudo bem?")
c.Speak("Você já ouviu falar sobre o Linux?")
c.Speak("O Linux é um sistema operacional, assim como o Windows e o MacOS")
c.Question("Ah, entendi! Mas o que é um sistema operacional?")
c.Speak("Um sistema operacional é um software que gerencia os recursos de hardware de um computador")
c.Speak("Ele fornece uma interface para o usuário interagir com o computador")
c.Speak("No caso do Linux, a interface mais comum é o terminal")
c.Speak("Você sabe o que é um terminal?")
c.StudentComment("Não, não sei! O que é um terminal?")
c.Speak("O terminal é uma interface de texto que permite que você execute comandos no sistema operacional")
c.Speak("É como se fosse uma janela para o sistema operacional")
c.Speak("Você pode executar comandos no terminal para realizar tarefas no sistema")
c.Speak("Por exemplo, você pode criar arquivos, copiar arquivos, instalar programas, entre outras coisas")
c.Speak("O terminal é uma ferramenta muito poderosa e flexível")
c.Speak("Você já usou um terminal antes?")
c.StudentComment("Sim, já usei algumas vezes, mas não sou muito familiarizado, na verdade não entendi bem a diferença entre um terminal e um emulador de terminal")
c.Speak("Ah, entendi! Vamos falar sobre isso então")
c.Speak("O terminal é a interface de texto que você usa para interagir com o sistema operacional")
c.Speak("Já o emulador de terminal é o programa que você usa para abrir o terminal")
c.Speak("Por exemplo, o terminal padrão do Linux é o 'gnome-terminal'")
c.Speak("Mas você pode usar outros emuladores de terminal, como o 'terminator' ou o 'konsole'")
c.Speak("Entendeu a diferença?")
c.StudentComment("Não muito, mas acho que sim! O terminal é a interface de texto e o emulador de terminal é o programa que abre essa interface, é isso?")
c.Speak("Isso mesmo! Você está entendendo!")
c.Speak("O terminal é o lugar onde você manda comandos para o sistema operacional e ele tenta interpreta-los e executar as tarefas que você pediu")
c.Speak("O emulador de terminal é o programa que você usa para abrir essa interface de texto")
c.Speak("Entendeu a diferença?")
c.StudentComment("Entendi sim! Obrigado pela explicação!")
c.Speak("De nada! Estou aqui para ajudar!")
c.Speak("Você tem alguma dúvida até agora?")
c.StudentComment("Não, por enquanto está tudo bem! Continue!")
c.Speak("Ótimo! Vamos falar um pouco sobre a história do Linux")
c.Speak("O Linux foi criado por Linus Torvalds em 1991")
c.Speak("Ele se inspirou no sistema operacional Unix, que foi criado na década de 1970")
c.Speak("O Unix foi um dos primeiros sistemas operacionais a serem desenvolvidos")
c.StudentComment("Interessante! Mas qual a diferença entre o Linux e o Unix? Para o que serve o Unix?")
c.Speak("O Unix é um sistema operacional muito antigo, criado na década de 1970")
c.Speak("Ele foi desenvolvido pela AT&T e posteriormente pela Universidade da Califórnia em Berkeley")
c.Speak("O Unix é um sistema operacional muito poderoso e flexível")
c.Speak("Ele foi muito importante para o desenvolvimento da computação")
c.Speak("O Linux foi inspirado no Unix e compartilha muitas características com ele")
c.Speak("Mas o Linux é um sistema operacional mais moderno e mais flexível")
c.Speak("O Linux é um sistema operacional de código aberto, o que significa que qualquer pessoa pode ver e modificar o código fonte do sistema")
c.Speak("Isso torna o Linux muito popular entre os desenvolvedores e empresas")
c.Speak("Entendeu a diferença?")
c.StudentComment("Entendi sim! Obrigado pela explicação! O Unix foi feito para rodar em computadores pessoais?")
c.Speak("Na verdade, o Unix foi desenvolvido para rodar em mainframes e servidores")
c.Speak("Ele era um sistema operacional muito poderoso e robusto")
c.Speak("Mas com o tempo, o Unix foi adaptado para rodar em computadores pessoais")
c.Speak("O Linux, por outro lado, foi desenvolvido desde o início para rodar em computadores pessoais")
c.Speak("Ele é um sistema operacional muito flexível e pode ser instalado em uma grande variedade de dispositivos")
c.Speak("Entendeu a diferença?")
c.StudentComment("Entendi sim! Eu acho, mas quais foram as motivações desse tal Linus para criar o Linux?")
c.Speak("Linus Torvalds criou o Linux porque ele queria um sistema operacional livre e de código aberto")
c.Speak("Ele estava insatisfeito com os sistemas operacionais proprietários da época")
c.Speak("Ele queria um sistema operacional que fosse flexível, poderoso e que pudesse ser modificado livremente")
c.Speak("Por isso, ele decidiu criar o Linux")
c.StudentComment("Interessante! E quais eram os sistemas operacionais na época que ele não gostava?")
c.Speak("Na época, os sistemas operacionais mais populares eram o Unix e o Windows")
c.StudentComment("E qual o problema do windows que irritou esse maluco?")
c.Speak("O Windows é um sistema operacional proprietário, ou seja, o código fonte não é aberto")
c.Speak("Isso significa que você não pode ver como o sistema operacional funciona por dentro")
c.Speak("Você não pode modificar o sistema operacional livremente")
c.Speak("O Linux, por outro lado, é um sistema operacional de código aberto")
c.Speak("Isso significa que você pode ver e modificar o código fonte do sistema livremente")
c.Speak("Entendeu a diferença?")
c.StudentComment("Entendi sim! Esse retardado criou um sistema operacional só porque não gostava do windows? Que loucura!")
c.Speak("Hahaha! Na verdade, o Linux se tornou muito mais do que isso")
c.Speak("Hoje em dia, o Linux é usado em uma grande variedade de dispositivos, desde servidores até smartphones")
c.Speak("O windows é um sistema operacional muito popular, ele evoluiu de um outro sistema rudimentar chamado DOS")
c.Speak("O DOS era um sistema operacional de linha de comando, muito simples e limitado, desenhado para funcionar em computadores pessoais")
c.Speak("O Windows foi desenvolvido pela Microsoft para ser um sistema operacional gráfico, com uma interface mais amigável e fácil de usar")
c.Speak("Mas para manter compatibilidade com o DOS, o Windows ainda mantém muitas características do DOS e isso se tornou um grande problema")
c.Speak("O Windows é um sistema operacional muito complexo e cheio de problemas de segurança")
c.Speak("O Linux, por outro lado, é um sistema operacional muito mais simples e seguro")
c.Speak("Ele foi projetado desde o início para ser seguro e confiável")
c.Speak("Entendeu a diferença?")
c.StudentComment("Entendi sim! E oque é um Kernel? já ouvi várias vezes sobre isso")
c.Speak("O Kernel é o núcleo do sistema operacional")
c.Speak("Ele é o componente responsável por gerenciar os recursos de hardware do computador")
c.Speak("O Kernel é o componente mais importante do sistema operacional")
c.Speak("Ele é responsável por controlar o acesso aos recursos de hardware, como a memória, o processador e os dispositivos de entrada e saída")
c.Speak("O Kernel é o componente que faz a ponte entre o software e o hardware")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! O Kernel do linux é igual ao do Unix?")
c.Speak("O Kernel do Linux foi inspirado no Kernel do Unix")
c.Speak("Mas o Kernel do Linux é um Kernel completamente novo, desenvolvido do zero por Linus Torvalds")
c.Speak("Ele é um dos principais motivos do sucesso do Linux")
c.Speak("Já o MacOS, por exemplo, é um sistema novo, usa um Kernel baseado no Kernel do Unix")
c.Speak("Ele foi desenvolvido pela Apple e é usado em computadores Mac, ele é feito considerando o hardware da Apple")
c.Speak("Essa é uma das razões pela qual o MacOS é tão estável e rápido, ele foi cuidadosamente criado para rodar em um hardware específico")
c.Speak("Enquanto o Linux pode rodar em qualquer hardware, o MacOS é otimizado para rodar em hardware da Apple")
c.Speak("Entendeu a diferença?")
c.StudentComment("Um pouco, e qual a diferença entre o Linux e o MacOS?")
c.Speak("O Linux e o MacOS são sistemas operacionais muito diferentes mas compartilham ao mesmo tempo uma série de características, vamos ver algumas delas")
c.Speak("O Linux é um sistema operacional de código aberto, o que significa que qualquer pessoa pode ver e modificar o código fonte do sistema")
c.Speak("Isso torna o Linux muito popular entre os desenvolvedores e empresas")
c.Speak("O MacOS, por outro lado, é um sistema operacional proprietário, desenvolvido pela Apple")
c.Speak("Isso significa que o código fonte do MacOS não é aberto, você não pode ver como o sistema funciona por dentro")
c.Speal("Olha essa linda tabela em Asciidoc que eu fiz para você!")
c.Speak("""
+---------------------------------+--------------------------------+
| Linux                           | MacOS                          |
+=================================+================================+
| Código aberto                   | Proprietário                   |
+---------------------------------+--------------------------------+
| Pode ser instalado em qualquer  | Otimizado para hardware da     |
| hardware                        | Apple                          |
+---------------------------------+--------------------------------+
| Pode ser modificado livremente  | Não pode ser modificado        |
+---------------------------------+--------------------------------+
| Muitas distribuições diferentes | Apenas uma versão              |
+---------------------------------+--------------------------------+""")
c.Question("Você falou em distribuições, o que é isso?")
c.Speak("As distribuições Linux são versões diferentes do sistema operacional Linux")
c.Speak("Elas são criadas por diferentes empresas e comunidades")
c.Speak("Cada distribuição tem suas próprias características e objetivos")
c.Speak("Por exemplo, a distribuição Ubuntu é muito popular entre os usuários domésticos")
c.Speak("Já a distribuição CentOS é muito popular entre os servidores")
c.Speak("Entendeu?")
c.StudentComment("Nossa, que legal! Quais são as principais distribuições Linux e de onde elas vieram?")
c.Speak("Existem muitas distribuições Linux, vamos novamente fazer uma linda tabela para te mostrar, com quais são elas, suas características, usos e de onde elas vieram!")
c.Speak("""
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Distribuição                    | Características                 | Uso                            | Origem                         |
+=================================+=================================+================================+================================+
| Ubuntu                          | Fácil de usar, muitos           | Desktop                        | Reino Unido                    |
|                                 | aplicativos disponíveis         |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| CentOS                          | Estável, seguro, muito          | Servidores                     | Estados Unidos                 |
|                                 | usado em servidores             |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Fedora                          | Atualizações frequentes,        | Desktop, servidores            | Estados Unidos                 |
|                                 | muitos aplicativos disponíveis  |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Debian                          | Estável, seguro, muitos         | Desktop, servidores            | Estados Unidos                 |
|                                 | aplicativos disponíveis         |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Arch Linux                      | Rolling release, muito          | Desktop, servidores            | Canadá                         |
|                                 | flexível, muita documentação    |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+""")
c.Speak("Essas são algumas das principais distribuições Linux, mas elas são apenas a ponta do iceberg")
c.Speak("Existem muitas outras distribuições Linux, cada uma com suas próprias características e objetivos")
c.Speak("Você tem alguma dúvida até agora?")
c.StudentComment("Sim, todas essas derivam do linux que o Linus criou? Como isso aconteceu?")
c.Speak("Sim, todas essas distribuições são baseadas no Linux criado por Linus Torvalds")
c.Speak("Mas cada distribuição tem suas próprias características e objetivos")
c.Question("Você poderia me mostrar uma linha do tempo da evolução do Linux? Assim, bonita e desenhada como se fosse uma árvore de git, mas com caracteres ascii e mostrando a partir do Unix, passando pelo kernel do Linus até as distribuições atuais como Ubuntu e Manjaro por exemplo?")
c.Speak("Claro! Vamos fazer uma linda linha do tempo em ASCII para você, colocando inclusive a data de ínicio de cada uma e de onde elas partiram, seus objetivos, públicos alvo e quem as iniciou, em ordem cronológica e principais características!")
c.Speak("""
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Unix                            | 1970                            | AT&T                           | Mainframes, servidores         |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| BSD                             | 1977                            | Universidade da Califórnia     | Mainframes, servidores         |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Linux                           | 1991                            | Linus Torvalds                 | Computadores pessoais          |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Debian                          | 1993                            | Debian Project                 | Desktop, servidores            |
| Arch Linux                      | 2002                            | Judd Vinet                     | Desktop, servidores            |
| Fedora                          | 2003                            | Red Hat                        | Desktop, servidores            |
| Ubuntu                          | 2004                            | Canonical                      | Desktop                        |
| CentOS                          | 2004                            | CentOS Project                 | Servidores                     |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+""")
c.Question("O que ouvi outro dia uns termos chamando de flavors, o que é isso?")
c.Speak("Os flavors são versões diferentes de uma distribuição Linux")
c.Speak("Eles são criados para atender a diferentes necessidades e públicos")
c.Speak("Por exemplo, o Ubuntu tem vários flavors, como o Ubuntu Mate, o Ubuntu Budgie e o Ubuntu Studio")
c.Speak("Cada flavor tem suas próprias características e objetivos")
c.Speak("Entendeu?")
c.StudentComment("Poderia me listar os flavors de Ubuntu por favor e me dizer o que cada um faz?")
c.Speak("Claro! Vamos fazer uma linda tabela em ASCII para você, com os flavors do Ubuntu, suas características e objetivos!")
c.Speak("""
+---------------------------------+---------------------------------+--------------------------------+
| Flavor                          | Características                 | Objetivo                       |
+=================================+=================================+================================+
| Ubuntu GNOME (Padrãa)           | Moderno, elegante, muitos       | Desktop                        |
|                                 | aplicativos disponíveis         |                                |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Mate                     | Leve, simples, fácil de usar    | Desktop                        |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Budgie                   | Moderno, elegante, muitos       | Desktop                        |
|                                 | aplicativos disponíveis         |                                |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Studio                   | Focado em produção de mídia     | Desktop                        |
+---------------------------------+---------------------------------+--------------------------------+
| Xubuntu                         | Leve, simples, fácil de usar    | Desktop                        |
+---------------------------------+---------------------------------+--------------------------------+
| Kubuntu                         | Moderno, elegante, muitos       | Desktop                        |
|                                 | aplicativos disponíveis         |                                |
+---------------------------------+---------------------------------+--------------------------------+
| Lubuntu                         | Leve, simples, fácil de usar    | Desktop                        |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Server                   | Estável, seguro, muitos         | Servidores                     |
|                                 | aplicativos disponíveis         |                                |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Core                     | Leve, seguro, focado em IoT     | IoT                            |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Kylin                    | Focado em usuários chineses     | Desktop                        |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Cloud                    | Focado em nuvem, muitos         | Servidores em nuvem            |
|                                 | aplicativos disponíveis         |                                |
+---------------------------------+---------------------------------+--------------------------------+        
| Ubuntu Touch                    | Focado em dispositivos móveis   | Smartphones, tablets           |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu Personal                 | Focado em dispositivos móveis   | Smartphones, tablets           |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu TV                       | Focado em dispositivos de TV    | Smart TVs                      |
+---------------------------------+---------------------------------+--------------------------------+
| Ubuntu for Android              | Focado em dispositivos móveis   | Smartphones, tablets           |
+---------------------------------+---------------------------------+--------------------------------+""")
c.StudentComment("Nossa, que legal são muitos! Vcoê me recomenda alguma dessas?")
c.Speak("Isso vai depender do que você precisa, mas eu uso o Xubuntu e gosto muito, ele usa o XFCE como ambiente gráfico, é muito leve e rápido")
c.Speak("Mas se você precisa de um sistema mais completo e moderno, o Ubuntu GNOME ou o Kubuntu podem ser boas escolhas")
c.Speak("Se você precisa de um sistema para servidores, o Ubuntu Server é uma excelente opção, eu uso para meus projetos pessoais")
c.Speak("E se você precisa de um sistema para IoT, o Ubuntu Core é uma excelente escolha")
c.Speak("Meu filho usa um Ubuntu Bunny, ele é muito bonito e tem uma interface muito amigável e customizada, é uma escolha bem pessoal!")
c.Speak("Em meu notebook, por exemplo, eu uso uma distribuição chamada Linux Mint, que é baseada no Ubuntu e tem uma interface muito bonita e amigável, chamada Cinnamon, a experiência é muito boa também!!")
c.StydentComment("Nossa, que legal! É um mundo novo... mas eu vi que vc falou sobre diferentes interfaces, como isso funciona?")
c.Speak("As interfaces gráficas são os ambientes visuais que você usa para interagir com o sistema operacional")
c.Speak("Elas são responsáveis por fornecer uma interface gráfica para o usuário")
c.Speak("Existem várias interfaces gráficas disponíveis para o Linux, cada uma com suas próprias características e objetivos")
c.Speak("Diferente do Windows, no Linux você pode escolher qual interface gráfica você quer usar, o Kernel, base do sistema e interfaces gráficas são separados e você pode escolher o que quiser")
c.Speak("Por exemplo, o Ubuntu usa a interface gráfica GNOME por padrão")
c.Speak("Mas você pode instalar outras interfaces gráficas, como o KDE, o XFCE ou o LXDE")
c.Speak("Cada interface gráfica tem suas próprias características e objetivos")
c.Speak("Até para deixar o entendimento dos diferentes flavors mais fácil, cada um deles usa uma interface gráfica diferente, para atender a diferentes públicos")
c.StudentComment("Entendi sim! Vou ter que estudar bastante para entender tudo isso... quais são as principais interfaces gráficas de Linux e seus objetivos?")
c.Speak("Vamos fazer uma linda tabela em ASCII para você, com as principais interfaces gráficas do Linux, suas características, objetivos e principais distribuições que as usam!")
c.Speak("""
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Interface                       | Características                 | Objetivo                       | Distribuições                  |
+=================================+=================================+================================+================================+
| GNOME                           | Moderna, elegante, muitos       | Desktop                        | Ubuntu, Fedora                 |
|                                 | aplicativos disponíveis         |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| KDE                             | Personalizável, muitos          | Desktop                        | Kubuntu, OpenSUSE              |
|                                 | aplicativos disponíveis         |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| XFCE                            | Leve, simples, fácil de usar    | Desktop                        | Xubuntu, Manjaro               |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| LXDE                            | Muito leve, simples, fácil      | Desktop                        | Lubuntu, Fedora                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| LXQt                            | Leve, moderna, muitos           | Desktop                        | Lubuntu, Fedora                |
|                                 | aplicativos disponíveis         |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Cinnamon                        | Moderna, elegante, muitos       | Desktop                        | Linux Mint, Fedora             |
|                                 | aplicativos disponíveis         |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| MATE                            | Leve, simples, fácil de usar    | Desktop                        | Ubuntu Mate, Fedora            |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Budgie                          | Moderna, elegante, muitos       | Desktop                        | Ubuntu Budgie, Solus           |
|                                 | aplicativos disponíveis         |                                |                                |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+""")
c.Speak("Essas são algumas das principais interfaces gráficas do Linux, mas existem muitas outras")
c.Question("Quais e como são as outras?")
c.Speak("Existem muitas outras interfaces gráficas disponíveis para o Linux, cada uma com suas próprias características e objetivos")
c.Speak("Por exemplo, o Enlightenment é uma interface gráfica muito leve e rápida, ideal para computadores antigos")
c.Speak("O Pantheon é uma interface gráfica desenvolvida pela Elementary OS, ela é muito bonita e elegante")
c.Speak("O Deepin é uma interface gráfica desenvolvida pela Deepin Linux, ela é muito moderna e elegante")
c.Speak("O Moksha é uma interface gráfica baseada no Enlightenment, ela é muito leve e rápida")
c.Speak("O Trinity é uma interface gráfica baseada no KDE 3, ela é muito leve e rápida")
c.Speak("O Razor-qt é uma interface gráfica baseada no Qt, ela é muito leve e rápida")
c.Speak("O Sugar é uma interface gráfica desenvolvida para o projeto OLPC, ela é muito simples e educativa")
c.Speak("O Unity é uma interface gráfica desenvolvida pela Canonical, ela é muito moderna e elegante")
c.Speak("O blackbox é uma interface gráfica muito leve e rápida, ideal para computadores antigos")
c.Speak("O fluxbox é uma interface gráfica baseada no blackbox, ela é muito leve e rápida") 
c.Speak("O IceWM é uma interface gráfica muito leve e rápida, ideal para computadores antigos")
c.Speak("O JWM é uma interface gráfica muito leve e rápida, ideal para computadores antigos")
c.Speak("O Openbox é uma interface gráfica muito leve e rápida, ideal para computadores antigos")
c.Speak("O Window Maker é uma interface gráfica baseada no NeXTSTEP, ela é muito leve e rápida")
c.Speak("O awesome é uma interface gráfica baseada no tiling, ela é muito leve e rápida")
c.Speak("O dwm é uma interface gráfica baseada no tiling, ela é muito leve e rápida")
c.Speak("Entendeu? Temos muitas opções para todos os gostos, mas nem todas são tão populares quanto as que eu te mostrei")
c.StudentComment("Nossa, que legal! Vou ter que estudar bastante para entender tudo isso... mas e o Android e o iOS?")
c.Speak("O Android e o iOS são sistemas operacionais para dispositivos móveis")
c.Speak("O Android é baseado no Kernel do Linux")
c.Speak("Ele é um sistema operacional de código aberto, desenvolvido pelo Google")  
c.Speak("O Android é muito popular em smartphones e tablets")
c.Speak("Já o iOS é um sistema operacional proprietário, desenvolvido pela Apple")
c.Speak("Ele é usado em iPhones e iPads")
c.Speak("O iOS é um sistema operacional muito estável e seguro")
c.Speak("Entendeu a diferença?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Eu estava estudando aqui e vi que o Linux é compatível com o POSIX, o que é isso?")
c.Speak("O POSIX é um conjunto de padrões para sistemas operacionais Unix-like")
c.Speak("Ele define uma série de interfaces e funções que os sistemas operacionais Unix-like devem implementar")
c.Speak("O Linux é compatível com o POSIX, o que significa que ele implementa os padrões definidos pelo POSIX")
c.Speak("Isso torna o Linux compatível com muitos programas e bibliotecas desenvolvidos para sistemas Unix-like")
c.Speak("Entendeu?")
c.StudentComment("Você agora está abusando do meu conhecimento, não faço ideia do que você tentou dizer, o que é unix-like e de que tipos de compatibilidade você está falando?")
c.Speak("Unix-like é um termo usado para descrever sistemas operacionais que são semelhantes ao Unix, ou seja, que seguem os mesmos princípios e padrões do Unix, mas não são o Unix")
c.Speak("O Linux é um sistema operacional Unix-like, ele foi inspirado no Unix e compartilha muitas características com ele")
c.Speak("A compatibilidade com o POSIX significa que o Linux implementa os padrões definidos pelo POSIX")
c.Speak("Isso torna o Linux compatível com muitos programas e bibliotecas desenvolvidos para sistemas Unix-like")
c.Speak("Entendeu?")
c.StudentComment("Está melhorando, você deixou claro o que é unix-like mas ainda não sei que raios quer dizer POSIX, o que é isso?")
c.Speak("O POSIX é um conjunto de padrões para sistemas operacionais Unix-like")
c.Speak("Ele define uma série de interfaces e funções que os sistemas operacionais Unix-like devem implementar")
c.Speak("O Linux é compatível com o POSIX, o que significa que ele implementa os padrões definidos pelo POSIX")
c.Question("E quem diabos fez esse POSIX, de onde ele vem?")
c.Speak("O POSIX foi desenvolvido pelo IEEE, o Instituto de Engenheiros Eletricistas e Eletrônicos")
c.Speak("Ele foi criado para padronizar as interfaces e funções dos sistemas operacionais Unix-like")
c.Speak("O POSIX é muito importante porque garante a compatibilidade entre os sistemas operacionais Unix-like")
c.Speak("Vou tentar simplificar isso aqui de uma forma mais didática, estou me repetindo já...")
c.Speak("O POSIX é como um manual de instruções para sistemas operacionais Unix-like")
c.Speak("Ele define como os sistemas operacionais Unix-like devem funcionar")
c.Speak("Por exemplo, uma diferente forma de criar arquivos, de listar arquivos, de copiar arquivos, de mover arquivos, de remover arquivos, de exibir o conteúdo de arquivos, de editar arquivos, de verificar processos, de verificar uso de memória, de verificar uso de disco, de verificar informações do sistema, de gerenciar pacotes, de se conectar a máquinas remotas, de verificar conexões de rede, de verificar informações de DNS, de verificar informações de rede")
c.Speak("Vamos dar alguns exemplo, você sabe como o Windows lida com arquivos e permissonamento?")
c.StudentComment("Sim, eu sei! No Windows, cada arquivo tem um conjunto de permissões que define quem pode acessá-lo e o que pode ser feito com ele")
c.Speak("Isso mesmo! No Windows, as permissões são definidas por um conjunto de regras que são aplicadas a cada arquivo")
c.Speak("Por exemplo, você pode definir quem pode ler, escrever ou executar um arquivo")
c.Speak("No Linux, o sistema de permissões é um pouco diferente")
c.Speak("No Linux, as permissões são definidas por um conjunto de regras que são aplicadas a cada arquivo e diretório")
c.Speak("Por exemplo, você pode definir quem pode ler, escrever ou executar um arquivo ou diretório")
c.Speak("As permissões no Linux são divididas em três grupos: o dono do arquivo, o grupo do arquivo e os outros")
c.Speak("O dono do arquivo é a pessoa que criou o arquivo, o grupo do arquivo é um grupo de usuários e os outros são todos os outros usuários")
c.Speak("Cada grupo podem tem permissões diferentes, é um modelo bem mais seguro, governado e flexível do que o usado no Windows")
c.Speak("O Windows carrega esse legado desde o DOS, que era um sistema operacional muito simples e limitado, desenhado para funcionar em computadores pessoais")
c.Speak("o MSDOS foi pensado para rodar apenas em um computador, sem rede, sem compartilhamento de arquivos, sem permissões, sem segurança, sem nada")
c.Speak("Enquanto o Unix nasceu em um ambiente de rede, com vários usuários, com necessidade de segurança, de permissões, de compartilhamento de arquivos, de controle de acesso, de controle de processos, de controle de recursos")
c.Speak("O Linux herdou essas características do Unix, por isso é um sistema operacional muito mais seguro e flexível")
c.Speak("Entendeu a diferença? Aqui que as coisas começa a ficar mais interessantes!")
c.StudentComment("Entendi sim! Obrigado pela explicação! Mas e o que é um sistema de arquivos? Você falou outra hora que eles eram diferentes também...")
c.Speak("O sistema de arquivos é a forma como os arquivos são organizados e armazenados em um disco")
c.Speak("Ele define como os arquivos são nomeados, organizados em diretórios, acessados e modificados")
c.Speak("Cada sistema operacional tem seu próprio sistema de arquivos")
c.Speak("Por exemplo, o Windows usa o sistema de arquivos NTFS, o MacOS usa o sistema de arquivos HFS+ e o Linux usa o sistema de arquivos ext4")
c.Speak("Cada sistema de arquivos tem suas próprias características e objetivos")
c.Speak("O sistema de arquivos ext4 é muito popular no Linux, ele é rápido, seguro e confiável")
c.Speak("Pegou a ideia?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Isso tem a ver com aquele negócio de partições?")
c.Speak("Sim, exatamente!")
c.Speak("As partições são divisões lógicas de um disco rígido")
c.Speak("Elas são usadas para organizar e gerenciar o espaço em disco")
c.Speak("Cada partição tem seu próprio sistema de arquivos")
c.Speak("Por exemplo, você pode ter uma partição para o sistema operacional, uma partição para os arquivos pessoais e uma partição para os programas")
c.Speak("As partições são muito úteis para organizar e gerenciar o espaço em disco")
c.Speak("Entendeu?")
c.StudentComment("E como o sistema operacional consegue achar meus arquivos em um disco assim?")
c.Speak("O sistema operacional usa uma tabela de partições para saber onde estão os arquivos em um disco")
c.Speak("A tabela de partições é um mapa que mostra onde estão as partições em um disco")
c.Speak("Ela é usada pelo sistema operacional para acessar e gerenciar as partições")
c.Speak("Por exemplo, quando você acessa um arquivo em um disco, o sistema operacional consulta a tabela de partições para saber onde está o arquivo")
c.Speak("A tabela de partições é muito importante para o funcionamento do disco")
c.Speak("Um exemplo, é parecido como como um bibliotecário consulta um catálogo para saber onde estão os livros na biblioteca")
c.Speak("Os dados ficam armazenados em setores, que são pequenas unidades de armazenamento em um disco")
c.Speak("E o sistema de arquivos possui um mapa, dizendo onde cada arquivo está armazenado em setores")
c.Speak("Assim quando você tenta acessar um arquivo, ele olha nesse mapa e vai direto no setor onde o arquivo está armazenado")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Fiquei aqui agora pensando, por que o disco no Windows se chama C:, eu vi que não tem um desses no Linux, por que isso?")
c.Speak("No Windows, o disco rígido é dividido em partições, cada partição é representada por uma letra")
c.Speak("Por exemplo, a primeira partição é representada pela letra C:, a segunda partição é representada pela letra D:, e assim por diante")
c.Speak("Essa é uma convenção usada pelo Windows para identificar as partições do disco rígido")
c.Question("Ué? e por que começa no C? Por que não no A ou no B?")
c.Speak("Essa é uma boa pergunta!")
c.Speak("No passado, o Windows usava as letras A: e B: para representar as unidades de disquete")
c.Speak("Quando o Windows foi desenvolvido, os disquetes eram muito populares e eram usados para armazenar dados")
c.Speak("Por isso, as letras A: e B: foram reservadas para as unidades de disquete")
c.Speak("Por isso, a primeira partição do disco rígido foi representada pela letra C:")
c.Question("Você disse que o Linux é de 1991, também haviam disquetes na época? Por que é diferente?") 
c.Speak("Sim, na época do desenvolvimento do Linux, os disquetes eram muito populares e eram usados para armazenar dados")
c.Speak("Mas o Linux foi desenvolvido para ser um sistema operacional mais moderno e flexível")
c.Speak("Por isso, as letras A: e B: não foram reservadas para as unidades de disquete no Linux")
c.Speak("No Linux, as partições são representadas por nomes como /dev/sda1, /dev/sda2, /dev/sdb1, /dev/sdb2, e assim por diante")
c.Speak("Esses nomes são mais genéricos e flexíveis do que as letras usadas pelo Windows")
c.Speak("No Linux o conteito de montagem de dispositivos é diferente, você pode montar um dispositivo em qualquer diretório, não precisa de uma letra específica")
c.Speak("Ele vem de uma arquitetura diferente, oriunda de servidores, onde você pode ter vários discos, com várias partições, com vários sistemas de arquivos, com vários tipos de dispositivos")
c.Speak("Entendeu? A coisa é muito melhor desenhada, agora pense esse cenário e ainda com aquele modelo de permissonamento que eu te falei, é muito mais seguro e flexível, foi pensado para crescer e evoluir")
c.StudentComment("Entendi sim! Obrigado pela explicação! Mas e o que é um diretório? Você falou que o Linux não usa letras para representar as partições, mas sim diretórios...")
c.Speak("Um diretório é uma pasta que contém arquivos e outras pastas")
c.Speak("Ele é usado para organizar e armazenar arquivos em um disco")
c.Speak("Mas no Linux, tudo são arquivos, inclusive os diretórios")
c.Speak("e todos os diretórios estão abaixo de algo que chamamos de raiz, que é representado por /, o que chamamos de root. Todos esses podem ser pontos de montagem e você pode montar um dispositivo em qualquer diretório")
c.Speak("Por exemplo, o diretório /home é usado para armazenar os arquivos dos usuários")
c.Speak("O diretório /etc é usado para armazenar arquivos de configuração do sistema")
c.Speak("O diretório /var é usado para armazenar arquivos de log do sistema")
c.Speak("O diretório /tmp é usado para armazenar arquivos temporários")
c.Speak("O diretório /dev é usado para representar dispositivos")
c.Speak("O diretório /proc é usado para representar processos")
c.Speak("O diretório /sys é usado para representar dispositivos e drivers")
c.Speak("O diretório /mnt é usado para montar dispositivos")
c.Speak("O diretório /media é usado para montar dispositivos removíveis")
c.Speak("O diretório /boot é usado para armazenar arquivos de inicialização do sistema")
c.Speak("O diretório /bin é usado para armazenar programas essenciais do sistema")
c.Speak("O diretório /sbin é usado para armazenar programas de administração do sistema")
c.Speak("O diretório /usr é usado para armazenar programas e arquivos de dados do sistema")
c.Speak("O diretório /opt é usado para armazenar programas de terceiros")
c.Speak("O diretório /lib é usado para armazenar bibliotecas compartilhadas")
c.Speak("O diretório /lib64 é usado para armazenar bibliotecas compartilhadas de 64 bits")
c.Speak("O diretório /srv é usado para armazenar arquivos de dados de serviços")
c.Speak("O diretório /root é usado para armazenar os arquivos do usuário root")
c.Speak("O diretório /run é usado para armazenar arquivos temporários do sistema")
c.Speak("O diretório /snap é usado para armazenar programas em formato snap")
c.Speak("O diretório /lost+found é usado para armazenar arquivos perdidos")
c.Question("E o que é um arquivo? Você falou que tudo são arquivos no Linux, mas o que é isso?")
c.Speak("Um arquivo é uma unidade de armazenamento de dados em um disco")
c.Speak("Ele pode conter texto, imagens, vídeos, programas, ou qualquer outro tipo de informação")
c.Speak("No Linux, tudo são arquivos, inclusive os diretórios")
c.Speak("Por exemplo, um arquivo de texto é um arquivo que contém texto")
c.Speak("Um arquivo de imagem é um arquivo que contém uma imagem")
c.Speak("Um arquivo de vídeo é um arquivo que contém um vídeo")
c.Speak("Um arquivo de programa é um arquivo que contém um programa")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Mas e o que é um processo? Você falou que o diretório /proc é usado para representar processos...")
c.Speak("Um processo é um programa em execução em um sistema operacional")
c.Speak("Ele é uma instância de um programa que está sendo executado em um sistema operacional")
c.Speak("Por exemplo, quando você abre um programa em um computador, ele é executado como um processo")
c.Speak("Cada processo tem um identificador único, chamado de PID")
c.Speak("O diretório /proc é usado para representar os processos em execução no sistema")
c.Speak("Ele contém informações sobre os processos, como o PID, o nome do programa, o uso de CPU, o uso de memória, e outras informações")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Mas e o que é um driver? Você falou que o diretório /sys é usado para representar dispositivos e drivers...")
c.Speak("Um driver é um programa que permite que o sistema operacional se comunique com um dispositivo de hardware")
c.Speak("Ele é responsável por controlar o dispositivo e fornecer uma interface para o sistema operacional")
c.Speak("Por exemplo, um driver de impressora permite que o sistema operacional envie documentos para a impressora")
c.Speak("O diretório /sys é usado para representar dispositivos e drivers no sistema")
c.Speak("Ele contém informações sobre os dispositivos e drivers no sistema, como o nome do dispositivo, o tipo de dispositivo, o driver associado, e outras informações")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Isso é o tal do LSB?")
c.Speak("O LSB é o Linux Standard Base")
c.Speak("Ele é um conjunto de padrões para sistemas operacionais Linux")
c.Speak("Ele define uma série de interfaces e funções que os sistemas operacionais Linux devem implementar")
c.Speak("O LSB é muito importante porque garante a compatibilidade entre os sistemas operacionais Linux")
c.Speak("Entendeu?")
c.StudentComment("Um pouco, você poderia montar aquela tabela maneira de novo com todas essas informações de pastas suas finalidades?")
c.Speak("Claro! Vamos fazer uma linda tabela em ASCII para você, com os diretórios do Linux, suas finalidades, quem pode acessa-los? 
c.Speak("""
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| Diretório                       | Finalidade                      | Quem pode acessar              | Quem pode modificar            |
+=================================+=================================+================================+================================+
| /                              | Raiz do sistema                  | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /home                          | Arquivos dos usuários            | Usuários                       | Usuários                       |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /etc                           | Arquivos de configuração         | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /var                           | Arquivos de log                  | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /tmp                           | Arquivos temporários             | Todos                          | Todos                          |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /dev                           | Dispositivos                     | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /proc                          | Processos                        | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /sys                           | Dispositivos e drivers           | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /mnt                           | Montagem de dispositivos         | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /media                         | Montagem de dispositivos         | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /boot                          | Arquivos de inicialização        | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /bin                           | Programas essenciais             | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /sbin                          | Programas de administração       | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /usr                           | Programas e arquivos de dados    | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /opt                           | Programas de terceiros           | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /lib                           | Bibliotecas compartilhadas       | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /lib64                         | Bibliotecas compartilhadas       | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /srv                           | Arquivos de dados de serviços    | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /root                          | Arquivos do usuário root         | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /run                           | Arquivos temporários do sistema  | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /snap                          | Programas em formato snap        | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
| /lost+found                    | Arquivos perdidos                | Root                           | Root                           |
+---------------------------------+---------------------------------+--------------------------------+--------------------------------+""")
c.Speak("Esses são alguns dos diretórios mais importantes do Linux, cada um com sua própria finalidade e permissões")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Mas e o que é um shell? Você falou que o Linux tem um shell... o que é isso? é uma casca?")
c.Speak("Um shell é um programa que fornece uma interface de linha de comando para o usuário")
c.Speak("Ele permite que o usuário interaja com o sistema operacional digitando comandos")
c.Speak("O shell é uma casca, uma interface entre o usuário e o sistema operacional")
c.Speak("Ele interpreta os comandos digitados pelo usuário e os executa no sistema operacional")
c.Speak("No Linux, o shell mais comum é o bash, que é o Bourne Again Shell")
c.Speak("O bash é muito poderoso e flexível, ele permite que o usuário execute uma grande variedade de comandos")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! Obrigado pela explicação! E o que é um terminal? Você falou que o Linux tem um terminal... o que é isso?")
c.Speak("Um terminal é uma janela de texto que permite que o usuário interaja com o sistema operacional")
c.Speak("Ele fornece uma interface de linha de comando para o usuário, onde ele pode digitar comandos e visualizar a saída dos comandos")
c.Speak("O terminal é uma forma de acessar o shell, que é o programa que fornece a interface de linha de comando")
c.Speak("No Linux, o terminal é uma ferramenta muito poderosa, que permite que o usuário execute uma grande variedade de comandos")
c.Speak("Entendeu?")
c.StudentComment("Entendi sim! Obrigado pela explicação! Pelo o que você fala, tudo no Linux é muito poderoso, flexível... e existem várias opções, com terminais isso também acontece?")
c.Speak("Sim, exatamente!")
c.Speak("No Linux, existem vários terminais disponíveis, cada um com suas próprias características e objetivos, vamos fazer uma tabelinha lindona para te mostrar os principais, com o nome, descrição, como instalar em distribuições Debian, RHEL e o site oficial de cada um deles? A escolha, assim como as distribuições são bem pessoais")
c.Speak("""
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Terminal                        | Descrição                           | Debian                         | RHEL                           |
+=================================+=====================================+================================+================================+
| GNOME Terminal                  | Terminal padrão do GNOME            | apt install gnome-terminal     | yum install gnome-terminal     |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Konsole                         | Terminal do KDE                     | apt install konsole            | yum install konsole            |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| XFCE Terminal                   | Terminal do XFCE                    | apt install xfce4-terminal     | yum install xfce4-terminal     |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| LXTerminal                      | Terminal do LXDE                    | apt install lxterminal         | yum install lxterminal         |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Terminator                      | Terminal com várias funcionalidades | apt install terminator         | yum install terminator         |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Tilda                           | Terminal dropdown                   | apt install tilda              | yum install tilda              |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Guake                           | Terminal dropdown                   | apt install guake              | yum install guake              |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Yakuake                         | Terminal dropdown                   | apt install yakuake            | yum install yakuake            |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Tilix                           | Terminal com várias funcionalidades | apt install tilix              | yum install tilix              |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Alacritty                       | Terminal leve e rápido              | apt install alacritty          | yum install alacritty          |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Kitty                           | Terminal leve e rápido              | apt install kitty              | yum install kitty              |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Termite                         | Terminal leve e rápido              | apt install termite            | yum install termite            |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| XTerm                           | Terminal padrão do X                | apt install xterm              | yum install xterm              |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| URxvt                           | Terminal leve e rápido              | apt install rxvt-unicode       | yum install rxvt-unicode       |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Cool Retro Term                 | Terminal retrô                      | apt install cool-retro-term    | yum install cool-retro-term    |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+
| Hyper                           | Terminal moderno                    | apt install hyper              | yum install hyper              |
+---------------------------------+-------------------------------------+--------------------------------+--------------------------------+""")