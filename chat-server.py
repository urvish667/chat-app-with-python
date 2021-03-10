#importing libraries for networking
#and threading
import os
import time
import socket
import threading

#protocol : UDP
protocol = socket.SOCK_DGRAM

#net address family : IPv4
net_address = socket.AF_INET

#socket module object
sckt = socket.socket(net_address, protocol)

#declaring variables for IP and Port 
#for this server
ip = "192.168.43.137"
port = 1234

#binding the IP address and Port
#IP + Port = Socket
sckt.bind((ip, port))

print("*****CHAT APPLICATION*****")
print("Enter exit to end the chat")
remote_ip = input("Enter Remote IP: ")

#For sending the message to the receiver
def msg_recv():
    while True:
        msg = sckt.recvfrom(1024)
        if msg[0].decode() == "1":
            print("Chat has been stopped by remote user!!!")
            os._exit(1)
        print("\t\t\t\tmsg: {0}:{1}".format(msg[0].decode(), msg[1][0]))

#For receiving the message from the sender	
def msg_send():
    while True:
        msg = input()
        if msg == "quit":
            print("Chat has been ended")
            sckt.sendto("1".encode(), (remote_ip, 1234))
            os._exit(1)
        sckt.sendto(msg.encode(), (remote_ip, 1234))
	
#Threads are used to provide
#multi-threading to the server
t1 = threading.Thread(target=msg_recv)
t2 = threading.Thread(target=msg_send)
t1.start()
t2.start()
