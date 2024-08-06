# learn-ops-content

## Vamos começar?

Olá, eu sou o Fino, escrevi esse projeto para tentar resolver um velho problema: sou um só e as vezes não consigo estar em todos os lugares que gostaria

Parece besta, gosto muito de tentar ajudar com as mentorias, tentando ajudar o pessoal a estudar e etc, mas nem sempre tenho todo o tempo que gostaria para fazer isso da melhor forma. Como então eu poderia melhorar isso e conseguir estar onde preciso para tentar passar alguma coisa?

Bom, temos hoje a IA que tem me ajudado demais a economizar tempo e fazer coisas de uma forma mais eficiente... não preciso dizer que atualmente (escrevo isso em 2024) a IA não faz milagres e não é nenhum Oraculo que sabe tudo, mas com certeza ajuda demais a automatizar tarefas, eu usei algumas alternativas aqui e indexei um monte de conversas com as turmas passadas e pedi para ela gerar conteúdo para uns bots, para simular aulas e eu fiz um programinha em Python que simula a conversa q costumamos ter durante as mentorias. Não ficou assim aquela obra de arte, mas acho que a IA conseguiu pegar bem a ideia de alguns temas e gerar um conteúdo interessante que pode ajudar em uma preparação para os papos com os alunos.

Básicamente todo o código dos bots está dentro da pasta *src/interative*, basta executar os programas python que a magia acontece.

## Mas Fino, eu não faço ideia de como eu posso executar isso! 

Verdade, a maioria de vcs sequer sabe o que é um git ou python é só uma cobra... ou talvez nem isso.. então vamos do começo

## Como pegar esse repositório e começar a brincar

- Primeiro, eu já devo ter dito isso, mas crie uma conta aqui no github.com
- Dados isso, você vai precisar instalar o git aí no seu computador (caso vc ainda não saiba o que é git, tudo bem, vamos falar disso mais para frente)

### No Windows
- Primeiro passo: Instale um *LINUX* 
- Segundo passo: Instale o git

Viu? é fácil... vc consegue!!!

Brincadeira, vamos lá...
- Acesse o site do git e baixe o instalador: https://git-scm.com/
- Execute o instalador e siga os passos
- Abra o terminal (sim, vc vai ter que aprender a usar o terminal, mas não se preocupe, é bem simples)
- Digite `git --version` e veja se o git foi instalado corretamente

Simples... não é?

### No Linux
- Abra o terminal
- Digite `sudo apt-get install git` e siga os passos
- Digite `git --version` e veja se o git foi instalado corretamente

E vcs devem estar se perguntando... tá bom, git? que diabos é isso?
Bom, o git é uma ferramenta de controle de versão, ou seja, ele vai te ajudar a controlar as mudanças que vc faz no código, quem fez, quando fez e etc. Isso é muito importante quando vc está trabalhando em um projeto com mais pessoas, mas mesmo que vc esteja sozinho, é uma boa prática usar o git para controlar as mudanças que vc faz no código.

complicado? não é não... vocês vão ver

## Clonando o repositório
- Abra o terminal
- Navegue até a pasta que vc quer clonar o repositório
- Digite `git clone https://github.com/rafaelfino/learn-ops-content.git`
- Pronto, vc clonou o repositório

## Legal! E agora?
Vamos rodar esses bots e ver o que eles tem a dizer
Vá até a pasta *src/interactive* e execute os arquivos python
Mas espere, vc não tem o python instalado, não é?
Vamos resolver isso também

### No Windows
- Formata seu computador e instala um linux: https://xubuntu.org/ (tá bom, brincadeira... vamos lá)
- Acesse o site do python e baixe o instalador: https://www.python.org/
- Execute o instalador e siga os passos
- Abra o terminal
- Digite `python --version` e veja se o python foi instalado corretamente

### No Linux
- Abra o terminal
- Digite `sudo apt-get install python3` e siga os passos
- Digite `python --version` e veja se o python foi instalado corretamente

Em alguns casos, pode ser que o comando para executar o python seja `python3`, então, ao invés de `python arquivo.py`, vc vai ter que executar `python3 arquivo.py`

## Executando os bots
- Abra o terminal
- Navegue até a pasta *src/interactive*
- Execute o arquivo python que vc quer rodar

## Bots disponíveis
Vamos ver uma tabela lindona em markdown com todos os bots?

| Bot | Descrição |
| --- | --- |
| code.py | Bot que fala sobre código, a estrutura básica de um programa python |
| vars.py | Bot que fala sobre variáveis, o que são, como usar |
| if.py | Bot que fala sobre estruturas condicionais, o que são, como usar |
| git.py | Bot que fala sobre git, o que é, como usar, comandos básicos |
| linux.py | Bot que fala sobre linux, o que é, como usar, comandos básicos |
| python.py | Bot que fala sobre python, o que é, como usar, comandos básicos |
| docker.py | Bot que fala sobre docker, o que é, como usar, comandos básicos |

E aí, o que achou? Legal, né?
