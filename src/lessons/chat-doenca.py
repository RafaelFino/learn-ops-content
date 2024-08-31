
#!/usr/bin/env python3

# Importing the chat class from the talker module
from operator import le
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
# O professor deve ser ironico para brincar com os alunos, mas sempre de forma respeitosa e descontraída.
# Os alunos devem se comportar como aprendizes, curiosos e com vontade de aprender, mas sem muito conhecimento sobre o tema, sempre questionando sobre explicações mais formais e pedindo exemplosp práticos.
# Sempre que o aluno tentar se referir ao professor, ele deve usar o método c.Teacher() para se referir ao professor, nunca diretamente. Dessa forma o nome do professor irá aparecer na tela do aluno.
# O aluno geralmente se perde nas explicações e não entende na primeira explicação, forçando o professor a tentar sempre simplificar o tema com exemplos práticos e analogias simplificadas.

def t(m):
    c.Speak(m)

def s(m):
    c.StudentComment(m)

def q(m):
    c.Question(m)

def code(code):
    c.ShowCode(code)

def run(code):
    c.ShowCodeAndRun(code)

def cmd(command):
    c.ShowCommand(command)

# Tema: Um exercício prático para criar uma aplicação em python, cliente de uma aplicação server de um chat feito para eles
# O prefessor deve explicar como um chat funciona, a ideia de ter um servidor e um cliente
# O professor deve explicar como funciona a comunicação entre o servidor e o cliente, com API HTTP
# O professor deve explicar como funciona o protocolo HTTP
# O professor deve explicar como funciona o protocolo REST
# O professor deve explicar como funcionam os verbos HTTP
# O professor deve explicar a diferença entre cada verbo HTTP e quando usar cada um deles
# O professor deve explicar como funciona o método GET
# O professor deve explicar como funciona o método POST
# O professor deve explicar como funciona o método PUT
# O professor deve explicar como funciona o método DELETE
# O professor deve explicar como funciona o método PATCH
# O professor deve explicar os retornos de status HTTP
# O professor deve explicar os retornos HTTP 1xx e dar exemplos práticos
# O professor deve explicar os retornos HTTP 2xx e dar exemplos práticos
# O professor deve explicar os retornos HTTP 3xx e dar exemplos práticos
# O professor deve explicar os retornos HTTP 4xx e dar exemplos práticos
# O professor deve explicar os retornos HTTP 5xx e dar exemplos práticos
# O professor deve explicar os retornos de status HTTP mais comuns
# O professor deve explicar as diferenças entre TCP, UDP, HTTP e HTML
# O professor deve explicar como funciona o TCP e sockets
# O professor deve explicar como funciona o UDP e sockets
# O professor deve explicar como funciona o HTTP e sua relação com o TCP e sockets
# O professor deve explicar como funciona o HTML e sua relação com o HTTP
# Após tudo isso, o professor deve explicar como criar um servidor HTTP em python, usando o módulo http.server
# O professor deve explicar como criar um servidor HTTP em python, usando o módulo Flask
# O professor deve mostrar como um servidor HTTP em python pode ser usado para criar uma API REST com um método simples de Hello World com um GET
# O professor deve mostrar como um servidor HTTP em python pode ser usado para criar uma API REST com um método simples de Hello World com um POST, usando forms e json
# com esse exemplo, deve ser explicado o que é json e como funciona
# O professor deve mostrar como um servidor HTTP em python pode ser usado para criar uma API REST com um método simples de Hello World com um PUT, usando forms e json
# Após isso, vamos voltar ao chat, vamos explicar que o chat tem apenas 2 métodos: um POST para enviar mensagens e um GET para receber mensagens
# O professor deve explicar como funciona o chat, como ele é simples e como o server é feito
# O objetivo do exercício é criar um client que use essas duas rotas para enviar e receber mensagens
# O profssor deve começar a criar o client, usando o módulo requests e flask para criar um client simples
# O professor deve ensinar o aluno a instalar o módulo requests e o flask com pip
# O servidor onde o chat está rodando responder pelo IP 192.168.1.9 e a porta 8080
# A rota para o envio de mensagens é /message, o POST envia mensagens e o GET recebe mensagens usando parametros de query, por exemplo /message/10, onde 10 é a ultima mensagem recebida, portanto o server vai enviar a partir da mensagem 10
# O método de post, devolve o ID da mensagem criada e o método de get, devolve uma lista de mensagens, sempre em json

