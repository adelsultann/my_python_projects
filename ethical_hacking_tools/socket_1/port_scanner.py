import socket
import termcolor


def fillter(target, ports):
    print(f"\n starting scan for{str(target)}")
    for port in range(1, ports):
        scan(target, port)


def scan(ip, port):
    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # connect_ex if return 0 that means the port is open otherwise it is closed
        result = s.connect_ex((ip, port))
        if result == 0:
            termcolor.cprint(f"Port {port} is open", 'green')
        else:
            termcolor.cprint(f"Port {port} is Closed", 'red')


    except:
        print("Error")


targets = input("Enter Targets to Scan (split them by,): ")
ports = int(input("Enter How Many Ports: "))

if "," in targets:
    for ips in targets.split(","):
        fillter(ips.strip(" "), ports)
else:
    fillter(targets, ports)
