import time
import os
import socket
import psutil

battery = psutil.sensors_battery()
login_pass = open('Käyttäjä/Salasana.txt')
login_name = open('Käyttäjä/Käyttäjänimi.txt')
l_p = login_pass.read()
l_n = login_name.read()
print("""
░█████╗░████████╗██╗░░░░░░█████╗░  ░██████╗░██████╗░
██╔══██╗╚══██╔══╝██║░░░░░██╔══██╗  ██╔════╝░╚════██╗
███████║░░░██║░░░██║░░░░░███████║  ██║░░██╗░░░███╔═╝
██╔══██║░░░██║░░░██║░░░░░██╔══██║  ██║░░╚██╗██╔══╝░░
██║░░██║░░░██║░░░███████╗██║░░██║  ╚██████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░╚═════╝░╚══════╝
""")
print("Aika: " + time.strftime("%d/%m/%y"))
print("""
[1] Google
[2] Teksti editori
[3] Resurssien hallinta
[4] BIOS
[5] Sulje G2 turvallisesti
[6] KATLA
[7] SIIM
""")
select = input("[system-8]: ")

if select == '1':
    os.startfile('Internet.py')

if select == '2':
    os.startfile('PATA.py')

if select == '3':
    os.startfile('Resurssienhallinta.py')

if select == '4':
    while True:
        login = input(str("Olkaa hyvä ja antakaa salasana osoitteeseen: " + l_n + " "))
        if login == l_p:
            print("Avataan BIOSia...")
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print("[1] Käyttäjänimi: " + l_n)
            print("[2] Salasana: " + l_p)
            print("operoijan nimi: " + host_name)
            print("IP: " + host_ip)
            edit_b = input("Paina [?] jotta voit vaihtaa asetuksia: ")
            if edit_b == '1':
                edit_c = input("Anna uusi käyttäjänimi: ")
                with open('Käyttäjä/Käyttäjänimi.txt', 'w') as f:
                    f.writelines(edit_c)
                print("Käyttäjänimi vaihdettu nimeen: " + edit_c)
                input("Paina oikeassa yläkulmassa olevaa rastia sulkeaksesi ikkunan(muuten se ei onnistu)")

            if edit_b == '2':
                edit_d = input("Anna uusi salasana: ")
                with open('Käyttäjä/Salasana.txt', 'w') as f:
                     f.writelines(edit_d)
                print("Salasana vaihdettu sanaan: "+ edit_d)
                input("Paina oikeassa yläkulmassa olevaa rastia sulkeaksesi ikkunan(muuten se ei onnistu)")

if select == '6':
    os.startfile('KATLA.py')

if select == '7':
    os.startfile('SIIM.py')