t("Olá Doença, hoje vamos falar sobre como criar um chat simples em python, usando um servidor e um cliente")
t("Você sabe o que é um chat? Já parou para pensar como um funciona?")
s(f"Ah, eu tenho uma noção {c.Teacher()}, mas acho que nunca parei para pensar como um chat funciona...")
t("Então, um chat é uma aplicação que permite a comunicação entre duas ou mais pessoas, em tempo real, é um lugar para guardar mensagens e enviar mensagens, simples assim, que nem seu whatsapp")
s("Acho que eu entendi... mas nunca pensei nisso...")
t("E você sabe como um chat funciona? Como ele envia e recebe mensagens?")
s(f"Acho que não {c.Teacher()}, todo mundo se conecta uns nos outros e envia mensagens, mas não sei como isso acontece")
t("Então, um chat é uma aplicação que tem um servidor e um cliente, o servidor é responsável por guardar as mensagens e o cliente por enviar e receber mensagens")
s("Entendi, mas como assim cliente e servidor? Como isso funciona? como eles se comunicam?")
t("Então, a comunicação entre o servidor e o cliente é feita usando o protocolo HTTP, você já ouviu falar dele?")
s(f"Já ouvi falar {c.Teacher()}, mas não sei muito bem como ele funciona, sempre vejo ele nos endereços de sites da internet, mas nunca entendi oq quer dizer...")
t("O HTTP é um protocolo que define como a comunicação entre o servidor e o cliente deve ser feita, ele define como os dados devem ser enviados e recebidos")
s(f"Protocolo? Como assim {c.Teacher()}? O que é um protocolo?")
t("Um protocolo é um conjunto de regras que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos")
s(f"{c.Teacher()} isso tá complicado, consegue me dar exemplos práticos do que é um protocolo?")
t("Claro, um exemplo de protocolo é o TCP, ele define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos")
s("Você náo ajudou, nem sei o que é um protocolo e você já me trouxe outra sigla... me explica melhor o que é um protocolo usando palavras mais simples e exemplos práticos com analogias por favor")
t("Então, um protocolo é como um manual de instruções, ele define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, é como um manual de instruções que define como um aparelho deve ser usado")
s(f"Entendi {c.Teacher()}, é um conjunto de regras para que a comunicação aconteça... acho que estou entendendo... é como a nossa lingua?")
t("Isso mesmo, é como a nossa lingua, é um conjunto de regras que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos")
s(f"Entendi {c.Teacher()}, mas e o HTTP? Como ele funciona? Entendi que é um protocolo, mas como que um cliente conecta em um servidor? ele liga pelo telefone?")
t("Então, o HTTP é um protocolo que define como a comunicação entre o servidor e o cliente deve ser feita, ele define como os dados devem ser enviados e recebidos, ele define como a comunicação entre o servidor e o cliente deve ser feita, mas a comunicação passa por uma série de camadas... eles usam redes para se comunicar")
s(f"Redes? Como assim {c.Teacher()}? O que são redes?")
t("Então, redes são como estradas, são caminhos que os dados percorrem para chegar de um ponto a outro, é como uma estrada que os dados percorrem para chegar de um ponto a outro")
t("Cada computador nessa rede possui um endereço, um IP, que é como o endereço de uma casa, é como o endereço de um computador na internet")
s(f"Entendi {c.Teacher()}, é como se cada computador tivesse um endereço, e a comunicação entre eles fosse feita por estradas, é isso então com o HTTP vc liga um IP no outro e eles conversam?")
t("Isso mesmo, é como se cada computador tivesse um endereço, um IP, então eles fecham uma comunicação entre eles, no casso do HTTP, por baixo eles usam uma camada de comunicação chamada TCP, que é como uma estrada de alta velocidade")
s("Ahhh!! Esse é o TCP que vc falou um pouco antes, como ele funciona?")
t("Então, o TCP é um protocolo que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada de alta velocidade que os dados percorrem para chegar de um ponto a outro")
s("Eu acho que já vi umas piadas sobre TCP e UDP na internet e nunca entendi, o que é UDP?")
t("Então, o UDP é um protocolo que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada de alta velocidade que os dados percorrem para chegar de um ponto a outro, mas ele é mais rápido que o TCP")
s("Eita... como assim? qual a grande diferença do TCP e UDP? Quando uso cada um deles e qual a relação deles com o HTTP? Tantas siglas...")
t("Então, o TCP é um protocolo que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada de alta velocidade que os dados percorrem para chegar de um ponto a outro, ele é mais lento que o UDP, mas é mais confiável")
s(f"Entendi {c.Teacher()}, o TCP é mais lento mas mais confiável, e o UDP é mais rápido mas menos confiável, é isso?")
t("Isso mesmo, o TCP é mais lento mas mais confiável, ele garante que os dados cheguem ao destino, já o UDP é mais rápido mas menos confiável, ele não garante que os dados cheguem ao destino. Vamos ver algums exeplos:")
t("Imagine que você está enviando uma carta, o TCP é como uma carta registrada, ele garante que a carta chegue ao destino, já o UDP é como uma carta simples, ele não garante que a carta chegue ao destino")
s(f"Entendi {c.Teacher()}, é como se o TCP fosse uma carta registrada e o UDP fosse uma carta simples, o TCP garante que a carta chegue ao destino, já o UDP não garante que a carta chegue ao destino")
t("Boa! acho que você está entendendo...")
q("Mas e o HTTP? Como ele se relaciona com o TCP e UDP?")
t("Então, o HTTP é um protocolo que define como a comunicação entre o servidor e o cliente deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada que os dados percorrem para chegar de um ponto a outro, ele usa o TCP como camada de comunicação")
t("Quando falamos em TCP, estamos falando de como a rede se conecta, é de uma camada de mais baixo nível, é ali que fica o tal do endereço IP, é como se fosse a estrada que os dados percorrem para chegar de um ponto a outro")
t("Quando falamos em HTTP, estamos falando de como a comunicação entre o servidor e o cliente deve ser feita, é uma camada de mais alto nível, é como se fosse o manual de instruções que define como a comunicação entre dois pontos deve ser feita")
s("Caramba! Que legal... nunca tinha parado para pensar nisso... e o HTML? Como ele se relaciona com o HTTP?")
t("Então, o HTML é uma linguagem de marcação que define como as páginas web devem ser exibidas, ele é como o conteúdo que é exibido na página, ele é como o conteúdo que é exibido na página, ele é como o conteúdo que é exibido na página")
s(f"Entendi {c.Teacher()}, o HTML é o que tem dentro da carta então? é o conteúdo que é exibido na página?")
t("Isso mesmo, o HTML é o que tem dentro da carta, é o conteúdo que é exibido na página, é como o conteúdo que é exibido na página, é como o conteúdo que é exibido na página")
s("Você poderia por favor resumir então esses conceitos? O que é o TCP, UDP, HTTP e HTML? Só para que eu possa fixar melhor e anotar aqui...")
t("Claro, o TCP é um protocolo que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada de alta velocidade que os dados percorrem para chegar de um ponto a outro")
t("O UDP é um protocolo que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada de alta velocidade que os dados percorrem para chegar de um ponto a outro, ele é mais rápido que o TCP")
t("O HTTP é um protocolo que define como a comunicação entre o servidor e o cliente deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada que os dados percorrem para chegar de um ponto a outro, ele usa o TCP como camada de comunicação")
t("O HTML é uma linguagem de marcação que define como as páginas web devem ser exibidas, ele é como o conteúdo que é exibido na página, ele é como o conteúdo que é exibido na página, ele é como o conteúdo que é exibido na página")
s(f"Entendi {c.Teacher()}, será que podemos tentar fazer isso com o exemplo das cartas e nessa analogia colocar o TCP, UDP, HTTP e HTML?")
t("Claro, imagine que você está enviando uma carta, o TCP é como uma carta registrada, ele garante que a carta chegue ao destino, já o UDP é como uma carta simples, ele não garante que a carta chegue ao destino")
t("O HTTP é como o envelope da carta, ele define como a comunicação entre o servidor e o cliente deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada que os dados percorrem para chegar de um ponto a outro, ele usa o TCP como camada de comunicação")
t("O HTML é como o conteúdo da carta, é o que tem dentro da carta, é o conteúdo que é exibido na página, é como o conteúdo que é exibido na página, é como o conteúdo que é exibido na página")
s(f"Entendi {c.Teacher()}, acho que agora eu entendi melhor... mas e o chat? Como ele funciona?")
t("Calma pequeno gafanhoto, vamos chegar lá... ainda existem alguns outros conceitos que precisamos entender antes de chegar no chat, vamos falar um pouco do HTTP e seus verbos")
q(f"Verbos? Como assim {c.Teacher()}? O que são verbos? Agora a casa caiu... eu era péssimo nas aulas de português...")
t("Então, os verbos são ações, são o que você faz, assim como na lingua portuguesa, os verbos no HTTP são ações que você faz e fazem parte desse acordo de comunicação entre o servidor e o cliente")
s(f"Entendi {c.Teacher()}, são ações que você faz, mas o que isso tem a ver com o HTTP?")
t("Os verbos sempre partem do cliente para o servidor, o cliente envia uma ação para o servidor, o servidor executa essa ação e devolve uma resposta, é como se o cliente pedisse algo para o servidor e o servidor respondesse")
s(f"Entendi {c.Teacher()}, e quais são as ações que o cliente pode fazer no HTTP?")
t("Então, os verbos HTTP são GET, POST, PUT, DELETE, PATCH, cada um deles tem uma ação específica e deve ser usado em um contexto específico")
s("Agora bagunçou, o que cada um desses faz e quando eu devo usar isso?")
t("Então, o GET é usado para buscar informações, o POST é usado para criar informações, o PUT é usado para atualizar informações, o DELETE é usado para deletar informações, o PATCH é usado para atualizar parcialmente informações")
s(f"Mas {c.Teacher()}, pensa só, sou um cliente de um servidor lá, e quero pedir uma informação, então eu abro uma conexão com o servidor, para isso preciso saber o IP dele, certo?")
t("Isso mesmo, você precisa saber o IP do servidor para se conectar a ele, é como se você precisasse saber o endereço de uma casa para enviar uma carta")
s("Tá, então com o IP dele, eu abro uma conexão TCP, certo? e aí eu vou lá e falo pra ele: GET! mas Get o que? O que ele vai me devolver?")
t("Então, o GET é usado para buscar informações, você envia um GET para o servidor e ele te devolve as informações que você pediu, é como se você pedisse para o servidor te enviar uma carta")
t("Agora é a hora que a coisa fica mais legal... quando você pede algo para o servidor, existe um padrão de respostas que ele pode te dar, são os códigos de status HTTP")
s(f"Códigos de status? Como assim {c.Teacher()}? O que são códigos de status?")
t("Então, os códigos de status HTTP são códigos que o servidor envia para o cliente para informar o status da requisição, ele informa se a requisição foi bem sucedida, se houve um erro, ou se é necessário fazer uma ação adicional")
s(f"Entendi {c.Teacher()}, mas quais são os códigos de status HTTP? E o que cada um deles significa?")
t("Então, os códigos de status HTTP são divididos em 5 classes, 1xx, 2xx, 3xx, 4xx e 5xx, cada uma delas tem um significado específico e deve ser usado em um contexto específico")
q(f"Eita {c.Teacher()}, quantos códigos de status HTTP, são muitos... e o que cada um deles significa?")
t("Então, os códigos de status HTTP 1xx são códigos informativos, eles informam que a requisição foi recebida e está sendo processada, os códigos de status HTTP 2xx são códigos de sucesso, eles informam que a requisição foi bem sucedida, os códigos de status HTTP 3xx são códigos de redirecionamento, eles informam que é necessário fazer uma ação adicional, os códigos de status HTTP 4xx são códigos de erro do cliente, eles informam que houve um erro na requisição, os códigos de status HTTP 5xx são códigos de erro do servidor, eles informam que houve um erro no servidor")
s(f"Entendi {c.Teacher()}, mas quais são os códigos de status HTTP mais comuns? E o que cada um deles significa?")
t("Então, os códigos de status HTTP mais comuns são 200, 201, 204, 400, 401, 403, 404, 500, 503, cada um deles tem um significado específico e deve ser usado em um contexto específico")
s(f"Entendi {c.Teacher()}, complicado isso... lembra q eu sou novo nesse negócio, então é muita informação... consegue me dar exemplo de cada uma dessas classes de retorno e quando eles acontecem?")
t("Ok doença, vamos devagar... começar pelo começo: os retornos 1xx:")
t("Os retornos 1xx são códigos informativos, eles informam que a requisição foi recebida e está sendo processada, por exemplo, o código 100 informa que a requisição foi recebida e o servidor está processando a requisição")
t("Os mais comuns são:")
t("100 - Continue")
t("101 - Switching Protocols")
t("102 - Processing")
t("103 - Early Hints")
q("E quando eles acontecem? consegue me dar exemplos simples usando a carta?")
t("Então, os retornos 1xx são códigos informativos, eles informam que a requisição foi recebida e está sendo processada, por exemplo, o código 100 informa que a requisição foi recebida e o servidor está processando a requisição")
t("Imagine que você está enviando uma carta, o código 100 é como uma carta registrada, ele informa que a carta foi recebida e está sendo processada, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida")
s(f"Entendi {c.Teacher()}, é como se eu enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada, é isso?")
t("Isso mesmo, o código 100 informa que a requisição foi recebida e está sendo processada, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada")
s(f"Entendi {c.Teacher()}, mas e os retornos 2xx? O que eles significam?")
t("Então, os retornos 2xx são códigos de sucesso, eles informam que a requisição foi bem sucedida, por exemplo, o código 200 informa que a requisição foi bem sucedida")
t("Os mais comuns são:")
t("200 - OK, quer dizer que você fez uma requisição e ela foi bem sucedida, é um retorno muito comum!")
t("201 - Created, quer dizer que você fez uma requisição e ela foi bem sucedida e um novo recurso foi criado, é usado quando você tentar enviar uma informação e ela foi criada com sucesso")
t("204 - No Content, quer dizer que você fez uma requisição e ela foi bem sucedida, mas não há conteúdo para ser retornado, é usado quando você tentar enviar uma informação e ela foi criada com sucesso, mas não há conteúdo para ser retornado")
t("203 - Non-Authoritative Information, quer dizer que você fez uma requisição e ela foi bem sucedida, mas o conteúdo não é autoritativo, é usado quando você tentar enviar uma informação e ela foi criada com sucesso, mas o conteúdo não é autoritativo")
t("205 - Reset Content, quer dizer que você fez uma requisição e ela foi bem sucedida, mas o conteúdo foi resetado, é usado quando você tentar enviar uma informação e ela foi criada com sucesso, mas o conteúdo foi resetado, que significa que você deve limpar o conteúdo")
t("206 - Partial Content, quer dizer que você fez uma requisição e ela foi bem sucedida, mas o conteúdo é parcial, é usado quando você tentar enviar uma informação e ela foi criada com sucesso, mas o conteúdo é parcial, que significa que você deve completar o conteúdo")
t("207 - Multi-Status, quer dizer que você fez uma requisição e ela foi bem sucedida, mas o conteúdo é multi-status, é usado quando você tentar enviar uma informação e ela foi criada com sucesso, mas o conteúdo é multi-status, que significa que você deve verificar o status do conteúdo")
t("208 - Already Reported, quer dizer que você fez uma requisição e ela foi bem sucedida, mas o conteúdo já foi reportado, é usado quando você tentar enviar uma informação e ela foi criada com sucesso, mas o conteúdo já foi reportado, que significa que você não precisa reportar novamente")
t("226 - IM Used, quer dizer que você fez uma requisição e ela foi bem sucedida, mas o conteúdo é IM Used, é usado quando você tentar enviar uma informação e ela foi criada com sucesso, mas o conteúdo é IM Used, que significa que você deve usar o IM")
q("E quando eles acontecem? consegue me dar exemplos simples usando a carta?")
t("Então, os retornos 2xx são códigos de sucesso, eles informam que a requisição foi bem sucedida, por exemplo, o código 200 informa que a requisição foi bem sucedida")
t("Imagine que você está enviando uma carta, o código 200 é como uma carta registrada, ele informa que a carta foi recebida e está sendo processada, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida")
s(f"Entendi {c.Teacher()}, é como se eu enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada, é isso?")
t("Isso mesmo, o código 200 informa que a requisição foi bem sucedida, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada")
s(f"Entendi {c.Teacher()}, mas e os retornos 3xx? O que eles significam?")
t("Então, os retornos 3xx são códigos de redirecionamento, eles informam que é necessário fazer uma ação adicional, por exemplo, o código 300 informa que é necessário fazer uma ação adicional")
t("Os mais comuns são:")
t("300 - Multiple Choices, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela tem várias opções, você deve escolher uma delas")
t("301 - Moved Permanently, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela foi movida permanentemente, você deve acessar a nova página")
t("302 - Found, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela foi encontrada, você deve acessar a nova página")
t("303 - See Other, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela é outra, você deve acessar a nova página")
t("304 - Not Modified, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela não foi modificada, você deve acessar a nova página")
t("305 - Use Proxy, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela deve ser acessada por um proxy, você deve acessar a nova página")
t("306 - Switch Proxy, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela deve ser acessada por um proxy, você deve acessar a nova página")
t("307 - Temporary Redirect, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela foi redirecionada temporariamente, você deve acessar a nova página")
t("308 - Permanent Redirect, quer dizer que é necessário fazer uma ação adicional, é usado quando você tentar acessar uma página e ela foi redirecionada permanentemente, você deve acessar a nova página")
q("E quando eles acontecem? consegue me dar exemplos simples usando a carta?")
t("Então, os retornos 3xx são códigos de redirecionamento, eles informam que é necessário fazer uma ação adicional, por exemplo, o código 300 informa que é necessário fazer uma ação adicional")
t("Imagine que você está enviando uma carta, o código 300 é como uma carta registrada, ele informa que a carta foi recebida e está sendo processada, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida")
s(f"Entendi {c.Teacher()}, é como se eu enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada, é isso?")
t("Isso mesmo, o código 300 informa que é necessário fazer uma ação adicional, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada")
s(f"Entendi {c.Teacher()}, mas e os retornos 4xx? O que eles significam?")
t("Então, os retornos 4xx são códigos de erro do cliente, eles informam que houve um erro na requisição, por exemplo, o código 400 informa que houve um erro na requisição")
t("Os mais comuns são:")
t("400 - Bad Request, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e houve um erro na requisição, você deve verificar a requisição, provavelmente você enviou algo errado ou no formato errado, o servidor não entendeu o que você tentou enviar, é um retorno comum quando estamos começando a desenvolver algo e não implementamos corretamente o uso de uma API")
t("401 - Unauthorized, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e você não está autorizado, você deve verificar a requisição, provavelmente você não tem permissão para acessar a página, é um retorno comum quando estamos tentando acessar uma página que precisa de autenticação e não estamos autenticados")
t("403 - Forbidden, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e você não tem permissão para acessar, você deve verificar a requisição, provavelmente você não tem permissão para acessar a página, é um retorno comum quando estamos tentando acessar uma página que não temos permissão")
t("404 - Not Found, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e ela não foi encontrada, você deve verificar a requisição, provavelmente você tentou acessar uma página que não existe, é um retorno comum quando estamos tentando acessar uma página que não existe")
t("405 - Method Not Allowed, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o método não é permitido, você deve verificar a requisição, provavelmente você tentou acessar uma página com um método que não é permitido, é um retorno comum quando estamos tentando acessar uma página com um método que não é permitido")
t("406 - Not Acceptable, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o conteúdo não é aceitável, você deve verificar a requisição, provavelmente você tentou acessar uma página com um conteúdo que não é aceitável, é um retorno comum quando estamos tentando acessar uma página com um conteúdo que não é aceitável")
t("407 - Proxy Authentication Required, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e a autenticação do proxy é necessária, você deve verificar a requisição, provavelmente você tentou acessar uma página que precisa de autenticação do proxy, é um retorno comum quando estamos tentando acessar uma página que precisa de autenticação do proxy")
t("408 - Request Timeout, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o tempo de requisição expirou, você deve verificar a requisição, provavelmente você tentou acessar uma página e o tempo de requisição expirou, é um retorno comum quando estamos tentando acessar uma página e o tempo de requisição expirou")
t("409 - Conflict, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e houve um conflito, você deve verificar a requisição, provavelmente você tentou acessar uma página e houve um conflito, é um retorno comum quando estamos tentando acessar uma página e houve um conflito")
t("410 - Gone, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e ela não está mais disponível, você deve verificar a requisição, provavelmente você tentou acessar uma página e ela não está mais disponível, é um retorno comum quando estamos tentando acessar uma página e ela não está mais disponível")
t("411 - Length Required, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o tamanho é necessário, você deve verificar a requisição, provavelmente você tentou acessar uma página e o tamanho é necessário, é um retorno comum quando estamos tentando acessar uma página e o tamanho é necessário")
t("412 - Precondition Failed, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e a condição prévia falhou, você deve verificar a requisição, provavelmente você tentou acessar uma página e a condição prévia falhou, é um retorno comum quando estamos tentando acessar uma página e a condição prévia falhou")
t("413 - Payload Too Large, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e a carga é muito grande, você deve verificar a requisição, provavelmente você tentou acessar uma página e a carga é muito grande, é um retorno comum quando estamos tentando acessar uma página e a carga é muito grande")
t("414 - URI Too Long, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o URI é muito longo, você deve verificar a requisição, provavelmente você tentou acessar uma página e o URI é muito longo, é um retorno comum quando estamos tentando acessar uma página e o URI é muito longo")
t("415 - Unsupported Media Type, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o tipo de mídia não é suportado, você deve verificar a requisição, provavelmente você tentou acessar uma página e o tipo de mídia não é suportado, é um retorno comum quando estamos tentando acessar uma página e o tipo de mídia não é suportado")
t("416 - Range Not Satisfiable, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o intervalo não é satisfatório, você deve verificar a requisição, provavelmente você tentou acessar uma página e o intervalo não é satisfatório, é um retorno comum quando estamos tentando acessar uma página e o intervalo não é satisfatório")
t("417 - Expectation Failed, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e a expectativa falhou, você deve verificar a requisição, provavelmente você tentou acessar uma página e a expectativa falhou, é um retorno comum quando estamos tentando acessar uma página e a expectativa falhou")
t("418 - I'm a teapot, quer dizer que houve um erro na requisição, é usado quando você tentar acessar uma página e o servidor é uma chaleira, você deve verificar a requisição, provavelmente você tentou acessar uma página e o servidor é uma chaleira, é um retorno comum quando estamos tentando acessar uma página e o servidor é uma chaleira")
q(f"CHALEIRA? Q PORRA É ESSA {c.Teacher()}?")
t("Então, os retornos 4xx são códigos de erro do cliente, eles informam que houve um erro na requisição, por exemplo, o código 400 informa que houve um erro na requisição, esse aí, o 418, é uma piada, é um código de status HTTP que não é usado, é uma brincadeira dos desenvolvedores")
s(f"Entendi {c.Teacher()}, você poderia dar exemplos de quando cada um desses retornos acontece? E como eles se relacionam com a carta?")
t("Então, os retornos 4xx são códigos de erro do cliente, eles informam que houve um erro na requisição, por exemplo, o código 400 informa que houve um erro na requisição")
t("Imagine que você está enviando uma carta, o código 400 é como uma carta registrada, ele informa que a carta foi recebida e está sendo processada, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida")
s(f"Entendi {c.Teacher()}, é como se eu enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada, é isso?")
t("Isso mesmo, o código 400 informa que houve um erro na requisição, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada")
s(f"Entendi {c.Teacher()}, mas e os retornos 5xx? O que eles significam?")
t("Então, os retornos 5xx são códigos de erro do servidor, eles informam que houve um erro no servidor, por exemplo, o código 500 informa que houve um erro no servidor")
t("Os mais comuns são:")
t("500 - Internal Server Error, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e houve um erro no servidor, você deve verificar a requisição, provavelmente o servidor está com problemas, é um retorno comum quando estamos tentando acessar uma página e o servidor está com problemas")
t("501 - Not Implemented, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e a funcionalidade não está implementada, você deve verificar a requisição, provavelmente a funcionalidade não está implementada, é um retorno comum quando estamos tentando acessar uma página e a funcionalidade não está implementada")
t("502 - Bad Gateway, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e a porta de entrada está ruim, você deve verificar a requisição, provavelmente a porta de entrada está ruim, é um retorno comum quando estamos tentando acessar uma página e a porta de entrada está ruim")
t("503 - Service Unavailable, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e o serviço está indisponível, você deve verificar a requisição, provavelmente o serviço está indisponível, é um retorno comum quando estamos tentando acessar uma página e o serviço está indisponível")
t("504 - Gateway Timeout, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e a porta de entrada expirou, você deve verificar a requisição, provavelmente a porta de entrada expirou, é um retorno comum quando estamos tentando acessar uma página e a porta de entrada expirou")
t("505 - HTTP Version Not Supported, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e a versão do HTTP não é suportada, você deve verificar a requisição, provavelmente a versão do HTTP não é suportada, é um retorno comum quando estamos tentando acessar uma página e a versão do HTTP não é suportada")
t("506 - Variant Also Negotiates, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e a variante também negocia, você deve verificar a requisição, provavelmente a variante também negocia, é um retorno comum quando estamos tentando acessar uma página e a variante também negocia")
t("507 - Insufficient Storage, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e o armazenamento é insuficiente, você deve verificar a requisição, provavelmente o armazenamento é insuficiente, é um retorno comum quando estamos tentando acessar uma página e o armazenamento é insuficiente")
t("508 - Loop Detected, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e o loop foi detectado, você deve verificar a requisição, provavelmente o loop foi detectado, é um retorno comum quando estamos tentando acessar uma página e o loop foi detectado")
t("510 - Not Extended, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e a extensão não foi feita, você deve verificar a requisição, provavelmente a extensão não foi feita, é um retorno comum quando estamos tentando acessar uma página e a extensão não foi feita")
t("511 - Network Authentication Required, quer dizer que houve um erro no servidor, é usado quando você tentar acessar uma página e a autenticação de rede é necessária, você deve verificar a requisição, provavelmente a autenticação de rede é necessária, é um retorno comum quando estamos tentando acessar uma página e a autenticação de rede é necessária")
q("E quando eles acontecem? consegue me dar exemplos simples usando a carta?")
t("Então, os retornos 5xx são códigos de erro do servidor, eles informam que houve um erro no servidor, por exemplo, o código 500 informa que houve um erro no servidor")
t("Imagine que você está enviando uma carta, o código 500 é como uma carta registrada, ele informa que a carta foi recebida e está sendo processada, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida")
s(f"Entendi {c.Teacher()}, é como se eu enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada, é isso?")
t("Isso mesmo, o código 500 informa que houve um erro no servidor, é como se você enviasse uma carta e recebesse um aviso de que a carta foi recebida, mas ainda está sendo processada")
q("Uau... bastante coisa, será que conseguimos montar uma tabelinha aqui, aquelas legais em ASCII Art, com os comandos mais comuns, seus códigos, nomes e significiados simplificados e quando eles acontecem e depois uma outra tabelinhas só com os retornos que são piadas?")
t("Claro, vamos lá, vou te ajudar a montar essas tabelas, vamos começar com os comandos mais comuns em formato de tabela ASCII, já formatada considerando fontes mono espaçadas")
t("Vamos lá, a tabela dos comandos mais comuns:")
t("|--------------------------------------------------------------------------------------------------------------------------------------------|")
t("| Comando | Código   | Nome        | Significado             | Quando acontece                                                               |")
t("|--------------------------------------------------------------------------------------------------------------------------------------------|")
t("| GET     | 200      | OK          | Requisição bem sucedida | Quando a requisição foi bem sucedida                                          |")
t("| POST    | 201      | Created     | Recurso criado          | Quando a requisição foi bem sucedida e um novo recurso foi criado             |")
t("| PUT     | 204      | No Content  | Sem conteúdo            | Quando a requisição foi bem sucedida, mas não há conteúdo para ser retornado  |")
t("| DELETE  | 404      | Not Found   | Não encontrado          | Quando a página não foi encontrada                                            |")
t("| PATCH   | 400      | Bad Request | Requisição ruim         | Quando houve um erro na requisição                                            |")
t("|--------------------------------------------------------------------------------------------------------------------------------------------|")
t("Agora a tabela dos retornos que são piadas:")
t("|--------------------------------------------------------------------------------------------------------------------------------------------|")
t("| Comando | Código   | Nome         | Significado             | Quando acontece                                                              |")
t("|--------------------------------------------------------------------------------------------------------------------------------------------|")
t("| GET     | 418      | I'm a teapot | Eu sou uma chaleira     | Quando o servidor é uma chaleira                                             |")
t("|--------------------------------------------------------------------------------------------------------------------------------------------|")
s(f"Entendi {c.Teacher()}, acho que agora eu entendi melhor... poderia então fazer um super resumo disso tudo para podermos ir para o chat?")
t("Claro, vamos lá, um super resumo de tudo que falamos até agora:")
t("O TCP é um protocolo que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada de alta velocidade que os dados percorrem para chegar de um ponto a outro")
t("O UDP é um protocolo que define como a comunicação entre dois pontos deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada de alta velocidade que os dados percorrem para chegar de um ponto a outro, ele é mais rápido que o TCP")
t("O HTTP é um protocolo que define como a comunicação entre o servidor e o cliente deve ser feita, ele define como os dados devem ser enviados e recebidos, ele é como uma estrada que os dados percorrem para chegar de um ponto a outro, ele usa o TCP como camada de comunicação")
t("O HTML é uma linguagem de marcação que define como as páginas web devem ser exibidas, ele é como o conteúdo que é exibido na página, ele é como o conteúdo que é exibido na página, ele é como o conteúdo que é exibido na página")
t("Os verbos HTTP são ações que o cliente faz e fazem parte desse acordo de comunicação entre o servidor e o cliente")
t("Os códigos de status HTTP são códigos que o servidor envia para o cliente para informar o status da requisição, ele informa se a requisição foi bem sucedida, se houve um erro, ou se é necessário fazer uma ação adicional")
t("Os códigos de status HTTP são divididos em 5 classes, 1xx, 2xx, 3xx, 4xx e 5xx, cada uma delas tem um significado específico e deve ser usado em um contexto específico")
t("Os retornos 1xx são códigos informativos, eles informam que a requisição foi recebida e está sendo processada")
t("Os retornos 2xx são códigos de sucesso, eles informam que a requisição foi bem sucedida")
t("Os retornos 3xx são códigos de redirecionamento, eles informam que é necessário fazer uma ação adicional")
t("Os retornos 4xx são códigos de erro do cliente, eles informam que houve um erro na requisição")
t("Os retornos 5xx são códigos de erro do servidor, eles informam que houve um erro no servidor")
t("Agora que você entendeu tudo isso, podemos falar sobre o chat, vamos lá?")
s(f"Vamos lá {c.Teacher()}, estou pronto para aprender mais sobre o chat!")
t("Ótimo, vamos lá, agora que você entendeu tudo isso, podemos falar sobre o chat, vamos lá?")
q("Tinha até esquecido do chat, vamos lá {c.Teacher()}, estou pronto para aprender mais sobre o chat... foi você que fez esse chat aí que vamos usar?")
t("Foi sim! até subi no github.com em https://github.com/RafaelFino/chat-doenca, dá uma olhada lá se quiser, mas vamos explicar aqui direitinho como ele funciona, vamos lá?")
s(f"Vamos lá {c.Teacher()}, sei que não vou entender quase nada, mas vou tentar!")
t("Vai sim, é pesado mas você é capaz! Primeiro: qual problema queremos resolver? O que esse chat precisa fazer? Você sabe?")
s(f"Então {c.Teacher()}, Deixa eu ver se entendi: o chat precisa enviar mensagens de um lado para o outro, certo? Tipo enviar mensagens de um cliente para o servidor e também conseguir perguntar se existem novas mensagens")
s("E ele deve fazer isso fazendo chamadas HTTP, e pelo o que você me contou, um POST para enviar mensagens e um GET para buscar mensagens, certo?")
t("Isso mesmo, o chat precisa enviar mensagens de um lado para o outro, ele precisa fazer chamadas HTTP para enviar mensagens e buscar mensagens, ele precisa fazer um POST para enviar mensagens e um GET para buscar mensagens")
t("Logo, o chat precisa de alguma forma guardar as mensagens que foram enviadas para que possam ser buscadas depois, certo? Para isso o server dá um ID para cada mensagem que ele recebe, e guarda essa mensagem com esse ID")
s(f"Entendi {c.Teacher()}, então o chat precisa de alguma maneira armazenar esses dados e guardar as mensagens que foram enviadas, e ele precisa de um ID para cada mensagem que ele recebe, e ele precisa guardar essa mensagem com esse ID")
t("Você está certo, em um servidor de verdade, isso ficaria em algum tipo de banco de dados, mas nesse exemplo simples que criamos, essas mensagens vão ficar apenas na memória do servidor, e o ID é um número sequencial que vai aumentando a cada nova mensagem, mas caso o servidor seja reiniciado, ele perde todas as mensagens. É apenas um servidor bem simples para o nosso exercício")
q(f"Entendi {c.Teacher()}, então em um servidor de verdade, essas mensagens ficariam em um banco de dados, mas nesse exemplo simples que criamos, essas mensagens vão ficar apenas na memória do servidor, e o ID é um número sequencial que vai aumentando a cada nova mensagem, mas caso o servidor seja reiniciado, ele perde todas as mensagens, é isso?")
t("Isso mesmo, você entendeu direitinho! Agora, vamos falar sobre o que o chat precisa fazer, vamos lá?")
t("Antes de continuar, preciso te contar sobre um outro concenito importante no HTTP, as rotas! Você sabe o que são rotas?")
s(f"Rotas? O que são rotas {c.Teacher()}? Tem aquela polícia que fica parando a gente na estrada? Ou em SP, que bate em pobre?")
t("Não, nesse caso não é isso... rotas no HTTP são caminhos que você define para acessar os recursos do seu servidor, por exemplo, você pode definir uma rota para acessar as mensagens do chat, uma rota para enviar mensagens, uma rota para buscar mensagens, etc.")
s(f"Entendi {c.Teacher()}, então rotas no HTTP são caminhos que você define para acessar os recursos do seu servidor, por exemplo, você pode definir uma rota para acessar as mensagens do chat, uma rota para enviar mensagens, uma rota para buscar mensagens, etc.")
t("São complementos dos endereços, por exemplo, nosso servidor de chat tem o endereço http://192.168.1.9:8080, e as rotas são os caminhos que você define para acessar os recursos desse servidor, por exemplo, http://192.168.1.9:8080/message e essa rota aceita dois métodos, o GET para buscar mensagens e o POST para enviar mensagens")
t("No caso do GET, você ainda precisa passar o ID da última mensagem que você recebeu, para que o servidor saiba a partir de qual mensagem ele deve te enviar as novas mensagens, por exemplo, http://192.168.1.9:8080/message/10 -> Essa rota vai te retornar todas as mensagens a partir do ID 10 até a ultima mensagem")
s(f"Entendi {c.Teacher()}, então as rotas são complementos dos endereços, acho q estou entendendo, mas você poderia me mostrar como é o código desse server?")
t("Claro, vou te mostrar o código do server, vamos lá!")
t("Esse é o código do server:")
code("""
from flask import Flask, request
from loguru import logger
import logging
import datetime
import json

class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())

app = Flask(__name__)
app.logger.addHandler(InterceptHandler())

class Message:
    def __init__(self, id: int, sender: str, text: str):
        self.id = id
        self.when = datetime.datetime.now().isoformat()
        self.sender = sender
        self.text = text

    def ToStr(self):
        return f'[{self.id:06}] {self.when} {self.sender} -> {self.text}'

    def ToJson(self):
        return {
            'id': self.id,
            'when': self.when,
            'sender': self.sender,
            'text': self.text
        }

messages = []

@app.route('/')
def index():
    return 'Chat Doenca API'

@app.route('/message', methods=['POST'])
def post_message():
    try:
        sender = request.form.get('sender')
        text = request.form.get('text')

        if sender is None or len(sender) == 0:
            logger.error("Sender is empty")
            return {
                "error": "Empty sender",
                "timestamp": datetime.datetime.now().isoformat()
            }, 400

        if text is None or len(text) == 0:
            logger.error("Text is empty")
            return {
                "error": "Empty text",
                "timestamp": datetime.datetime.now().isoformat()
            }, 400

        message = Message(len(messages), sender, text)
        messages.append(message)

        logger.info(f'Received message: {message.ToStr()}')

        return {
            "id": message.id,
            "timestamp": datetime.datetime.now().isoformat()
            }, 201
    except Exception as e:
        logger.error(f'Error processing message: {e}')
        return {
            "error": str(e),
            "timestamp": datetime.datetime.now().isoformat()
            }, 500

@app.route('/message/<last>', methods=['GET'])
def get_messages(last: int = 0):
    try:
        ret = []
        if not last.isdigit():
            return {
                "error": "Invalid message index",
                "timestamp": datetime.datetime.now().isoformat()
            }, 400
        last = int(last)
        if last < 0:
            last = 0

        if last >= len(messages):
            return {
                "messages": ret,
                "timestamp": datetime.datetime.now().isoformat()
                }, 200

        for m in messages[last+1:]:
            ret.append(m.ToJson())

        logger.info(f"Returning {len(ret)} messages messages from {last}: {ret}")
        return {
            "messages": ret,
            "timestamp": datetime.datetime.now().isoformat()
            }, 200
    except Exception as e:
        logger.error(f'Error processing message: {e}')
        return {
            "error": str(e),
            "timestamp": datetime.datetime.now().isoformat()
            }, 500

def start_app():
    logger.info('Starting Chat Doenca API')
    from waitress import serve
    serve(app, host="192.168.1.9", port=8080)
    logger.info('Exiting Chat Doenca API')

""")
s(f"PORRA {c.Teacher()}! é MUITA coisa, não entendi nada...")
t("Calma, vou te explicar o que esse código faz, vamos lá!")
t("Primeiro, quem faz a parte de lidar com o HTTP é o Flask, que é um framework web para Python, ele é quem vai lidar com as requisições HTTP que chegam no servidor e vai chamar as funções que você definiu para cada rota")
t("O Flask é quem vai chamar as funções que você definiu para cada rota, por exemplo, a função post_message() é chamada quando você faz uma requisição POST para a rota /message, e a função get_messages() é chamada quando você faz uma requisição GET para a rota /message/<last>")
t("Também usamos um cara chamdo loguru para fazer os logs, ele é um logger bem legal que permite fazer logs de forma mais fácil e bonita")
t("Olha como são as chamadas do código que importam essas bibliotecas:")
code("""
from flask import Flask, request
from loguru import logger
import logging
import datetime
import json
""")
s("Acho que essa parte nem tem muito o que explicar, né?")
t("Sim, são só os módulos que usamos. Temos também a parte que adiciona um handler para o logger, esse handler é responsável por interceptar os logs que são gerados pelo Flask e redirecioná-los para o loguru, que é o logger que estamos usando")
code("""
class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())
     
app = Flask(__name__)
app.logger.addHandler(InterceptHandler())     
""")
s("Até aqui tudo bem, não sei se conseguiria fazer isso, mas entendi o que está acontecendo")
t("Depois disso, nós defimos o que é uma mensagem para esse servidor, olha esse cara aqui:")
code("""
class Message:
    def __init__(self, id: int, sender: str, text: str):
        self.id = id
        self.when = datetime.datetime.now().isoformat()
        self.sender = sender
        self.text = text

    def ToStr(self):
        return f'[{self.id:06}] {self.when} {self.sender} -> {self.text}'
    
    def ToJson(self):
        return {
            'id': self.id,
            'when': self.when,
            'sender': self.sender,
            'text': self.text
        }
""")
s("Agora tá ficando mais tenso... o que é isso?")
t("Esse é o modelo de uma mensagem, ele é responsável por representar uma mensagem que é enviada para o servidor, ele tem um ID, que é o identificador da mensagem, um remetente, que é quem enviou a mensagem, um texto, que é o conteúdo da mensagem, e uma data, que é a data e hora que a mensagem foi enviada")
t("Além disso, ele tem dois métodos, o ToStr() que retorna a mensagem em formato de string, e o ToJson() que retorna a mensagem em formato JSON")
q(f"JSON? O que é isso {c.Teacher()}? É tipo aquele cara do filme de terror que anda devagar e mata todo mundo q tá na frente dele?")
t("Não, JSON é um formato de dados que é muito usado na web, ele é um formato de dados que é fácil de ler e escrever para humanos e fácil de gerar e interpretar para máquinas, ele é muito usado para enviar dados entre o servidor e o cliente")
t("O JSON é um formato de dados que é muito usado na web, ele é um formato de dados que é fácil de ler e escrever para humanos e fácil de gerar e interpretar para máquinas, ele é muito usado para enviar dados entre o servidor e o cliente")
s(f"Entendi {c.Teacher()}, JSON é um formato de dados que é muito usado na web, ele é um formato de dados que é fácil de ler e escrever para humanos e fácil de gerar e interpretar para máquinas, ele é muito usado para enviar dados entre o servidor e o cliente, consegue me dar alguns exemplos disso por favor?")
t("Claro, vou te mostrar um exemplo de uma mensagem em formato JSON, vamos usar o nosso modelo de mensagem:")
code("""
import datetime
import json
    
class Message:
    def __init__(self, id: int, sender: str, text: str):
        self.id = id
        self.when = datetime.datetime.now().isoformat()
        self.sender = sender
        self.text = text

    def ToStr(self) -> str:
        return f'[{self.id:06}] {self.when} {self.sender} -> {self.text}'
    def ToJson(self) -> str:
        return {
            'id': self.id,
            'when': self.when,
            'sender': self.sender,
            'text': self.text
        }

# cria uma mensagem
message = Message(1, 'Fulano', 'Ola pessoal, essa eh a minha mensagem de exemplo de como fica um json!')
# imprime uma mensagem no formato Json
print(json.dumps(message.ToJson(), indent=4)) 
""", )
t("Esse é o resultado:")
c.ShowCode("""
{
    "id": 1,
    "when": "2021-09-01T15:00:00.000000",
    "sender": "Fulano",
    "text": "Ola pessoal, essae eh a minha mensagem de exemplo de como fica um json!"
}
""", lexer="json")
t("A função post_message() é responsável por receber as mensagens que são enviadas para o servidor, ela recebe o remetente e o texto da mensagem, cria um objeto Message com esses dados e adiciona esse objeto na lista de mensagens")
t("Veja o código dessa parte")
code("""
@app.route('/message', methods=['POST'])
def post_message():
    try:
        sender = request.form.get('sender')
        text = request.form.get('text')

        if sender is None or len(sender) == 0:
            logger.error("Sender is empty")
            return {
                "error": "Empty sender",
                "timestamp": datetime.datetime.now().isoformat()
            }, 400

        if text is None or len(text) == 0:
            logger.error("Text is empty")
            return {
                "error": "Empty text",
                "timestamp": datetime.datetime.now().isoformat()
            }, 400

        message = Message(len(messages), sender, text)
        messages.append(message)

        logger.info(f'Received message: {message.ToStr()}')

        return { 
            "id": message.id,
            "timestamp": datetime.datetime.now().isoformat()
            }, 201
    except Exception as e:
        logger.error(f'Error processing message: {e}')
        return { 
            "error": str(e),
            "timestamp": datetime.datetime.now().isoformat()
            }, 500
""")

