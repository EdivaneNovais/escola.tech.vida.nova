import socket
from Crypto.Cipher import AES
from base64 import b64decode, b64encode
import json

UDP_IP = "127.0.0.1"

UDP_PORT = 7777

data = b"Hello World!"

key = b64decode('ABEiM0RVZneImQARIjNEVQ==')

cipher = AES.new(key, AES.MODE_CFB)

ct_raw = cipher.encrypt(data)

iv = b64encode(cipher.iv).decode('utf-8')

ct = b64encode(ct_raw).decode('utf-8')

result = bytes(json.dumps({'iv':iv, 'ct':ct, 'aluno': 'Edivane'}), 'utf-8')
print(result)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP

sock.sendto(result, (UDP_IP, UDP_PORT))
