
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
# Os alunos devem ser chamados de "padawans", "Pobres", "Padawans", "Pequenos Gafanhotos", "Jovem Tartarugas" e outros jargões da cultura pop para se referir a aprendizes.
# O professor deve ser ironico para brincar com os alunos, mas sempre de forma respeitosa e descontraída.
# Os alunos devem se comportar como aprendizes, curiosos e com vontade de aprender, mas sem muito conhecimento sobre o tema, sempre questionando sobre explicações mais formais e pedindo exemplosp práticos.
# Sempre que o aluno tentar se referir ao professor, ele deve usar o método c.Teacher() para se referir ao professor, nunca diretamente. Dessa forma o nome do professor irá aparecer na tela do aluno. Nessas linhas a string sempre deve ser formatada com o nome do professor usando o 'f' antes das aspas.
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

# Tema: Um exercício prático para criar uma aplicação em python, cliente de uma aplicação server de um chat feito para eles, esse será a versão 3 desse chat, onde o aluno irá aprender a criar um cliente para se comunicar com o servidor do chat.
# Objetivo: Ensinar o aluno a criar um cliente para se comunicar com o servidor de um chat, utilizando o protocolo HTTP e o formato JSON para enviar e receber mensagens.
# O aluno irá aprender a fazer requisições HTTP para o servidor do chat, enviar mensagens e receber mensagens do servidor. Levando em conta que o aluno já implementou as versões 1 e 2 do servidor e do client de chat.
# vamos falar rapidamente sobre as 3 versões criadas até agora:
# A versão 1:
# É um chat simples, onde o aluno aprendeu a criar um servidor de chat e um cliente para se comunicar com o servidor. O server não tinha persistência de mensagens, ou seja, as mensagens eram perdidas quando o servidor era reiniciado.
# Haviam apenas 2 métodos:
# - POST /message/ para enviar mensagens, passando no corpo da requisição o texto da mensagem e o nome do usuário. Essa API retorna o id da mensagem enviada e um código de status 201 -> Created.
# - GET /message/<last> para receber mensagens, onde <last> é o id da última mensagem recebida. Essa API retorna um array de mensagens e um código de status 200 -> OK. O formato das mensagens é um objeto com o id, o texto da mensagem e o nome do usuário:
# {
#   "messages": [
#     {
#       'id': 1,
#       'when': '2021-09-01T12:00:00',
#       'sender': 'user1',
#       'text': 'Hello World!'
#     },
#     {
#       'id': 2,
#       'when': '2021-09-01T12:00:01',
#       'sender': 'user2',
#       'text': 'Hi!'
#     }
#   ],
#   "timestamp": "2021-09-01T12:00:02"
# }, 200

# A versão 2:
# Nessa versão, foi implementado um banco de dados SQLITE3 para persistir as mensagens, ou seja, as mensagens não são perdidas quando o servidor é reiniciado. Também foi implementado uma mudança para buscar as mensagens, no lugar de ir no path o last, agora ele é um query parameter, ou seja, ele é passado na URL como um parâmetro de query.
# As APIs são as mesmas da versão 1, mas com a mudança do last para um query parameter:
# - POST /message/ para enviar mensagens, passando no corpo da requisição o texto da mensagem e o nome do usuário. Essa API retorna o id da mensagem enviada e um código de status 201 -> Created.
# - GET /message/?last=<last> para receber mensagens, onde <last> é o id da última mensagem recebida. Essa API retorna um array de mensagens e um código de status 200 -> OK. O formato das mensagens é um objeto com o id, o texto da mensagem e o nome do usuário:
# Os formatos de resposta se mantem o mesmos da versão 1.

# A versão 3:
# Nessa versão, foi implementado um sistema de autenticação para os usuários, onde o usuário precisa se autenticar para enviar e receber mensagens. O usuário se autentica passando um id e uma senha, e recebe um token de autenticação, que deve ser passado no header de todas as requisições para enviar e receber mensagens.
# As APIs são as mesmas da versão 2, mas com a adição de uma API de autenticação e a necessidade de passar o token de autenticação no header de todas as requisições e uma API para a criação de usuário:
# - POST /user/ para criar um usuário, passando no corpo da requisição o nome do usuário e a senha. Essa API retorna um código de status 201 -> Created. Formato do Post:
# {
#   "name": "user1",
#   "password": "123456"
# }
# O retorno desse post é um código de status 201 -> Created com o seguinte formato:
# {
#   "id": "<id>"
# }

