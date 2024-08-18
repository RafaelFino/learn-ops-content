#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import os
import sys

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
    exit()
    
if lesson < 1 or lesson > len(lessons):
    print("Opção inválida")
    exit()
    
lesson = lessons[lesson-1]
cmd = f"'{sys.executable}' '{os.getcwd()}/{path}/{lesson}'"
print(f"Você escolheu a aula {lesson}")

os.system(cmd)
