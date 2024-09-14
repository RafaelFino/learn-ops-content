# learn-ops-content

``` bash
██      ███████  █████  ██████  ███    ██      ██████  ██████  ███████     ██████   ██████  ████████ 
██      ██      ██   ██ ██   ██ ████   ██     ██    ██ ██   ██ ██          ██   ██ ██    ██    ██    
██      █████   ███████ ██████  ██ ██  ██     ██    ██ ██████  ███████     ██████  ██    ██    ██    
██      ██      ██   ██ ██   ██ ██  ██ ██     ██    ██ ██           ██     ██   ██ ██    ██    ██    
███████ ███████ ██   ██ ██   ██ ██   ████      ██████  ██      ███████     ██████   ██████     ██   
      
```

## Vamos começar?

Olá, eu sou o Fino, escrevi esse projeto para tentar resolver um velho problema: sou um só e as vezes não consigo estar em todos os lugares que gostaria

Parece besta, gosto muito de tentar ajudar com as mentorias, tentando ajudar o pessoal a estudar e etc, mas nem sempre tenho todo o tempo que gostaria para fazer isso da melhor forma. Como então eu poderia melhorar isso e conseguir estar onde preciso para tentar passar alguma coisa?

Bom, temos hoje a IA que tem me ajudado demais a economizar tempo e fazer coisas de uma forma mais eficiente... não preciso dizer que atualmente (escrevo isso em 2024) a IA não faz milagres e não é nenhum Oraculo que sabe tudo, mas com certeza ajuda demais a automatizar tarefas, eu usei algumas alternativas aqui e indexei um monte de conversas com as turmas passadas e pedi para ela gerar conteúdo para uns bots, para simular aulas e eu fiz um programinha em Python que simula a conversa q costumamos ter durante as mentorias. Não ficou assim aquela obra de arte, mas acho que a IA conseguiu pegar bem a ideia de alguns temas e gerar um conteúdo interessante que pode ajudar em uma preparação para os papos com os alunos.

Básicamente todo o código dos bots está dentro da pasta **src/interative**, basta executar os programas python que a magia acontece.

> Mas Fino, eu não faço ideia de como eu posso executar isso! 

Verdade, a maioria de vcs sequer sabe o que é um git ou python é só uma cobra... ou talvez nem isso.. então vamos do começo

> Como pegar esse repositório e começar a brincar?

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
Vá até a pasta *src/lessons* e execute os arquivos python
Mas espere, vc não tem o python instalado, não é?
Vamos resolver isso também

### No Windows
- Formata seu computador e instala um linux: https://xubuntu.org/ (você já deve ter percebido que sua vida será mais complexa com Windows... pare de sofrer e resolve logo isso)
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
- Navegue até a pasta *src/lessons*
- Execute o arquivo python que vc quer rodar

> Não entendi... como começar?

Bom, a ideia é que vc vá até a pasta *src/lessons* e execute os arquivos python que estão lá, eles vão simular uma conversa com um bot, que vai te ajudar a entender um pouco mais sobre os temas que a gente costuma conversar nas mentorias.

Mas fiz um cara que deve te ajudar a começar, ele se chama `start.py`, execute ele e siga as instruções:

- Abra o terminal
- Navegue até a pasta *src*
- Execute o arquivo `start.py`

### No linux
``` bash
cd
cd learn-ops-content
python3 -m venv .
source bin/activate
pip3 install -r requirements.txt
cd src
./start.py
```

### No Windows
Primeiro: respira fundo, se acalma, não é o fim do mundo, vc vai conseguir
``` bash
cd
cd learn-ops-content 
python3 -m venv . 
source bin/activate
pip3 install -r requirements.txt 
cd src
python start.py
```

### Ainda há outra alternativa: Killercoda
> Mas Fino, não estou conseguindo fazer essa desgraça aí funcionar! Parece grego misturado com latim e um pouco de aramaico...

Pelo visto você deve ter uma dívida de sangue e uma promessa para um deus antigo que não vai tirar o windows e está tomando uma surra do prompt de comando... certo? calma... você vai conseguir...

Calma, calma... vamos resolver isso também:
- Acesse o site do killercoda e abra um playground de Ubuntu: https://killercoda.com/playgrounds/scenario/ubuntu

Rode o seguinte comando (GIGANTE! vai ser um pouco chato, mas é só copiar e colar):
``` bash
cd && git clone https://github.com/RafaelFino/learn-ops-content.git && cd learn-ops-content && python3 -m venv . && source bin/activate && pip3 install -r requirements.txt && cd src && python3 start.py
```

Explicado:
``` bash
cd # Vai para a pasta do usuário
git clone https://github.com/RafaelFino/learn-ops-content.git # Clona o repositório
cd learn-ops-content  # Entra na pasta do repositório
python3 -m venv .  # Cria um ambiente virtual
source bin/activate  # Ativa o ambiente virtual
pip3 install -r requirements.txt  # Instala as dependências
cd src  # Entra na pasta src, onde estão os arquivos python
python3 start.py # Executa o arquivo start.py
```

