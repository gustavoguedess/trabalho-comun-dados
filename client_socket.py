import socket
from datetime import datetime
import random
from colorama import Fore, init, Back

# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]
sep=':::'

class Client:
    def __init__(self, client_name):
        self.name = client_name
        self.socket = socket.socket()
        self.room = ''
        self.color = random.choice(colors)

    def set_server(self, ip):
        self.server_host = ip 
        self.server_port = 8860
        self.connect()
    
    def set_room(self, room):
        self.room = room

    def listen(self):
        print('Ouvindo...')
        message = self.socket.recv(1024).decode()
        print("\n" + message)
        print('Parou de ouvir')
    
    def connect(self):
        print(f"[*] Conectando ao {self.server_host}:{self.server_port}...")
        self.socket.connect((self.server_host, self.server_port))
        print(f"[*] Conectado!")

    def send_message(self, msg):
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        message = f"[{date_now}] {self.name}:{msg}"
        encode_msg = f"{self.room}{sep}" + self.encode(message)
        self.send(encode_msg)
        print('mensagem enviada: ', encode_msg)
    
    def encode(self, msg):
        #TODO encode
        return msg

    def quit(self):
        self.socket.close()




name = input('Digite seu nome: ')
client = Client(name)
server = input('server: ')
server = server if server else 'localhost'
client.set_server(server)

while True:
    client.listen()

    msg = input()
    print(msg)
    if msg == 'q':
        print('Saindo...')
        client.quit()
        break
    
    if msg:
        client.send_message(msg)