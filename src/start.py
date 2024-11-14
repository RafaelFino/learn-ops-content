#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join
import os
import sys
import time
import sqlite3

print(f"""
██      ███████  █████  ██████  ███    ██      ██████  ██████  ███████     ██████   ██████  ████████ 
██      ██      ██   ██ ██   ██ ████   ██     ██    ██ ██   ██ ██          ██   ██ ██    ██    ██    
██      █████   ███████ ██████  ██ ██  ██     ██    ██ ██████  ███████     ██████  ██    ██    ██    
██      ██      ██   ██ ██   ██ ██  ██ ██     ██    ██ ██           ██     ██   ██ ██    ██    ██    
███████ ███████ ██   ██ ██   ██ ██   ████      ██████  ██      ███████     ██████   ██████     ██   
      """)

def insertMetric(name: str, value: float = 1):
    db = sqlite3.connect('metrics.db', isolation_level=None, check_same_thread=False)
    cursor = db.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS metrics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL, 
                    value decimal DEFAULT 1,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
                   );""")
    
    cursor.execute("INSERT INTO metrics (name, value) VALUES (?, ?)", (name, value,))    
    db.close()

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

insertMetric("app.load")
k = input("\nEscolha uma aula: ")
start = time.time()
try:
    lesson = int(k)
except:
    print("Opção inválida, digite por favor o número da aula")
    time.sleep(2)
    insertMetric("invalid.option")
    sys.exit()
    
if lesson < 1 or lesson > len(lessons):
    print("Opção inválida, escolha um número de aula válido")
    insertMetric("invalid.option")
    sys.exit()
    
lesson = lessons[lesson-1]
cmd = f"'{sys.executable}' '{os.getcwd()}/{path}/{lesson}'"
print(f"Você escolheu a aula {lesson}")
insertMetric(f"""{lesson}.start""")

try:
    os.system(cmd)
    insertMetric(f"""{lesson}.end""", float(time.time() - start))
    time.sleep(2)
except KeyboardInterrupt:
    insertMetric(f"""{lesson}.interrupted""", float(time.time() - start))
    sys.exit(0)