Note que se vc ficar executando tudo toda vez, você fará todo o processo de novo, então, para facilitar, vc pode criar um script para fazer isso para vc, assim, toda vez que vc precisar, basta executar o script e ele fará tudo para vc.

Depois de instalado, vc pode executar o script com o comando:
``` bash
cd # Vai para a pasta do usuário
cd learn-ops-content  # Entra na pasta do repositório
source bin/activate  # Ativa o ambiente virtual, caso não esteja ativo
cd src  # Entra na pasta src, onde estão os arquivos python
./start.py # Executa o script diratemente, sem precisar do python
# CASO QUEIRA FAZER CHAMANDO O PYTHON DIRETAMENTE:
# python3 start.py # Mas o resultado é o mesmo
```

### POR FAVOR NÃO ESQUEÇA:
- Se você está no Windows, o executável do **python** é **python** e não **python3**
- Se você está no Linux, o executável do **python** é **python3** e não **python**
- Quando você chama um script no linux, você pode dizer que ele é um executável, por isso no Linux você consegue chamar diretamente por `./start.sh`, no Windows você precisa chamar o python diretamente
- Se você está no Windows e não consegue executar o script, você pode tentar executar o script com o python diretamente, assim: `python start.py`
- Entenda o que está fazendo, não saia executando scripts que você não conhece, isso pode ser perigoso
- Entenda o que é o ambiente virtual do python e como ele funciona, isso vai te ajudar a entender o que está acontecendo
- Se você não entendeu nada do que eu falei, não se preocupe, é normal, estamos aqui para aprender juntos, me procure e vou te ajudar

# Se tudo mais der errado...
Tente acessar a versão web: https://rgt-tools.duckdns.org/bot/


# Tópicos que queremos estudar

Tópicos para uma base sólida de profissional de tecnologia
- Fundamentos de tecnologia
    - O que é um computador
    - O que ele faz
    - Quais são os componentes básicos de um computador
    - A História básicas que explica algumas coisas importantes do que temos hoje
    - O que é memória RAM
    - O que é um Storage
    - O que é uma CPU
        - Arquiteturas de CPU (X86,Arm e etc)
        - História, funcionamento básicos
    - Sistemas operacionais
        - O que são, oq fazem, a história até aqui e pq são como são
        - Arquiteturas dos principais: Windows, Linux, macOS, Android, iOS, Unix, BSD    
    - O que é um servidor
    - O que é uma rede
    - O que é um DataCenter
    - O que é Virtualização
    - Tipos de programas:
        - Scripts
        - Interpretados
        - Com Máquina Virtual
        - Compilados
- Terminal
    - Operação básica
    - Git
- Código:
    - Variáveis
        - Alocação de memória
        - Tipos
        - Números, caracteres, strings e tipos complexos
    - Algorítimos
        - If/Else
        - Loops/Repetições
        - Funções
        - Estrutura básica de código
    - Estruturas de dados
        - Arrays
        - Listas
            - Tipos de listas
        - Mapas
        - Comparativos
    - Algorítimos de busca
    - Notação de complexidade (Big O)
- Arquiteturas básicas de uma solução
    - Onde ela acontece
    - Onde as coisas ficam
    - O que é um servidor
    - Como usar um Docker e por que isso vai te ajudar
    - O que é um servidor de aplicação
    - O que é um servidor de banco de dados
    - O que é um servidor de mensageria
    - O que é qlqr outro tipo de recurso: Noções de SaaS, PaaS, IaaS
- Bancos de dados
    - Modelagem básica de dados
    - O que é SQL e noSQL
    - Como modelar algo
    - Como inserir dados lá
    - Como consultar seus dados
    - Como alterar seus dados
    - Como apagar seus dados
- Noções de Orietação a objeto
    - Onde fica cada coisa na sua aplicação
    - Como segregar as coisas e estruturar seu código, onde colocar seus métodos
    - Noções de classes, heranças, interfaces
    - Afinal, oq é esse objeto q tanto falam?
    - DDD
- **Primeira grande prova: o CRUD**: https://github.com/RafaelFino/plataforma-crud
- Arquitetura de serviços
    - O que é um serviço
    - Noções de arquitetura de solução: Onde fica cada coisa
    - Como eles se conversam?
    - Mensagerias    
    - Quem faz oq em modelos mais complexos?
    - SOLID
    - Arquiteturas sincronas e assincronas
    - Eventos
    - Cache
    - Modelos distribuídos
- **Prova final: O TCC**: https://github.com/RafaelFino/plataforma-tcc


E aí, o que achou? Legal, né?
