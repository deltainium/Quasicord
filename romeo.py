#!/bin/python3

# Hello, I am --> Romeo <--

import socket as sock

import threading
assert threading # Stop complaining about threading not being used yet

def incoming(juliet_addr, juliet_port):
    juliet = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
    juliet.bind((juliet_addr, juliet_port))


def outgoing(addr, port):
    



juliet_addr = "127.0.0.1"
juliet_port = 8888

buffer = 1024
data, addr = secondpeer.recvfrom(buffer)

print(data.decode())
