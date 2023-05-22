# -------------------- Port Scanner -------------------- #
# Reference: Vinsloev Academy (https://www.youtu.be/bH-3PuQC_n0)
# Author: Cody Bell
# Last updated: 05/17/2023
# --------------------------------------------------------------------------------#


import socket

def singleScan(tgtHost, tgtPort):
    try:
        connect = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #creating network object
        connect.connect((tgtHost, tgtPort))
        print(f'[+] {tgtPort} tcp open') # output for successful connection
        connect.close()

    except:
        print(f'[-] {tgtPort} tcp closed')


def multiScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    
    except:
        print(f'[-] could not resolve {tgtName}.')
        return
    
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print(f'\n[+] Scan result of: {tgtName}.')
    
    except:
        print(f'\n[+] Scan result of: {tgtIP}.')

    socket.setdefaulttimeout(1)
    
    for port in tgtPorts:
        print(f'Scanning Port: {port}')
        singleScan(tgtHost, port)





if __name__ == '__main__':

    multiScan('google.com', [80,53])





# To be continued... with more features!