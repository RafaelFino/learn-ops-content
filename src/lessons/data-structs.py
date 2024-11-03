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

def t(m):
    c.Speak(m)

def s(m):
    c.StudentComment(m)

def q(m):
    c.Question(m)

def code_c(code):
    c.ShowCode(code, lexer="c")

def code_cs(code):
    c.ShowCode(code, lexer="cs")

def code(code):
    c.ShowCode(code)    

# Sobre o tema:
# Vamos falar sobre o que é a memória RAM do computador
# precisamos falar sobre alocação de memória, sobre a visão do que é um byte, um char e um inteiro, como uma string fica na memória
# A partir disso, devemos explicar o que é um Array, sobre como a memória é alocada de forma sequencial e como podemos acessar os elementos de um array
# A partir disso, explicamos que com um index, podemos acessar diretamente um elemento do array
# Por isso, devemos explicar o que é complexidade algorítmica, e como acessar um elemento de um array é uma operação de complexidade O(1), mas os alunos não fazem ideia do que seja essa complexidade O, então devemos explicar de forma bem simples
# APós isso, vamos explicar as dificuldades de extender um array, sobre como incluir um novo item que aumente o tamanho do array nos obriga a sempre criar um novo array e copiar todos os elementos do array antigo para o novo array e como isso aumenta o custo
# Como solução para isso, vamos explicar que existem lista e que elas resolvem essa questão do tamanho dinâmico, e que podemos adicionar elementos no final da lista e remover elementos do início da lista, porém a forma com que percorremos uma lista é diferente, indo item a item
# Vamos explicar então o que é uma lista, como ela funciona e como podemos implementar uma lista, sobre o que é uma lista ligada e uma lista duplamente ligada
# Vamos mostrar a implementação de uma lista em C, dando um pouco de contexto também sobre ponteiros e como apontamos para os próximos itens da lista
# Vamos mostrar as diferenças, vantagens e desvantagens de uma lista ligada e uma lista duplamente ligada e comparar com um array
# Também é importante mostrar outros casos de uso para listass: como filas e pilhas
# Dar exemplos práticos e didáticos de como essas estruturas podem ser uteis e que tipos de problemas elas resolvem
# Após deixar claro o uso de arrays, listas, filas, pilhas, vamos falar sobre dicionários e como eles são estruturados, como podemos acessar os elementos de um dicionário e como eles são úteis para acessar elementos de forma rápida
# Vamos mostrar o uso de um dicionário ou mapa em python, em C e C#, mostrando que o conceito é o mesmo, mas a implementação é diferente
# Também é importante após isso, falar sobre a complexidade algorítmica de um dicionário, que é O(1) para acessar um elemento
# Vamos mostrar também que essas estruturas podem ser combinadas, como um dicionário de listas, ou uma lista de dicionários
# devemos mostrar tabelas em ASCII para comparar os casos de uso onde cada estrutura faz mais sentido e também ao explicar cada uma delas, mostrar uma matriz SWOT para mostrar as vantagens e desvantagens de cada estrutura
# Sempre devemos usar exemplos bem didáticos de como usar cada uma delas e mostrar que elas são ferramentas para resolver problemas

