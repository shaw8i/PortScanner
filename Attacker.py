import socket

target = input('target > ')

print('''Options:
          1- Enter a single Port number
          2- Enter a range of Port numbers
          3- Enter specific Ports
          4- change target
          5- exit
          
          -options
          -help
    ''')

while True:

    while True:
        try:
            choice = (input('Select a number > '))
            break
        except:
            pass

    if choice == '1':
        while True:
            try:
                port = int(input("Port number > "))
                break
            except:
                print("[-] Error")
                break
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if sock.connect_ex((target, port)) == 0:
                print("\n[+] Port %i is open\n" % port)
            else:
                print("\n[-] Port %i is closed\n" % port)
        except socket.error as e:
            print(e)

    elif choice == '2':
        while True:
            try:
                first_port, last_port = map(int,input("Enter range of Port numbers > ").split('-'))
                break
            except:
                print("[-] Error")
                break
        for port in range(first_port, last_port+1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if sock.connect_ex((target, port)) == 0:
                    print("[+] Port %i is open" % port)
                else:
                    print("[-] Port %i is closed" % port)
            except socket.error as e:
                print(e)
        print('\n')
    elif choice == '3':
        while True:
            try:
                ports = list(map(int, input("Enter Port numbers > ").split(',')))
                break
            except:
                print("[-] Error")
                break
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if sock.connect_ex((target, port)) == 0:
                    print("[+] Port %i is open" % port)
                else:
                    print("[-] Port %i is closed" % port)
            except socket.error as e:
                print(e)
        print('\n')
    elif choice == '4':
        target = input('target > ')

    elif choice.lower() == 'target':
        print(target)

    elif choice.lower() == 'options':
        print('''Options:
                  1- Enter a Port number
                  2- Enter a range of Ports numbers
                  3- change target
                  4- exit

                  -options
                  -help
            ''')
    elif choice.lower() == 'help':
        print('''Note: 
                2- for scanning range of ports write startingPort-finishingPort 
                e.g. '1-1000'
                
                3- for scanning a specific ports write the ports with a comma between them
                e.g. '80,443,...'
                ''')

    elif choice == '5':
        exit()

    else:
        print("\n Wrong Input !\n")
