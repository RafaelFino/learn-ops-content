
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

# Tema: Uma cloud privada, usando um proxmox como virtualizador
# O professor deve explicar o que é um servidor e como ele funciona.
# O professor deve explicar o que é uma cloud privada e como ela pode ser utilizada.
# O professor deve explicar a arquitetura utilizada para montar uma cloud privada.
# O professor deve explicar o que é um virtualizador e como ele funciona.
# O professor deve explicar o que é o Proxmox e como ele funciona.
# A arquitetura utilizada, usa um serviço chamado FRP, que faz papel de proxy reverso, o professor deve explicar o que é um proxy reverso e como ele funciona.
# A arquitetura usa um servidor hospedado na OCI, servindo como ponto de entrada para essa infraestrutura, o professor deve explicar o que é a OCI e como ela funciona.
# Nesse servidor, usamos um DNS de um serviço gratuito, chamado DuckDNS, o professor deve explicar o que é um DNS e como ele funciona.
# Nessa arquitetura, uma máquina virtual na OCI, hospeda o lado servidor do FRP, o FRPS, que abre uma porta específica, usando um token de segurança para garantir a comunicação, o professor deve explicar como funciona o FRPS.
# Dentro da rede privada da casa do professor, existe um servidor Xeon muito poderoso onde um proxmox está instalado.
# Para garantir a segregação das redes, existe uma rede separada dentro do virtualizador, onde as máquinas virtuais são criadas.
# Existe uma VM chamada Proxy, que faz papel de proxy de internet usando um serviço chamado Squid, o professor deve explicar o que é um proxy de internet e como ele funciona.
# Existe uma VM chamada Tools, onde o FRPC (cliente do FRP) está instalado, o professor deve explicar como funciona o FRPC.
# Existe uma VM chamada Server, onde o professor hospeda o projetos de estudo e iremos usar em exercícios práticos.
# Para ter acesso a essas VMs, o professor criou um sistema que usa os usuários do github para autenticação, o professor deve explicar como funciona esse sistema.
# Usando o comando http://github.com/USUARIO.keys, o professor consegue pegar a chave pública do usuário e adicionar ao arquivo authorized_keys, permitindo o acesso via SSH.
# O professor deve explicar como acessar as máquinas virtuais via SSH.
# O professor criou uma automação, que de hora em hora, usando esse serviço, atualiza as chaves públicas dos usuários, garantindo que sempre tenham acesso.
# O professor deve explicar como funciona essa automação.
# Existem 20 vms criadas, partindo da porta 7112 até a porta 7132, o professor deve explicar como acessar cada uma dessas vms.
# Os Jedis vão apoiar os alunos a acessar essas vms, para que possam fazer exercícios práticos. Eles possuem acesso a todas as VMs dos alunos.
# O professor deve explicar como os alunos podem acessar as VMs, com o comando 'ssh -oPort=PORTA -i ~/.ssh/id_ed25519 dev@learnops.duckdns.org'


t("Olá, Pequenos Gafanhotos! Hoje vamos explorar uma cloud privada, usando um Proxmox como virtualizador. Já ouviu falar sobre isso?")
s(f"Oi, {c.Teacher()}! Já ouvi um pouco, mas não entendo muito bem o que é. Pode me explicar?")
t("Claro, Jovem Tartaruga! Uma cloud privada é como ter um datacenter em casa, onde você pode criar e gerenciar suas próprias máquinas virtuais e serviços. É como ter um pedaço da internet só para você.")
t("O Proxmox é um software de virtualização que permite criar e gerenciar máquinas virtuais e containers. Ele é baseado no sistema operacional Debian e tem uma interface web muito amigável.")
t("Nessa arquitetura, usamos um serviço chamado FRP, que faz papel de proxy reverso. Um proxy reverso é um servidor que recebe solicitações de clientes externos e as encaminha para os servidores internos.")
t("Usamos um servidor hospedado na OCI, que serve como ponto de entrada para essa infraestrutura. A OCI é a Oracle Cloud Infrastructure, uma plataforma de nuvem da Oracle.")
t("Nesse servidor, usamos um DNS de um serviço gratuito, chamado DuckDNS. Um DNS é como um catálogo telefônico que traduz nomes de domínio em endereços IP.")
t("Nessa arquitetura, uma máquina virtual na OCI hospeda o lado servidor do FRP, o FRPS. Ele abre uma porta específica, usando um token de segurança para garantir a comunicação.")
t("Dentro da rede privada da casa do professor, existe um servidor Xeon muito poderoso onde um Proxmox está instalado. Para garantir a segregação das redes, existe uma rede separada dentro do virtualizador, onde as máquinas virtuais são criadas.")
t("Existe uma VM chamada Proxy, que faz papel de proxy de internet usando um serviço chamado Squid. Um proxy de internet é um servidor que atua como intermediário entre os clientes e a internet.")
t("Existe uma VM chamada Tools, onde o FRPC (cliente do FRP) está instalado. Ele se conecta ao FRPS na OCI para estabelecer a comunicação.")
t("Existe uma VM chamada Server, onde eu hospedo projetos de estudo e iremos usar em exercícios práticos.")
t("Para ter acesso a essas VMs, criei um sistema que usa os usuários do GitHub para autenticação. Usando o comando:")
c.ShowCommand("ssh -oPort=PORTA -i ~/.ssh/id_ed25519 dev@learnops.duckdns.org")
t("Você consegue acessar as máquinas virtuais com o seu usuário do GitHub.")
t("Os Jedis vão apoiar vocês a acessar essas VMs, para que possam fazer exercícios práticos. Eles possuem acesso a todas as VMs dos alunos.")
t("Para ver todos os usuários disponíveis, você pode acessar o arquivo com o seguinte comando:")
c.ShowCommand(
    "curl https://rgt-tools.duckdns.org/drive/api/public/dl/JzcWHOIA/plataforma/vm-users.json")
