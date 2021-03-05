import socket

ip='127.0.0.1'
porta=6000

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,porta))
print("collegato")
while True:
    data=(client.recv(4096).decode())
    risultato=str(eval(data))
    client.sendall(risultato.encode())
    #client.sendall("exit".encode())
client.close()