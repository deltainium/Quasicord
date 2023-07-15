#!/bin/python3

# Hello, I am --> Romeo <--
# By convention Juliet is meant to ping first

import socket as sock

import threading
assert threading # Stop complaining about threading not being used yet


romeo_addr = "127.0.0.1"
romeo_port = 8888

juliet_addr = "127.0.0.1"
juliet_port = 9999

# Require's romeo's address and port
def startup(romeo_addr, romeo_port):
    romeo = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
    romeo.bind((romeo_addr, romeo_port))
    return(romeo)

def ping(romeo, juliet_addr, juliet_port):
    status = romeo.recvfrom(4)
    if status[0].decode() == "ping":
        romeo.sendto("conf".encode("utf-8"), (juliet_addr, juliet_port))
        print("Pass")
        pass
    else:
        #try again
        print("Fail")

def request(romeo, juliet_addr, juliet_port):
    while True:
        choice = input("Would you like to request a call? (y/n): ")
        goodvals = ("y", "n")
        if choice not in goodvals:
            print("You have made an invalid selection, please try again.")
            continue
        else:
            if choice == "y":
                t = threading.Thread(target=transmit, args=(), daemon=True)
                r = threading.Thread(target=recieve, args=(juliet_addr, juliet_port), daemon=True)

                t.start()
                r.start()
                print("Threading pass")
                exit()
            else:
                print("Exiting...")
                exit()

def transmit():
    pass


def recieve(juliet_addr, juliet_port):
    pass


romeo = startup(romeo_addr, romeo_port)

ping(romeo, juliet_addr, juliet_port)
request(romeo, juliet_addr, juliet_port)
romeo.close()
