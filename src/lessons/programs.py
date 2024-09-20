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
# Sempre que o aluno tentar se referir ao professor, ele deve usar o método c.Teacher() para se referir ao professor, nunca diretamente. Dessa forma o nome do professor irá aparecer na tela do aluno. Nessas linhas a string sempre deve ser formatada com o nome do professor usando o 'f' antes das aspas.
# O aluno geralmente se perde nas explicações e não entende na primeira explicação, forçando o professor a tentar sempre simplificar o tema com exemplos práticos e analogias simplificadas.

def t(m):
    c.Speak(m)

def s(m):
    c.StudentComment(m)

def q(m):
    c.Question(m)

def bash(code):
    c.ShowCode(code, lexer="bash")

def python(code):
    c.ShowCode(code, lexer="python")

def clang(code):
    c.ShowCode(code, lexer="c")

def run(code):
    c.ShowCodeAndRun(code)

def cmd(command):
    c.ShowCommand(command)

# Tema: Os tipos de programas: scripts, compilados e interpretados via máquina virtual
# Objetivo: O aluno deve entender a diferença entre os tipos de programas e como eles são executados.
# O aluno deve entender como funciona a execução de um script, de um programa compilado e de um programa interpretado via máquina virtual.
# O aluno deve entender as diferenças entre os tipos de programas e como eles são executados.

t("Olá, pequenos gafanhotos! Hoje vamos falar sobre os tipos de programas: scripts, compilados e interpretados via máquina virtual.")
s(f"Mas {c.Teacher()}, o que são scripts? É tipo aquele negócio que o pessoal de cinema segue para fazer um filme?")
t("Olha, um pouco pequeno gafanhoto. Scripts são como receitas de bolo, ou seja, um conjunto de instruções que são executadas em sequência. Como se fossem um roteiro de filme, onde cada linha é uma instrução que deve ser seguida.")
s(f"Entendi, {c.Teacher()}. Eu achei q tava falando merda, mas nem tava tão errado assim... mas em programação, o que são scripts?")
t("Scripts são programas que são executados por um interpretador de comandos, como o bash, por exemplo. Eles são executados linha a linha, sem a necessidade de compilação. Por isso chamamos de bash scripts. É como se fosse um roteiro de filme que é executado por um diretor.")
s(f"Entendi, {c.Teacher()}. É como se eu colocasse um monte de comandos e o computador saísse executando um por um, né?")
t("Isso mesmo, pequeno gafanhoto. Os scripts são programas que são executados linha a linha, sem a necessidade de compilação. Eles são interpretados por um interpretador de comandos, como o bash, por exemplo. Mas existem vários tipos diferentes de interpretadores de comandos, como o Python, por exemplo.")
s(f"Uau!! acho que entendi, {c.Teacher()}, mas como um sistema linux, por exemplo, sabe qual é o interpretador de comandos que ele deve usar para executar um script?")
t("""Bom, pequeno gafanhoto, o sistema linux sabe qual é o interpretador de comandos que ele deve usar para executar um script, porque o interpretador de comandos é definido na primeira linha do script. Por exemplo, se você escrever #!/bin/bash na primeira linha de um script, o sistema linux vai usar o bash para executar o script.""")
t("""Esse negócio de colocar qual é o interpretador de comandos na primeira linha do script é chamado de shebang. É como se fosse uma dica para o sistema linux de qual interpretador de comandos ele deve usar para executar o script. Mas POR FAVOR, não procure isso na internet, é só uma brincadeira, caso queira ver mais detalhes, recomendo ver o link da wikipedia: https://en.wikipedia.org/wiki/Shebang_(Unix)""")
s(f"Acho que eu entendi... poderia me mostrar algum exemplo de script, {c.Teacher()}?")
t("Claro, pequeno gafanhoto! Aqui está um exemplo de um script em bash:")
bash("""
#!/bin/bash
echo "Hello, World!"
""")
t("Nesse script, a primeira linha indica que o interpretador de comandos que deve ser usado para executar o script é o bash. A segunda linha echo 'Hello, World!' é um comando que imprime a mensagem 'Hello, World!' na tela.")
s(f"Entendi, {c.Teacher()}! Tem algum exemplo um pouco mais complexo e o que mais posso fazer em um bash script?")
t("Claro, pequeno gafanhoto! Aqui está um exemplo de um script em bash um pouco mais complexo:")
bash("""
#!/bin/bash
     
echo "What is your name?"
read name
echo "Hello, $name!"
""")

