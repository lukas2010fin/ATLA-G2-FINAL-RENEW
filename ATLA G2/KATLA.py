import subprocess
import platform
import socket
import time
import os

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("KATLA V 0.1.0, ATLA copyright act 2021. Kaikki oikeudet on pidätetty.")
while True:
    code = input(">>> ")
    if code == 'ping':
        host = input("Syötä verkko ospite joka täytyy pingata: ")
        number = input("Kuinka monta kertaa pingataan: ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'local':
        print("Sinun IP on: " + host_ip)
        print("Sinun koneen nimi on: " + host_name)
    if code == 'date':
        print("Päivämäärä(PP/KK/VV)" + time.strftime("%d/%m/%y"))
    if code == 'list':
        dir_list = os.listdir(path)
        print("Kansiot ja kohteet paikassa '", path, "' :")
        print(dir_list)
    if code == 'list -a':
        file = input("Syötä suora tiedostopolku luettavaksi: ")
        dir_list2 = os.listdir(file)
        print("Tiedostot ja hakemistot '", file, "':")
        print(dir_list2)
    if code == 'echo me':
        echo = input("Mitä sinä haluat minun kuuluttavan: ")
        print(echo)