# -*- coding: utf-8 -*-
import os
import random
from time import sleep
import time
import sys
from pprint import pformat
from typing import Any

from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer, BashLexer

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


nextStepMessages = [
    """Ok, entendi...""",
    """Certo, vamos ver esse negócio""",
    """Hummm... interessante!""",
    """Vamos falar sobre isso...""",
    """Bom ponto! Vamos falar disso aí...""",
    """Não é complexo, vamos olhar de perto...""",
    """Vamos ver isso aí...""",
    """Olha... vc tem razão, um passo de cada vez, vamos explicar essa parte...""",
    """Estamos indo bem, vamos chegar lá..."""
    """Vamos com calma... vou te explicar isso...""",
    """Um passo de cada vez querido Doença...""",
    """Vamos chegar nesse dia...""",
    """Qual problema você quer resolver? (tenho q dizer isso... rs...)"""
    """Vamos ver isso aí...""",
]

pressEnterMessages = [
    """Para continuar, aperta o ENTER aí...""",
    """ENTER e vamos em frente...""",
    """Será que hoje vai chover? Aperta o ENTER aí para seguir...""",
    """Aperta o ENTER aí vai...""",
    """Manda um ENTER pra continuarmos...""",
    """Só estou esperando vc apertar o ENTER para seguirmos...""",
    """No seu tempo campeão... aperta o ENTER aí quando vc quiser...""",
    """E aí? td bem com vc? quando estiver de boa, aperta o ENTER aí que continuamos... """,
    """Tá divertido? quando quiser, aperta o ENTER que vamos em frente..."""
    """Vamos com calma...mas vc precisa apertar o ENTER para continuarmos...""",    
    """Aperta o ENTER aí...""",
    """Quando vc estiver de boa, aperta o ENTER aí que continuamos...""",
    """Aperta o ENTER aí que vamos em frente...""",
    """Vamos lá, aperta o ENTER aí...""",
    """CTRL+C para tudo, mas se vc quiser continuar, aperta o ENTER aí...""",
    """Tá com preguiça? aperta o ENTER aí que continuamos...""",
    """Eu tbm tô cansado, mas aperta o ENTER aí que continuamos...""",
    """Sei que é muita coisa, mas temos que continuar, aperta o ENTER aí...""",
    """Ah... nem é tão complicado assim, sei que vc já fez coisa pior.. aperta o ENTER aí...""",
    """Se precisar, vai buscar um café e depois aperta o ENTER aí...""",
]


def ClearScreen():
    # Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # windows
        _ = os.system('cls')


class Chat:
    _teacher = ""
    _student = ""
    _wait = 1

    def __init__(self):
        self._student = os.getlogin()
        self._teacher = "Fino"

    def slowPrint(self, msg):       
        for char in msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)

    def Speak(self, msg):
        for line in msg.splitlines():
            print(color.END + color.PURPLE + color.BOLD + "# [{0}] ".format(self._teacher) +
                  color.END + color.GREEN, end="")
            self.slowPrint(line)
            print(color.END)

            # Espera um pouquinho para cada linha poder ser lida...
            sleep(len(line)/200)

    def StudentComment(self, msg):
        print(color.END + color.DARKCYAN + color.BOLD +
              "\n# [{0}] ".format(self._student) + color.END + color.YELLOW, end="")
        self.slowPrint(msg)
        print(color.END)
        sleep(self._wait)

    def Question(self, msg, wait=True):
        print(color.END + color.DARKCYAN + color.BOLD +
              "\n# [{0}] ".format(self._student) + color.END + color.YELLOW, end="")
        self.slowPrint(msg)
        print(color.END)
        sleep(self._wait)
        if wait:
            self.NextStep()

    def ShowCode(self, code, wait=True, run=True):
        print(color.END + color.BOLD + "# [Python code]:" + color.END)
        print(highlight(code, PythonLexer(), Terminal256Formatter()))
        if run:
            print(color.END + color.BOLD +
                  "\n# [Python code] - Exec:" + color.END)
            exec(code)
            print(color.END + "\n")
        
        if wait:
            self.AskEnter()

    def ShowCommand(self, command, wait=True, run=False):
        print(color.END + color.BOLD + "\n# [Shell command]:" + color.END)
        for line in command.splitlines():
            print(color.END + color.BOLD + color.GREEN + "$> " + color.END, end="")
            print(highlight(line, BashLexer(), Terminal256Formatter()))
        if run:
            print(color.END + color.BOLD +
                  "# [Shell command] - EXEC:\n" + color.END)
            os.system(command)
        
        if wait:
            self.AskEnter()

    def PrintResult(self, msg):
        print(color.END + color.CYAN + "# Result: {}".format(msg) + color.END)

    def AskEnter(self):
        print(color.END + color.PURPLE + color.BOLD + "# [{0}] ".format(self._teacher) +
              color.END + color.BOLD + pressEnterMessages[random.randint(0, len(pressEnterMessages)-1)] + color.END)
        input()

    def NextStep(self):
        self.Speak(nextStepMessages[random.randint(
            0, len(nextStepMessages)-1)])
        self.AskEnter()
