#!/bin/python3

import socket as sock

import threading
assert threading # Stop complaining about threading not being used yet

secondpeer = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)

addr = "127.0.0.1"
firstport = 8888

secondpeer.bind((addr, firstport))

buffer = 1024
data, addr = secondpeer.recvfrom(buffer)

print(data.decode())