t("Olá, Doenças! Hoje vamos falar sobre memória RAM e estruturas de dados. Você sabe o que é a memória RAM do computador?")
s(f"Olá, {c.Teacher()} Memória RAM? é tipo uma memória que parece um SAPO?")
t("Hahaha, não, A memória RAM é a memória de acesso aleatório do computador, onde os dados são armazenados temporariamente enquanto o computador está ligado.")
s("Ah, entendi! Então quando desligamos o computador, os dados são perdidos?")
t("Isso mesmo! A memória RAM é volátil, ou seja, quando desligamos o computador, os dados são perdidos. Mas você faz ideia de como um programa usa isso aí?")
s("Não faço ideia! Como assim?")
t("Quando um programa é executado, ele aloca espaço na memória RAM para armazenar os dados temporários, como variáveis, mas você sabe quem cuida disso?")
s("Não faço ideia! Quem é?")
t("O sistema operacional é o responsável por gerenciar a memória RAM e alocar espaço para os programas. Mas você sabe o que é um byte?")
s("Não faço ideia! O que é um byte? Bit? Char? É de comer?")
t("Hahaha, não! Um byte é a menor unidade de informação que um computador pode armazenar. Um char é um caractere, que é representado por um byte. E um inteiro é representado por 4 bytes.")
s("Entendi! Eu acho que já vi isso em algum lugar! Tem uma outra aula aqui nesse bot maneiro que fala disso, certo?")
t("Isso mesmo! Mas você sabe o que é um array?")
s("Não faço ideia! O que é um array?")
t("Um array é uma estrutura de dados que armazena uma coleção de elementos do mesmo tipo. Os elementos de um array são armazenados de forma sequencial na memória RAM.")
s(f"Pow {c.Teacher()}, isso é muito legal! Mas  não entendi nada... lembra que eu sou só um aluno começando aqui, você vai ter que explicar sem esquecer que eu não sei nada!")
t("Claro! Vou explicar de forma mais simples. Um array é como uma lista de coisas do mesmo tipo, em ordem e por estarem em ordem, podemos acessar cada item do array por um índice, que seria a posição do item na lista. Olha um exemplo:")
t("Se temos um array de inteiros, podemos acessar o primeiro elemento do array com o índice 0, o segundo com o índice 1 e assim por diante.")
s("Na explicação você mandou bem, no exemplo ficou abstrato! Pode dar um exemplo mais prático?")
t("Claro! Imagine que temos um array de nomes de pessoas: ['João', 'Maria', 'José']. Se quisermos acessar o nome 'Maria', podemos fazer isso com o índice 1, pois ela está na posição 1 do array.")
q(f"Como assim 1 {c.Teacher()}? Não era 2?")
t("Hahaha, não! Em programação, a contagem começa do zero, então o primeiro elemento de um array é o índice 0. O segundo elemento é o índice 1 e assim por diante.")
t("Deixe eu te mostrar um pouco de código para ficar mais claro. Vou mostrar como acessar um elemento de um array em C.")
code_c("""
#include <stdio.h>

int main() {
    int numeros[3] = {10, 20, 30};
    printf("%d", numeros[1]);
    return 0;
}
""")

