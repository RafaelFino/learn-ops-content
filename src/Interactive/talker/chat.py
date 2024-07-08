# -*- coding: utf-8 -*-
import os
import random
from time import sleep


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

    def __init__(self, teacher, student):
        self._student = student
        self._teacher = teacher

    def Speak(self, msg):
        for line in msg.splitlines():
            print(color.END + color.PURPLE + color.BOLD + "# [{0}] ".format(self._teacher) +
                  color.END + color.GREEN + line + color.END)
            # Espera um pouquinho para cada linha poder ser lida...
            sleep(len(line)/100)

    def StudentComment(self, msg):
        print(color.END + color.DARKCYAN + color.BOLD +
              "\n# [{0}] ".format(self._student) + color.END + color.YELLOW + msg + color.END)
        # tempo para entender oq está acontecendo
        sleep(2)

    def Question(self, msg, wait=True):
        print(color.END + color.DARKCYAN + color.BOLD +
              "\n# [{0}] ".format(self._student) + color.END + color.YELLOW + msg + color.END)
        # tempo para entender oq está acontecendo
        sleep(2)
        if wait:
            self.NextStep()

    def ShowCode(self, code, wait=True, run=True):
        print(color.END + color.BOLD + "\n# [Python code] - START" + color.END)
        print(color.END + color.BOLD + color.BLUE +
              "{}".format(code) + color.END)
        if run:
            print(color.END + color.BOLD +
                  "# [Python code] - EXEC:\n" + color.END)
            exec(code)

        print(color.END + color.BOLD +
              "# [Python code] - END\n" + color.END)
        
        if wait:
            self.AskEnter()

    def ShowCommand(self, command, wait=True, run=False):
        print(color.END + color.BOLD + "\n# [Shell command] - START" + color.END)
        print("\n")
        print(color.END + color.BOLD + color.BLUE +
              "{}".format(command) + color.END)
        print("\n")
        if run:
            print(color.END + color.BOLD +
                  "# [Shell command] - EXEC:\n" + color.END)
            os.system(command)

        print(color.END + color.BOLD +
              "# [Shell command] - END\n" + color.END)
        
        if wait:
            self.AskEnter()

    def PrintResult(self, msg):
        print(color.END + color.CYAN + "# RESULTADO: {}".format(msg) + color.END)

    def AskEnter(self):
        print(color.END + color.PURPLE + color.BOLD + "# [{0}] ".format(self._teacher) +
              color.END + color.BOLD + pressEnterMessages[random.randint(0, len(pressEnterMessages)-1)] + color.END)
        input()

    def NextStep(self):
        self.Speak(nextStepMessages[random.randint(
            0, len(nextStepMessages)-1)])
        self.AskEnter()