# - POST /auth/<id> para autenticar um usuário, passando no corpo da requisição a senha do usuário. Essa API retorna um token de autenticação e um código de status 200 -> OK. Formato do Post:
# {
#   "password": "123456"
# }
# e o retorno desse post tem o seguinte formato:
# {
#   "token": "<TOKEN>"
# }
# Esse token deve ser enviado no header de todas as chamadas para enviar e receber mensagens usando o header "Authorization" com o valor.
# - DELETE /auth/<id> para deslogar um usuário, passando no header da requisição o token de autenticação. Essa API retorna um código de status 200 -> OK.
# Para o envio de mensagens, o usuário deve passar o token de autenticação no header da requisição, com a chave "Authorization" e o valor do token e não é mais ncessário passar o id do usuário no corpo da requisição, pois o token já resolve isso.
# Para o recebimento de mensagens, o usuário deve passar o token de autenticação no header da requisição, com a chave "Authorization" e o valor do token e o last como um query parameter na URL.


swagger = """
{
  "swagger": "2.0",
  "basePath": "/v3",
  "paths": {
    "/auth/{id}": {
      "parameters": [
        {
          "name": "id",
          "in": "path",
          "required": true,
          "type": "string"
        }
      ],
      "post": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "post_auth_controller",
        "parameters": [
          {
            "name": "payload",
            "required": true,
            "in": "body",
            "schema": {
              "$ref": "#/definitions/AuthModel"
            }
          }
        ],
        "tags": [
          "Auth"
        ]
      },
      "delete": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "delete_auth_controller",
        "parameters": [
          {
            "in": "header",
            "description": "Authorization token",
            "name": "Authorization",
            "type": "string"
          }
        ],
        "tags": [
          "Auth"
        ]
      }
    },
    "/message/": {
      "get": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "get_message_controller",
        "parameters": [
          {
            "required": false,
            "in": "query",
            "description": "Last message id",
            "name": "last",
            "type": "string"
          },
          {
            "in": "header",
            "description": "Authorization token",
            "name": "Authorization",
            "type": "string"
          }
        ],
        "tags": [
          "Message"
        ]
      },
      "post": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "post_message_controller",
        "parameters": [
          {
            "name": "payload",
            "required": true,
            "in": "body",
            "schema": {
              "$ref": "#/definitions/MessageModel"
            }
          },
          {
            "in": "header",
            "description": "Authorization token",
            "name": "Authorization",
            "type": "string"
          }
        ],
        "tags": [
          "Message"
        ]
      }
    },
    "/user/": {
      "get": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "get_user_controller",
        "parameters": [
          {
            "in": "header",
            "description": "Authorization token",
            "name": "Authorization",
            "type": "string"
          }
        ],
        "tags": [
          "User"
        ]
      },
      "post": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "post_user_controller",
        "parameters": [
          {
            "name": "payload",
            "required": true,
            "in": "body",
            "schema": {
              "$ref": "#/definitions/UserModel"
            }
          }
        ],
        "tags": [
          "User"
        ]
      }
    },
    "/user/{id}": {
      "parameters": [
        {
          "in": "header",
          "description": "Authorization token",
          "name": "Authorization",
          "type": "string"
        },
        {
          "name": "id",
          "in": "path",
          "required": true,
          "type": "string"
        }
      ],
      "get": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "get_user_id_controller",
        "tags": [
          "User"
        ]
      },
      "put": {
        "responses": {
          "200": {
            "description": "Success"
          }
        },
        "operationId": "put_user_id_controller",
        "parameters": [
          {
            "name": "payload",
            "required": true,
            "in": "body",
            "schema": {
              "$ref": "#/definitions/UpdateModel"
            }
          }
        ],
        "tags": [
          "User"
        ]
      }
    }
  },
  "info": {
    "title": "Chat-Doenca V3",
    "version": "3.0",
    "description": "Chat-Doenca API"
  },
  "produces": [
    "application/json"
  ],
  "consumes": [
    "application/json"
  ],
  "tags": [
    {
      "name": "User",
      "description": "User related operations"
    },
    {
      "name": "Auth",
      "description": "Auth related operations"
    },
    {
      "name": "Message",
      "description": "Message related operations"
    }
  ],
  "definitions": {
    "UserModel": {
      "properties": {
        "name": {
          "type": "string"
        },
        "password": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "UpdateModel": {
      "properties": {
        "enable": {
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "AuthModel": {
      "properties": {
        "password": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "MessageModel": {
      "properties": {
        "text": {
          "type": "string"
        }
      },
      "type": "object"
    }
  },
  "responses": {
    "ParseError": {
      "description": "When a mask can't be parsed"
    },
    "MaskError": {
      "description": "When any error occurs on mask"
    }
  },
  "host": "http://learnops.duckdns.org:7111/"
}
"""

