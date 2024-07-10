#!/usr/bin/env python3

# Importing the chat class from the talker module
from talker import chat

c = chat.Chat()
c.ShowCode("""
minhaVar = False
print(minhaVar)
""", lexer="python")

c.ShowCommand("""
docker run -d -p 8080:80 nginx
""")

c.ShowCode("""
FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py
           """, lexer="docker")
