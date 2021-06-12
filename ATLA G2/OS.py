import time
import os

print("""
░█████╗░████████╗██╗░░░░░░█████╗░  ░██████╗░██████╗░
██╔══██╗╚══██╔══╝██║░░░░░██╔══██╗  ██╔════╝░╚════██╗
███████║░░░██║░░░██║░░░░░███████║  ██║░░██╗░░░███╔═╝
██╔══██║░░░██║░░░██║░░░░░██╔══██║  ██║░░╚██╗██╔══╝░░
██║░░██║░░░██║░░░███████╗██║░░██║  ╚██████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░╚═════╝░╚══════╝
""")
print("""
[1] Jatka asennusta.
[2] Olen jo tehnyt asennuksen.
""")
setup = input("[system32]: ")
if setup == '1':
    name = input(str("Olkaa hyvä ja antakaa käyttäjä nimenne: "))
    pas = input(str("Olkaa hyvä ja antakaa salasananne: "))
    lines = [name]
    with open('Käyttäjä/Käyttäjänimi.txt', 'w') as f:
        f.writelines(lines)

    lines2 = [pas]
    with open('Käyttäjä/Salasana.txt', 'w') as f:
        f.writelines(lines2)
    print("Asennus onnistui!")
    input("Paina enter poistuaksesi.")

if setup == '2':
    login_pass = open('Käyttäjä/Salasana.txt')
    login_name = open('Käyttäjä/Käyttäjänimi.txt')
    l_p = login_pass.read()
    l_n = login_name.read()

while True:
    login = input(str("Olkaa hyvä ja antakaa salasana osoitteeseen: " + l_n))
    if login == l_p:
        os.startfile("Kotisivu.py")
        break
    else:
        print("Väärä salasana! Yritä uudelleen.")