t("Olá padawan, hoje vamos falar sobre a versão 3 do nosso chat, onde vamos implementar um sistema de autenticação para os usuários, agora sim parece uma API de verdade, não é mesmo?")
s(f"Legal, {c.Teacher()}! Mas como funciona esse sistema de autenticação?")
t("Bom, para começar, vamos falar sobre as APIs que vamos implementar nessa versão.")
t("Vamos começar com a API de criação de usuário.")
s("Vixi... antes eu só mandava o tal de 'sender' e 'text' e agora tem 'name' e 'password'... tá ficando complicado, hein?")
t("Calma, padawan! Vou te explicar como funciona.")
t("Primeiro vamos ter que criar um usuário... antes era só mandar qlqr coisa que funcionava, agora a coisa está ficando mais profissional, temos várias APIs para criar, autenticar e deslogar usuários.")
t("pegue um papel e anote isso, é importante...")
s("Oi?")
t("Tá dormindo padawan? se liga nisso, pq EU SEI Q VCS VÃO VACILAR AQUI:")
t(" #### Informação importante, anote isso #### ")
t("QUANDO CRIAREM UM USUÁRIO, APENAS UM USUÁRIO JÁ AUTENTICADO SERÁ CAPAZ DE AUTORIZAR UM NOVO USUÁRIO, LOGO, VCS PRECISAM ME AVISAR QUE CRIARAM UM USUÁRIO!!!!")
t("Vamos começar com a API de criação de usuário.")
code("""
POST /user/
{
  "name": "user1",
  "password": "123456"
}
""")
t("Essa API é bem simples, você só precisa passar o nome do usuário e a senha.")
t("Essa API retorna o id do usuário criado.")
s(f"Acho que entendi {c.Teacher()}! Agora o usuário precisa se autenticar para enviar e receber mensagens, certo? Mas como vem esse id dele aí q vc falou?")
t("O id do usuário é gerado automaticamente pelo servidor quando o usuário é criado.")
t("Ele vem em um json na resposta do seu post, caso ele tenha funcionado, o código HTTP de retorno é 201 -> Created.")
t("Olha só como é o json de retorno desse método:")
code("""
{
  "id": "<id>"
}
""")
s(f"Entendi, {c.Teacher()}! E como o usuário se autentica?")
t("Para se autenticar, o usuário precisa passar o id do usuário e a senha. Então é importante vc guardar seu id e senha em um lugar seguro... ou pelo menos se lembrar dele, caso contrário não será possível se logar.")
t("Vamos ver como é a API de autenticação:")
code("""
POST /auth/<id>
{
  "password": "123456"
}
""")
t("Essa API retorna um token de autenticação se der certo e com um código HTTP de retorno 200 -> OK.")
t("Esse token é um código que você deve passar no header de todas as requisições para enviar e receber mensagens.")
t("Olha só como é o json de retorno desse método:")
code("""
{
    "token": "<TOKEN>"
}
""")
s(f"Entendi, {c.Teacher()}! Que legal isso aí!! mas pera... e quando eu tiver esse token, eu uso ele onde?")
t("Você deve passar o token no header de todas as requisições para enviar e receber mensagens.")
s(f"Header??? Mas {c.Teacher()}, o que é isso?")
t("O header é uma parte da requisição HTTP onde você pode passar informações adicionais. Mas pow aspira... a essa altura do campeonato você já deveria saber o que é um header, né?")
s(f"Pow {c.Teacher()}, tava na correria, tá dificil de estudar, mas eu vou me esforçar mais, prometo! Mas me explica o que é um header, por favor.")
t("Mas tudo bem, vou te explicar.")
t("O header é uma parte da requisição HTTP onde você pode passar informações adicionais. Pensa que cada requisição HTTP é como uma carta que você envia para o servidor.")
t("O header é como o envelope da carta, onde você coloca informações adicionais, como o token de autenticação. Eles ficam do lado de fora dessa carta e podem ser lidos sem precisar abrir a carta. É uma prática muito comum em APIs RESTful.")
t("Vamos ver como você deve passar o token no header de uma requisição, veja por exemplo como faremos para enviar uma mensagem com o header de autenticação:")
code("""
POST /message/
{
  "text": "Hello World
}
     
Authorization <TOKEN>
""")
s("Isso aí ainda não me diz muita coisa... se for no python, como que eu faço isso?")
t("No python, você pode passar o token no header da requisição assim:")
code("""
import requests
     
url = 'http://learnops.duckdns.org:7111/message/'
headers = {
    'Authorization': '<TOKEN>'
}
data = {
    'text': 'Hello World'
}
     
response = requests.post(url, headers=headers, json=data)
     
print(response.json())
""")
t("E é isso aí, padawan! Com isso você já pode enviar mensagens para o servidor. Não é dificil vai?")
s(f"Acho que entendi, {c.Teacher()}! Mas e para receber mensagens?")
t("Para receber mensagens é a mesma coisa, você deve passar o token no header da requisição. Acorda aí jovem tartaruga!")
t("Vamos ver como você deve passar o token no header de uma requisição para receber mensagens, veja por exemplo como faremos para receber mensagens com o header de autenticação:")
code("""
GET /message/?last=<last>
     
Authorization <TOKEN>
""")
s(f"Entendi, {c.Teacher()}! E no python, como eu faço?")
t("No python, você pode passar o token no header da requisição assim:")
code("""
import requests
     
url = 'http://learnops.duckdns.org:7111/message/?last=1'
headers = {
    'Authorization': '<TOKEN>'
}

response = requests.get(url, headers=headers)
     
print(response.json())
""")
t("E é isso aí, padawan! Com isso você já pode receber mensagens do servidor. E vc aí batendo cabeça... não é dificil vai? Logo vai piorar...")
s(f"Deus me livre, a cada dia eu me sinto mais burro... mas acho que entendi, {c.Teacher()}! Mas e se eu quiser deslogar?")
t("Para deslogar, você deve passar o token no header da requisição.")
t("Vamos ver como você deve passar o token no header de uma requisição para deslogar, veja por exemplo como faremos para deslogar com o header de autenticação:")
code("""
DELETE /auth/<id>
     
Authorization <TOKEN>
     
""")
s(f"Entendi, {c.Teacher()}! E no python, como eu faço?")
t("No python, você pode passar o token no header da requisição assim:")
code("""
import requests
     
url = 'http://learnops.duckdns.org:7111/auth/1'
headers = {
    'Authorization': '<TOKEN>'
}
     
response = requests.delete(url, headers=headers)
     
print(response.json())
""")