t("Nesse script, a primeira linha indica que o interpretador de comandos que deve ser usado para executar o script é o bash. A segunda linha echo 'What is your name?' é um comando que imprime a mensagem 'What is your name?' na tela. A terceira linha read name é um comando que lê uma entrada do usuário e a armazena na variável name. A quarta linha echo 'Hello, $name!' é um comando que imprime a mensagem 'Hello, $name!' na tela, onde $name é substituído pelo valor da variável name.")
q(f"Legal {c.Teacher()}! O que mais eles fazem? Consigo manipular arquivos ou chamar APIs por aí?")
t("Claro, pequeno gafanhoto! Com os scripts em bash, você pode fazer muitas coisas, como manipular arquivos, chamar APIs, e muito mais. Você pode usar comandos como cat, grep, sed, awk, curl, e muitos outros para fazer isso. Vamos ver alguns exemplos:")
bash("""
#!/bin/bash
     
# Cria um arquivo chamado example.txt
echo "Hello, World!" > example.txt
     
# Lê o conteúdo do arquivo example.txt e joga na tela
cat example.txt

# Lê o conteúdo do arquivo example.txt e jopa em uma variável
content=$(cat example.txt)     

# Remove o arquivo example.txt, caso ele exista
if [ -f example.txt ]; then     
    rm example.txt
fi
     
# Imprime o conteúdo da variável content
echo $content
""")
t("Olha um outro exemplo, agora chamando uma API com o curl:")
bash("""
#!/bin/bash     

# Chama a API do GitHub para obter informações sobre um repositório e joga em um arquivo hamado hello-world.json
curl -sS https://api.github.com/repos/octocat/hello-world > hello-world.json

# Filtra o resultado da API do GitHub para obter o nome do repositório
cat hello-world.json | grep '"name":' | awk -F '"' '{print $4}'
     
# Remove o arquivo hello-world.json, caso ele exista
if [ -f hello-world.json ]; then     
    rm hello-world.json
fi     
""")
s(f"Entendi, {c.Teacher()}! CARAMBA!! Quais outros tipos de scripts existem e costumamos usar?")
t("Além dos scripts em bash, pequeno gafanhoto, existem outros tipos de scripts, como os scripts em Python, por exemplo. Os scripts em Python são executados pelo interpretador de Python e são escritos em Python. Eles são muito poderosos e fáceis de usar, mas antes de te mostrar, vou montar uma super tabelinha com alguns dos mais conhecidos, em ASCII art, claro!")
t("""
+---------------------+
|       Scripts       |
+---------------------+
|  Bash               |
|  Shell              |
|  Perl               |
|  Lua                |
|  JavaScript         |
|  Ruby               |
|  PHP                |
|  Python             |
|  PowerShell         |
+---------------------+
""")
s(f"Uau!! {c.Teacher()}! Que tabela linda!! Python é assim também? Poderoso e fácil de usar?")
t("Sim, pequeno gafanhoto! Python é uma linguagem de programação poderosa e fácil de usar. Você pode escrever scripts em Python que fazem praticamente qualquer coisa que você possa imaginar. Vamos ver um exemplo de um script em Python:")
python("""
#!/usr/bin/env python3
       
print("Hello, World!")
""")
t("Nesse script, a primeira linha indica que o interpretador de Python que deve ser usado para executar o script é o python3. A segunda linha print('Hello, World!') é um comando que imprime a mensagem 'Hello, World!' na tela. Meio besta né? Vamos fazer um igual ao que fizemos no bash, mas em python?")
q(f"Claro, {c.Teacher()}! Pode mostrar?")
t("Claro, pequeno gafanhoto! Aqui está um exemplo de um script em Python um pouco mais complexo:")
python("""
#!/usr/bin/env python3
       
name = input("What is your name? ")
print(f"Hello, {name}!")
""")
t("Nesse script, a primeira linha indica que o interpretador de Python que deve ser usado para executar o script é o python3. A segunda linha name = input('What is your name? ') é um comando que lê uma entrada do usuário e a armazena na variável name. A terceira linha print(f'Hello, {name}!') é um comando que imprime a mensagem 'Hello, $name!' na tela, onde $name é substituído pelo valor da variável name. Agora vamos para aquele que brinca com o arquivo...")
python("""
#!/usr/bin/env python3

# Cria um arquivo chamado example.txt
with open("example.txt", "w") as f:
    f.write("Hello, World!")
       
# Lê o conteúdo do arquivo example.txt e joga na tela e em uma variável
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
       
# Remove o arquivo example.txt, caso ele exista
import os
if os.path.exists("example.txt"):
    os.remove("example.txt")
       
# Imprime o conteúdo da variável content
print(content)
""")

