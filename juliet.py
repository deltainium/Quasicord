#!/bin/python3

# Hello, I am --> Juliet <--

import socket as sock

import threading
assert threading


juliet_addr = "127.0.0.1"
juliet_port = 9999

def startup(juliet_addr, juliet_port):
    juliet = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
    juliet.bind((juliet_addr, juliet_port))
    return(juliet)
    

def ping(juliet):
    juliet.sendto("ping".encode("utf-8"), ("127.0.0.1", 8888))
    status, romeo_addr = juliet.recvfrom(4)
    if status.decode() == "conf":
        print("Pass")
        pass
    else:
        print("Fail")
        
juliet = startup(juliet_addr, juliet_port)

ping(juliet)
juliet.close()
