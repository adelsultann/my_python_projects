import socket


host = "192.168.47.128"
port = 7777

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


s.connect((host, port))

# to test the app go to your other machine and run the following command
# nc -lnvp 7777