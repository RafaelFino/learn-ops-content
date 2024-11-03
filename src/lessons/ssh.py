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

# Tema: SSH - Secure Shell e como lidar com as chanves de segurança
# O professor deve explicar o que é o SSH, como ele funciona e como ele pode ser utilizado.
# O professor deve usar exemplos práticos e didáticos para explicar o SSH
# O professor deve explicar como funciona a autenticação por senha no SSH.
# O professor deve explicar como funciona a autenticação por chave no SSH.
# O professor deve explicar o que são chaves e os conceitos de chaves públicas e privadas.
# O professor deve explicar como criar suas próprias chaves SSH.
# O professor deve explicar como gerenciar chaves SSH.
# O professor deve explicar como adicionar chaves SSH em servidores remotos.
# O professor deve explicar como remover chaves SSH de servidores remotos.
# O professor deve explicar como fazer login em servidores remotos com SSH.
# O professor deve explicar como fazer login em servidores remotos com chaves SSH.
# O professor deve explicar como fazer login em servidores remotos com senhas e os riscos de fazer dessa forma, recomendando sempre o uso de chaves SSH.
# O professor deve explicar como instalar o SSH no Linux.
# O professor deve explicar como instalar o SSH no Windows.
# O professor deve explicar como gerar chaves SSH.
# professor deve explicar como configurar o SSH para aceitar chaves SSH.
# O professor deve explicar com exemplos como acessar um servidor remoto com SSH.
# O professor deve explicar como acessar um servidor remoto com chaves SSH.

