# chat_client.py
from datetime import datetime
import sys, socket, select

#FMT = '%H:%M:%S.%f'
FMT = '%Y-%m-%d %H:%M:%S.%f'
def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. You can start sending messages'
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:            
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                # print data
		
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :  
                    print "Data is: ", data[0], " ", data
		    print data[1]
                    if data[1] == 'p':
                        t0 = data[4:]
                    	print "local device time: "
                    	print t0
                    elif data[1] == 's':
                        print "server time: "
                        ts= data[4:]
                        print ts
                        tdelta1 =  datetime.strptime(ts, FMT) - datetime.strptime(t0, FMT)
                        print "time it takes to send image:"
                        print tdelta1
            else :
                # user entered a message
                msg = sys.stdin.readline()
                #s.send(msg)
                sys.stdout.write('[Me] '); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())

