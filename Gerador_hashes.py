import hashlib
import sys
import threading

menu = int(input(''' ###### MENU - ESCOLHA O TIPO DE HASH #####
1) MD5
2) SHA1
3) SHA256
4) SHA512
5) Sair
Digite o número do hash a ser gerado '''))
print('-'*60)


if menu == 1:
    with open('lista.txt', 'r') as file:
        for i in file:
            resultado = hashlib.md5(i.encode('utf-8'))
            print("O resultado MD5 é {}".format(resultado.hexdigest()))
            print('-'*60)
            
      
elif menu == 2:
    with open('lista.txt', 'r') as file:
        for i in file:
            resultado = hashlib.sha1(i.encode('utf-8'))
            print("O resultado SHA1 é {}".format(resultado.hexdigest()))
            print('-'*60)

elif menu == 3:
    with open('lista.txt', 'r') as file:
        for i in file:
            resultado = hashlib.sha256(i.encode('utf-8'))
            print("O resultado SHA256 é {}".format(resultado.hexdigest()))
            print('-'*60)

elif menu == 4:
    with open('lista.txt', 'r') as file:
        for i in file:
            resultado = hashlib.sha512(i.encode('utf-8'))
            print("O resultado sha512 é {}".format(resultado.hexdigest()))
            print('-'*60)

elif menu == 4:
    sys.exit()



