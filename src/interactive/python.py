#!/usr/bin/env python3

# Importing the chat class from the talker module
from talker import chat

# Tema: Python
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
# Sobre o tema:

c = chat.Chat()
c.ShowCommand( """python3 -m venv 'venv' && ls -lha && pwd""" )
c.ShowCode( """
# Python
# Exemplo de criação de variavel
num = 10
print(num)
# Exemplo de criação de lista
lista = [1, 2, 3, 4, 5]
print(lista)
# Exemplo de criação de dicionário
dicionario = {'nome': 'Fino', 'idade': 30}
print(dicionario)
# Exemplo de criação de função
def soma(a, b):
    return a + b
print(soma(10, 20))
# Exemplo de
for i in range(10):
    print(i)
# Exemplo de
if num > 10:
    print('Maior que 10')
else:
    print('Menor ou igual a 10')
"""
)
