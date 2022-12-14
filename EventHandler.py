class EventHandler:
    def fileno(self):
        'Return thr associated file descriptor'
        raise NotImplemented('must implement')
    
    def wants_to_recieve(self):
        'Return true if recieving is allowed'
        return False

    def handle_recieve(self):
        'Perform the recieve operation'
        pass
    def wants_to_send(self):
        'Return True sending is requested'
        return False
    def handle_send(self):
        pass
    
import select
def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_recieve()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _= select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_recieve()
        for h in can_send:
            h,handle_send()

import socket
import time

class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)
    def fileno(self):
        return self.sock.fileno()
    def wants_to_recieve(self):
        return True


class UDPTimeServer(UDPServer):
    def handle_recieve(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)

class UDPEchoServer(UDPServer):
    def handle_recieve(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)

if __name__ == '__main__':
    handlers = [UDPTimeServer(('', 14000)), UDPEchoServer(('', 15000)) ]
    event_loop(handlers)
    

            
