#!/bin/python3

# Hello, I am --> Juliet <--

import socket as sock

firstpeer = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)

addr = "127.0.0.1"
port = 9999

firstpeer.bind((addr, port))

buffer = (1024)

firstpeer.sendto("test".encode(), ("127.0.0.1", 8888))

firstpeer.close()