s("Entendi! Mas e se eu quiser adicionar um novo elemento no array?")
t("Bom, aí que está o problema dos arrays. Se quisermos adicionar um novo elemento no array, precisamos criar um novo array com um tamanho maior e copiar todos os elementos do array antigo para o novo array.")
q("Nossa! E como eu faria isso?")
t("Vamos ver como fazer isso em C. Vou mostrar um exemplo de como adicionar um novo elemento no array.")
code_c("""
#include <stdio.h>
#include <stdlib.h>
       
int main() {
    int *numeros = malloc(3 * sizeof(int));
    numeros[0] = 10;
    numeros[1] = 20;
    numeros[2] = 30;
    
    int *novo = malloc(4 * sizeof(int));
    for (int i = 0; i < 3; i++) {
        novo[i] = numeros[i];
    }
    novo[3] = 40;
    
    free(numeros);
    numeros = novo;
    
    for (int i = 0; i < 4; i++) {
        printf("%d ", numeros[i]);
    }
    
    free(numeros);
    
    return 0;
}
""")
s("Nossa! Parece complicado! Em outras linguagens isso é mais fácil?")
t("Usando apenas arrays, não muito, olha esse mesmo exemplo em C#.")
code_cs("""
using System;
        
class Program {
    static void Main() {
        int[] numeros = new int[3] {10, 20, 30};
        
        int[] novo = new int[4];
        Array.Copy(numeros, novo, 3);
        novo[3] = 40;
        
        foreach (int numero in novo) {
            Console.Write(numero + " ");
        }
    }
}
""")
s("Entendi! E se forem muitos elementos? ficaria muito grande o código?")
t("O código em si, não, mas pense agora no custo de copiar todos os elementos de um array para outro. Isso pode ser um problema se tivermos muitos elementos. Já ouviu falar sobre complexidade algorítmica?")
s("Não faço ideia! O que é isso? Pelo nome, parece algo complexo rs...")
t("Hahaha, não é tão complexo assim! A complexidade algorítmica é uma medida de quão eficiente um algoritmo é. No caso de acessar um elemento de um array, a complexidade é O(1).")
s("O que é esse O(1)? Agora complicou mesmo")
t("O(1) significa que o tempo de execução do algoritmo é constante, ou seja, não importa o tamanho do array, o tempo para acessar um elemento é sempre o mesmo.")
q("Não entendi nada... que raio e O é esse? explica esse trem aí pq eu até estava acompanhando, agora com esse O de sei lá o que eu me perdi...")
t("Hahaha, desculpa! Esse O é uma forma de expressar quanto tempo ou quanto de recursos um algoritmo precisa para executar. Esse O é uma forma de expressar isso, quando dizemos O(1), quer dizer que será 1 unidade de tempo para cada instrução, é o mais rápido que dá para ser e quer dizer que o tempo é constante, vai depender de quantos elementos tem no array.")
t("É uma forma de medir, matematicamente, o quanto complexo ou eficiente é um algorítimo, é algo que vocês como programadores devem SEMPRE se preocupar, pois um algoritmo mais eficiente, é um algoritmo que consome menos recursos do computador e é mais rápido.")
s("E quando fica diferente, como fica esse tal de O aí? Ainda não entendi, consegue me dar uns exemplos de como ficaria diferente?")
t("Claro! Vamos ver um exemplo de um algoritmo de complexidade O(n), que significa que o tempo de execução do algoritmo é proporcional ao tamanho do array.")
t("Vou mostrar um exemplo de um algoritmo de complexidade O(n) em C.")
code_c("""
#include <stdio.h>
       
int main() {
    int numeros[5] = {10, 20, 30, 40, 50};
    for (int i = 0; i < 5; i++) {
        printf("%d ", numeros[i]);
    }
    return 0;
}
""")
s("Entendi! Então se eu tiver 5 elementos, vai demorar 5 vezes mais para acessar todos os elementos?")
t("Isso mesmo! Se tivermos 5 elementos, o tempo para acessar todos os elementos será proporcional ao tamanho do array, ou seja, 5 vezes mais. Mas se tivermos 10 elementos, será 10 vezes mais e assim por diante.")
q("Entendi! Mas e se eu quiser adicionar um novo elemento no final do array, dá um trabalhão, né? Como eu resolvo isso?")
t("Bom, aí que entra a lista! Uma lista é uma estrutura de dados que permite adicionar e remover elementos de forma dinâmica. Vamos falar sobre isso?")
s("Claro! Vamos falar sobre lista! O que é uma lista?")
t("Primeiro vamos lembrar uma característica do array, ele é uma estrutura de dados estática, ou seja, tem um tamanho fixo. Isso quer dizer que lá na memória RAM do computador, ele é alocado em um espaço fixo e não podemos mudar isso. É um item na sequência do outro, EM ORDEM! lembra?")
s("Lembro! Todos juntinhos... grudados, em ordem...")
t("Isso mesmo! E como o seu programa sabe o tamanho de cada item da lista, ele consegue fazendo uma conta simples de O(1) saber onde começa e termina cada item, onde cada item está apenas com o índice. Isso torna o acesso a essa lista muito efiiciente, pois ele sabe exatamente onde está cada item.")
q("Mas e se eu quiser adicionar um novo item no final do array vou ter que criar um novo e copiar todo mundo? Caramba! que trampo!! não tem outra forma de resolver isso? Parece terrível de complicado e custoso, vai virar um O de um número bem grande, né?")
t("Hahaha, exatamente! Se vc percebeu isso está me deixando muito orgulhoso!!! Para resolver esse problema, podemos usar uma lista, que é uma estrutura de dados dinâmica, ou seja, podemos adicionar e remover elementos facilmente. Vamos ver como funciona?")
s("Claro! Vamos ver como funciona essa lista! Como eu faço para adicionar um novo item na lista? Mas pera, primeiro, o que é uma lista?")
t("Uma lista é uma estrutura de dados que armazena uma coleção de elementos de forma sequencial, mas diferente de um array, os elementos de uma lista não precisam estar em um espaço fixo na memória RAM. Vamos dar um exemplo simples:")
t("Imagine que temos uma lista de números: [10, 20, 30]. Se quisermos adicionar o número 40 no final da lista, podemos fazer isso facilmente.")
s("Entendi! Mas como eu faço isso?")
t("Vou te mostrar um exemplo de como adicionar um elemento no final de uma lista em C.")
code_c("""
#include <stdio.h>
#include <stdlib.h>
       
struct Node {
    int data;
    struct Node *next;
};
       
struct Node *add(struct Node *head, int data) {
    struct Node *new = malloc(sizeof(struct Node));
    new->data = data;
    new->next = NULL;
    
    if (head == NULL) {
        return new;
    }
    
    struct Node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    current->next = new;
    
    return head;
}
       
int main() {
    struct Node *head = NULL;
    head = add(head, 10);
    head = add(head, 20);
    head = add(head, 30);
    head = add(head, 40);
    
    struct Node *current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    
    return 0;
}
""")
s(f"Pow {c.Teacher()}, isso é muito legal! Mas ainda não entendi muito bem... Você deve estar de sacanagem comigo, né? Isso é muito complicado!")
t("Hahaha, não! Vou explicar de forma mais simples. Uma lista é como uma fila de pessoas, onde cada pessoa está ligada à pessoa da frente. Quando adicionamos um novo elemento na lista, ele é colocado no final da fila.")
t("Cada elemento da lista é chamado de nó e cada nó tem um ponteiro para o próximo nó. Assim, podemos percorrer a lista de nó em nó para acessar os elementos.")
s("É... vc tá achando q eu comi espinafre e a minha força tá toda aí, né? Isso é muito complicado! Mas eu entendi! É como uma fila de pessoas, uma atrás da outra, certo?")
t("Isso mesmo! E se quisermos remover um elemento da lista, podemos fazer isso facilmente. Vamos ver como remover um elemento do início da lista em C. No caso da lista, ela os itens não ficam na memória fisicamente juntos, mas sim ligados por ponteiros. Cada item aponta para os seus vizinhos, usamos ponteiros para fazer isso.")
t("É como se cada item da lista fosse um nó, e cada nó tivesse um ponteiro para o próximo nó. Assim, podemos percorrer a lista de nó em nó para acessar os elementos. Cada nó da lista conhece quem vem antes e quem vem depois, assim você pode ir de um nó para o outro.")
t("Mas como sempre diz o grande sábio Lennon Machado 'Cada escolha é uma renúncia', a lista ligada tem suas vantagens e desvantagens. Aquele código em C que mostrei é legal pois você pode ver como a lista é, mas acredito que seja improvável que você vá usar isso em um projeto real, pois existem bibliotecas que fazem isso de forma mais eficiente. Vamos ver como usamos uma lista em C# por exemplo, mas usando o compoente nativo da linguagem?")
code_cs("""
using System;
using System.Collections.Generic;
        
class Program 
{
    static void Main() 
    {
        var l = new List<int>()
        l.Add(10);
        l.Add(20);
        l.Add(30);
        l.Add(40);

        foreach (var item in l) 
        {
            Console.Write(item + " ");
        }
    }
}
""")
q("Caraca! Isso é muito mais fácil! Por que não começamos com isso?")
t("Hahaha, é verdade! Mas é importante entender como as coisas funcionam por baixo dos panos. Mas você entendeu a diferença entre uma lista ligada e um array?")
s("Entendi! O array é uma lista de itens em ordem, um atrás do outro, e a lista é como uma fila de pessoas, uma atrás da outra, certo?")
t("Isso mesmo! E a lista ligada tem a vantagem de ser dinâmica, ou seja, podemos adicionar e remover elementos facilmente. Mas a desvantagem é que o acesso a um elemento da lista é mais lento, pois precisamos percorrer a lista de nó em nó.")
t("Mas a lista ligada não é a única estrutura de dados que podemos usar. Existem outras estruturas de dados, como a lista duplamente ligada, que tem a vantagem de poder percorrer a lista de trás para frente.")
t("Vamos ver um exemplo de como adicionar um elemento no final de uma lista duplamente ligada em C.")
code_c("""
#include <stdio.h>
       
struct Node {
    int data;
    struct Node *prev;
    struct Node *next;
};
       
struct Node *add(struct Node *head, int data) {
    struct Node *new = malloc(sizeof(struct Node));
    new->data = data;
    new->prev = NULL;
    new->next = NULL;
    
    if (head == NULL) {
        return new;
    }
    
    struct Node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    current->next = new;
    new->prev = current;
    
    return head;
}
       
int main() {
    struct Node *head = NULL;
    head = add(head, 10);
    head = add(head, 20);
    head = add(head, 30);
    head = add(head, 40);
    
    struct Node *current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    
    return 0;
}
""")

