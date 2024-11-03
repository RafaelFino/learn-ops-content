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

def sql(code):
    c.ShowCode(code, lexer="sql")

# Sobre o tema:
# O professor deve explicar o que é um banco de dados e para que serve.
# O professor deve explicar os tipos de bancos de dados.
# O professor deve explicar o que é um SGBD.
# O professor deve explicar o que é um SQL.
# O professor deve explicar o que é uma aplicação cliente de um banco de dados.
# O professor deve explicar onde um banco de dados deve ser executado, da diferença entre o SGDB e o Cliente.
# O professor deve explicar o que é um tipo de dados e quais são os tipos de dados mais comuns.
# O professor deve explicar o que é uma tabela.
# O professor deve explicar o que é uma linha.
# O professor deve explicar o que é uma coluna.
# O professor deve explicar o que é um registro.
# O professor deve explicar o que é uma chave primária.
# O professor deve explicar o que é uma chave estrangeira.
# O professor deve explicar o que é um índice.
# O professor deve explicar o que é uma consulta.
# O professor deve explicar o que é uma transação.
# O professor deve explicar o que é uma visão lógica dos dados, um MER
# O professor deve explicar o que é um NoSQL, ou seja, um banco de dados de chave e valor ou um banco de dados de documentos.
# O professor deve explicar o que é um banco de dados em memória.
# O professor deve explicar o que é um banco de dados distribuído.

