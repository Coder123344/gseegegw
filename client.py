import socket
from threading import Thread
nickname=input("Hi, Whats your Name?!")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000
client.connect((ip_address,port))
print("Bro, ur thing connected")

def recieve():
    while True:
        try:
            msg=client.recv(2048).decode('utf-8')
            if msg=='NICKNAME':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print("Bro, ur stuff aint working")
            client.close()     
            break
def write():
    while True:
        msg='{}:{}'.format(nickname,input(''))
        client.send(msg.encode('utf-8'))

recieve_thread=Thread(target=recieve)
recieve_thread.start()
write_thread=Thread(target=write)
write_thread.start()