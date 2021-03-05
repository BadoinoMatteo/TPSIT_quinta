import socket

ipServer='127.0.0.1'
porta = 5000

def main ():
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipServer, porta))
    body = "username=matteo&password=1234"
    msg = f"POST http://127.0.0.1:5000/index/ HTTP/1.1\r\n" \
          f"Host:  http://127.0.0.1:5000\r\n" \
          f"Content-Length: {len(body)}\r\n" \
          f"Content-Type: application/x-www-form-urlencoded\r\n" \
          f"\r\n"\
          f"{body}"
    print(msg)
    client.sendall(msg.encode())
    data = (client.recv(4096)).decode()
    print(data)


if __name__ == '__main__':
    main()