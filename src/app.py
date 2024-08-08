#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import os

path = "lessons"
lessons = []
for f in listdir(path): 
    if isfile(join(path, f)):
        lessons.append(f)

print("\nAulas disponíveis:")
for i in range(len(lessons)):
    print(f" {i+1}: {lessons[i]}")

lesson = int(input("\nEscolha uma aula: "))
lesson = lessons[lesson-1]
print(f"Você escolheu a aula {lesson}")
os.system(f"python3 {path}/{lesson}")
