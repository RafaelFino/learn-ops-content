#!/bin/bash
cd src
echo "Starting..."
ttyd -p 5002 -m 20 -W -t titleFixed='Learn Ops BOT' ./start.py