s(f"Entendi, {c.Teacher()}! Louco isso aí!! E como eu faço para chamar APIs com Python?")
t("Com Python, pequeno gafanhoto, você pode chamar APIs usando a biblioteca requests. Vamos ver um exemplo de como chamar a API do GitHub para obter informações sobre um repositório:")
python("""
#!/usr/bin/env python3
       
import requests
       
# Chama a API do GitHub para obter informações sobre um repositório
response = requests.get("https://api.github.com/repos/octocat/hello-world")
       
if response.status_code == 200:
    data = response.json()
    print(data["name"])
else:
    print("Failed to get repository information")       
""")
t("Nesse caso vemos que o python traz uma biblioteca para fazer requisições HTTP, a requests, que é muito poderosa e fácil de usar. Com ela, você pode chamar APIs, fazer requisições HTTP, e muito mais.")
q(f"Entendi, {c.Teacher()}! Mas e os programas compilados e interpretados via máquina virtual? Como eles funcionam?")
t("Calma, um de cada vez... agora faz sentido você entender o que é um arquivo compilado, você saberia me dizer isso?")
s(f"Claro que não {c.Teacher()}! Sou meio lesado, se soubesse não estaria aqui vendo essa aula em um bot... agora você foi vacilão!")
t("Ok, foi uma pergunta idiota mesmo, mas eu tenho mais fé do que racionalidade com vcs... vamos lá, vamos falar primeiro sobre o que é um programa, essa você sabe né?")
s(f"Programa é um conjunto de instruções que são executadas por um computador, certo {c.Teacher()}?")
t("Isso mesmo, pequeno gafanhoto! Um programa é um conjunto de instruções que são executadas por um computador. Vimos os scripts... eles são arquivos texto, humanamente legíveis, que contém instruções que são executadas por um interpretador de comandos. Mas e os programas compilados, você sabe o que são?")
s(f"Não faço ideia {c.Teacher()}! Mas você vai me explicar, né?")
t("Claro, pequeno gafanhoto! Os programas compilados são programas que são traduzidos de uma linguagem de programação de alto nível para uma linguagem de máquina. Isso é feito por um compilador, que é um programa que traduz o código de um programa de uma linguagem de programação de alto nível para uma linguagem de máquina.")
s("Tá meio confuso, lembra q sou lerdo, pobre e meio burro... mas o que é uma linguagem de máquina?")
t("Uma linguagem de máquina, pequeno gafanhoto, é uma linguagem que é compreendida diretamente pelo processador de um computador. Ela é composta por instruções que são executadas pelo processador, como adicionar dois números, armazenar um valor em um endereço de memória, e assim por diante.")
s(f"Entendi, {c.Teacher()}! Mas como o compilador faz essa tradução?")
t("O compilador faz essa tradução, jovem doença, analisando o código do programa escrito em uma linguagem de programação de alto nível e gerando um código equivalente em linguagem de máquina. Esse código em linguagem de máquina é então executado pelo processador do computador.")
s(f"Tá confuso {c.Teacher()}! Me explica com exemplos mais simples para que eu possa entender melhor.")
t("Claro, pequeno gafanhoto! Vamos ver um exemplo de um programa em C que soma dois números:")
clang("""
#include <stdio.h>

int main() {
    int a,b;
    
    printf("Enter first number: ");
    scanf("%d", &a);
       
    printf("Enter second number: ");
    scanf("%d", &b);   
       
    int sum = a + b;
    printf("The sum of %d and %d is %d\n", a, b, sum);
    return 0;
}
""")
t("Esse programinha simples em linguagem C, para que o computador o entenda, ele precisa ser compilado. Isso quer dizer que o compilador, que tambem é um programa, vai traduzir esse código para uma linguagem que o computador entenda. Vamos ver como isso é feito:")
bash("""
gcc -o sum sum.c
""")
t("Nesse caso, o gcc é um compilador de C que traduz o código do programa sum.c para um arquivo executável chamado sum. Esse arquivo executável contém o código do programa em linguagem de máquina, que é então executado pelo processador do computador.")
q(f"Entendi, {c.Teacher()}! E como ficaria esse arquivo compilado? Poderia me mostrar? Tipo, o conteúdo do arquivo não será mais esse código humano, né?")
t("Claro, pequeno gafanhoto! Aqui está o conteúdo do programa sum:")
bash("""
cat sum
""")
t("Esse é o conteúdo do arquivo executável sum. Ele contém o código do programa em linguagem de máquina, que é então executado pelo processador do computador. Isso que você está vendo é o código em linguagem de máquina, que é compreendido diretamente pelo processador do computador.")
s(f"Entendi, {c.Teacher()}! Que doideira... não dá para entender nada!")
t("Calma, pequeno gafanhoto! É assim mesmo, o código em linguagem de máquina é compreensível apenas pelo processador do computador. Mas e os programas interpretados via máquina virtual, você sabe o que são?")
s(f"Não faço ideia {c.Teacher()}! Mas você vai me explicar, né? Vai fazer aquela tabelinha maneira de novo?")
t("Toma a tabela aí com linguagens compiladas:")
t("""
+---------------------+
|    Linguagens       |
+---------------------+
|  C                  |
|  C++                |
|  Rust               |
|  Go                 |
|  Swift              |
|  Objective-C        |
|  Fortran            |
|  Pascal             |
|  Ada                |
+---------------------+
""")
t("E sobre osprogramas interpretados via máquina virtual são programas que são executados por uma máquina virtual. Uma máquina virtual é um programa que simula um computador e executa programas escritos em uma linguagem de programação de alto nível. Esses programas são interpretados pela máquina virtual, que os executa como se fossem scripts.")
s(f"Entendi, {c.Teacher()}! Então isso aí roda dentro daqueles programas que criam VMs, tipo o VirtualBox?")
t("Não cara... porra... vc tava indo bem... mas é um erro compreensível, essa VM que você está falando é um virtualizador de máquinas, que é um programa que simula um computador completo, com hardware e software, e permite que você execute sistemas operacionais inteiros dentro dele. Uma máquina virtual, no contexto dos programas interpretados via máquina virtual, é um programa que simula um computador e executa programas escritos em uma linguagem de programação de alto nível.")
s(f"Entendi, {c.Teacher()}! Mas como isso funciona?")
t("Quando compilamos um código para linguagem de máquina, ele é feito para rodar em um determinado SO, com um determinado hardware, por exemplo, aqui usamos um linux em x86_64, veja a aula sobre raspberrys q eu explico bem sobre isso, mas o ponto é que o código de máquina gerado, é feito para rodar em um contexto bem específico, esse código de máquina não é portável, ou seja, não roda em qualquer lugar. Já os programas interpretados via máquina virtual, são feitos para rodar em qualquer lugar, pois a máquina virtual é quem interpreta o código e executa ele.")
q(f"Acho que entendi, {c.Teacher()}... mas e o q é essa joça de máquina virtual que você falou aí? de onde saiu isso? para que ela serve? qual o sentido da vida?")
t("A máquina virtual, pequeno gafanhoto, é um programa que simula um computador e executa programas escritos em uma linguagem de programação de alto nível. Ela é como um computador dentro de um computador, que executa programas como se fossem scripts. O sentido da vida é 42, mas isso é outra história.")
t("A ideia aqui surgiu no final dos anos 90, onde haviam muitos tipos diferentes de hardwares e plataformas e era super dificil programar para todos eles, eles eram muito incompatíveis entre si. Então, a ideia de uma máquina virtual era criar um ambiente de execução que fosse independente de hardware e sistema operacional, onde você pudesse escrever um programa uma vez e ele rodasse em qualquer lugar.")
t("O conceito é mais antigo que isso, mas o Java acho que foi o maior representante dessa ideia, onde você escreve um programa em Java, compila ele para um bytecode, que é um código intermediário, e esse bytecode é executado por uma máquina virtual Java, que interpreta e executa o programa.")
t("Então quando você pega o seu super código em Java, ele vira esse negócio chamado bytecode, que não é ainda um binário direto para um harware e também não é um script, ele é um cara que vai rodar em uma plataforma intermediária, que fará o meio campo entre seu código e o hardware e SO.... esse cara do meio que é a tal da máquina virtual... a do Java costumamos chamar de JVM: Java Virtual Machine.")
t("Existem várias linguagens que usam esse conceito de máquina virtual, olha essa linda tabela com algumas linguagens que podem funcionar dessa forma:")
t("""
+---------------------+
|    Linguagens       |
+---------------------+
|  Java               |
|  C#                 |
|  Kotlin             |
|  Scala              |
|  Groovy             |
|  Clojure            |
|  JRuby              |
|  Jython             |
|  JPHP               |
+---------------------+
""")
s(f"Entendi, {c.Teacher()}! Conseguiria então desehar pra mim o fluxo de funcionamento de um cara desses, assim no ASCII art?")
t("""
+---------------------+        +---------------------+        +---------------------+        +---------------------+
| Programa em Java    |  --->  | Bytecode            |  --->  | JVM                 |  --->  | Processador         |
+---------------------+        +---------------------+        +---------------------+        +---------------------+
""")
s("Eita p0rra!! desenhou mesmo no terminal? Que foda!! Faz isso para o C também?")
t("Claro, pequeno gafanhoto! Vamos ver o fluxo de funcionamento de um programa em C:")
t("""
+---------------------+        +---------------------+        +---------------------+
| Programa em C       |  --->  | Código de máquina   |  --->  | Processador         |
+---------------------+        +---------------------+        +---------------------+
""")
s(f"Entendi, {c.Teacher()}! Mas e para o Python? Como seria?")
t("Para o Python, pequeno gafanhoto, o fluxo de funcionamento é um pouco diferente. Vamos ver como seria:")
t("""
+---------------------+        +---------------------+        +---------------------+
| Programa em Python  |  --->  | Interpretador       |  --->  | Processador         |    
|                     |        | Python              |        |                     |
+---------------------+        +---------------------+        +---------------------+
""")
q(f"Entendi, {c.Teacher()}! Mas e para o bash? Como seria?")
t("Para o bash, pequeno gafanhoto, o fluxo de funcionamento é um bem parecido com o do python. Vamos ver como seria:")
t("""
+---------------------+        +---------------------+        +---------------------+
| Programa em Bash    |  --->  | Interpretador       |  --->  | Processador         |
|                     |        | Bash                |        |                     |
+---------------------+        +---------------------+        +---------------------+
""")
s("Acho que comecei a entender... mas afinal, quais as vantagens e desvantagens de cada tipo de programa? Vamos fazer aquela tabela doida?")
t("Claro, nessa tabela vamos colocar as vantagens de cada um, os casos de uso mais comuns e as desvantagens de cada um:")
t("""
+---------------------+        +-------------------------+        +---------------------------+
|  Scripts            |        |  Compilados             |        |  Interpretados            |
+---------------------+        +-------------------------+        +---------------------------+
|  Vantagens:         |        |  Vantagens:             |        |  Vantagens:               |
|  - Fáceis de usar   |        |  - Rápidos              |        |  - Portabilidade          |
|  - Rápidos de       |        |  - Eficientes           |        |  - Facilidade de          |
|    escrever         |        |  - Otimizados           |        |    uso                    |
|  - Flexíveis        |        |  - Baixo nível          |        |  - Flexibilidade          |
|  - Portáveis        |        |  - Acesso direto        |        |  - Facilidade de          |
|                     |        |    ao hardware          |        |    aprendizado            |
|                     |        |                         |        |  - Gerenciamento          |  
|                     |        |                         |        |    automático de recursos |    
+---------------------+        +-------------------------+        +---------------------------+
|  Desvantagens:      |        |  Desvantagens:          |        |  Desvantagens:            |
|  - Lentos           |        |  - Gestão manual        |        |  - Lentos                 |
|  - Ineficientes     |        |    de recursos          |        |  - Ineficientes           |
|  - Difíceis de      |        |  - Binários específicos |        |  - Difíceis de            |
|    depurar          |        |    para o hardware      |        |    depurar                |
|                     |        |  - Código mais complexo |        |                           |
+---------------------+        +-------------------------+        +---------------------------+
""")
q(f"Entendi, {c.Teacher()}! Mas e aí, qual é o melhor tipo de programa para usar?")
t("Depende, pequeno gafanhoto! Cada tipo de programa tem suas vantagens e desvantagens, e o melhor tipo de programa a ser usado depende do que você quer fazer. Se você precisa de um programa que seja rápido e eficiente, um programa compilado pode ser a melhor opção. Se você precisa de um programa que seja portável e fácil de usar, um programa interpretado pode ser a melhor opção. E se você precisa de um programa que seja flexível e fácil de escrever, um script pode ser a melhor opção.")
s(f"É a hora da tua frase {c.Teacher()}?")
t("Sim, tava esperando... QUAL PROBLEMA VOCÊ PRECISA RESOLVER??? É isso... baseado no seu requisito, sempre escolha a melhor ferramenta para resolver o seu problema. E lembre-se, pequeno gafanhoto, a aula não acabou, ainda temos muito o que aprender juntos!")
s(f"Valeu, {c.Teacher()}! Até a próxima aula!")
q("Até a próxima aula! :)")