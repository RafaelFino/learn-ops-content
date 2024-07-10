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

c = chat.Chat("Fino", "Aluno")

c.Speak("Olá, Aluno! Tudo bem?")
c.Speak("Hoje vamos falar sobre Linux e sobre o terminal, tudo bem?")
c.Speak("Você já ouviu falar sobre o Linux?")
c.Speak("O Linux é um sistema operacional, assim como o Windows e o MacOS")
c.StudentComment("Ah, entendi! Mas o que é um sistema operacional?")
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