t("E é isso aí, padawan! Com isso você já pode deslogar do servidor. Tranquilo né?")
s(f"Mas {c.Teacher()}, e se eu não deslogar, o que esse nosso server faz? o token dura para sempre?")
t("O token tem um tempo de vida, ele expira depois de um tempo. Aqui no nosso servidor, o token expira depois de 5 minutos de inatividade.")
s("Inatividade?")
t("Isso mesmo, padawan! Se você ficar 5 minutos sem enviar ou receber mensagens, o token expira e você precisa se autenticar novamente. Caso contrário, você não poderá enviar ou receber mensagens.")
s(f"Entendi, {c.Teacher()}! Acho que já consigo fazer um client em python aqui... você poderia por favor me mostrar, usando um 'curl' como eu poderia fazer todos os processos? desde criar um usuário, autenticar, mandar e receber mensagens por favor?")
t("Claro, padawan! Vou te mostrar como você pode fazer isso usando o curl.")
t("Vamos começar criando um usuário:")
cmd(
    "curl -X POST -sS -H 'Content-Type: application/json' -d '{\"name\": \"user1\", \"password\": \"123456\"}' http://learnops.duckdns.org:7111/user/")
t("Agora vamos autenticar o usuário:")
cmd(
    "curl -X POST -sS -H 'Content-Type: application/json' -d '{\"password\": \"123456\"}' http://learnops.duckdns.org:7111/auth/1")
t("você irá ver no retorno o token de autenticação. Vamos usar ele nos próximos comandos, olha só:")
cmd(
    "curl -X POST -sS -H 'Content-Type: application/json' -d '{\"text\": \"Hello World\"}' -H \"Authorization: <TOKEN>\" http://learnops.duckdns.org:7111/message/")
t("E para receber mensagens, a partir da mensagem de id=1:")
cmd("curl -X GET -sS -H \"Authorization: <TOKEN>\" http://learnops.duckdns.org:7111/message/?last=1")
t("E para deslogar:")
cmd("curl -X DELETE -sS -H \"Authorization: <TOKEN>\" http://learnops.duckdns.org:7111/auth/1")
t("E é isso aí, padawan! Com isso você já pode criar um cliente para se comunicar com o servidor do chat.")
s(f"Entendi, {c.Teacher()}! Acho que consigo fazer isso... mas e se eu quiser saber mais sobre as APIs?")
t("Você pode acessar a documentação da API para saber mais sobre as APIs. No caminho http://learnops.duckdns.org:7111/ você encontra a documentação da API.")
s("E você teriam mais alguns materiais para estudar mais APIs?")
t("Você pode acessar o site da Swagger para saber mais sobre APIs RESTful. Eu também criei um material para um curso de pós graduação que pode ajudar bastante, ele está no meu repositório: https://github.com/RafaelFino/learnops-api-python")
s(f"Entendi, {c.Teacher()}! Muito obrigado por me ensinar sobre APIs RESTful! Acho que agora consigo fazer um client para o nosso chat!")
c.LastStep()
