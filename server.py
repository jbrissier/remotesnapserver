import select
import sys
import pybonjour
import socket
import threading
import random

name    = "Remotesnap"
regtype = "_remotesnapsync._tcp"
port    = 49386

class Server(threading.Thread):
    def __init__(self,port):
        self.port=port
        self.running = True
        self.host=''

        threading.Thread.__init__ ( self )
        self.setDaemon(True)


    def run(self):

        while self.running:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.host,self.port))


            s.listen(1)

            conn, addr= s.accept()
            openfile= open("/Users/jochenbrissier/Desktop/foo%s.jpg" % random.randrange(1024) ,'w')
            while True:
                print "...."
                data = conn.recv(1024)
                if not data:break
                openfile.write(data)
            openfile.close()
            conn.close()







def register_callback(sdRef, flags, errorCode, name, regtype, domain):
    if errorCode == pybonjour.kDNSServiceErr_NoError:
        print 'Registered service:'
        print '  name    =', name
        print '  regtype =', regtype
        print '  domain  =', domain


sdRef = pybonjour.DNSServiceRegister(name = name,
                                     regtype = regtype,
                                     port = port,
                                     callBack = register_callback)



server = Server(port).start()


try:
    try:
        while True:
            ready = select.select([sdRef], [], [])
            if sdRef in ready[0]:
                pybonjour.DNSServiceProcessResult(sdRef)
    except KeyboardInterrupt:
        pass
finally:
    sdRef.close()
