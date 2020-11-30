import re
import socket
import turtle


# 0.0,B50R90F600L90F400
# B 50  R 90    F 600   L 90    F 400
# [(b, 50), ]s

ip='127.0.0.1'
porta=8000

def client():
    print("creo istanza")
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate

    c.connect((ip,porta))
    print("connect")

    print("Enter 'exit' to end the connection")
    msg = input("->")  # take input
    alphabot = Alphabot()
    while True:
        try:
            c.sendall(msg.encode())  # send message
        except:
            print(f"failed")

        data = c.recv(4096).decode()  # receive response
        print(f"Received from server: {data}")  # show response
        data = (data.split(","))[1]
        lista_potenze = re.split('B|R|F|L', data)
        lista_potenze.pop(0)
        regex = ''
        for index, el in enumerate(lista_potenze):
            if index == len(lista_potenze) - 1:
                regex += el
            else:
                regex += el + '|'
        lista_direzioni = re.split(regex, data)
        lista_direzioni.pop(-1)
        comandi = []
        for index, el in enumerate(lista_potenze): comandi.append((lista_direzioni[index], int(el)))
        print(comandi)
        for el in comandi: istruction(alphabot, el[0], el[1])
        msg = input("->")  # again take input

        if msg == "exit":
            c.sendall(msg.encode())  # send message
            print("Close the connection")
            break

    c.close()  # close the connection


def istruction(alphabot, command, number):
    switcher = {
        "F": alphabot.forward,
        "B": alphabot.backward,
        "R": alphabot.right,
        "L": alphabot.left
    }
    switcher[command](number)




class Alphabot(object):

    def __init__(self):
        self.turtle = turtle.Turtle()

    def forward(self, potenza):
        self.turtle.fd(potenza)

    """def stop(self):
        self.turtle.fd(potenza)"""

    def backward(self, potenza):
        self.turtle.bk(potenza)

    def left(self, potenza):
        self.turtle.lt(potenza)

    def right(self, potenza):
        self.turtle.right(potenza)

    def setPWMA(self, value):
        self.PWMA.ChangeDutyCycle(value)

    """
    def setPWMB(self,value):
        self.PWMB.ChangeDutyCycle(value)    

    def setMotor(self, left, right):
        if((right >= 0) and (right <= 100)):
            GPIO.output(self.IN1,GPIO.HIGH)
            GPIO.output(self.IN2,GPIO.LOW)
            self.PWMA.ChangeDutyCycle(right)
        elif((right < 0) and (right >= -100)):
            GPIO.output(self.IN1,GPIO.LOW)
            GPIO.output(self.IN2,GPIO.HIGH)
            self.PWMA.ChangeDutyCycle(0 - right)
        if((left >= 0) and (left <= 100)):
            GPIO.output(self.IN3,GPIO.HIGH)
            GPIO.output(self.IN4,GPIO.LOW)
            self.PWMB.ChangeDutyCycle(left)
        elif((left < 0) and (left >= -100)):
            GPIO.output(self.IN3,GPIO.LOW)
            GPIO.output(self.IN4,GPIO.HIGH)
            self.PWMB.ChangeDutyCycle(0 - left)"""

    """
    def istruction(istr, t):
    istr = istr.decode()
    command = istr.split("_")[0]
    number = int(istr.split("_")[1])
    switcher = {
        "forward": forward,
        "f": forward,
        "backward": backward,
        "b": backward,
        "right": right,
        "r": right,
        "left": left,
        "l":left
    }
    switcher[command](t, number)

def forward(t, number):
    t.fd(number)
def backward(t, number):
    t.bk(number)
def right(t, number):
    t.right(number)
def left(t, number):
    t.left(number)
    """

if __name__ == '__main__':
    client()