t("Olá, jovens aprendizes da arte de conjurar sistemas! Hoje vamos falar sobre banco de dados. Você sabe o que é um banco de dados?")
s(f"Então {c.Teacher()}, é uma cadeira feita com dados, tipo aqueles de jogos de tabuleiro?")
t("É... hoje vai ser complicado... dormiu com o Bozo?")
s(f"Não, não, {c.Teacher()}, foi mal... rs... mas eu não sei o que é um banco de dados não, me explica?")
t("Claro, jovem padawan! Um banco de dados é um sistema de armazenamento de dados que permite a criação de um conjunto de informações organizadas e relacionadas entre si. Ele serve para armazenar informações de forma organizada e segura.")
s(f"Entendi, {c.Teacher()}, então é tipo um arquivo de texto, mas mais organizado?")
t("Isso mesmo, pequeno gafanhoto! Um banco de dados é um arquivo de texto mais organizado e seguro. Existem vários tipos de bancos de dados, você sabia?")
s(f"Não, {c.Teacher()}, não sabia... quais são os tipos de bancos de dados?")
t("Existem vários tipos de bancos de dados, como os bancos de dados relacionais, os bancos de dados de documentos, os bancos de dados em memória, os bancos de dados distribuídos, entre outros.")
s(f"E o que é um banco de dados relacional, {c.Teacher()}?")
t("Um banco de dados relacional é um banco de dados que armazena dados em tabelas, onde as tabelas são relacionadas entre si por meio de chaves primárias e chaves estrangeiras.")
s(f"Entendi, {c.Teacher()}, e o que é uma chave primária?")
t("Uma chave primária é um campo ou conjunto de campos que identifica de forma única cada registro em uma tabela.")
s(f"E o que é uma chave estrangeira, {c.Teacher()}?")
t("Uma chave estrangeira é um campo ou conjunto de campos que faz referência a uma chave primária em outra tabela. É como relacionamos dados de tabelas diferentes.")
s(f"Entendi, {c.Teacher()}, você aí falando de tabelas, como assim tabelas? Tipo o Excel?")
t("Isso mesmo, pequeno gafanhoto! Uma tabela é uma estrutura de dados que organiza os dados em linhas e colunas, como uma planilha do Excel. Seria como se cada aba de uma planilha fosse uma tabela e com essas chaves conseguimos relacionar dados entre as abas")
s(f"Entendi, {c.Teacher()}, eu acho, e como eu organizo essas coisas nessas tabelas, é só jogar os dados lá?")
t("Não é bem assim, pequeno gafanhoto! Antes de jogar os dados na tabela, é preciso definir o tipo de dados de cada coluna, como texto, número, data, entre outros.")
s(f"E o que é um tipo de dados, {c.Teacher()}?")
t("Um tipo de dados é um conjunto de valores que uma coluna pode armazenar, como texto, número, data, entre outros. Vou montar um tabelinha Ascii bonito para você entender melhor cada tipo de dado fundmental, olha só:")
t("""
+----------------+-----------------+
| Tipo de Dado   | Exemplo         |
+----------------+-----------------+
| Texto          | 'Olá, Mundo!'   |
+----------------+-----------------+
| Número         | 42              |
+----------------+-----------------+
| Data           | 2022-01-01      |
+----------------+-----------------+
| Booleano       | True            |
+----------------+-----------------+
""")
s("Nossa, me tirou de tonto agora... isso aí é óbvio, não?")
t("Nunca vou perder a chance de rir da sua cara, mas você está enganado, modelar de uma forma eficiênte é uma arte, e não é tão óbvio assim, pense que em um banco de dados, teremos grandes volumes de dados, você já parou para pensar na diferença de comsumo de espaço e recursos computacionais usar o tipo errado para guadar um dado?")
s(f"Não, {c.Teacher()}, não tinha pensado nisso... eu não poderia por exemplo usar sempre Texto e guardar tudo lá?")
t("Poderia, mas não seria eficiente, pequeno gafanhoto! O ideal é usar o tipo de dado correto para cada coluna, para garantir a integridade dos dados e a eficiência do banco de dados. Vamos ver um exemplo de má prática, usando todos os campos como texto e ver o tamanho que ficam no final do dia:")
t("Pense na seguinte estrutura: Nome, Idade, Data de Nascimento, Salário, Telefone, Email, Endereço, Cidade, Estado, CEP, País,  e vamos ver o tamanho que isso ocuparia em disco e o custo de manipular esses dados:")
t("""
+------------------+------------------------------+-------------------------------------------+
| Coluna           | Tamanho com dados tipo Texto | Tamanho com os dados corretamente tipados |
+------------------+------------------------------+-------------------------------------------+
| Nome             | 200 bytes                    | (varchar) 200 bytes                       |
+------------------+------------------------------+-------------------------------------------+
| Idade            | 3 bytes                      | (uint) 1 bytes                            |
+------------------+------------------------------+-------------------------------------------+
| Data Nascimento  | 10 bytes                     | (date) 4 bytes                            |
+------------------+------------------------------+-------------------------------------------+
| Salário          | 10 bytes                     | (decimal) 8 bytes                         |
+------------------+------------------------------+-------------------------------------------+
| Telefone         | 15 bytes                     | (varchar) 15 bytes                        |
+------------------+------------------------------+-------------------------------------------+
| Email            | 50 bytes                     | (varchar) 50 bytes                        |
+------------------+------------------------------+-------------------------------------------+
| Endereço         | 100 bytes                    | (varchar) 100 bytes                       |
+------------------+------------------------------+-------------------------------------------+
| Cidade           | 50 bytes                     | (varchar) 50 bytes                        |
+------------------+------------------------------+-------------------------------------------+
| Estado           | 2 bytes                      | (char) 2 bytes                            |
+------------------+------------------------------+-------------------------------------------+
| Total            | 440 bytes                    | 430 bytes                                 |
+------------------+------------------------------+-------------------------------------------+
""")
s(f"Nossa, {c.Teacher()}, nesse exemplo nem é tanta diferença de tamanho, mas imagino que na escala isso faça muita diferença, não?")
t("Exatamente, pequeno gafanhoto! Na escala de um banco de dados, a diferença de tamanho e de recursos computacionais pode ser significativa. Por isso, é importante escolher o tipo de dado correto para cada coluna.")
t("Ainda mais por que além do espaço físico, é como o banco de dados vai manipular esses dados, se você tem um campo de data, por exemplo, e você quer fazer uma busca por data, se você tiver o campo tipado como texto, o banco de dados vai ter que fazer uma conversão de todos os registros para data para fazer a busca, o que é muito mais custoso do que se o campo já estiver tipado como data.")
s(f"Entendi, {c.Teacher()}, isso então é um registro e seus tipos de dados certo?")
t("Isso mesmo, pequeno gafanhoto! Um registro é uma linha em uma tabela, onde cada coluna é um tipo de dado. E cada linha é um registro.")
s(f"E o que é um índice, {c.Teacher()}?")
t("Um índice é uma estrutura de dados que melhora a velocidade de busca em uma tabela. Ele é como um índice de um livro, que facilita a busca de informações.")
s(f"Entendi, {c.Teacher()}, isso tem a ver com as chaves primárias e estrangeiras?")
t("Não exatamente, pequeno gafanhoto! Um índice é uma estrutura de dados que melhora a velocidade de busca em uma tabela, enquanto as chaves primárias e estrangeiras são usadas para relacionar dados entre tabelas.")
s(f"{c.Teacher()} você tá achando que eu estou entendendo tudo, mas eu não entendi nada... consegue me dar uns exemplos considerando que eu sou um completo leigo?")
t("Claro, pequeno gafanhoto! Vamos fazer um exemplo prático para você entender melhor. Vamos criar um banco de dados de alunos, com as seguintes tabelas: Alunos, Cursos, Matrículas, Notas.")
t("Na tabela Alunos, teremos os campos: id, nome, idade, email, telefone.")
t("Na tabela Cursos, teremos os campos: id, nome, carga_horaria, valor.")
t("Na tabela Matrículas, teremos os campos: id, aluno_id, curso_id, data_matricula.")
t("Na tabela Notas, teremos os campos: id, matricula_id, nota.")
t("Vamos criar as tabelas e inserir alguns registros para você entender melhor:")
sql("""
CREATE TABLE Alunos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    email VARCHAR(100),
    telefone VARCHAR(15)
);

CREATE TABLE Cursos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    carga_horaria INT,
    valor DECIMAL(10, 2)
);
    
CREATE TABLE Matriculas (
    id INT PRIMARY KEY,
    aluno_id INT,
    curso_id INT,
    data_matricula DATE,
    FOREIGN KEY (aluno_id) REFERENCES Alunos(id),
    FOREIGN KEY (curso_id) REFERENCES Cursos(id)
);
    
CREATE TABLE Notas (
    id INT PRIMARY KEY,
    matricula_id INT,
    nota DECIMAL(10, 2),
    FOREIGN KEY (matricula_id) REFERENCES Matriculas(id)
);
""")
q("Eita!? Q negócio é esse aí que você fez?")
t("Isso é um código SQL, pequeno gafanhoto! É uma linguagem de consulta estruturada que usamos para criar, consultar e manipular bancos de dados relacionais.")
q("SQL? Que treta é essa?")
t("SQL é a sigla para Structured Query Language, que é uma linguagem de consulta estruturada que usamos para criar, consultar e manipular bancos de dados relacionais.")
s(f"Entendi, {c.Teacher()}, de forma bem resumida, é isso? De onde saiu? quem inventou? Como era antes disso? Como é que funciona? Quais são as aplicações práticas? Quais bancos usam isso aí?")
t("Calma, pequeno gafanhoto! Vamos por partes... A linguagem SQL foi criada pela IBM nos anos 70, com o objetivo de padronizar a forma de consultar e manipular bancos de dados relacionais.")
t("Antes do SQL, cada banco de dados tinha sua própria linguagem de consulta, o que dificultava a migração de um banco de dados para outro. Com o SQL, é possível usar a mesma linguagem em diferentes bancos de dados.")
t("O SQL é uma linguagem de alto nível, que permite escrever consultas de forma simples e intuitiva. Ele é dividido em várias partes, como DDL, DML, DCL, DQL, entre outras.")
t("O SQL é amplamente utilizado em bancos de dados relacionais, como MySQL, PostgreSQL, Oracle, SQL Server, SQLite, entre outros.")
s(f"Entendi, {c.Teacher()}, um pouco na verdade, você usou um monte de letrinhas aí... DDL, DML, DCL, DQL... o que é isso?")
t("Calma, pequeno gafanhoto! Vou explicar cada uma dessas partes do SQL para você entender melhor.")
t("DDL é a sigla para Data Definition Language, que é usada para definir a estrutura do banco de dados, como criar tabelas, alterar tabelas, excluir tabelas, entre outros.")
t("DML é a sigla para Data Manipulation Language, que é usada para manipular os dados do banco de dados, como inserir dados, atualizar dados, excluir dados, entre outros.")
t("DCL é a sigla para Data Control Language, que é usada para controlar o acesso aos dados do banco de dados, como conceder permissões, revogar permissões, entre outros.")
t("DQL é a sigla para Data Query Language, que é usada para consultar os dados do banco de dados, como selecionar dados, filtrar dados, ordenar dados, entre outros.")
s(f"Entendi, {c.Teacher()}, é tipo um conjunto de comandos para fazer tudo no banco de dados, não?")
t("Isso mesmo, pequeno gafanhoto! O SQL é uma linguagem de consulta estruturada que permite criar, consultar e manipular bancos de dados relacionais de forma simples e intuitiva. Vou resumir DDL, DML, DCL e DQL em uma tabela para você entender melhor:")
t("""
+------------------+---------------------------------------------------------------+
| Comando          | Descrição                                                     |
+------------------+---------------------------------------------------------------+
| CREATE TABLE     | Cria uma tabela no banco de dados                             |
+------------------+---------------------------------------------------------------+
| ALTER TABLE      | Altera a estrutura de uma tabela no banco de dados            |
+------------------+---------------------------------------------------------------+
| DROP TABLE       | Exclui uma tabela do banco de dados                           |
+------------------+---------------------------------------------------------------+
| INSERT INTO      | Insere um registro em uma tabela no banco de dados            |
+------------------+---------------------------------------------------------------+
| UPDATE           | Atualiza um registro em uma tabela no banco de dados          |
+------------------+---------------------------------------------------------------+
| DELETE           | Exclui um registro de uma tabela no banco de dados            |
+------------------+---------------------------------------------------------------+
| GRANT            | Concede permissões de acesso a um usuário no banco de dados   |
+------------------+---------------------------------------------------------------+
| REVOKE           | Revoga permissões de acesso a um usuário no banco de dados    |
+------------------+---------------------------------------------------------------+
| SELECT           | Seleciona dados de uma tabela no banco de dados               |
+------------------+---------------------------------------------------------------+
""")
q(f"Entendi, {c.Teacher()}, você falou um monte de coisas e não me falou quais deles são DML, DDL, DCL ou DQL, consegue refazer essa tabela aí correlacionando os comandos com as siglas?")
t("Claro, pequeno gafanhoto! Vou refazer a tabela para você entender melhor:")
t("""
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| Tipo      | Comando      | Descrição                                                   | Exemplo                                          |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DDL       | CREATE TABLE | Cria uma tabela no banco de dados                           | CREATE TABLE Alunos (id INT PRIMARY KEY);        |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DDL       | ALTER TABLE  | Altera a estrutura de uma tabela no banco de dados          | ALTER TABLE Alunos ADD COLUMN nome VARCHAR(100); |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DDL       | DROP TABLE   | Exclui uma tabela do banco de dados                         | DROP TABLE Alunos;                               |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DML       | INSERT INTO  | Insere um registro em uma tabela no banco de dados          | INSERT INTO Alunos VALUES (1, 'João', 25);       |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DML       | UPDATE       | Atualiza um registro em uma tabela no banco de dados        | UPDATE Alunos SET idade = 26 WHERE id = 1;       |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DML       | DELETE       | Exclui um registro de uma tabela no banco de dados          | DELETE FROM Alunos WHERE id = 1;                 |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DCL       | GRANT        | Concede permissões de acesso a um usuário no banco de dados | GRANT SELECT ON Alunos TO 'usuario';             |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DCL       | REVOKE       | Revoga permissões de acesso a um usuário no banco de dados  | REVOKE SELECT ON Alunos FROM 'usuario';          |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
| DQL       | SELECT       | Seleciona dados de uma tabela no banco de dados             | SELECT * FROM Alunos;                            |
+-----------+--------------+-------------------------------------------------------------+--------------------------------------------------+
""")
s(f"Entendi, {c.Teacher()}, é tipo um conjunto de comandos para fazer tudo no banco de dados, não? Consegue agora só fazer uma tabelinha só com os tipos e suas descrições?")
t("Claro, pequeno gafanhoto! Vou fazer uma tabelinha para você entender melhor:")
t("""
+-----------+-----------------------------------------------------------------------------------+
| Tipo      | Descrição                                                                         |
+-----------+-----------------------------------------------------------------------------------+
| DDL       | Data Definition Language, usada para definir a estrutura do banco de dados        |
+-----------+-----------------------------------------------------------------------------------+
| DML       | Data Manipulation Language, usada para manipular os dados do banco de dados       |
+-----------+-----------------------------------------------------------------------------------+
| DCL       | Data Control Language, usada para controlar o acesso aos dados do banco de dados  |
+-----------+-----------------------------------------------------------------------------------+
| DQL       | Data Query Language, usada para consultar os dados do banco de dados              |
+-----------+-----------------------------------------------------------------------------------+
""")
s(f"{c.Teacher()}, Essas IAs que usamos as vezes se perdem não? ficam rodando sem sair do lugar, as vezes são objetivas demais e as vezes não são objetivas o suficiente, você precisa cuidar mais com isso")
t("Não se preocupe, pequeno gafanhoto! Eu estou aqui para te ajudar a entender o mundo mágico dos bancos de dados. Se tiver alguma dúvida, é só perguntar!")
s(f"Entendi, {c.Teacher()}, e o que é uma aplicação cliente de um banco de dados? Onde esses caras rodam? É meio confuso isso pra mim ainda...")
t("Uma aplicação cliente de um banco de dados é um software que se conecta a um banco de dados para consultar, manipular e exibir os dados. Ela pode ser um sistema web, um sistema desktop, um aplicativo mobile, entre outros.")
t("A aplicação cliente roda em um ambiente separado do banco de dados, e se comunica com o banco de dados por meio de uma conexão de rede, como a internet ou uma rede local.")
t("Por exemplo, um sistema de vendas de uma loja pode ser uma aplicação cliente de um banco de dados, onde os vendedores podem consultar, cadastrar e atualizar os produtos, clientes e pedidos.")
s(f"Entendi, {c.Teacher()}, é tipo o sistema que eu uso para fazer as compras online, não? Ele se conecta com o banco de dados da loja para mostrar os produtos e fazer as compras?")
t("Isso mesmo, pequeno gafanhoto! Um sistema de compras online é uma aplicação cliente de um banco de dados, onde os clientes podem consultar, cadastrar e atualizar os produtos, clientes e pedidos.")
t("Mas existem mais camadas aí entre o cliente e o banco de dados, como a camada de negócio, a camada de acesso a dados, entre outras. Cada camada tem uma responsabilidade específica no sistema. Vamos ver isso mais no detalhe quando falarmos de arquitetura de software.")
s(f"Entendi, {c.Teacher()}, e onde um banco de dados deve ser executado? Qual a diferença entre o SGDB e o Cliente?")
t("Um banco de dados pode ser executado em vários lugares, como em um servidor local, em um servidor na nuvem, em um cluster de servidores, entre outros.")
t("O SGBD, ou Sistema de Gerenciamento de Banco de Dados, é o software responsável por gerenciar o banco de dados, como criar, consultar e manipular os dados. Ele é o servidor de banco de dados.")
t("O Cliente, por outro lado, é o software que se conecta ao servidor de banco de dados para consultar, manipular e exibir os dados. Ele é a aplicação cliente.")
s(f"Entendi, {c.Teacher()}, é tipo o cliente é o que eu uso para acessar o banco de dados, e o SGBD é o que gerencia o banco de dados, não?")
t("Isso mesmo, pequeno gafanhoto! O Cliente é o que você usa para acessar o banco de dados, e o SGBD é o que gerencia o banco de dados. Cada um tem sua responsabilidade no sistema. Vamos montar uma lista aqui com os principais SGDBs e suas aplicações clientes de administração para você ter uma ideia:")
t("""
+------------------+-----------------------------------------------+
| SGDB             | Cliente de Administração                      |
+------------------+-----------------------------------------------+
| MySQL            | MySQL Workbench, phpMyAdmin, HeidiSQL         |
+------------------+-----------------------------------------------+
| PostgreSQL       | pgAdmin, phpPgAdmin, DBeaver                  |
+------------------+-----------------------------------------------+
| Oracle           | Oracle SQL Developer, SQL*Plus, Toad          |
+------------------+-----------------------------------------------+
| SQL Server       | SQL Server Management Studio, Azure Data      |
+------------------+-----------------------------------------------+
| SQLite           | DB Browser for SQLite, SQLiteStudio           |
+------------------+-----------------------------------------------+
""")
q("Caramba! Quantos?! E esses aí são os principais? Como vou saber quando usar cada um deles?")
t("Esses são alguns dos principais SGDBs e suas aplicações clientes de administração, pequeno gafanhoto! Cada um tem suas vantagens e desvantagens, e a escolha vai depender das necessidades do projeto. Deixa eu te explicar um pouco sobre cada um deles, com uma tabela e principais características:")
t("""
+------------------+----------------------------------------------------------------+------------------------------------------+--------------------+
| SGDB             | Principais Características                                     | Casos comuns de uso                      | Tipo de licença    |
+------------------+----------------------------------------------------------------+------------------------------------------+--------------------+
| MySQL            | Open-source, fácil, rápido, escalável, suporta transações     | Sites, blogs, e-commerce, aplicações web  | GPL                |
+------------------+----------------------------------------------------------------+------------------------------------------+--------------------+
| PostgreSQL       | Open-source, robusto, poderoso, suporta transações            | Aplicações críticas, BI, data warehousing | PostgreSQL License |
+------------------+----------------------------------------------------------------+------------------------------------------+--------------------+
| Oracle           | Poderoso, escalável, suporta transações, suporte comercial    | Empresas, aplicações críticas, BI         | Proprietária       |
+------------------+----------------------------------------------------------------+------------------------------------------+--------------------+
| SQL Server       | Poderoso, escalável, suporta transações, integração com Azure | Empresas, aplicações críticas, BI         | Proprietária       |
+------------------+----------------------------------------------------------------+------------------------------------------+--------------------+
| SQLite           | Leve, rápido, fácil, não requer servidor                      | Aplicações mobile, IoT, pequenos projetos | Public Domain      |
+------------------+----------------------------------------------------------------+------------------------------------------+--------------------+
""")
s(f"Entendi, {c.Teacher()}, é tipo um conjunto de comandos para fazer tudo no banco de dados, não? Consegue agora só fazer uma tabelinha só com os tipos e suas descrições?")
t("Claro, pequeno gafanhoto! Vou fazer uma tabelinha para você entender melhor:")
t("""
+------------------+----------------------------------------------------------------+
| SGDB             | Descrição                                                      |
+------------------+----------------------------------------------------------------+
| MySQL            | Open-source, fácil, rápido, escalável, suporta transações      |
+------------------+----------------------------------------------------------------+
| PostgreSQL       | Open-source, robusto, poderoso, suporta transações             |
+------------------+----------------------------------------------------------------+
| Oracle           | Poderoso, escalável, suporta transações, suporte comercial     |
+------------------+----------------------------------------------------------------+
| SQL Server       | Poderoso, escalável, suporta transações, integração com Azure  |
+------------------+----------------------------------------------------------------+
| SQLite           | Leve, rápido, fácil, não requer servidor                       |
+------------------+----------------------------------------------------------------+
""")
q(f"Entendi, {c.Teacher()}, e o que é uma transação? O que isso tem a ver com banco de dados?")
t("Uma transação é uma sequência de operações que são executadas de forma atômica, consistente, isolada e durável. Ela é usada para garantir a integridade dos dados em um banco de dados. Mas antes exitem algumas coisas que você precisa saber:")
t("Atômica significa que a transação é executada como uma única unidade, ou seja, todas as operações são executadas ou nenhuma é executada.")
t("Consistente significa que a transação leva o banco de dados de um estado consistente para outro estado consistente, ou seja, o banco de dados não fica em um estado inválido.")
t("Isolada significa que a transação é executada de forma isolada, ou seja, as operações de uma transação não interferem nas operações de outras transações.")
t("Durável significa que as alterações feitas por uma transação são permanentes, ou seja, elas são salvas no banco de dados mesmo em caso de falha.")
t("Quando juntamos todas essas características, temos uma transação que garante a integridade dos dados em um banco de dados, dizemos que é um banco de dados ACID.")
s(f"Entendi, {c.Teacher()}, é tipo um conjunto de comandos para fazer tudo no banco de dados, não? Consegue agora só fazer uma tabelinha só com os tipos e suas descrições?")
t("Claro, pequeno gafanhoto! Vou fazer uma tabelinha para você entender melhor:")
t("""
+------------------+----------------------------------------------------------------+
| Tipo             | Descrição                                                      |
+------------------+----------------------------------------------------------------+
| Atômica          | A transação é executada como uma única unidade                 |
+------------------+----------------------------------------------------------------+
| Consistente      | A transação leva o banco de dados de um estado consistente     |
+------------------+----------------------------------------------------------------+
| Isolada          | A transação é executada de forma isolada                       |
+------------------+----------------------------------------------------------------+
| Durável          | As alterações feitas por uma transação são permanentes         |
+------------------+----------------------------------------------------------------+
""")
s("Acho que estou entendendo, mas você poderia me contar quais os riscos caso algum desses não aconteça? Por quê isso é tão importante?")
t("Claro, pequeno gafanhoto! Se uma transação não for atômica, pode acontecer de algumas operações serem executadas e outras não, o que pode deixar o banco de dados em um estado inválido.")
t("Quando falamos em consistência, se uma transação não for consistente, pode acontecer de o banco de dados ficar em um estado inválido, o que pode levar a erros e corrupção de dados.")
t("O termo isolamento é importante para garantir que as operações de uma transação não interfiram nas operações de outras transações, o que pode levar a problemas de concorrência e inconsistência de dados.")
t("Por fim, a durabilidade é importante para garantir que as alterações feitas por uma transação sejam permanentes, mesmo em caso de falha, o que evita a perda de dados e a corrupção do banco de dados.")
s(f"Entendi, {c.Teacher()}, é tipo um conjunto de comandos para fazer tudo no banco de dados, não? Consegue agora só fazer uma tabelinha só com os tipos e suas descrições?")
t("Claro, pequeno gafanhoto! Vou fazer uma tabelinha para você entender melhor:")
t("""
+------------------+------------------------------------------------------------+----------------------------------------------------+----------------------------------------------+
| Tipo             | Descrição                                                  | Importância                                        | Riscos de não usar                           |
+------------------+------------------------------------------------------------+----------------------------------------------------+----------------------------------------------+
| Atômica          | A transação é executada como uma única unidade             | Evita operações parciais                           | Estado inválido do banco de dados            |
+------------------+------------------------------------------------------------+----------------------------------------------------+----------------------------------------------+
| Consistente      | A transação leva o banco de dados de um estado consistente | Evita estado inválido do banco de dados            | Erros e corrupção de dados                   |
+------------------+------------------------------------------------------------+----------------------------------------------------+----------------------------------------------+
| Isolada          | A transação é executada de forma isolada                   | Evita problemas de concorrência                    | Inconsistência de dados                      |
+------------------+------------------------------------------------------------+----------------------------------------------------+----------------------------------------------+
| Durável          | As alterações feitas por uma transação são permanentes     | Evita perda de dados e corrupção do banco de dados | Perda de dados e corrupção do banco de dados |
+------------------+------------------------------------------------------------+----------------------------------------------------+----------------------------------------------+
""")
s("Acho que o negócio tá fazendo mais sentido... mas e o que é uma visão lógica dos dados, um MER?")
t("Uma visão lógica dos dados, ou Modelo Entidade-Relacionamento (MER), é uma representação visual dos dados de um banco de dados, que mostra as entidades, os atributos e os relacionamentos entre as entidades.")
t("O MER é uma ferramenta poderosa para modelar a estrutura de um banco de dados, pois permite visualizar de forma clara e intuitiva como os dados estão organizados e relacionados entre si.")
t("O MER é composto por entidades, que são os objetos do mundo real que queremos representar no banco de dados, e por relacionamentos, que são as conexões entre as entidades.")
t("Por exemplo, em um sistema de vendas, teríamos as entidades Cliente, Produto, Pedido, e os relacionamentos entre elas, como Cliente faz Pedido, Pedido contém Produto, entre outros.")
s(f"Entendi foi nada {c.Teacher()}, explica aí lembrando que eu ralei o dia inteiro em um emprego que me esfola em uma sociedade que me massacra o tempo todo... consegue me dar um exemplo bem didático e prático disso?")
t("Claro, jovem tartaruga! Vou dar um exemplo prático para você entender melhor. Vamos modelar um banco de dados de uma biblioteca, com as seguintes entidades: Livro, Autor, Editora, Empréstimo.")
t("Na entidade Livro, teremos os atributos: id, título, ano, autor_id, editora_id.")
t("Na entidade Autor, teremos os atributos: id, nome, nacionalidade.")
t("Na entidade Editora, teremos os atributos: id, nome, país.")
t("Na entidade Empréstimo, teremos os atributos: id, livro_id, data_empréstimo, data_devolução.")
t("Vamos modelar o MER desse banco de dados para você entender melhor:")
t("""
+------------------+-----------------------------------------------+
| Entidade         | Atributos                                     |
+------------------+-----------------------------------------------+
| Livro            | id, título, ano, autor_id, editora_id         |
+------------------+-----------------------------------------------+
| Autor            | id, nome, nacionalidade                       |
+------------------+-----------------------------------------------+
| Editora          | id, nome, país                                |
+------------------+-----------------------------------------------+
| Empréstimo       | id, livro_id, data_empréstimo, data_devolução |
+------------------+-----------------------------------------------+
""")
s(f"Entendi, {c.Teacher()}, é tipo um conjunto de comandos para fazer tudo no banco de dados, não? Conseguimos então criar essas tabelas usando aquele tal de SQL?")
t("Isso mesmo, pequeno gafanhoto! Podemos criar essas tabelas usando a linguagem SQL. Vou montar um código SQL para você criar essas tabelas no banco de dados:")
sql("""
CREATE TABLE Livro (
    id INT PRIMARY KEY,
    titulo VARCHAR(100),
    ano INT,
    autor_id INT,
    editora_id INT,
    FOREIGN KEY (autor_id) REFERENCES Autor(id),
    FOREIGN KEY (editora_id) REFERENCES Editora(id)
);
    
CREATE TABLE Autor (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    nacionalidade VARCHAR(50)
);
    
CREATE TABLE Editora (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    país VARCHAR(50)
);
    
CREATE TABLE Empréstimo (
    id INT PRIMARY KEY,
    livro_id INT,
    data_empréstimo DATE,
    data_devolução DATE,
    FOREIGN KEY (livro_id) REFERENCES Livro(id)
);
""")
s(f"Entendi, {c.Teacher()}, ou acho que entendi... então o MER é tipo um esboço do banco de dados, não? Ele é um desenho então?")
t("Isso mesmo, pequeno gafanhoto! O MER é um esboço do banco de dados, que mostra as entidades, os atributos e os relacionamentos entre as entidades. Ele é um desenho visual que ajuda a modelar a estrutura do banco de dados.")
q("Ok, acho que estou pegando o jeito... mas e o que é um NoSQL, como assim um banco que não tem essa linguagem aí? como as coisas ficam nele?")
t("Um banco de dados NoSQL é um banco de dados que não utiliza a linguagem SQL para consultar e manipular os dados. Ele é um banco de dados não relacional, que armazena os dados de forma mais flexível e escalável.")
t("Os bancos de dados NoSQL são mais adequados para aplicações que precisam de alta disponibilidade, escalabilidade e flexibilidade, como aplicações web, IoT, Big Data, entre outras.")
t("Existem vários tipos de bancos de dados NoSQL, como os bancos de dados de chave e valor, os bancos de dados de documentos, os bancos de dados de colunas, entre outros.")
s(f"Não sei se entendi, {c.Teacher()}, mas como é que isso funciona? Como eu faço para consultar e manipular os dados em um banco de dados NoSQL?")
t("Em um banco de dados NoSQL, você não usa a linguagem SQL para consultar e manipular os dados, pequeno gafanhoto! Cada tipo de banco de dados NoSQL tem sua própria linguagem de consulta e manipulação de dados.")
t("Por exemplo, em um banco de dados de chave e valor, você usa comandos como GET, PUT, DELETE para consultar e manipular os dados. Em um banco de dados de documentos, você usa comandos como FIND, INSERT, UPDATE para consultar e manipular os dados.")
t("Cada tipo de banco de dados NoSQL tem suas próprias características e vantagens, e a escolha vai depender das necessidades do projeto. Vou montar uma tabelinha aqui com os principais tipos de bancos de dados NoSQL e suas características:")
t("""
+------------------+---------------------------------------------------------------+
| Tipo             | Características                                               |
+------------------+---------------------------------------------------------------+
| Chave e Valor    | Simples, rápido, escalável, flexível                          |
+------------------+---------------------------------------------------------------+
| Documentos       | Flexível, escalável, suporta dados semiestruturados           |
+------------------+---------------------------------------------------------------+
| Colunas          | Rápido, escalável, suporta consultas complexas                |
+------------------+---------------------------------------------------------------+
""")
q("É... tá nebuloso, consegue me dar um exemplo prático de um banco de dados NoSQL?")
t("Claro, pequeno gafanhoto! Vou dar um exemplo prático de um banco de dados NoSQL para você entender melhor. Vamos modelar um banco de dados de uma loja online, com as seguintes entidades: Produto, Categoria, Pedido.")
t("No banco de dados de chave e valor, teremos os comandos: GET, PUT, DELETE para consultar e manipular os dados.")
t("No banco de dados de documentos, teremos os comandos: FIND, INSERT, UPDATE para consultar e manipular os dados.")
t("Vamos modelar o banco de dados NoSQL para você entender melhor, desenhando o que seriam cada uma dessas entidades e suas capacidades e características:")
t("""
+------------------+-----------------------------------------------+------------------------------------+
| Entidade         | Comandos                                      | Campos                             |
+------------------+-----------------------------------------------+------------------------------------+
| Produto          | GET, PUT, DELETE                              | id, nome, preço, categoria_id      |
+------------------+-----------------------------------------------+------------------------------------+
| Categoria        | GET, PUT, DELETE                              | id, nome                           |
+------------------+-----------------------------------------------+------------------------------------+
| Pedido           | GET, PUT, DELETE                              | id, produto_id, quantidade, total  |
+------------------+-----------------------------------------------+------------------------------------+
""")
t("Em casos de bancos de chave e valor, de documentos, uma das características é a flexibilidade, onde você pode adicionar campos sem precisar alterar a estrutura do banco de dados, o que é uma grande vantagem em relação aos bancos de dados relacionais.")
t("Dizemos que a estrutura das colunas não é rígida, o que permite armazenar dados semiestruturados, como JSON, XML, entre outros.")
s("Caramba! então eu não vou usar aquele CREATE TABLE dizendo quais são os campos e tipos de dados?")
t("Exatamente, querido pobre sofredor! Em um banco de dados NoSQL, você não precisa definir a estrutura do banco de dados antes de inserir os dados, como em um banco de dados relacional. Mas, cada escolha é uma renúncia, e você perde a garantia de integridade dos dados.")
s("Então aquele negócio de chave estrangeria não existe aqui?")
t("Boa observação, em um banco de dados NoSQL, você não tem a mesma garantia de integridade dos dados que em um banco de dados relacional, pois não há a mesma rigidez na definição da estrutura do banco de dados. Daó inclusive o nome de BANCO RELACIONAL, é dessa relação que falamos...")
q(f"Entendi, {c.Teacher()}, é tipo um conjunto de comandos para fazer tudo no banco de dados, não? E quais são os principais bancos de dados NoSQL e suas aplicações e tipos de licença?")
t("Os principais bancos de dados NoSQL são o MongoDB, o Cassandra, o Redis, o Couchbase, o Amazon DynamoDB, entre outros. Cada um tem suas características e vantagens, clientes, e a escolha vai depender das necessidades do projeto. Vamos fazer uma tabelinha:")
t("""
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Banco de Dados   | Características                               | Casos comuns de uso                | Aplicações cliente para administração           | Tipo de licença   |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| MongoDB          | Flexível, escalável, suporta dados semiestru  | Aplicações web, IoT, Big Data, BI  | MongoDB Compass, Robo 3T, Studio 3T             | SSPL              |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Cassandra        | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | DataStax Studio, Cassandra Query Language       | Apache 2.0        |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Redis            | Rápido, escalável, suporta dados em memória   | Cache, sessões, filas de mensagens | RedisInsight, Redis Commander, Redis Desktop    | BSD               |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Couchbase        | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | Couchbase Web Console, Couchbase CLI            | Proprietária      |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| AWS DynamoDB     | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | AWS Management Console, AWS CLI                 | Proprietária      |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| AWS DocumentDB   | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | AWS Management Console, AWS CLI                 | Proprietária      |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Google Firestore | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | Google Cloud Console, gcloud CLI                | Proprietária      |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| CouchDB          | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | Fauxton, CouchDB CLI                            | Apache 2.0        |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Neo4j            | Flexível, escalável, suporta dados semiestru  | Big Data, IoT, aplicações web, BI  | Neo4j Browser, Neo4j Desktop, Cypher Shell      | GPL               |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| ArangoDB         | Flexível, escalável, suporta dados semiestru  | Big Data, IoT, aplicações web, BI  | ArangoDB Web Interface, arangosh                | Apache 2.0        |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| RavenDB          | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | RavenDB Studio, RavenDB Management Studio       | Proprietária      |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Firebase         | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | Firebase Console, Firebase CLI                  | Proprietária      |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| ScyllaDB         | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | Scylla Manager, Scylla Monitoring               | AGPL              |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| DataStax Astra   | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | DataStax Studio, Cassandra Query Language       | Proprietária      |
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
| Spanner          | Escalável, distribuído, suporta dados semies  | Big Data, IoT, aplicações web, BI  | Google Cloud Console, gcloud CLI                | Proprietária      |  
+------------------+-----------------------------------------------+------------------------------------+-------------------------------------------------+-------------------+
""")
q("Caramba! Quantos?! E esses aí são os principais? Como vou saber quando usar cada um deles?")
t("Esses são alguns dos principais bancos de dados NoSQL e suas aplicações clientes de administração, pequeno gafanhoto! Cada um tem suas vantagens e desvantagens, e a escolha vai depender das necessidades do projeto.")
t("Por exemplo, se você precisa de alta disponibilidade e escalabilidade, pode escolher o Cassandra. Se você precisa de um banco de dados em memória, pode escolher o Redis. Se você precisa de um banco de dados distribuído, pode escolher o Couchbase.")
t("Cada banco de dados NoSQL tem suas características e vantagens, e a escolha vai depender das necessidades do projeto. Se tiver alguma dúvida, é só perguntar!")
s(f"Acho que cansei... se precisar de mais alguma coisa eu te chamo, {c.Teacher()}.")
t("Fique à vontade, pequeno gafanhoto! Estou aqui para te ajudar a entender o mundo mágico dos bancos de dados. Se tiver alguma dúvida, é só chamar! Caso queira uma super aula sobre bancos de dados Mongo, recomendo esse conteúdo: https://learn.mongodb.com/learning-paths/mongodb-python-developer-path e https://learn.mongodb.com/learning-paths/mongodb-atlas-administrator-path ")