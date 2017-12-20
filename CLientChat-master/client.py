# chat_client.py
# -*- coding: utf-8 -*-
########################################
# Write by IT PLUS TEAM
########################################

import sys
import socket
import select
import os
import time

sys.path.append("BLL")
from Client_BLL import *
from Process_BLL import *
port = 8888
port2= 8889

timeout=2
class clientChat:
    def __init__(self):
        os.system('clear')
        self.Ps=Process()

        print """


	\nChào mừng đến với chat online X


	"""

    def chat_client(self):
        
        if(len(sys.argv) < 2) :
            print bcolors.BOLD+bcolors.FAIL+'Cú pháp : python client.py [Server]'+bcolors.ENDC+"\n\n"
            sys.exit()
    
        host = sys.argv[1]

        command=''
        Cl=Client()
        flag=False
        # Khoi tao socket
        s=Cl.ConnectServer(timeout)
        try:
            if s:
                # Ket noi den Server
                self.Ps.MsgClientconnectServer(port)
                if Cl.TrytoConnect(s,host,port):
                    self.Ps.MsgClientconnectServerOK(port)
                    flag=True
                else:
                    self.Ps.MsgClientconnectServerFail(port)
                    self.Ps.MsgClientconnectServer(port2)
                    
                    if Cl.TrytoConnect(s,host,port2):
                        self.Ps.MsgClientconnectServerOK(port2)
                        flag=True
                        
                    else:
                        self.Ps.MsgClientconnectServerFail(port2)
                        sys.exit()
                        

                if(flag):
                    print bcolors.BOLD+bcolors.FAIL+'#exit: Thoát \n\n'+bcolors.ENDC
                    name=raw_input("Nhập NickNam3: ")
                    #Gui ten username den server
                    s.send("#user:"+name)
                    
                    sys.stdout.write('>'); sys.stdout.flush()
                    while 1:
                        # Nhan du lieu tu keyboard
                        socket_list = [sys.stdin, s]

                        # Get the list sockets which are readable
                        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])

                        for sock in ready_to_read:
                            Cl.StreamData(sock,s)

        except KeyboardInterrupt:
            print "\nĐóng chat!!!"
if __name__ == "__main__":
    chat=clientChat()
    sys.exit(chat.chat_client())
