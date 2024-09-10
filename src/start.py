#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import os
import sys
import time

print(f"""
██      ███████  █████  ██████  ███    ██      ██████  ██████  ███████     ██████   ██████  ████████ 
██      ██      ██   ██ ██   ██ ████   ██     ██    ██ ██   ██ ██          ██   ██ ██    ██    ██    
██      █████   ███████ ██████  ██ ██  ██     ██    ██ ██████  ███████     ██████  ██    ██    ██    
██      ██      ██   ██ ██   ██ ██  ██ ██     ██    ██ ██           ██     ██   ██ ██    ██    ██    
███████ ███████ ██   ██ ██   ██ ██   ████      ██████  ██      ███████     ██████   ██████     ██   
      """)

path = "lessons"

lessons = []
for f in listdir(path): 
    if isfile(join(path, f)) and f.endswith(".py"):
        lessons.append(f)

lessons.sort()

print("\nAulas disponíveis:")
for i in range(len(lessons)):
    pos = i+1
    print(f" {pos:>3}: {os.path.splitext(lessons[i])[0]}")

k = input("\nEscolha uma aula: ")

try:
    lesson = int(k)
except:
    print("Opção inválida, digite por favor o número da aula")
    time.sleep(2)
    sys.exit()
    
if lesson < 1 or lesson > len(lessons):
    print("Opção inválida, escolha um número de aula válido")
    sys.exit()
    
lesson = lessons[lesson-1]
cmd = f"'{sys.executable}' '{os.getcwd()}/{path}/{lesson}'"
print(f"Você escolheu a aula {lesson}")

try:
    os.system(cmd)
    time.sleep(2)
except KeyboardInterrupt:
    sys.exit(0)
