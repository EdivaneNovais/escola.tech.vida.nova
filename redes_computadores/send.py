import socket
from unittest import result

UDP_IP = "127.0.0.1"

UDP_PORT =  7777

result = b"Edivane!"

print("UDP target IP: %s" % UDP_IP)

print("UDP target port: %s" % UDP_PORT)

print("message: %s" % result)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP

sock.sendto(result, (UDP_IP, UDP_PORT))

