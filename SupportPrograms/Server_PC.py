#!/usr/bin/env python3

import socket
from time import sleep
import sys
from struct import pack,Struct,unpack

def write(text):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host, port = '127.0.1.1', 6502
    server_address = (host, port)

    # Generate some random start value

    # Send a message
    # Pack three 32-bit floats into message and send
    s = Struct('10s')
    message = s.pack(text.encode("utf-8"))
    sock.sendto(message, server_address)
    sleep(3)
    
def read():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    host, port = '192.168.1.2', 65000
    server_address = (host, port)

    sock.bind(server_address)

    while True:
        message, address = sock.recvfrom(4096)

        one= unpack('30s',message)
        return one