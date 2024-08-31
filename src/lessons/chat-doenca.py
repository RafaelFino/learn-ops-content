
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
# O professor deve ser ironico para brincar com os alunos, mas sempre de forma respeitosa e descontraída.
# Os alunos devem se comportar como aprendizes, curiosos e com vontade de aprender, mas sem muito conhecimento sobre o tema, sempre questionando sobre explicações mais formais e pedindo exemplosp práticos.

def t(m):
    c.Speak(m)

def s(m):
    c.StudentComment(m)

def q(m):
    c.Question(m)

def code(code):
    c.ShowCode(code)

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
