# Python-Su-BruteForce
A python script to escalate to a desired used using bruteforce
   _____                  ____             _       ______                  
  / ____|                |  _ \           | |     |  ____|                 
 | (___  _   _   ______  | |_) |_ __ _   _| |_ ___| |__ ___  _ __ ___ ___  
  \___ \| | | | |______| |  _ <| '__| | | | __/ _ \  __/ _ \| '__/ __/ _ \ 
  ____) | |_| |          | |_) | |  | |_| | ||  __/ | | (_) | | | (_|  __/ 
 |_____/ \__,_|          |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___| 

============================ Created by Hgo08 =============================

usage: main.py [-h] -w WORDLIST -u USER [-T THREADS] [-t TIMEOUT] [-v]

options:
  -h, --help            show this help message and exit
  -w, --wordlist WORDLIST
                        Ruta del diccionario de contraseñas
  -u, --user USER       Usuario para probar contraseñas
  -T, --threads THREADS
                        Threads a usar, por defecto 8
  -t, --timeout TIMEOUT
                        Timeout
  -v, --verbose         Timeout

example: 
```shell
python main.py -u test -w /usr/share/wordlists/fasttrack.txt
```
<img width="613" height="265" alt="image" src="https://github.com/user-attachments/assets/4be61bd3-cabc-432c-bf6e-f9516baab5a5" />