q(f"PUTA MERDA CALMA! Me perdi geral {c.Teacher()}, eu não sei nem oq é uma VM, um proxy, um container, um ssh, um curl... nada! Vamos do começo cara...")
t("Sem problemas, Pequeno Gafanhoto! Vamos começar do começo. Uma máquina virtual é como um computador dentro de outro computador. Ela simula um ambiente de hardware e software independente.")
t("Um proxy é um intermediário entre o cliente e o servidor. Ele recebe as solicitações do cliente e as encaminha para o servidor, mantendo a comunicação segura e eficiente.")
t("Um container é uma unidade de software que empacota uma aplicação e todas as suas dependências. Ele é leve, portátil e pode ser executado em qualquer ambiente.")
t("SSH é um protocolo de rede seguro que permite acessar e gerenciar máquinas remotas. Com ele, você pode executar comandos, transferir arquivos e acessar serviços de forma segura.")
t("Curl é uma ferramenta de linha de comando que permite transferir dados com URLs. Com ele, você pode baixar arquivos, fazer requisições HTTP e muito mais.")
t("Agora que você entendeu os conceitos básicos, vamos explorar a cloud privada e ver como tudo funciona na prática. Vamos começar?")
s(f"Tá maluco {c.Teacher()}? Tô mais perdido que cego em tiroteio! Lembra q eu sou só um pobre aprendiz e a essa altura, estou cansado e com fome! Consegue me explicar considerando minhas limitações?")
t("Claro, Pobre Aprendiz! Vamos fazer o seguinte: vou te mostrar como acessar as máquinas virtuais e você vai poder explorar cada uma delas. Vamos começar com a VM Proxy. Você consegue acessar a VM Proxy com o comando:")
c.ShowCommand("ssh -oPort=7112 -i ~/.ssh/id_ed25519 dev@learnops.duckdns.org")
q("Pera aí... onde eu rodo isso? clico onde?")
t("Assim fica dificil campeão, larga esse mouse aí... estamos falando de comandos de terminal pow... 6 meses de curso e ainda não entendeu q estamos te treinando pra vida adulta aqui?")
t("Vamos lá, abre o terminal aí e cola o comando que te mostrei. Vamos acessar a VM Proxy e ver o que tem lá dentro. Só fica esperto que vc precisa usar a porta certa e a chave que vc cadastrou lá no github.bom")
s("Github.com? O que é isso?")
t("O GitHub é uma plataforma de hospedagem de código-fonte e colaboração. Lá você pode compartilhar seus projetos, colaborar com outros desenvolvedores e aprender muito.")
s("Entendi... mas eu não tenho conta lá...")
t("...")
t("...")
t("...")
t("Tô contando até 10 aqui para não te ofender...")
t("...")
t("Bom, vai lá e cria tua conta xará... se vc não colaborar não vamos conseguir avançar...")
s("Tá bom, pera... estou criando!")
q("Pronto, criei! E agora? O que tem a ver essa conta com a minha chave SSH? alias, considerando q eu não entendo nada disso, oq é mesmo essa chave e para q ela serve? Me explica lembrando q eu sou só um jovem aprendiz por favor")
t("A chave SSH é como uma chave de segurança que permite você acessar as máquinas virtuais de forma segura. Ela é composta por um par de chaves: uma pública e uma privada.")
s("Sempre escuto sobre esse negócio de publica e privada, nunca entendi isso direito...")
t("A chave pública é como a sua identidade, você pode compartilhá-la com outras pessoas sem problemas. A chave privada é como a sua senha, você deve mantê-la em segredo.")
s("Acho que entendi, é como se as duas fossem partes de uma mesma coisa, uma eu entrego para as pessoas (a publica) e a outra, eu guardo só pra mim (a privada), é isso?")
t("Isso, você pegou o jeito! A chave pública é adicionada ao servidor para permitir o acesso e a chave privada é usada para autenticar o seu acesso. Combinadas, elas garantem a segurança da comunicação.")
t("Agora que você criou a sua conta no GitHub, você pode adicionar a sua chave pública lá e usá-la para acessar as máquinas virtuais. O github.com tem um serviço muito legal que eu consigo puxar as chaves publicas do usuários, olha só:")
c.ShowCommand("curl https://github.com/rafaelfino.keys")
t("Com esse comando, eu consigo pegar a chave pública do usuário rafaelfino e adicionar ao arquivo authorized_keys, permitindo o acesso via SSH.")
s("Entendi... mas como eu faço para adicionar a minha chave lá?")
t("...")
t("...")
t("...")
t("Tô contando até 10 aqui para não te ofender mais uma vez... eu acho aqui q o seu google é igual ao meu, vc já tentou pesquisar lá?")
s("é... tô vacilando né? vou pesquisar aqui...")
s("Pronto, achei esse link aqui: https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent , é isso?")
t("Isso mesmo! Esse link explica como gerar uma nova chave SSH e adicionar ao seu agente SSH. Siga os passos e você vai conseguir adicionar a sua chave ao GitHub.")
t("Mas vou te contar aqui como vc pode gerar uma chave aí no seu linux (LINUX, não no Windows... se vc quiser usar windows, dá teus pulos aí...)")
c.ShowCommand("ssh-keygen -t ed25519 -C 'seu@email.com'")
t("Esse comando vai gerar um par de chaves SSH, uma pública e uma privada. A chave pública você adiciona ao GitHub e a chave privada você guarda com muito cuidado.")
s("Entendi... mas aqui diz que eu não tenho o ssh não sei oq, como eu instalo ele?")
t("...")
t("...")
t("...")
t("Teu google quebrou?")
s("Ops... não, desculpa... vou pesquisar aqui...")
q("Pronto, achei esse link aqui: https://www.cyberciti.biz/faq/how-to-install-ssh-on-ubuntu-linux-using-apt-get/ , é isso?")
t("Isso mesmo! Esse link explica como instalar o OpenSSH no Ubuntu. O OpenSSH é uma implementação livre do protocolo SSH e é muito utilizado em sistemas Linux.")
t("Mas vou te ajudar... caso não tenha instalado, você pode instalar o OpenSSH com o comando:")
c.ShowCommand("sudo apt-get install -y openssh-client openssh-server")
t("Esse comando vai instalar o cliente e o servidor SSH no seu sistema. Com isso, você vai poder acessar as máquinas virtuais e fazer muitas outras coisas.")
s("Entendi... mas e agora? O que eu faço?")
t("Agora que você instalou o OpenSSH e gerou a sua chave SSH, você pode adicionar a sua chave pública ao GitHub e acessar as máquinas virtuais. Vamos tentar acessar a VM Proxy?")
t("Uma coisa legal também é usar o ssh-agent")
c.ShowCommand("eval $(ssh-agent -s)")
t("Esse comando vai iniciar o ssh-agent e adicionar a sua chave privada ao agente. Assim, você não precisa digitar a senha toda vez que acessar uma máquina.")
s("Entendi... mas oq é esse agent? por que ele vai me ajudar?")
t("O ssh-agent é um programa que gerencia as chaves privadas do SSH. Ele armazena as chaves em memória e as usa para autenticar as conexões SSH.")
t("Com o ssh-agent, você pode adicionar a sua chave privada ao agente e ele vai cuidar de autenticar as suas conexões de forma segura e eficiente.")
s("Entendi... mas e se eu não quiser usar ele?")
t("Sem problemas, você pode acessar as máquinas virtuais sem o ssh-agent. Basta usar o comando ssh com a sua chave privada e a porta correta.")
t("Mas nesse caso, sem ele, todas as vezes que você acessar uma máquina, vai precisar digitar a senha da chave privada.")
s("Entendi... mas e se eu esquecer a senha?")
t("...")
t("...")
t("...")
t("Pow campeão, não tem jeito, vc é um adulto, não pode ficar esquecendo senha de acesso a servidor, se vira aí... se vc esquecer a senha, vai ter que gerar uma nova chave e adicionar ao GitHub e as máquinas virtuais novamente... é a vida...")
t("Para facilitar a nossa vida eu criei uma planilha onde vc deve cadastrar seu usuário do github e lá tem a porta que vc vai acessar... vamos lá?")
t("https://docs.google.com/spreadsheets/d/1F-x23F-llyVXF0y_HUnyquuJruDzD1S8_XVdW7V00iE/edit?gid=0#gid=0")
t("Notem que existe uma aba para os Jedis e uma outra para os alunos, cadastrem lá que eu sempre olho essa planilha e dou carga no sistema de permissionamento, em geral, de hora em hora esse processo acontece, não baguncem a planilha!")
t("Vamos lá, agora que você já tem a sua chave SSH e sabe como acessar as máquinas virtuais, vamos tentar acessar a VM Proxy. Você consegue acessar a sua VM, por exemplo, de porta 7120 com o comando:")
c.ShowCommand("ssh -oPort=7120 -i ~/.ssh/id_ed25519 dev@learnops.duckdns.org")
t("Com esse comando, você vai acessar a VM Proxy e poder explorar o que tem lá dentro. Vamos lá?")
q("Me explica melhor o que é cada parte desse comando por favor? o que é o -oPort=7120? e esse -i? e esse dev@ aí?")
t("Claro, Pequeno Gafanhoto! O comando SSH é usado para acessar máquinas remotas de forma segura. Vamos ver o que cada parte do comando significa:")
t("-oPort=7120: Esse parâmetro define a porta que você vai acessar na máquina remota. Nesse caso, a porta 7120 corresponde à VM Proxy.")
t("-i ~/.ssh/id_ed25519: Esse parâmetro define o arquivo de chave privada que você vai usar para autenticar a conexão. Nesse caso, você está usando a sua chave SSH.")
t("o dev@learnops.duckdns.org é o usuário e o endereço da máquina remota. O usuário é o dev e o endereço é learnops.duckdns.org, que é o servidor de entrada para a infraestrutura.")
t("Com essas informações, o comando SSH vai estabelecer uma conexão segura com a máquina remota e você vai poder acessar a VM Proxy. Vamos tentar?")
s("Entendi... mas e se eu quiser acessar outra máquina?")
t("Para acessar outra máquina, você precisa mudar a porta no comando SSH. Cada máquina tem uma porta específica, que vai de 7112 até 7132.")
t("Por exemplo, se você quiser acessar a VM Server, que está na porta 7125, você usa o comando:")
c.ShowCommand("ssh -oPort=7125 -i ~/.ssh/id_ed25519 dev@learnops.duckdns.org")
t("Com esse comando, você vai acessar a VM Server e poder explorar o que tem lá dentro. Vamos tentar?")
s("Entendi... mas e se eu não conseguir acessar?")
t("Se você não conseguir acessar, pode ser que a porta esteja errada, a chave não esteja configurada corretamente ou a máquina esteja fora do ar.")
t("Nesse caso, você pode pedir ajuda aos Jedis, que vão te ajudar a resolver o problema e acessar a máquina. Eles são os mestres da força e vão te guiar no caminho certo.")
t("Conseguiu entrar aí? Se você conseguiu, deve ver o prompt do terminal da VM, algo como dev@vm125:~$... se não conseguiu, me avise que eu chamo um Jedi para te ajudar.")
s("Consegui acessar sim! Mas não entendi uma coisa, a porta é a 7125 e o nome da VM é vm125, por que?")
t("Boa pergunta, Pobre Aprendiz! A porta é o número que você usa para acessar a máquina, enquanto o nome da VM é o nome que você dá para identificar a máquina.")
t("Dentro do virtualizador, cada VM possui um ID, indentificando essa VM. Esse ID é usado para mapear a porta de acesso e o nome da VM.")
t("Para não ficar maluco, eu usei o mesmo ID da VM como o IP dela, que está em uma rede 192.168.1.1, nesse caso, essa vm é a 125, logo, ela tem o ID 125, se chama vm125 e tem o IP 192.168.1.125")
s("Ok, entendi essa parte, e esse 7000 aí? de onde saiu?")
t("Quando falamos de portas de rede, é normal usarmos portas de numeração mais alta, a partir de 7000, para evitar conflitos com as portas padrão dos serviços.")
t("Então por puro 'EU QUIS', eu comecei a partir da 7100 até 7200, no caso, para vcs, eu separei das portas 7112 até a 7132, foi uma escolha minha, não tem nada de especial nisso.")
t("Agora que você entendeu como acessar as máquinas virtuais, você pode explorar cada uma delas e ver o que tem lá dentro. Vamos continuar?")
s("Entendi... mas e se eu quiser sair da máquina?")
t("Para sair da máquina, você pode usar o comando exit ou pressionar as teclas Ctrl + D. Isso vai encerrar a sessão SSH e voltar para o seu terminal local.")
c.ShowCommand("exit")
t("Com esse comando, você vai sair da máquina virtual e voltar para o seu terminal local. Simples, não é? Agora que você sabe como acessar as máquinas virtuais, você pode explorar cada uma delas e ver o que tem lá dentro.")
q("E o que eu posso fazer dentro dessa máquina?")
t("Dentro da máquina virtual, você pode executar comandos, instalar programas, configurar serviços e muito mais. É como ter um computador só seu, onde você pode fazer o que quiser.")
t("Você tem acesso a internet, porém não deixei a parte de liberação de portas para sair da rede privada, então, você pode acessar a internet, mas não pode expor serviços para fora da rede.")
t("Mas as VMs conseguem se comunicar entre si, vocês podem criar APIs para interagir entre as VMs, criar um ambiente de desenvolvimento, testar aplicações e muito mais.")
q("Estamos falando, falando, falando... mas ainda não entendi direito, oq é uma VM e como você conseguiu fazer isso dentro da sua casa?")
t("Uma VM é uma máquina virtual, ou seja, um computador virtualizado dentro de outro computador. Ela simula um ambiente de hardware e software independente.")
t("Para montar essa cloud privada, eu usei um servidor Xeon muito poderoso com o Proxmox instalado. O Proxmox é um software de virtualização que permite criar e gerenciar VMs.")
t("Dentro do Proxmox, eu criei uma rede privada para as VMs, onde elas são isoladas e podem se comunicar entre si. Cada VM tem um propósito específico e juntas formam a infraestrutura.")
t("Eu usei o FRP para fazer o proxy reverso, a OCI como ponto de entrada, o DuckDNS para o DNS, o Squid para o proxy de internet e o GitHub para a autenticação dos usuários.")
t("Com essa arquitetura, eu consegui montar uma cloud privada em casa, onde posso criar e gerenciar as minhas próprias máquinas virtuais e serviços. É como ter um datacenter só meu.")
s("Caramba! tudo isso em casa? Então é como se fossem um caminhão levando um monte de carros em cima?")
t("É, é uma ótima analogia... é como se fosse um grande computador poderoso, com vários computadores menores dentro dele... é uma ótima maneira de entender o conceito! Muito bom padawan!")
q("Na vida real é assim que os servidores funcionam?")
t("Sim, na vida real os servidores funcionam de forma semelhante. Eles são computadores poderosos que hospedam serviços e aplicações para os usuários.")
t("Os servidores podem ser físicos, como o servidor Xeon que eu tenho em casa, ou virtuais, como as VMs que você acessou. Eles são essenciais para manter a internet funcionando.")
t("Os servidores podem hospedar sites, bancos de dados, aplicativos, jogos e muitos outros serviços. Eles são a base da infraestrutura de TI e garantem que tudo funcione corretamente.")
q("Clouds... vc falou de clouds, mas o que exatamente são elas?")
t("As clouds, ou nuvens, são ambientes de computação em rede que permitem o acesso remoto a recursos de computação, armazenamento e rede.")
t("Elas são como datacenters virtuais, onde você pode criar e gerenciar máquinas virtuais, armazenar dados, executar aplicativos e muito mais.")
t("As clouds podem ser públicas, privadas ou híbridas. As clouds públicas são mantidas por provedores de serviços, como a AWS e o Azure. As clouds privadas são mantidas pelas empresas ou usuários.")
t("As clouds híbridas combinam os recursos das clouds públicas e privadas, permitindo maior flexibilidade e escalabilidade.")
q("E como eu posso usar uma cloud?")
t("Você pode usar uma cloud para hospedar sites, aplicativos, bancos de dados, armazenar arquivos, executar testes e muito mais.")
t("É muito caro e trabalhoso ter o seu prṕprio datacenter, então esses provedores de cloud, oferecem um modelo em que você aluga a capacidade e usa e eles cuidam da parte de infraestrutura.")
s("Acho que entendi, é como se fossem o Uber dos datacenters? no lugar de você ter o seu carro, você aluga um quando precisa?")
t("Exatamente! É como o Uber dos datacenters. Você aluga a capacidade de computação, armazenamento e rede de acordo com a sua necessidade e paga apenas pelo que usar.")
t("Agora que você entendeu o conceito de cloud, virtualização e servidores, você pode explorar a cloud privada e ver como tudo funciona na prática. Vamos continuar?")
s("Entendi... mas e se eu quiser aprender mais sobre isso?")
t("Se você quiser aprender mais sobre cloud, virtualização e servidores, existem muitos recursos disponíveis na internet. Vale estudar sobre AWS, GCP, OCI, Azure e etc")
t("Além disso, você pode ler livros, fazer cursos online, participar de comunidades e praticar o que aprendeu. A prática é fundamental para fixar o conhecimento.")
t("Se você tiver alguma dúvida ou quiser saber mais sobre algum tema específico, pode me perguntar que eu vou te ajudar no que precisar.")
s("Entendi... mas e se eu quiser praticar mais?")
t("Se você quiser praticar mais, pode acessar as máquinas virtuais e explorar cada uma delas. Você pode instalar programas, configurar serviços, criar scripts e muito mais.")
t("Além disso, você pode colaborar com outros alunos, compartilhar conhecimento e aprender juntos. A colaboração é uma ótima forma de aprender e evoluir.")
t("Se você tiver alguma dúvida ou precisar de ajuda para praticar, pode contar com os Jedis, que vão te apoiar e guiar no caminho certo.")
s("Entendi... mas e se eu quiser mais dicas?")
t("Se você quiser mais dicas, pode acessar os materiais de estudo que eu indiquei, como livros, cursos online, documentações e comunidades.")
q("Você teria alguns bons links para me indicar para estudar?")
t("Claro, Pobre Aprendiz! Aqui estão alguns links que podem te ajudar a estudar mais sobre cloud, virtualização e servidores:")
t("https://aws.amazon.com/pt/ - AWS - Amazon Web Services")
t("https://cloud.google.com/ - GCP - Google Cloud Platform")
t("https://www.oracle.com/cloud/ - OCI - Oracle Cloud Infrastructure")
t("https://azure.microsoft.com/pt-br/ - Azure - Microsoft Azure")
t("https://www.proxmox.com/ - Proxmox - Virtualizador")
t("https://www.squid-cache.org/ - Squid - Proxy de Internet")
t("https://github.com/fatedier/frp - FRP - Proxy Reverso")
t("https://www.duckdns.org/ - DuckDNS - DNS Dinâmico")
t("https://www.debian.org/ - Debian - Sistema Operacional")
t("https://www.ubuntu.com/ - Ubuntu - Sistema Operacional")
t("https://www.linux.org/ - Linux - Sistema Operacional")
t("https://www.cyberciti.biz/ - Cyberciti - Site com tutoriais de Linux")
t("https://www.digitalocean.com/community/tutorials - DigitalOcean - Tutoriais de TI")
t("https://www.udemy.com/ - Udemy - Cursos Online")
t("https://www.alura.com.br/ - Alura - Cursos Online")
t("https://www.coursera.org/ - Coursera - Cursos Online")
t("https://www.edx.org/ - edX - Cursos Online")
t("https://www.youtube.com/ - YouTube - Vídeos e Tutoriais")
t("https://www.reddit.com/r/linux/ - Reddit - Comunidade de Linux")
t("https://www.stackoverflow.com/ - Stack Overflow - Comunidade de Programadores")
s(f"Nossa, bastante coisa... vou dar uma olhada nesses links... muito obrigado por tudo {c.Teacher()}! Aprendi muito hoje!")
t("De nada, Pobre Aprendiz! Fico feliz em poder te ajudar e compartilhar conhecimento. Se precisar de mais alguma coisa, pode me chamar. Estou aqui para te apoiar no que precisar.")
t("Agora que você entendeu o conceito de cloud, virtualização e servidores, você pode explorar a cloud privada e ver como tudo funciona na prática. Vamos continuar?")
s("Vamos sim! Obrigado mais uma vez!")
c.LastStep()
