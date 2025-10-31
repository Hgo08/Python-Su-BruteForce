# Python-Su-BruteForce
A python script to escalate to a desired used using bruteforce

## Usage:
main.py [-h] -w WORDLIST -u USER [-T THREADS] [-t TIMEOUT] [-v]

options:

  -h, --help                show this help message and exit
  
  -w, --wordlist WORDLIST   Ruta del diccionario de contraseñas
  
  -u, --user USER           Usuario para probar contraseñas
  
  -T, --threads THREADS     Threads a usar, por defecto 8
  
  -t, --timeout TIMEOUT     Timeout

example: 
```shell
python main.py -u test -w /usr/share/wordlists/fasttrack.txt
```
<img width="613" height="265" alt="image" src="https://github.com/user-attachments/assets/4be61bd3-cabc-432c-bf6e-f9516baab5a5" />
