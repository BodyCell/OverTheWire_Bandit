# -------------------- Port Scanner -------------------- #
# Reference: Vinsloev Academy (https://www.youtu.be/bH-3PuQC_n0)
# Author: Cody Bell
# Last updated: 05/17/2023
# --------------------------------------------------------------------------------#


import socket

def connectionScan(tgtHost, tgtPort):
    try:
        connect = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        connect.connect((tgtHost, tgtPort))
        print(f'[+]{tgtPort} tcp open') # output for successful connection
        connect.close()

    except:
        print(f'[-]{tgtPort} tcp closed')



if __name__ == '__main__':

    connectionScan('142.251.33.14',80)