t("As mensagens ficam todas em uma lista chamada messages, e cada mensagem tem um ID sequencial, que é o índice dela na lista, olha:")
code("""
messages = []
""")
t("A função get_messages() é responsável por retornar as mensagens que estão armazenadas no servidor, ela recebe o ID da última mensagem que foi recebida pelo cliente e retorna todas as mensagens a partir desse ID, dá uma olhada no código:")
code("""
@app.route('/message/<last>', methods=['GET'])
def get_messages(last: int = 0):
    try:
        ret = []
        if not last.isdigit():
            return {
                "error": "Invalid message index",
                "timestamp": datetime.datetime.now().isoformat()
            }, 400
        last = int(last)
        if last < 0:
            last = 0

        if last >= len(messages):
            return {
                "messages": ret,
                "timestamp": datetime.datetime.now().isoformat()
                }, 200

        for m in messages[last+1:]:
            ret.append(m.ToJson())

        logger.info(f"Returning {len(ret)} messages messages from {last}: {ret}")
        return {
            "messages": ret,
            "timestamp": datetime.datetime.now().isoformat()
            }, 200
    except Exception as e:
        logger.error(f'Error processing message: {e}')
        return {
            "error": str(e),
            "timestamp": datetime.datetime.now().isoformat()
            }, 500
""")
t("O servidor também tem uma rota / que retorna uma mensagem simples, apenas para mostrar que o servidor está funcionando")
t("O servidor também tem uma rota / que retorna uma mensagem simples, apenas para mostrar que o servidor está funcionando, é como um 'olá mundo' do servidor, mas mais legal, olha:")
code("""
@app.route('/')
def index():
    return 'Chat Doenca API'
""")
t("E por fim, temos a função start_app() que é responsável por iniciar o servidor, ela usa o Waitress para servir a aplicação, olha:")
code("""
def start_app():
    logger.info('Starting Chat Doenca API')
    from waitress import serve
    serve(app, host="192.168.1.9", port=8080)    
    logger.info('Exiting Chat Doenca API')
""")     
s("Entendi {c.Teacher()}, acho que agora eu entendi melhor como funciona o servidor, mas ainda é muita coisa para mim, acho que vou precisar de mais tempo para entender tudo isso")
t("Não tem problema, é muita informação mesmo, mas com o tempo você vai pegando o jeito, e se precisar de ajuda, pode contar comigo! Vou te pentelhar até você entender tudo!")
s("Obrigado {c.Teacher()}, e como seria o client disso aí???")
t("O client é bem simples, ele é um programa que faz requisições HTTP para o servidor para enviar e buscar mensagens, ele pode ser feito em qualquer linguagem de programação que suporte requisições HTTP, como Python, JavaScript, Java, etc.")
s("Você me ajuda a fazer um client em Python para esse server por favor, acho que ainda não consigo sozinho?")
t("Claro, vou te ajudar a fazer um client em Python, vamos lá!")
t("Esse é o código do client:")
code("""
import requests
import json
import threading
import time

server_url = "http://192.168.1.9:8080"

def post_message(sender: str, text: str) -> int:
    url = f"{server_url}/message"
    data = {
        'sender': sender,
        'text': text
    }

    response = requests.post(url, data=data)
    if response.status_code != 201:
        print('Failed to send message')
        print(response.json())

class receiver(threading.Thread):
    def set_sender(self, sender: str):
        self.sender = sender

    def get_messages(self):
        url = f"{server_url}/message/{self.last}"
        response = requests.get(url)
        if response.status_code != 200:
            print('Failed to get messages')
            print(response.json())
        else:
            messages = response.json()['messages']
            for message in messages:
                id = int(message['id'])
                if id >= self.last:
                    print(f">> [{message['when']}] {message['sender']}: {message['text']}")
                    self.last = int(message['id'])

    def run(self, *args, **kwargs):
        self.last = 0
        #Loop para receber mensagens
        while True:
            self.get_messages()
            time.sleep(5)

sender = input('>> Digite seu nome: ')

rcv = receiver()
rcv.set_sender(sender)
rcv.start()
time.sleep(1)

#Loop para envio de mensagens
while True:
    text = input('\n$> ')
    post_message(sender, text)
    rcv.get_messages()
""")
s("Esse código é um pouco mais complexo, você acha que eu vou entender isso aí sozinho?")
t("Não se preocupe, vou te explicar o que esse código faz, vamos lá!")
t("Esse código é um client para o servidor que criamos, ele é responsável por enviar e buscar mensagens do servidor, ele tem duas funções principais, a post_message() que é responsável por enviar mensagens para o servidor e a receiver() que é responsável por buscar mensagens do servidor")
t("A função post_message() recebe o remetente e o texto da mensagem, cria um objeto com esses dados e envia esse objeto para o servidor usando uma requisição POST, olha o código:")
code("""
def post_message(sender: str, text: str) -> int:
    url = f"{server_url}/message"
    data = {
        'sender': sender,
        'text': text
    }

    response = requests.post(url, data=data)
    if response.status_code != 201:
        print('Failed to send message')
        print(response.json())
""")
t("A função receiver() é uma thread que fica rodando em background e busca as mensagens do servidor a cada 5 segundos, ela faz uma requisição GET para o servidor para buscar as mensagens, olha o código:")
code("""
class receiver(threading.Thread):
    def set_sender(self, sender: str):
        self.sender = sender

    def get_messages(self):
        url = f"{server_url}/message/{self.last}"
        response = requests.get(url)
        if response.status_code != 200:
            print('Failed to get messages')
            print(response.json())
        else:
            messages = response.json()['messages']
            for message in messages:
                id = int(message['id'])
                if id >= self.last:
                    print(f">> [{message['when']}] {message['sender']}: {message['text']}")
                    self.last = int(message['id'])

    def run(self, *args, **kwargs):
        self.last = 0
        #Loop para receber mensagens
        while True:
            self.get_messages()
            time.sleep(5)
""")
t("Agora que você entendeu o que esse código faz, vamos rodar ele para ver como ele funciona, vamos lá?")
s(f"Vamos lá {c.Teacher()}, estou pronto para rodar o client!")
t("Ótimo, vamos rodar o client, mas antes, você precisa entrar na sua VM para ter acesso ao server e instalar todos as dependencias necessárias, você sabe como fazer isso?")
s(f"Não sei {c.Teacher()}, você pode me ajudar?")
t("Claro, vou te ajudar a fazer isso, vamos lá!")
t("Primeiro, você precisa entrar na sua VM, você pode fazer isso usando o comando ssh, olha:")
cmd("ssh -oPort=<SUA-PORTA> -i ~/.ssh/id_ed25519  dev@learnops.duckldns.org")
t("Depois que você entrar na sua VM, você precisa instalar o Python e as dependências do client, você pode fazer isso usando o comando apt-get ou o pip, se não souber fazer isso, recomendo fortemente que faça a aulas de python aqui no nosso bot")
t("Depois que você instalar o Python e as dependências do client, você pode rodar o client usando o comando python3 client.py, mas essa parte é com vc!")
s(f"Entendi {c.Teacher()}, vou fazer isso agora, obrigado pela ajuda!")
t("De nada, qualquer coisa estou por aqui! Até mais!")
q(f"Vai dar uma canseira fazer esse... mas vamos lá, obrigado pela ajuda {c.Teacher()}, até mais!")