t("Olá, pequeno padawan! Hoje vamos falar sobre o SSH - Secure Shell. Você sabe o que é o SSH?")
s("Sei não, professor. Parece coisa de hacker.")
t("Hahaha, não é coisa de hacker. O SSH é um protocolo de rede que permite a conexão segura com servidores remotos.")
s("Ah, entendi. Tipo um acesso remoto?")
t("Isso mesmo, mas com segurança. O SSH é utilizado para acessar servidores remotos de forma segura.")
s("Legal! E como eu faço para usar o SSH?")
t("Para usar o SSH, você precisa de um cliente SSH instalado no seu computador e um servidor SSH instalado no servidor remoto.")
s("Entendi. E como eu faço para instalar o SSH?")
t("No Linux, você pode instalar o SSH com o comando:")
c.ShowCommand("sudo apt install openssh-client")
s("E no Windows?")
t("No Windows, você pode instalar o SSH ativando o recurso nas configurações do Windows ou usando o PuTTY.")
s("Legal! Putty? Que nome engraçado!")
t("Hahaha, é um nome engraçado mesmo. O PuTTY é um cliente SSH para Windows.")
s("E como eu faço para me conectar a um servidor remoto com o SSH?")
t("Para se conectar a um servidor remoto com o SSH, você pode usar o comando:")
c.ShowCommand("ssh usuario@servidor")
t("Mas existe uma forma bem mais segura de se fazer isso, usando chaves SSH")
s("Chaves SSH? O que é isso?")
t("As chaves SSH são pares de chaves criptográficas, uma pública e uma privada, que são usadas para autenticar a conexão com o servidor remoto.")
s("E como eu faço para criar minhas próprias chaves SSH?")
t("Você pode criar suas próprias chaves SSH com o comando:")
c.ShowCommand("ssh-keygen -t rsa -b 2048")
s("E depois?")
t("Depois de criar suas chaves SSH, você pode adicionar a chave pública no servidor remoto para se autenticar.")
s("E como eu faço isso?")
t("Você pode adicionar a chave pública no servidor remoto com o comando:")
c.ShowCommand("ssh-copy-id usuario@servidor")
s("E como eu faço login no servidor remoto com as chaves SSH?")
t("Para fazer login no servidor remoto com as chaves SSH, você pode usar o comando:")
c.ShowCommand("ssh -i chave_privada usuario@servidor")
s("E se eu quiser remover as chaves SSH do servidor remoto?")
t("Você pode remover as chaves SSH do servidor remoto com o comando:")
c.ShowCommand("ssh-keygen -R servidor")
s("E se eu quiser fazer login com senha?")
t("Você pode fazer login com senha no servidor remoto com o comando:")
c.ShowCommand("ssh usuario@servidor")
t("Mas eu não recomendo fazer login com senha, pois é menos seguro do que usar chaves SSH.")
s("Entendi. Vou sempre usar chaves SSH então.")
q("Eu ouvi uns termos, algo como chave publica e privada, que treta é essa?")
t("As chaves públicas e privadas são pares de chaves criptográficas que são usadas para autenticar a conexão com o servidor remoto.")
s("E como elas funcionam?")
t("A chave pública é usada para criptografar os dados que só podem ser descriptografados pela chave privada.")
s("Ainda estou confuso, poderia me explicar melhor?")
t("Claro! A chave pública é compartilhada com o servidor remoto e a chave privada fica apenas no seu computador.")
s("Como assim, isso parece meio confuso ainda... o que tem dentro dessas chaves?")
t("Dentro das chaves SSH, existem números primos e algoritmos de criptografia que garantem a segurança da conexão. Elas são arquivos de texto que contém essas informações.")
s("Você poderia me mostrar aqui como elas são por dentro?")
t("Claro! Vamos abrir a chave pública:")
c.ShowCommand("cat ~/.ssh/id_rsa.pub")
t("E agora vamos abrir a chave privada:")
c.ShowCommand("cat ~/.ssh/id_rsa")
s("E o que tem dentro desses arquivos?")
t("Dentro da chave pública temos a chave que será compartilhada com o servidor remoto. E dentro da chave privada temos a chave que fica apenas no seu computador.")
s("Como seria o resultado desse comando de cat?")
t("O comando cat exibe o conteúdo do arquivo. Você verá uma sequência de caracteres que representam a chave SSH. Olha só como ficaria a chave pública:")
c.ShowCommand("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQKz2Y2Q3z ...")
t("E a chave privada seria parecida com isso:")
c.ShowCommand("""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Cs9mNkN8
...
-----END RSA PRIVATE KEY -----
""")
t("A chave privada é um arquivo que você deve manter em segredo, nunca compartilhe a chave privada com ninguém. A chave pública é a que você compartilha com o servidor remoto.")
s("Entendi, eu acho, mas como eu crio uma chave pública, ela vem de onde?")
t("A chave pública é gerada a partir da chave privada. Quando você cria suas chaves SSH, o sistema gera automaticamente a chave pública a partir da chave privada.")
s("E como eu faço para gerar essas chaves?")
t("Você pode gerar suas chaves SSH com o comando:")
c.ShowCommand("ssh-keygen -t rsa -b 2048")
s("E como eu sei se deu certo?")
t("Quando você executa o comando, o sistema irá gerar as chaves SSH e salvará os arquivos no diretório ~/.ssh.")
s("E se eu quiser usar outra chave?")
t("Você pode gerar chaves SSH com outros algoritmos e tamanhos de bits, como o algoritmo ECDSA ou o tamanho de 4096 bits.")
s("Eu vi algumas vezes você falando desse RSA, o que é isso?")
t("O RSA é um algoritmo de criptografia assimétrica que é amplamente utilizado para a geração de chaves SSH.")
s("Assimétrica? Q bagulho é esse?")
t("A criptografia assimétrica utiliza um par de chaves, uma pública e uma privada, que são usadas para criptografar e descriptografar os dados.")
s("Não ajudou, você está falando de uma forma muito complexa, faz de conta que eu sou um Pobre da Favela e que não sabe nada sobre isso. Como isso funciona?")
t("Hahaha, desculpe. A criptografia assimétrica utiliza um par de chaves, uma pública e uma privada, que são usadas para garantir a segurança da comunicação.")
s("Nâo ajudou, tá complexo... se tem uma assimétrica, tem também uma simétrica? Ainda não entendi como isso funciona, poderia dar uns exemplos mais simples?")
t("Claro! Vamos fazer uma analogia. Imagine que a chave pública é uma caixa de correio e a chave privada é a chave da caixa de correio.")
s("E como isso funciona?")
t("Quando alguém quer enviar uma mensagem para você, ela coloca a mensagem na caixa de correio e tranca com a chave pública.")
s("E depois?")
t("Você recebe a mensagem e usa a chave privada para abrir a caixa de correio e ler a mensagem.")
s("Entendi, mas e se alguém roubar a chave pública?")
t("Se alguém roubar a chave pública, ela só poderá colocar mensagens na caixa de correio, mas não poderá abrir a caixa para ler as mensagens.")
s("E se alguém roubar a chave privada?")
t("Se alguém roubar a chave privada, ela poderá abrir a caixa de correio e ler as mensagens. Por isso é importante manter a chave privada em segredo.")
s(f"Entendi, {c.Teacher()}. Obrigado pela explicação. Agora você melhorou bem isso")
t("Hahaha, obrigado! Mas a aula ainda não acabou, ainda temos muito mais para aprender sobre o SSH.")
s("Sério? Achei que já tinha aprendido tudo.")
t("Não, não. Ainda temos muito mais para aprender. Vamos continuar?")
s("Claro, estou pronto para aprender mais!")
t("Ótimo! Vamos continuar então.")
t("Agora que você já sabe o que é o SSH e como funciona a autenticação por chaves, vamos falar sobre como gerenciar suas chaves SSH.")
s("Como assim, gerenciar chaves SSH?")
t("Gerenciar chaves SSH significa criar, adicionar, remover e listar suas chaves SSH.")
s("E como eu faço isso?")
t("Você pode gerenciar suas chaves SSH com os comandos ssh-keygen, ssh-add, ssh-copy-id e ssh-keyscan.")
s("E como eu faço para listar minhas chaves SSH?")
t("Você pode listar suas chaves SSH com o comando:")
c.ShowCommand("ls ~/.ssh")
s("E como eu faço para adicionar minhas chaves SSH em servidores remotos?")
t("Você pode adicionar suas chaves SSH em servidores remotos com o comando:")
c.ShowCommand("ssh-copy-id usuario@servidor")
s("E como eu faço para remover minhas chaves SSH de servidores remotos?")
t("Você pode remover suas chaves SSH de servidores remotos com o comando:")
c.ShowCommand("ssh-keygen -R servidor")
s("E se eu quiser adicionar mais de uma chave SSH?")
t("Você pode adicionar mais de uma chave SSH em um servidor remoto, basta executar o comando ssh-copy-id para cada chave.")
s("E se eu quiser remover todas as chaves SSH de um servidor remoto?")
t("Você pode remover todas as chaves SSH de um servidor remoto com o comando:")
c.ShowCommand("ssh-keygen -R servidor")
s("E se eu quiser remover todas as chaves SSH de todos os servidores remotos?")
t("Você pode remover todas as chaves SSH de todos os servidores remotos com o comando:")
c.ShowCommand("ssh-keygen -R '*'")
s("E se eu quiser remover todas as chaves SSH?")
t("Você pode remover todas as chaves SSH com o comando:")
c.ShowCommand("rm -rf ~/.ssh")
s("E se eu quiser adicionar uma chave SSH manualmente?")
t("Você pode adicionar uma chave SSH manualmente no arquivo ~/.ssh/authorized_keys.")
s("E se eu quiser remover uma chave SSH manualmente?")
t("Você pode remover uma chave SSH manualmente do arquivo ~/.ssh/authorized_keys.")
s("E se eu quiser listar as chaves SSH de um servidor remoto?")
t("Você pode listar as chaves SSH de um servidor remoto com o comando:")
c.ShowCommand("ssh-keyscan servidor")
s("E se eu quiser saber mais sobre o ssh-keyscan?")
t("O ssh-keyscan é um utilitário que é usado para coletar as chaves públicas dos servidores remotos.")
s("E se eu quiser saber mais sobre o ssh-keygen?")
t("O ssh-key gen é um utilitário que é usado para gerar, gerenciar e converter chaves SSH.")
s("E se eu quiser saber mais sobre o ssh-add?")
t("O ssh-add é um utilitário que é usado para adicionar chaves privadas ao agente de autenticação SSH.")
s("E se eu quiser saber mais sobre o ssh-copy-id?")
t("O ssh-copy-id é um utilitário que é usado para adicionar chaves públicas ao arquivo ~/.ssh/authorized_keys de um servidor remoto.")
s("E se eu quiser saber mais sobre o ssh-keygen?")
t("O ssh-key gen é um utilitário que é usado para gerar, gerenciar e converter chaves SSH.")
s("E se eu quiser saber mais sobre o ssh-keyscan?")
t("O ssh-keyscan é um utilitário que é usado para coletar as chaves públicas dos servidores remotos.")
s("E se eu quiser saber mais sobre o ssh-add?")
t("O ssh-add é um utilitário que é usado para adicionar chaves privadas ao agente de autenticação SSH.")
s("E se eu quiser saber mais sobre o ssh-copy-id?")
t("O ssh-copy-id é um utilitário que é usado para adicionar chaves públicas ao arquivo ~/.ssh/authorized_keys de um servidor remoto.")
s("Eu reparei que isso tudo são comandos de Linux, é isso mesmo?")
t("Sim, esses comandos são comandos do Linux. No Windows, você pode usar o PuTTY para gerenciar suas chaves SSH.")
s("E se eu quiser saber mais sobre o PuTTY?")
t("O PuTTY é um cliente SSH para Windows que permite gerenciar suas chaves SSH de forma gráfica.")
t("Mas eu recomendo que você aprenda a usar os comandos do Linux, pois são mais poderosos e flexíveis. A esmagadora maioria dos servidores remotos são Linux e SSH é a forma mais comum de acessá-los.")
s(f"Entendi, {c.Teacher()}. Vou aprender a usar os comandos do Linux.")
t("Ótimo! Se tiver alguma dúvida, é só me chamar. Vamos continuar?")
s("Claro, estou pronto para aprender mais!")
t("Ótimo! Vamos continuar então.")
t("Agora que você já sabe o que é o SSH, como funciona a autenticação por chaves e como gerenciar suas chaves SSH, vamos falar sobre como acessar servidores remotos com o SSH.")
s("Como assim, acessar servidores remotos com o SSH?")
t("Acessar servidores remotos com o SSH significa fazer login em servidores remotos de forma segura e autenticada.")
s("E como eu faço isso?")
t("Você pode fazer login em servidores remotos com o SSH usando o comando:")
c.ShowCommand("ssh usuario@servidor")
s("E como eu faço para fazer login com chaves SSH?")
t("Para fazer login em servidores remotos com chaves SSH, você pode usar o comando:")
c.ShowCommand("ssh -i chave_privada usuario@servidor")
s("E se eu quiser fazer login com senha?")
t("Você pode fazer login com senha no servidor remoto com o comando:")
c.ShowCommand("ssh usuario@servidor")
t("Mas eu não recomendo fazer login com senha, pois é menos seguro do que usar chaves SSH.")
s("Entendi, vou sempre usar chaves SSH então.")
s("E se eu quiser fazer login em uma porta diferente?")
t("Você pode fazer login em uma porta diferente com o comando:")
c.ShowCommand("ssh -p porta usuario@servidor")
s("E se eu quiser fazer login como outro usuário?")
t("Você pode fazer login como outro usuário com o comando:")
c.ShowCommand("ssh outro_usuario@servidor")
s("E se eu quiser fazer login como root?")
t("Você pode fazer login como root com o comando:")
c.ShowCommand("ssh root@servidor")
t("Mas eu não recomendo fazer login como root, pois é menos seguro do que fazer login como um usuário comum.")
s("Entendi, vou sempre fazer login como um usuário comum.")
s("E se eu quiser fazer login em um servidor remoto e executar um comando?")
t("Você pode fazer login em um servidor remoto e executar um comando com o comando:")
c.ShowCommand("ssh usuario@servidor 'comando'")
s("E se eu quiser fazer login em um servidor remoto e copiar um arquivo?")
t("Você pode fazer login em um servidor remoto e copiar um arquivo com o comando:")
c.ShowCommand("scp arquivo usuario@servidor:/caminho")
q("scp? O que é isso?")
t("O scp é um utilitário que é usado para copiar arquivos de forma segura entre servidores remotos.")
s("E se eu quiser copiar um diretório?")
t("Você pode copiar um diretório com o comando:")
c.ShowCommand("scp -r diretorio usuario@servidor:/caminho")
s("E se eu quiser copiar um arquivo de um servidor remoto para o meu computador?")
t("Você pode copiar um arquivo de um servidor remoto para o seu computador com o comando:")
c.ShowCommand("scp usuario@servidor:/caminho/arquivo .")
s("E se eu quiser copiar um diretório de um servidor remoto para o meu computador?")
t("Você pode copiar um diretório de um servidor remoto para o seu computador com o comando:")
c.ShowCommand("scp -r usuario@servidor:/caminho/diretorio .")
q("E eu consigo usar o scp com chaves SSH para copiar arquivos?")
t("Sim! Você pode usar o comando scp passando chaves como forma de autenticação, veja:")
c.ShowCommand("scp -i chave_privada arquivo usuario@servidor:/caminho")
s("E se eu quiser copiar um arquivo de um servidor remoto para outro servidor remoto?")
t("Você pode copiar um arquivo de um servidor remoto para outro servidor remoto com o comando:")
c.ShowCommand("scp usuario1@servidor1:/caminho/arquivo usuario2@servidor2:/caminho")
s("E se eu quiser copiar um diretório de um servidor remoto para outro servidor remoto?")
t("Você pode copiar um diretório de um servidor remoto para outro servidor remoto com o comando:")
c.ShowCommand("scp -r usuario1@servidor1:/caminho/diretorio usuario2@servidor2:/caminho")
s("E se eu quiser copiar um arquivo de um servidor remoto para o meu computador e vice-versa?")
t("Você pode copiar um arquivo de um servidor remoto para o seu computador e vice-versa com o comando:")
c.ShowCommand("scp usuario@servidor:/caminho/arquivo .")
c.ShowCommand("scp arquivo usuario@servidor:/caminho")
s("E se eu quiser copiar um diretório de um servidor remoto para o meu computador e vice-versa?")
t("Você pode copiar um diretório de um servidor remoto para o seu computador e vice-versa com o comando:")
c.ShowCommand("scp -r usuario@servidor:/caminho/diretorio .")
c.ShowCommand("scp -r diretorio usuario@servidor:/caminho")
s("Caramba! Isso tudo é bem legal mesmo! Acho que aprendi algo bem importante hoje.")
t("Fico feliz que tenha aprendido! O SSH é uma ferramenta muito poderosa e útil para acessar servidores remotos de forma segura.")
s(f"Obrigado pela aula, professor{c.Teacher()}. Aprendi muito!")