s("Pronto... já veio bagunçar tudo de novo... esse negócio de código em C cheio de ponteiros é de amassar o peão...")
t("Hahaha, desculpa! Mas é importante entender como as coisas funcionam por baixo dos panos. Mas você entendeu a diferença entre uma lista ligada e uma lista duplamente ligada?")
s("Entendi! A lista duplamente ligada é como uma lista ligada, mas cada item tem um ponteiro para o próximo e para o anterior, certo?")
t("Isso mesmo! A lista duplamente ligada tem a vantagem de poder percorrer a lista de trás para frente, mas a desvantagem é que cada nó ocupa mais espaço na memória, pois precisa de um ponteiro a mais. Vou montar uma tabelinha mostrando as diferenças, vantagens e desvantagens de cada estrutura dessas: o Array, a lista ligada e a lista duplamente ligada.")
t("Ficou claro a razão que faz a lista ter um custo maior para ser percorrida do que um array? Eu sei que falamos mas não é tão óbvio...")
s("É, você tem razão, ficou meio abstrato... poderia me explicar de uma forma bem simples, com exemplo e mostrar como isso funciona na prática e mostrando o tal do O(xpto) aí?")
t("Claro! Vamos ver um exemplo de como percorrer uma lista em C.")
code_c("""
#include <stdio.h>

//Isso é o que chamamos de um nó da lista      
struct Node {
    int data;
    struct Node *next;
};

//Essa função adiciona um novo elemento no final da lista             
*Node add(struct Node *head, int data) {
    //Aqui efetivamente criamos um nó da lista, é aqui que é feita a alocação de um novo item
    struct Node *new = malloc(sizeof(struct Node));
    new->data = data;
    new->next = NULL;
    
    //Se a lista estiver vazia, o novo nó é o primeiro da lista
    if (head == NULL) {
        return new;
    }

    //Se a lista não estiver vazia, percorremos a lista até o último nó    
    struct Node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    //Adicionamos o novo nó no final da lista
    current->next = new;
    
    return head;
}
       
// Essa função adiciona um novo elemento no final da lista       
void print(struct Node *head) {
    //Percorremos a lista e imprimimos cada elemento
    struct Node *current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        // Note aqui que ele irá passar por todos os nós da lista, um a um, até chegar no final, pulando de um em um, isso gera um O(n) pois ele irá passar por todos os nós da lista
        current = current->next;
    }
}
       
// Essa função adiciona um novo elemento no final da lista       
void print(struct Node *head) {
    struct Node *current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        // Note aqui que ele irá passar por todos os nós da lista, um a um, até chegar no final, pulando de um em um, isso gera um O(n) pois ele irá passar por todos os nós da lista
        current = current->next;
    }
}

// Função principal       
int main() {
    struct Node *head = NULL;
    head = add(head, 10);
    head = add(head, 20);
    head = add(head, 30);
    head = add(head, 40);
    
    print(head);
    
    return 0;
}
""")
t("Complexo a implemtanção, mas o resultado e o uso são simples... mas vamos pensar na complexidade, vamos em um exemplo simples: você tem uma lista com 100 elementos e precisa chegar no item 57, qual seria o caminho que você teria que passar para fazer isso?")
s("Nossa! Teria que passar por todos os 56 itens antes de chegar no 57, né?")
t("Isso mesmo! E se tivermos 1000 elementos? Teríamos que passar por todos os 999 elementos antes de chegar no 1000. Isso é o que chamamos de complexidade O(n), pois o tempo de execução do algoritmo é proporcional ao tamanho da lista.")
s("Entendi! Mas e se eu quiser, por exemplo, acessar o item 537 de um array com 1000 elementos? Como seria?")
t("Se tivermos um array com 1000 elementos, podemos acessar o item 537 diretamente, pois sabemos exatamente onde ele está na memória. Isso é o que chamamos de complexidade O(1), pois o tempo de execução do algoritmo é constante.")
s("UAU!! entendi... então a lista é mais lenta para acessar um item, mas é mais fácil de adicionar e remover itens, né?")
t("Isso mesmo! A lista é mais lenta para acessar um item, pois precisamos percorrer a lista de nó em nó, mas é mais fácil de adicionar e remover itens, pois não precisamos copiar todos os elementos.")
t("Por isso, lembre-se sempre: 'QUAL PROBLEMA VOCÊ PRECISA RESOLVER?'")
t("Se precisar de acesso rápido aos elementos, use um array. Se precisar adicionar e remover elementos com facilidade, use uma lista.")
t("Mas a lista não é a única estrutura de dados que podemos usar. Existem outras estruturas de dados, como filas e pilhas, que são baseadas em listas.")
q("Filas? Pilhas? O que são essas coisas?")
t("Uma fila é uma estrutura de dados que permite adicionar elementos no final e remover elementos do início. É como uma fila de pessoas, onde a primeira pessoa a entrar é a primeira a sair.")
t("É importante você também saber o nome dessas estruturas em inglês, é como normalmente chamamos essas estruturas, olha essa tabelinha aqui")
t("Tabela com o nome da estrutura em PT-BR e em EN-US, em Ascii Art, veja:")
t("""
+-----------------+-----------------+
| PT-BR           | EN-US           |
+-----------------+-----------------+
| Arranjo         | Array           |  
| Lista           | Liste           |
| Fila            | Queue           |
| Pilha           | Stack           |
| Dicionário      | Dictionary      |  
| Mapa            | Map             |
| Matriz          | Matrix          |
+-----------------+-----------------+
""")
s("Arranjo? acho que nunca ouvi assim...")
t("Hahaha, arranjo é o mesmo que array! Mas concordo com você, não é comum chamar de arranjo. Mas e a pilha, você sabe o que é?")
s("Não faço ideia! O que é uma pilha?")
t("Uma pilha é uma estrutura de dados que permite adicionar elementos no topo e remover elementos do topo. É como uma pilha de pratos, onde o último prato a ser colocado é o primeiro a ser retirado. Chamamos esse tipo de lista de LIFO, que significa Last In, First Out.")
t("Vamos ver um exemplo de como usar uma pilha em C.")
code_c("""
#include <stdio.h>
#include <stdlib.h>
       
struct Node {
    int data;
    struct Node *next;
};
       
struct Node *push(struct Node *top, int data) {
    struct Node *new = malloc(sizeof(struct Node));
    new->data = data;
    new->next = top;
    
    return new;
}
       
struct Node *pop(struct Node *top) {
    struct Node *temp = top;
    top = top->next;
    free(temp);
    
    return top;
}
       
int main() {
    struct Node *top = NULL;
    top = push(top, 10);
    top = push(top, 20);
    top = push(top, 30);
    
    top = pop(top);
    
    struct Node *current = top;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    
    return 0;
}
""")
s("Meio complexo esse negócio de C mesmo, pode me mostrar como é o uso em C# usando a implementação padrão da linguagem por favor?")
t("Claro! Vamos ver um exemplo de como usar uma pilha em C#.")
code_cs("""
using System;
using System.Collections.Generic;
        
class Program {
    static void Main() {
        var stack = new Stack<int>();
        stack.Push(10);
        stack.Push(20);
        stack.Push(30);
        
        stack.Pop();
        
        foreach (var item in stack) {
            Console.Write(item + " ");
        }
    }
}
""")
s("Entendi! A pilha é como uma pilha de pratos, o último a entrar é o primeiro a sair, certo?")
t("Isso mesmo! E a fila é como uma fila de pessoas, a primeira a entrar é a primeira a sair. Simples também, certo? Nesse caso chamamos esse tipo de lista de FIFO, que significa First In, First Out. É o exemplo que usamos desde o começo da aula, a fila de pessoas.")
t("E o dicionário, você sabe o que é?")
s("O Aurélio? Aquele que tem todas as palavras? rsrsrs")
t("Hahaha, não! O dicionário é uma estrutura de dados que armazena pares de chave e valor. Cada chave é única e associada a um valor. É como um dicionário de palavras, onde cada palavra tem um significado.")
t("Vamos ver um exemplo de como usar um dicionário em Python.")
code("""
# Criando um dicionário
dicionario = {
    'nome': 'João',
    'idade': 20
}
     
# Acessando um valor do dicionário
print(dicionario['nome'])
""")
s("Entendi! O dicionário é como um dicionário de palavras, onde cada palavra tem um significado, certo?")
t("Isso mesmo! E o dicionário é muito útil para acessar elementos de forma rápida, pois a complexidade para acessar um elemento é O(1). Vamos ver um exemplo de como usar um dicionário em C.")
code_c("""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
       
struct Node {
    char *key;
    int value;
    struct Node *next;
};
       
int hash(char *key) {
    int hash = 0;
    for (int i = 0; i < strlen(key); i++) {
        hash += key[i];
    }
    return hash % 10;
}
       
struct Node *put(struct Node *table[], char *key, int value) {
    int index = hash(key);
    
    struct Node *new = malloc(sizeof(struct Node));
    new->key = key;
    new->value = value;
    new->next = table[index];
    
    table[index] = new;
    
    return table;
}
       
int get(struct Node *table[], char *key) {
    int index = hash(key);
    
    struct Node *current = table[index];
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) {
            return current->value;
        }
        current = current->next;
    }
    
    return -1;
}
       
int main() {
    struct Node *table[10] = {NULL};
    
    table = put(table, "nome", 20);
    table = put(table, "idade", 30);
    
    printf("%d ", get(table, "nome"));
    
    return 0;
}
""")
s("Entendi! O dicionário é muito útil para acessar elementos de forma rápida, pois a complexidade para acessar um elemento é O(1), certo? Mas se te disser que entendi esse código em C aí seria um grande exagero...")
t("Hahaha, não se preocupe! O importante é entender o conceito. E o dicionário é muito útil para acessar elementos de forma rápida, pois a complexidade para acessar um elemento é O(1). Vamos ver como usar isso aí em C# e Python para você entender?")
t("Vamos ver um exemplo de como usar um dicionário em C#.")
code_cs("""
using System;
using System.Collections.Generic;
        
class Program {
    static void Main() {
        var dictionary = new Dictionary<string, int>();
        dictionary.Add("nome", 20);
        dictionary.Add("idade", 30);
        
        Console.WriteLine(dictionary["nome"]);
    }
}
""")
s(f"Agora sim {c.Teacher()}! Entendi! Parece bem tranquilo de usar... e como ficaria em python?")
t("Vamos ver um exemplo de como usar um dicionário em Python. Mas acho que você tá vacilando aí, já fizemos isso... vamos tentar um cara agora mais complexo, vamos combinar essas estruturas de dados, o que acha?")
code("""
# Vamos criar uma agenda de contatos misturando todas essas estruturas de dados
agenda = {
    'contatos': [
        {
            'nome': 'João',
            'telefone': '1234-5678',
            'email': 'joao@email.com',
            'endereco': 'Rua da casa do João'
        },
        {
            'nome': 'Maria',
            'telefone': '9876-5432',
            'email': 'maria@email.com',
            'endereco': 'Rua da casa da Maria'
        }
    ]
}
     
# Acessando um contato da agenda
print(agenda['contatos'][0]['nome'])
""")
s(f"Entendi! Agora sim {c.Teacher()}! Entendi! Parece bem tranquilo de usar... e como ficaria em C#?")
t("Vamos ver um exemplo de como usar um dicionário em C#.")
code_cs("""
using System;
using System.Collections.Generic;
        
class Program {
    static void Main() {
        var agenda = new Dictionary<string, List<Dictionary<string, string>>>();
        agenda.Add("contatos", new List<Dictionary<string, string>>());
        agenda["contatos"].Add(new Dictionary<string, string>() {
            {"nome", "João"},
            {"telefone", "1234-5678"},
            {"email", "joao@email.com",
            {"endereco", "Rua da casa do João"}
        });
        agenda["contatos"].Add(new Dictionary<string, string>() {
            {"nome", "Maria"},
            {"telefone", "9876-5432"},
            {"email", "maria@email.com",
            {"endereco", "Rua da casa da Maria"}
        });

        Console.WriteLine(agenda["contatos"][0]["nome"]);
    }   
}
""")
s("Entendi! Agora sim {c.Teacher()}! Entendi! Parece bem tranquilo de usar... e como ficaria em C? (talvez eu me arrependa disso)")
t("Vamos ver um exemplo de como usar um dicionário em C.")
code_c("""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
       
struct Node {
    char *key;
    char *value;
    struct Node *next;
};
       
int hash(char *key) {
    int hash = 0;
    for (int i = 0; i < strlen(key); i++) {
        hash += key[i];
    }
    return hash % 10;
}
       
struct Node *put(struct Node *table[], char *key, char *value) {
    int index = hash(key);
    
    struct Node *new = malloc(sizeof(struct Node));
    new->key = key;
    new->value = value;
    new->next = table[index];
    
    table[index] = new;
    
    return table;
}
       
char *get(struct Node *table[], char *key) {
    int index = hash(key);
    
    struct Node *current = table[index];
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) {
            return current->value;
        }
        current = current->next;
    }
    
    return NULL;
}
       
int main() {
    struct Node *table[10] = {NULL};
    
    table = put(table, "nome", "João");
    table = put(table, "telefone", "1234-5678");
    table = put(table, "email", "joao@email.com");
    table = put(table, "endereco", "Rua da casa do João");
       
    printf("%s;", get(table, "nome"));
       
    return 0;
}
""")
s("Entendi! Agora sim {c.Teacher()}! Entendi! Parece bem tranquilo de usar... são meio parecidos na ideia né?")
t("Isso mesmo! E essas são apenas algumas das estruturas de dados que podemos usar. Existem muitas outras, como árvores, grafos, conjuntos, entre outras. Mas essas são as mais comuns e mais utilizadas.")
t("O importante aqui é ter noção de que os conceitos são os mesmos, independente da linguagem de programação que você estiver usando. Entender como as estruturas de dados funcionam é essencial para se tornar um bom programador.")
t("E lembre-se sempre: 'QUAL PROBLEMA VOCÊ PRECISA RESOLVER?'")
s("Entendi! Obrigado {c.Teacher()} por me ajudar a entender esses conceitos! Vou continuar estudando para me tornar um bom programador!")
t("De nada! Estou aqui para ajudar no que precisar! Continue estudando e praticando, que você vai longe! Se precisar de ajuda, estou por aqui! Para se tornar mestre nisso aí, use o livro de estruturas de dados fundamentais do Silvio do Lago Pereira, é um dos melhores que temos no Brasil!")
s("Valeu {c.Teacher()}! Até a próxima!")